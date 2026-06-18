# Transcript: j3aXJNu9804

**URL:** https://www.youtube.com/watch?v=j3aXJNu9804
**Segments:** 1194

---

## Full Text

Well, Anthropic just launched routines, which allows Claude to kick off automations via schedule, trigger, or even web hook. And this closes the loop and basically turns Claude into a dedicated automation platform competing with no code drag and drop builders like NADEN and others. In this video, I'm going to show you guys how you can build routines very quickly. I'm going to give you guys a couple of demos and I'm going to walk you through step by step setting up your own routines on both the Claude desktop interface as well as behind the scenes via API. Okay, so for the most prototypical example, I have a daily mailbox summary plus draft routine. And what I'm doing here is I just clicked run now because they have a little demo or test feature that allows you to actually run it and then see the inputs and outputs live. If I click on this little runs button, you'll see that all I've really done is I've just fed in a prompt. And this is the exact same thing as cloud code. It's just occurring on a standardized cloud container, not on my computer. And in this case, I'm just testing it using their interface, but you can also schedule it. You can have it trigger based off web hook. And then you can also send an API request to trigger it. And so you can trigger it based on incoming data. You can trigger it based off outgoing data. It's very powerful. If anybody has watched my previous video on Agentic Workflows, this is basically the standardized and enterprise version of Agentic Workflows. So this is now searching through Gmail emails. It's actually doing everything more or less that I would normally do if running this locally on my computer. The only difference being obviously that because it's occurring on the cloud, it's not something that I realistically am going to want to have to steer. Typically, you want to be a lot clear about the instructions and make sure that it has all the information that it needs. After that, it's just going to go through various tool calls and everything like that until it gets to the definition of done, which in my case is going to be, hey, once you're finished, use a Slack connector to send me an update. Now, on the Cloud Code docs page, the majority of the use cases are what I'd consider to be overly technical things like backlog maintenance, alert triage, bespoke code review. I mean, most people don't even know what any of the stuff means. Um, but I want you to know this is basically a standin replacement for automation. You can automate anything using this tool. And what's really cool is you can do it using natural language. So, what I've done is I've developed a cloud skill that you can import into your own workspace. Then you can just give that skill any pre-existing workflow whether it's in natural language written as an SOP or it's something on a no code tool like naden or make.com. Back to the skill page here. You can see it's found two unreads. The thing is I don't really care about this because if you think about it, this is the conversation thread. What I want to do is I want to see this Slack update that was sent to my DMs because you know if I'm using this like a traditional automation, that's where I'd probably be getting the notification. So, if I go, I actually see I did receive a notification at 12:01 where it pulled my own reds and then it fed me the information as well as like a highle summary along with a polite decline that it drafted as well as an acceptance for for this one. And I can go on to my email and I can actually open up the drafts and I could I could see them all as well. And just because I'm trying not to dox all of these people too hard, um, you know, in this case, I immediately drafted, hey Corey, thanks for reaching out. Tell the other Nick I own one. Happy to come on. Send over a few time slots that work on your end. Uh, and then I just removed the two email, but that was previously populated. Okay, so that's probably the simplest example of a demo. And I just did all this stuff uh live using the test feature because I wanted to show you that that's how it works. But you can also schedule it. And then you can also fire things off based off web hooks and API calls. So what I'm going to do next is I'm very quickly going to show you how the scheduling feature works. And then after I'm going to show you how you can use triggers like web hooks and so on and so forth to run your routines. Once we're done with that, I'll actually walk through like the UX and show you guys uh more of the deep dive behind how this works. So anyway, for scheduling purposes, all I need to do is go back to the routine that I made a moment ago. I click on this little button here, and then I can just select a different trigger. So in this case, I have call via API, but I could also click schedule. And as you see here, we have this little visual interface where I could select hourly, daily, and so on and so forth. Because this is going to be an email triage flow, I'm probably going to want to run this pretty early before I wake up. I'm waking up around 5:20 these days, so it'll probably be about 510. And what I should note is you can add multiple of these triggers at any point in time. So now after saving, if I go back to routines, you'll see there's a little calendar feature here. And you can now see that there's a daily mailbox summary plus draft opened at 5:10, as well as a couple of other ones that I was playing around with earlier today. You don't have to pay attention to those. What that means is without me having to do anything, the exact same exercise is going to occur. The agent is going to check my mailbox using the Gmail connector. It's going to run through whatever SOP or logic that I gave it, which in this case was just, hey, go see if we've had any previous email communicate. And then it's going to draft up the message and send it to me in Slack. Okay. What I have here is another routine. This one takes a transcript that is generated using Fireflies, which is a transcript service that joins your call, listens to what you say, and then basically stores it all as text. And essentially what I'm going to do just for the purposes of this demo is I'm going to do it via API request, but I'm going to show you guys as well how you can hook it up via web hook so it just fires automatically. So I have my transcript to proposal routine right over here. And I could click run now, but there's no actual transcript. The instructions here are I give you a transcript via API call. So what I'm going to do is I'm going to open up a cloud code instance. I'm just going to have it send an API request using uh this transcript. And then I'm just going to press enter. And I'm not going to expand this because I've just hard-coded an API key for uh demo purposes. But you can see here what it's going to start off by doing is basically sending that curl request as a text payload and then also generating the proposal entirely on its own. And when this occurs, it's actually going to trigger that routine. I guess I already just leaked my API key. Whatever the hell. Um it's going to fire that routine, which it's done right over here. And now it's actually running in the cloud with the full transcript and whatever the deal terms are of the, you know, conversation. And so I can actually open this up and then I can see what's going on. So you can see I give you a transcript via API call. I want you to create a full proposal using one of my other AI agents in a managed session. And this is where managed sessions come in handy, which if you guys didn't know is just a similar way that you could set up different endpoints out there that allow AI to basically create an an interconnected network of managed agents or agents that all have their own siloed containers both for security and then safety purposes. So, it's just verifying that we actually have what we need for Slack. And now it's going to go ahead and generate a high-quality proposal. Now, I just want to be clear about what problem exactly this solves. The old way of designing automations typically involved some sort of event or outside trigger like a schedule, maybe something that occurred, you know, at 5:00 a.m. every morning or whatever. That event would be fed into a platform like NAN, which was responsible for basically proceeding through a chain of logic that you created. You know, it' be a bunch of drag and drop uh nodes that you put together to do some function. In this case, this is a Reddit scraper for a live build that I did for one of my communities. And see this whole section in the middle here, this logic, this can take a fair amount of time to put together. You know, you have to drag and drop all these nodes, you have to set up all of these credentials, you have to do all the authentication, you got to get the data and and map the right variables and the fields. This is really like where the meat and potatoes of your work as somebody that was looking to automate your business um um came in. Okay? And then from there, your NAD system, typically, it doesn't just like work by itself. It does something to some platform, right? So it'll then grab its output and then shove that into Slack or maybe some sort of CRM somewhere or whatever it is that you do, some database. The new way is basically the exact same thing. You have an event, okay? And that event is either an API call. It's a web hook or it's some sort of schedule. So again, you know, waking it up at 5:00 a.m. every morning. It's just instead of putting that into NADN and then having to build all that stuff yourself with those drag and drop nodes, all you have to do, okay, is just give it some natural language which is far easier obviously with some very high level instructions and then it can then output things as uh ND did before to you know some other platform Slack or CRM and so the reason why I'm equating it like this is because routines effectively solve that middle problem. Uh I've made some videos in the past to the tune of N8N is over because XYZ thing is now launched and it does it way better and you know sometimes a specific feature was missing that you know N8N or some other no code platform handled. Um that didn't make it an exactly one to one overlap but routines are uh cla's literal 1 to1 overlap. It replaces the exact same functionality. It's capable of scheduling. It's capable of orchestrating workflows and so on and so forth. And it really is like the next step in agentic uh execution of knowledge tasks. When all this stuff finishes, I actually have the proposal right over here. I can take a look at that. Click this button to open it in a new page. And you can see I now have the proposal, which is just part of the template of the manage agent that generates this thing. Pull out all of the data. So, you know, we're an AI content writing marketplace that matches business clients with vetted freelancer writers. And then this is leftclick, which you know is pitching them. And so, these are the sorts of proposals that we actually send day-to-day. And hopefully you guys see how easy it is to actually like integrate a routine or some sort of API eventbased system into your infrastructure in like two minutes. Uh boy, have we come a long way from back in the day when me designing that proposal generator would have taken like 2 and 1 half to 3 hours. The current UX for routines looks like this. And in order to get there, all you have to do is type in cloud.ai/code/ routines. You'll be given a page that looks something like this where you can see all routines stored in a grid-like pattern over here alongside their title, the time that they are running, and then also the the next scheduled run as well as what looks like some category listing which they provide uh with or without you. There's also a calendar view and so you can see the actual ones that are going to be executed and exactly which times they're going to be executed. And so here I created a couple of demos, daily nicks, arrive mention scan, morning inbox drafts and news video ideas. You can see that today this one's going to execute at 651, this one at 7:43, and this one at 8:17. So, you also get a little bit of a visual aspect there. When you click new routine up in the top right, it'll immediately ask you for some information like the name. So, I'm just going to provide a quick demo here called mailbox drafter. Next, you can describe what Claude should do in each session. So, this is where you basically give it a prompt. And this prompt is essentially analogous to a skill. Just like in a skill, you have a standardized list of steps that you need the model to take in order to perform some economically valuable piece of work for you. Um, so too should you construct this routine description like a list of SOPs or steps to allow it to perform uh a tasks for you. It's just my recommendation here is be a little bit more precise than you are probably in your skill because whereas in your skill you could modify things on the fly, change your trajectory of the task and so on and so forth, here the routine occurs entirely hands-off, meaning that it basically needs to work almost perfectly every time. So decrease the total scope of possible messups and screw-ups that it could make by being as clear and precise as possible. But for instance, I wrote pull all of my unreads using the provided Gmail connector. More on that in a sec. For each unread, check if there's any pre-existing conversations with that contact. If so, pull those two for context. Then draft replies based on what you know about me and the context of the task. Once done, use the Slack connector. More on that in a second to send me an update. And so, as you can see here, um, you know, you can make this about as long or as as short as you want. I don't believe there's a length limit. I went and I checked just by pasting this a bunch of times and I couldn't find anything. So, I would definitely lean on the side of more contacts as opposed to less. From there, you can select a repository. So, whatever repository you want. I'm just going to say this business one. You can select a model type. So, I'm going to use Opus 4.61 mil. And then you can also select which cloud environment you want to run it in. And so, you can hear basically create a cloud environment with a bunch of environment variables, keys, uh, you know, API credentials and so on and so forth as needed. So, in my case, I'm fine with default. I'm just going to move on. You can then select a trigger. So, you can schedule it. You can go via GitHub event or you can go via API. Now, realistically, this is probably something you're going to want to do on a schedule since we are just going to be going through our on reds and then drafting. But for demonstration purposes, I'm just going to go via API. And the whole idea is by doing this, I'll be able to very quickly call and then test in another Cloud Code instance to show you guys what's happening live. So, I'm just going to add a trigger. And then once we've added said trigger, we're going to receive a little curl request, which is a snippet of code that you can give any model. And finally, now we just need to add our connector. So, here I'm going to click add connector. And then I'm going to connect my own Gmail. By the way, if you don't have a connector, just head on down to Claude code settings, then go to connectors over here. Then you can actually add uh just clicking on this little connect button. When you do, it'll ask to connect Claude to your Gmail account. You can click continue and then you can sign into the particular one that you want. So, in my case, this I'm also going to need one other connector if you guys think about it because I'm going to want a Slack message sent. So, here I can use this little search bar and then click a plus button. Then I'll just have to perform again some OOTH in a new browser tab. Here I'm going to click allow. And just like any simple OOTH screen, we're now going to be connected. So now what we can do is we can go back to the routine and then I can add the connector manually. From here, you'll be given a token. You can copy that token, store it somewhere safe. So that's what I'm going to do here. And now we basically have our skill or our routine ready to go. Okay. And then once you're done, just head over to the run now in the top right hand corner to basically start the workflow run. And uh we're just going to do this here using the GUI graphical user interface for testing purposes. But you'll see a new little run just populated. So I'm going to go down here and you'll see all we're really doing is we're just sending it this message. Once it's done, it'll use the Slack connector to send me an update. You can see it's already starting to fire off a tool search. So I'll just double back when it's done. And I should note, I mean, I'm watching it here, but the whole idea is that I don't even know that this thing's going on, right? This was triggered uh ideally on a schedule or something like that, and I just wake up in the morning to my Slack uh message with a bunch of different emails and their various drafts. If I head back over here, you can see that we actually have both of those fed in. Um, looks like somebody invited me for a podcast interview and then somebody else asked me a couple of questions about a few things here. Finally, I want to show you guys how easy it is to convert workflows that you built on third party tools like NAD, for instance, into routines. And what's really cool about NAND is they allow you just to like mouse over if you hold shift and then hold command C or just right click and press copy. And then now you basically have access to a bunch of JSON. And you could tell just by me pasting it in. This is like JSON or the syntax that these nodes are represented in if we're talking through text. Well, anyway, if I go back to anti-gravity, which contains my little cloud code window, and then I type in this JSON, and then at the very top, I say use the routine generator to turn this naden workflow into a routine. Okay, I'm just going to divide this to make it really simple. Uh what this is going to do is use the skill that I'm giving all of you guys out of the box to basically turn this into a flow that we can call just using natural language. So I'm not necessarily going to encourage you to use all of your workflows or to port them over from NADN or some other no code tool to uh claude's back end. Reason being is you know when you're dealing in the domain of tokens things are going to be a little bit more expensive than dealing entirely in the domain of compute. And really the point is not hey just turn all your nadn or make.com workflows into routines. The point is more like, you know, if you have something you can build today that previously would have taken you a couple of hours in NAN, might make more sense just to oneshot it as a routine. But, um, you know, what this will do really quickly is just go ahead and do the creation. So, as you guys can see here, it's doing some thinking. It's loading the routines. In this case, it's just going to schedule one cuz I didn't provide any context as to how I wanted to run it. Um, but yeah, here we go. It's now going to fetch stories from the HackerN Algolia API, extract the hits, format them into a markdown report, and commit it, which was what the actual flow was doing. So, just like this one here, if I click execute workflow, this goes through the scraper. It then generates a bunch of hits basically from um a website called Hacker News. HackerNews is the source here, which in this case is going to contain a bunch of different um comments like this one on how open source AI is the path forward. Certainly not when Claude drops a freaking update like this. Well, the same routine is going to work here the exact same way. And you can see it just said routine created and fired hacker use AI stories fetch, right? And what's really cool about this is I mean it's it's just so easy for me to to change things. Um so I mean right now this is obviously going to fetch that data, right? And you know fetching that data is okay, but what am I going to do with it? It's just sort of like stuck here, right? You know, if I were in NAD, I'd have to modify this. Uh it'd be significantly harder to modify this here. I can literally just go connectors Slack. Okay, save. I can then set it to run on, you know, 733 MDT or via API request, which I'm going to click done. And now what I can also do is I can go back here and I can say great, update this so that it sends me a message in Slack with the scrape after it's done. And now in 3 seconds, you know, it can make an HTTP request over to the routine and just edit it on the fly for me. I don't have to drag and drop any notes. It's much easier and much faster. Okay, so hopefully you guys can see that this has a lot of potential and you're likely to see larger and larger flows be passed off to agents in this manner. Um, I didn't really give you guys an extraordinarily comprehensive look at all the different things you could do with this, but just off the top of my head, some ways that I'm implementing this in my agency today, some ways that I've already done so, and some ways that I can I'm going to continue to do so after this video are I'm going to replace all of my proposal generators with these built-in routines. I'm going to connect a couple of additional routines so that after a call, like a a sales call with a prospect, um, I'll receive a web hook with um, essentially like a transcript. I'm going to feed that transcript into a routine that's going to generate an immediate post call email and then uh like a workflow diagram draft based on our conversations that I can also pin alongside it just for the impression of of more effort and higher perceived quality. Uh when we send out the proposal, I'm going to be monitoring to see if somebody's signed. When they do, it's going to route back to another routine via a web hook, which is going to proceed with the next step, which is sending them a message with an email with an onboarding uh you know, calendar notification, as well as congratulating them and thanking them on on coming aboard. You guys can automate more or less all of the non like human facetime steps in a business right now. And it's not like you couldn't before. It's just in order to do it before it was pretty laborious and you needed a fair amount of knowhow. Um now as long as you understand sort of the routine spec and more or less what I've showed you in this video, you guys are good to go. So it's an exciting time to be in AI and automation. Hopefully you guys appreciated this video. Looking forward to the next one. Catch y'all on it. Well, Anthropic just launched routines, which allows Claude to kick off automations via schedule, trigger, or even web hook. And this closes the loop and basically turns Claude into a dedicated automation platform competing with no code drag and drop builders like NADEN and others. In this video, I'm going to show you guys how you can build routines very quickly. I'm going to give you guys a couple of demos and I'm going to walk you through step by step setting up your own routines on both the Claude desktop interface as well as behind the scenes via API. Okay, so for the most prototypical example, I have a daily mailbox summary plus draft routine. And what I'm doing here is I just clicked run now because they have a little demo or test feature that allows you to actually run it and then see the inputs and outputs live. If I click on this little runs button, you'll see that all I've really done is I've just fed in a prompt. And this is the exact same thing as cloud code. It's just occurring on a standardized cloud container, not on my computer. And in this case, I'm just testing it using their interface, but you can also schedule it. You can have it trigger based off web hook. And then you can also send an API request to trigger it. And so you can trigger it based on incoming data. You can trigger it based off outgoing data. It's very powerful. If anybody has watched my previous video on Agentic Workflows, this is basically the standardized and enterprise version of Agentic Workflows. So this is now searching through Gmail emails. It's actually doing everything more or less that I would normally do if running this locally on my computer. The only difference being obviously that because it's occurring on the cloud, it's not something that I realistically am going to want to have to steer. Typically, you want to be a lot clear about the instructions and make sure that it has all the information that it needs. After that, it's just going to go through various tool calls and everything like that until it gets to the definition of done, which in my case is going to be, hey, once you're finished, use a Slack connector to send me an update. Now, on the Cloud Code docs page, the majority of the use cases are what I'd consider to be overly technical things like backlog maintenance, alert triage, bespoke code review. I mean, most people don't even know what any of the stuff means. Um, but I want you to know this is basically a standin replacement for automation. You can automate anything using this tool. And what's really cool is you can do it using natural language. So, what I've done is I've developed a cloud skill that you can import into your own workspace. Then you can just give that skill any pre-existing workflow whether it's in natural language written as an SOP or it's something on a no code tool like naden or make.com. Back to the skill page here. You can see it's found two unreads. The thing is I don't really care about this because if you think about it, this is the conversation thread. What I want to do is I want to see this Slack update that was sent to my DMs because you know if I'm using this like a traditional automation, that's where I'd probably be getting the notification. So, if I go, I actually see I did receive a notification at 12:01 where it pulled my own reds and then it fed me the information as well as like a highle summary along with a polite decline that it drafted as well as an acceptance for for this one. And I can go on to my email and I can actually open up the drafts and I could I could see them all as well. And just because I'm trying not to dox all of these people too hard, um, you know, in this case, I immediately drafted, hey Corey, thanks for reaching out. Tell the other Nick I own one. Happy to come on. Send over a few time slots that work on your end. Uh, and then I just removed the two email, but that was previously populated. Okay, so that's probably the simplest example of a demo. And I just did all this stuff uh live using the test feature because I wanted to show you that that's how it works. But you can also schedule it. And then you can also fire things off based off web hooks and API calls. So what I'm going to do next is I'm very quickly going to show you how the scheduling feature works. And then after I'm going to show you how you can use triggers like web hooks and so on and so forth to run your routines. Once we're done with that, I'll actually walk through like the UX and show you guys uh more of the deep dive behind how this works. So anyway, for scheduling purposes, all I need to do is go back to the routine that I made a moment ago. I click on this little button here, and then I can just select a different trigger. So in this case, I have call via API, but I could also click schedule. And as you see here, we have this little visual interface where I could select hourly, daily, and so on and so forth. Because this is going to be an email triage flow, I'm probably going to want to run this pretty early before I wake up. I'm waking up around 5:20 these days, so it'll probably be about 510. And what I should note is you can add multiple of these triggers at any point in time. So now after saving, if I go back to routines, you'll see there's a little calendar feature here. And you can now see that there's a daily mailbox summary plus draft opened at 5:10, as well as a couple of other ones that I was playing around with earlier today. You don't have to pay attention to those. What that means is without me having to do anything, the exact same exercise is going to occur. The agent is going to check my mailbox using the Gmail connector. It's going to run through whatever SOP or logic that I gave it, which in this case was just, hey, go see if we've had any previous email communicate. And then it's going to draft up the message and send it to me in Slack. Okay. What I have here is another routine. This one takes a transcript that is generated using Fireflies, which is a transcript service that joins your call, listens to what you say, and then basically stores it all as text. And essentially what I'm going to do just for the purposes of this demo is I'm going to do it via API request, but I'm going to show you guys as well how you can hook it up via web hook so it just fires automatically. So I have my transcript to proposal routine right over here. And I could click run now, but there's no actual transcript. The instructions here are I give you a transcript via API call. So what I'm going to do is I'm going to open up a cloud code instance. I'm just going to have it send an API request using uh this transcript. And then I'm just going to press enter. And I'm not going to expand this because I've just hard-coded an API key for uh demo purposes. But you can see here what it's going to start off by doing is basically sending that curl request as a text payload and then also generating the proposal entirely on its own. And when this occurs, it's actually going to trigger that routine. I guess I already just leaked my API key. Whatever the hell. Um it's going to fire that routine, which it's done right over here. And now it's actually running in the cloud with the full transcript and whatever the deal terms are of the, you know, conversation. And so I can actually open this up and then I can see what's going on. So you can see I give you a transcript via API call. I want you to create a full proposal using one of my other AI agents in a managed session. And this is where managed sessions come in handy, which if you guys didn't know is just a similar way that you could set up different endpoints out there that allow AI to basically create an an interconnected network of managed agents or agents that all have their own siloed containers both for security and then safety purposes. So, it's just verifying that we actually have what we need for Slack. And now it's going to go ahead and generate a high-quality proposal. Now, I just want to be clear about what problem exactly this solves. The old way of designing automations typically involved some sort of event or outside trigger like a schedule, maybe something that occurred, you know, at 5:00 a.m. every morning or whatever. That event would be fed into a platform like NAN, which was responsible for basically proceeding through a chain of logic that you created. You know, it' be a bunch of drag and drop uh nodes that you put together to do some function. In this case, this is a Reddit scraper for a live build that I did for one of my communities. And see this whole section in the middle here, this logic, this can take a fair amount of time to put together. You know, you have to drag and drop all these nodes, you have to set up all of these credentials, you have to do all the authentication, you got to get the data and and map the right variables and the fields. This is really like where the meat and potatoes of your work as somebody that was looking to automate your business um um came in. Okay? And then from there, your NAD system, typically, it doesn't just like work by itself. It does something to some platform, right? So it'll then grab its output and then shove that into Slack or maybe some sort of CRM somewhere or whatever it is that you do, some database. The new way is basically the exact same thing. You have an event, okay? And that event is either an API call. It's a web hook or it's some sort of schedule. So again, you know, waking it up at 5:00 a.m. every morning. It's just instead of putting that into NADN and then having to build all that stuff yourself with those drag and drop nodes, all you have to do, okay, is just give it some natural language which is far easier obviously with some very high level instructions and then it can then output things as uh ND did before to you know some other platform Slack or CRM and so the reason why I'm equating it like this is because routines effectively solve that middle problem. Uh I've made some videos in the past to the tune of N8N is over because XYZ thing is now launched and it does it way better and you know sometimes a specific feature was missing that you know N8N or some other no code platform handled. Um that didn't make it an exactly one to one overlap but routines are uh cla's literal 1 to1 overlap. It replaces the exact same functionality. It's capable of scheduling. It's capable of orchestrating workflows and so on and so forth. And it really is like the next step in agentic uh execution of knowledge tasks. When all this stuff finishes, I actually have the proposal right over here. I can take a look at that. Click this button to open it in a new page. And you can see I now have the proposal, which is just part of the template of the manage agent that generates this thing. Pull out all of the data. So, you know, we're an AI content writing marketplace that matches business clients with vetted freelancer writers. And then this is leftclick, which you know is pitching them. And so, these are the sorts of proposals that we actually send day-to-day. And hopefully you guys see how easy it is to actually like integrate a routine or some sort of API eventbased system into your infrastructure in like two minutes. Uh boy, have we come a long way from back in the day when me designing that proposal generator would have taken like 2 and 1 half to 3 hours. The current UX for routines looks like this. And in order to get there, all you have to do is type in cloud.ai/code/ routines. You'll be given a page that looks something like this where you can see all routines stored in a grid-like pattern over here alongside their title, the time that they are running, and then also the the next scheduled run as well as what looks like some category listing which they provide uh with or without you. There's also a calendar view and so you can see the actual ones that are going to be executed and exactly which times they're going to be executed. And so here I created a couple of demos, daily nicks, arrive mention scan, morning inbox drafts and news video ideas. You can see that today this one's going to execute at 651, this one at 7:43, and this one at 8:17. So, you also get a little bit of a visual aspect there. When you click new routine up in the top right, it'll immediately ask you for some information like the name. So, I'm just going to provide a quick demo here called mailbox drafter. Next, you can describe what Claude should do in each session. So, this is where you basically give it a prompt. And this prompt is essentially analogous to a skill. Just like in a skill, you have a standardized list of steps that you need the model to take in order to perform some economically valuable piece of work for you. Um, so too should you construct this routine description like a list of SOPs or steps to allow it to perform uh a tasks for you. It's just my recommendation here is be a little bit more precise than you are probably in your skill because whereas in your skill you could modify things on the fly, change your trajectory of the task and so on and so forth, here the routine occurs entirely hands-off, meaning that it basically needs to work almost perfectly every time. So decrease the total scope of possible messups and screw-ups that it could make by being as clear and precise as possible. But for instance, I wrote pull all of my unreads using the provided Gmail connector. More on that in a sec. For each unread, check if there's any pre-existing conversations with that contact. If so, pull those two for context. Then draft replies based on what you know about me and the context of the task. Once done, use the Slack connector. More on that in a second to send me an update. And so, as you can see here, um, you know, you can make this about as long or as as short as you want. I don't believe there's a length limit. I went and I checked just by pasting this a bunch of times and I couldn't find anything. So, I would definitely lean on the side of more contacts as opposed to less. From there, you can select a repository. So, whatever repository you want. I'm just going to say this business one. You can select a model type. So, I'm going to use Opus 4.61 mil. And then you can also select which cloud environment you want to run it in. And so, you can hear basically create a cloud environment with a bunch of environment variables, keys, uh, you know, API credentials and so on and so forth as needed. So, in my case, I'm fine with default. I'm just going to move on. You can then select a trigger. So, you can schedule it. You can go via GitHub event or you can go via API. Now, realistically, this is probably something you're going to want to do on a schedule since we are just going to be going through our on reds and then drafting. But for demonstration purposes, I'm just going to go via API. And the whole idea is by doing this, I'll be able to very quickly call and then test in another Cloud Code instance to show you guys what's happening live. So, I'm just going to add a trigger. And then once we've added said trigger, we're going to receive a little curl request, which is a snippet of code that you can give any model. And finally, now we just need to add our connector. So, here I'm going to click add connector. And then I'm going to connect my own Gmail. By the way, if you don't have a connector, just head on down to Claude code settings, then go to connectors over here. Then you can actually add uh just clicking on this little connect button. When you do, it'll ask to connect Claude to your Gmail account. You can click continue and then you can sign into the particular one that you want. So, in my case, this I'm also going to need one other connector if you guys think about it because I'm going to want a Slack message sent. So, here I can use this little search bar and then click a plus button. Then I'll just have to perform again some OOTH in a new browser tab. Here I'm going to click allow. And just like any simple OOTH screen, we're now going to be connected. So now what we can do is we can go back to the routine and then I can add the connector manually. From here, you'll be given a token. You can copy that token, store it somewhere safe. So that's what I'm going to do here. And now we basically have our skill or our routine ready to go. Okay. And then once you're done, just head over to the run now in the top right hand corner to basically start the workflow run. And uh we're just going to do this here using the GUI graphical user interface for testing purposes. But you'll see a new little run just populated. So I'm going to go down here and you'll see all we're really doing is we're just sending it this message. Once it's done, it'll use the Slack connector to send me an update. You can see it's already starting to fire off a tool search. So I'll just double back when it's done. And I should note, I mean, I'm watching it here, but the whole idea is that I don't even know that this thing's going on, right? This was triggered uh ideally on a schedule or something like that, and I just wake up in the morning to my Slack uh message with a bunch of different emails and their various drafts. If I head back over here, you can see that we actually have both of those fed in. Um, looks like somebody invited me for a podcast interview and then somebody else asked me a couple of questions about a few things here. Finally, I want to show you guys how easy it is to convert workflows that you built on third party tools like NAD, for instance, into routines. And what's really cool about NAND is they allow you just to like mouse over if you hold shift and then hold command C or just right click and press copy. And then now you basically have access to a bunch of JSON. And you could tell just by me pasting it in. This is like JSON or the syntax that these nodes are represented in if we're talking through text. Well, anyway, if I go back to anti-gravity, which contains my little cloud code window, and then I type in this JSON, and then at the very top, I say use the routine generator to turn this naden workflow into a routine. Okay, I'm just going to divide this to make it really simple. Uh what this is going to do is use the skill that I'm giving all of you guys out of the box to basically turn this into a flow that we can call just using natural language. So I'm not necessarily going to encourage you to use all of your workflows or to port them over from NADN or some other no code tool to uh claude's back end. Reason being is you know when you're dealing in the domain of tokens things are going to be a little bit more expensive than dealing entirely in the domain of compute. And really the point is not hey just turn all your nadn or make.com workflows into routines. The point is more like, you know, if you have something you can build today that previously would have taken you a couple of hours in NAN, might make more sense just to oneshot it as a routine. But, um, you know, what this will do really quickly is just go ahead and do the creation. So, as you guys can see here, it's doing some thinking. It's loading the routines. In this case, it's just going to schedule one cuz I didn't provide any context as to how I wanted to run it. Um, but yeah, here we go. It's now going to fetch stories from the HackerN Algolia API, extract the hits, format them into a markdown report, and commit it, which was what the actual flow was doing. So, just like this one here, if I click execute workflow, this goes through the scraper. It then generates a bunch of hits basically from um a website called Hacker News. HackerNews is the source here, which in this case is going to contain a bunch of different um comments like this one on how open source AI is the path forward. Certainly not when Claude drops a freaking update like this. Well, the same routine is going to work here the exact same way. And you can see it just said routine created and fired hacker use AI stories fetch, right? And what's really cool about this is I mean it's it's just so easy for me to to change things. Um so I mean right now this is obviously going to fetch that data, right? And you know fetching that data is okay, but what am I going to do with it? It's just sort of like stuck here, right? You know, if I were in NAD, I'd have to modify this. Uh it'd be significantly harder to modify this here. I can literally just go connectors Slack. Okay, save. I can then set it to run on, you know, 733 MDT or via API request, which I'm going to click done. And now what I can also do is I can go back here and I can say great, update this so that it sends me a message in Slack with the scrape after it's done. And now in 3 seconds, you know, it can make an HTTP request over to the routine and just edit it on the fly for me. I don't have to drag and drop any notes. It's much easier and much faster. Okay, so hopefully you guys can see that this has a lot of potential and you're likely to see larger and larger flows be passed off to agents in this manner. Um, I didn't really give you guys an extraordinarily comprehensive look at all the different things you could do with this, but just off the top of my head, some ways that I'm implementing this in my agency today, some ways that I've already done so, and some ways that I can I'm going to continue to do so after this video are I'm going to replace all of my proposal generators with these built-in routines. I'm going to connect a couple of additional routines so that after a call, like a a sales call with a prospect, um, I'll receive a web hook with um, essentially like a transcript. I'm going to feed that transcript into a routine that's going to generate an immediate post call email and then uh like a workflow diagram draft based on our conversations that I can also pin alongside it just for the impression of of more effort and higher perceived quality. Uh when we send out the proposal, I'm going to be monitoring to see if somebody's signed. When they do, it's going to route back to another routine via a web hook, which is going to proceed with the next step, which is sending them a message with an email with an onboarding uh you know, calendar notification, as well as congratulating them and thanking them on on coming aboard. You guys can automate more or less all of the non like human facetime steps in a business right now. And it's not like you couldn't before. It's just in order to do it before it was pretty laborious and you needed a fair amount of knowhow. Um now as long as you understand sort of the routine spec and more or less what I've showed you in this video, you guys are good to go. So it's an exciting time to be in AI and automation. Hopefully you guys appreciated this video. Looking forward to the next one. Catch y'all on it.

---

## Timestamped Segments

**[0:00]** Well, Anthropic just launched routines,

**[0:02]** which allows Claude to kick off

**[0:03]** automations via schedule, trigger, or

**[0:05]** even web hook. And this closes the loop

**[0:07]** and basically turns Claude into a

**[0:09]** dedicated automation platform competing

**[0:11]** with no code drag and drop builders like

**[0:13]** NADEN and others. In this video, I'm

**[0:15]** going to show you guys how you can build

**[0:16]** routines very quickly. I'm going to give

**[0:18]** you guys a couple of demos and I'm going

**[0:19]** to walk you through step by step setting

**[0:21]** up your own routines on both the Claude

**[0:23]** desktop interface as well as behind the

**[0:25]** scenes via API. Okay, so for the most

**[0:27]** prototypical example, I have a daily

**[0:29]** mailbox summary plus draft routine. And

**[0:32]** what I'm doing here is I just clicked

**[0:34]** run now because they have a little demo

**[0:36]** or test feature that allows you to

**[0:37]** actually run it and then see the inputs

**[0:39]** and outputs live. If I click on this

**[0:41]** little runs button, you'll see that all

**[0:43]** I've really done is I've just fed in a

**[0:44]** prompt. And this is the exact same thing

**[0:46]** as cloud code. It's just occurring on a

**[0:48]** standardized cloud container, not on my

**[0:51]** computer. And in this case, I'm just

**[0:53]** testing it using their interface, but

**[0:54]** you can also schedule it. You can have

**[0:56]** it trigger based off web hook. And then

**[0:58]** you can also send an API request to

**[1:00]** trigger it. And so you can trigger it

**[1:01]** based on incoming data. You can trigger

**[1:02]** it based off outgoing data. It's very

**[1:04]** powerful. If anybody has watched my

**[1:06]** previous video on Agentic Workflows,

**[1:08]** this is basically the standardized and

**[1:10]** enterprise version of Agentic Workflows.

**[1:13]** So this is now searching through Gmail

**[1:14]** emails. It's actually doing everything

**[1:16]** more or less that I would normally do if

**[1:18]** running this locally on my computer. The

**[1:20]** only difference being obviously that

**[1:22]** because it's occurring on the cloud,

**[1:24]** it's not something that I realistically

**[1:25]** am going to want to have to steer.

**[1:27]** Typically, you want to be a lot clear

**[1:28]** about the instructions and make sure

**[1:29]** that it has all the information that it

**[1:31]** needs. After that, it's just going to go

**[1:33]** through various tool calls and

**[1:34]** everything like that until it gets to

**[1:36]** the definition of done, which in my case

**[1:38]** is going to be, hey, once you're

**[1:39]** finished, use a Slack connector to send

**[1:40]** me an update. Now, on the Cloud Code

**[1:42]** docs page, the majority of the use cases

**[1:44]** are what I'd consider to be overly

**[1:46]** technical things like backlog

**[1:47]** maintenance, alert triage, bespoke code

**[1:50]** review. I mean, most people don't even

**[1:51]** know what any of the stuff means. Um,

**[1:53]** but I want you to know this is basically

**[1:55]** a standin replacement for automation.

**[1:57]** You can automate anything using this

**[1:59]** tool. And what's really cool is you can

**[2:01]** do it using natural language. So, what

**[2:03]** I've done is I've developed a cloud

**[2:04]** skill that you can import into your own

**[2:05]** workspace. Then you can just give that

**[2:07]** skill any pre-existing workflow whether

**[2:09]** it's in natural language written as an

**[2:11]** SOP or it's something on a no code tool

**[2:14]** like naden or make.com. Back to the

**[2:16]** skill page here. You can see it's found

**[2:18]** two unreads. The thing is I don't really

**[2:20]** care about this because if you think

**[2:21]** about it, this is the conversation

**[2:22]** thread. What I want to do is I want to

**[2:24]** see this Slack update that was sent to

**[2:26]** my DMs because you know if I'm using

**[2:27]** this like a traditional automation,

**[2:29]** that's where I'd probably be getting the

**[2:30]** notification. So, if I go, I actually

**[2:32]** see I did receive a notification at

**[2:34]** 12:01 where it pulled my own reds and

**[2:36]** then it fed me the information as well

**[2:38]** as like a highle summary along with a

**[2:40]** polite decline that it drafted as well

**[2:42]** as an acceptance for for this one. And I

**[2:45]** can go on to my email and I can actually

**[2:46]** open up the drafts and I could I could

**[2:47]** see them all as well. And just because

**[2:49]** I'm trying not to dox all of these

**[2:50]** people too hard, um, you know, in this

**[2:52]** case, I immediately drafted, hey Corey,

**[2:54]** thanks for reaching out. Tell the other

**[2:55]** Nick I own one. Happy to come on. Send

**[2:57]** over a few time slots that work on your

**[2:59]** end. Uh, and then I just removed the two

**[3:00]** email, but that was previously

**[3:01]** populated. Okay, so that's probably the

**[3:03]** simplest example of a demo. And I just

**[3:06]** did all this stuff uh live using the

**[3:08]** test feature because I wanted to show

**[3:09]** you that that's how it works. But you

**[3:11]** can also schedule it. And then you can

**[3:12]** also fire things off based off web hooks

**[3:14]** and API calls. So what I'm going to do

**[3:16]** next is I'm very quickly going to show

**[3:17]** you how the scheduling feature works.

**[3:18]** And then after I'm going to show you how

**[3:20]** you can use triggers like web hooks and

**[3:22]** so on and so forth to run your routines.

**[3:24]** Once we're done with that, I'll actually

**[3:25]** walk through like the UX and show you

**[3:27]** guys uh more of the deep dive behind how

**[3:29]** this works. So anyway, for scheduling

**[3:31]** purposes, all I need to do is go back to

**[3:33]** the routine that I made a moment ago. I

**[3:35]** click on this little button here, and

**[3:36]** then I can just select a different

**[3:38]** trigger. So in this case, I have call

**[3:39]** via API, but I could also click

**[3:42]** schedule. And as you see here, we have

**[3:43]** this little visual interface where I

**[3:45]** could select hourly, daily, and so on

**[3:46]** and so forth. Because this is going to

**[3:48]** be an email triage flow, I'm probably

**[3:49]** going to want to run this pretty early

**[3:50]** before I wake up. I'm waking up around

**[3:52]** 5:20 these days, so it'll probably be

**[3:53]** about 510. And what I should note is you

**[3:56]** can add multiple of these triggers at

**[3:57]** any point in time. So now after saving,

**[4:00]** if I go back to routines, you'll see

**[4:01]** there's a little calendar feature here.

**[4:03]** And you can now see that there's a daily

**[4:05]** mailbox summary plus draft opened at

**[4:07]** 5:10, as well as a couple of other ones

**[4:09]** that I was playing around with earlier

**[4:10]** today. You don't have to pay attention

**[4:11]** to those. What that means is without me

**[4:13]** having to do anything, the exact same

**[4:15]** exercise is going to occur. The agent is

**[4:17]** going to check my mailbox using the

**[4:19]** Gmail connector. It's going to run

**[4:20]** through whatever SOP or logic that I

**[4:22]** gave it, which in this case was just,

**[4:23]** hey, go see if we've had any previous

**[4:25]** email communicate. And then it's going

**[4:26]** to draft up the message and send it to

**[4:28]** me in Slack. Okay. What I have here is

**[4:30]** another routine. This one takes a

**[4:32]** transcript that is generated using

**[4:34]** Fireflies, which is a transcript service

**[4:36]** that joins your call, listens to what

**[4:38]** you say, and then basically stores it

**[4:40]** all as text. And essentially what I'm

**[4:42]** going to do just for the purposes of

**[4:43]** this demo is I'm going to do it via API

**[4:45]** request, but I'm going to show you guys

**[4:47]** as well how you can hook it up via web

**[4:48]** hook so it just fires automatically. So

**[4:50]** I have my transcript to proposal routine

**[4:52]** right over here. And I could click run

**[4:54]** now, but there's no actual transcript.

**[4:55]** The instructions here are I give you a

**[4:57]** transcript via API call. So what I'm

**[4:59]** going to do is I'm going to open up a

**[5:00]** cloud code instance. I'm just going to

**[5:02]** have it send an API request using uh

**[5:05]** this transcript.

**[5:07]** And then I'm just going to press enter.

**[5:09]** And I'm not going to expand this because

**[5:10]** I've just hard-coded an API key for uh

**[5:12]** demo purposes. But you can see here what

**[5:14]** it's going to start off by doing is

**[5:16]** basically sending that curl request as a

**[5:19]** text payload and then also generating

**[5:21]** the proposal entirely on its own. And

**[5:23]** when this occurs, it's actually going to

**[5:24]** trigger that routine. I guess I already

**[5:27]** just leaked my API key. Whatever the

**[5:29]** hell. Um it's going to fire that

**[5:31]** routine, which it's done right over

**[5:32]** here. And now it's actually running in

**[5:34]** the cloud with the full transcript and

**[5:35]** whatever the deal terms are of the, you

**[5:37]** know, conversation. And so I can

**[5:39]** actually open this up and then I can see

**[5:41]** what's going on. So you can see I give

**[5:42]** you a transcript via API call. I want

**[5:44]** you to create a full proposal using one

**[5:46]** of my other AI agents in a managed

**[5:48]** session. And this is where managed

**[5:49]** sessions come in handy, which if you

**[5:51]** guys didn't know is just a similar way

**[5:52]** that you could set up different

**[5:54]** endpoints out there that allow AI to

**[5:56]** basically create an an interconnected

**[5:59]** network of managed agents or agents that

**[6:01]** all have their own siloed containers

**[6:03]** both for security and then safety

**[6:05]** purposes. So, it's just verifying that

**[6:06]** we actually have what we need for Slack.

**[6:08]** And now it's going to go ahead and

**[6:09]** generate a high-quality proposal. Now, I

**[6:11]** just want to be clear about what problem

**[6:13]** exactly this solves. The old way of

**[6:15]** designing automations typically involved

**[6:17]** some sort of event or outside trigger

**[6:20]** like a schedule, maybe something that

**[6:22]** occurred, you know, at 5:00 a.m. every

**[6:24]** morning or whatever. That event would be

**[6:26]** fed into a platform like NAN, which was

**[6:29]** responsible for basically proceeding

**[6:31]** through a chain of logic that you

**[6:33]** created. You know, it' be a bunch of

**[6:35]** drag and drop uh nodes that you put

**[6:37]** together to do some function. In this

**[6:39]** case, this is a Reddit scraper for a

**[6:41]** live build that I did for one of my

**[6:42]** communities. And see this whole section

**[6:45]** in the middle here, this logic, this can

**[6:47]** take a fair amount of time to put

**[6:48]** together. You know, you have to drag and

**[6:49]** drop all these nodes, you have to set up

**[6:51]** all of these credentials, you have to do

**[6:52]** all the authentication, you got to get

**[6:54]** the data and and map the right variables

**[6:56]** and the fields. This is really like

**[6:57]** where the meat and potatoes of your work

**[6:59]** as somebody that was looking to automate

**[7:00]** your business um um came in. Okay? And

**[7:03]** then from there, your NAD system,

**[7:05]** typically, it doesn't just like work by

**[7:06]** itself. It does something to some

**[7:08]** platform, right? So it'll then grab its

**[7:10]** output and then shove that into Slack or

**[7:12]** maybe some sort of CRM somewhere or

**[7:14]** whatever it is that you do, some

**[7:15]** database. The new way is basically the

**[7:17]** exact same thing. You have an event,

**[7:19]** okay? And that event is either an API

**[7:21]** call. It's a web hook or it's some sort

**[7:23]** of schedule. So again, you know, waking

**[7:25]** it up at 5:00 a.m. every morning. It's

**[7:27]** just instead of putting that into NADN

**[7:28]** and then having to build all that stuff

**[7:30]** yourself with those drag and drop nodes,

**[7:32]** all you have to do, okay, is just give

**[7:34]** it some natural language which is far

**[7:37]** easier obviously with some very high

**[7:39]** level instructions and then it can then

**[7:41]** output things as uh ND did before to you

**[7:44]** know some other platform Slack or CRM

**[7:46]** and so the reason why I'm equating it

**[7:48]** like this is because routines

**[7:50]** effectively solve that middle problem.

**[7:52]** Uh I've made some videos in the past to

**[7:54]** the tune of N8N is over because XYZ

**[7:57]** thing is now launched and it does it way

**[7:58]** better and you know sometimes a specific

**[8:01]** feature was missing that you know N8N or

**[8:03]** some other no code platform handled. Um

**[8:05]** that didn't make it an exactly one to

**[8:06]** one overlap but routines are uh cla's

**[8:09]** literal 1 to1 overlap. It replaces the

**[8:11]** exact same functionality. It's capable

**[8:12]** of scheduling. It's capable of

**[8:14]** orchestrating workflows and so on and so

**[8:16]** forth. And it really is like the next

**[8:17]** step in agentic uh execution of

**[8:20]** knowledge tasks. When all this stuff

**[8:21]** finishes, I actually have the proposal

**[8:23]** right over here. I can take a look at

**[8:24]** that. Click this button to open it in a

**[8:26]** new page. And you can see I now have the

**[8:28]** proposal, which is just part of the

**[8:30]** template of the manage agent that

**[8:31]** generates this thing. Pull out all of

**[8:33]** the data. So, you know, we're an AI

**[8:35]** content writing marketplace that matches

**[8:37]** business clients with vetted freelancer

**[8:38]** writers. And then this is leftclick,

**[8:40]** which you know is pitching them. And so,

**[8:42]** these are the sorts of proposals that we

**[8:43]** actually send day-to-day. And hopefully

**[8:45]** you guys see how easy it is to actually

**[8:46]** like integrate a routine or some sort of

**[8:49]** API eventbased system into your

**[8:52]** infrastructure in like two minutes. Uh

**[8:55]** boy, have we come a long way from back

**[8:56]** in the day when me designing that

**[8:58]** proposal generator would have taken like

**[8:59]** 2 and 1 half to 3 hours. The current UX

**[9:02]** for routines looks like this. And in

**[9:03]** order to get there, all you have to do

**[9:05]** is type in cloud.ai/code/

**[9:08]** routines. You'll be given a page that

**[9:10]** looks something like this where you can

**[9:11]** see all routines stored in a grid-like

**[9:13]** pattern over here alongside their title,

**[9:16]** the time that they are running, and then

**[9:18]** also the the next scheduled run as well

**[9:20]** as what looks like some category listing

**[9:22]** which they provide uh with or without

**[9:24]** you. There's also a calendar view and so

**[9:26]** you can see the actual ones that are

**[9:28]** going to be executed and exactly which

**[9:29]** times they're going to be executed. And

**[9:31]** so here I created a couple of demos,

**[9:32]** daily nicks, arrive mention scan,

**[9:34]** morning inbox drafts and news video

**[9:36]** ideas. You can see that today this one's

**[9:38]** going to execute at 651, this one at

**[9:40]** 7:43, and this one at 8:17. So, you also

**[9:42]** get a little bit of a visual aspect

**[9:44]** there. When you click new routine up in

**[9:46]** the top right, it'll immediately ask you

**[9:47]** for some information like the name. So,

**[9:50]** I'm just going to provide a quick demo

**[9:51]** here called mailbox drafter. Next, you

**[9:54]** can describe what Claude should do in

**[9:55]** each session. So, this is where you

**[9:57]** basically give it a prompt. And this

**[9:58]** prompt is essentially analogous to a

**[10:00]** skill. Just like in a skill, you have a

**[10:02]** standardized list of steps that you need

**[10:04]** the model to take in order to perform

**[10:05]** some economically valuable piece of work

**[10:07]** for you. Um, so too should you construct

**[10:10]** this routine description like a list of

**[10:13]** SOPs or steps to allow it to perform uh

**[10:16]** a tasks for you. It's just my

**[10:17]** recommendation here is be a little bit

**[10:20]** more precise than you are probably in

**[10:22]** your skill because whereas in your skill

**[10:24]** you could modify things on the fly,

**[10:26]** change your trajectory of the task and

**[10:27]** so on and so forth, here the routine

**[10:29]** occurs entirely hands-off, meaning that

**[10:32]** it basically needs to work almost

**[10:33]** perfectly every time. So decrease the

**[10:36]** total scope of possible messups and

**[10:37]** screw-ups that it could make by being as

**[10:39]** clear and precise as possible. But for

**[10:41]** instance, I wrote pull all of my unreads

**[10:43]** using the provided Gmail connector. More

**[10:45]** on that in a sec. For each unread, check

**[10:47]** if there's any pre-existing

**[10:48]** conversations with that contact. If so,

**[10:50]** pull those two for context. Then draft

**[10:52]** replies based on what you know about me

**[10:54]** and the context of the task. Once done,

**[10:56]** use the Slack connector. More on that in

**[10:58]** a second to send me an update. And so,

**[11:01]** as you can see here, um, you know, you

**[11:03]** can make this about as long or as as

**[11:05]** short as you want. I don't believe

**[11:06]** there's a length limit. I went and I

**[11:07]** checked just by pasting this a bunch of

**[11:09]** times and I couldn't find anything. So,

**[11:11]** I would definitely lean on the side of

**[11:13]** more contacts as opposed to less. From

**[11:15]** there, you can select a repository. So,

**[11:17]** whatever repository you want. I'm just

**[11:18]** going to say this business one. You can

**[11:20]** select a model type. So, I'm going to

**[11:21]** use Opus 4.61 mil. And then you can also

**[11:24]** select which cloud environment you want

**[11:26]** to run it in. And so, you can hear

**[11:28]** basically create a cloud environment

**[11:29]** with a bunch of environment variables,

**[11:31]** keys, uh, you know, API credentials and

**[11:34]** so on and so forth as needed. So, in my

**[11:36]** case, I'm fine with default. I'm just

**[11:37]** going to move on. You can then select a

**[11:39]** trigger. So, you can schedule it. You

**[11:41]** can go via GitHub event or you can go

**[11:43]** via API. Now, realistically, this is

**[11:45]** probably something you're going to want

**[11:46]** to do on a schedule since we are just

**[11:48]** going to be going through our on reds

**[11:49]** and then drafting. But for demonstration

**[11:51]** purposes, I'm just going to go via API.

**[11:52]** And the whole idea is by doing this,

**[11:54]** I'll be able to very quickly call and

**[11:56]** then test in another Cloud Code instance

**[11:58]** to show you guys what's happening live.

**[12:00]** So, I'm just going to add a trigger. And

**[12:02]** then once we've added said trigger,

**[12:04]** we're going to receive a little curl

**[12:05]** request, which is a snippet of code that

**[12:07]** you can give any model. And finally, now

**[12:08]** we just need to add our connector. So,

**[12:10]** here I'm going to click add connector.

**[12:11]** And then I'm going to connect my own

**[12:12]** Gmail. By the way, if you don't have a

**[12:14]** connector, just head on down to Claude

**[12:16]** code settings, then go to connectors

**[12:18]** over here. Then you can actually add uh

**[12:20]** just clicking on this little connect

**[12:21]** button. When you do, it'll ask to

**[12:23]** connect Claude to your Gmail account.

**[12:25]** You can click continue and then you can

**[12:26]** sign into the particular one that you

**[12:27]** want. So, in my case, this I'm also

**[12:29]** going to need one other connector if you

**[12:31]** guys think about it because I'm going to

**[12:32]** want a Slack message sent. So, here I

**[12:34]** can use this little search bar and then

**[12:35]** click a plus button. Then I'll just have

**[12:37]** to perform again some OOTH in a new

**[12:38]** browser tab. Here I'm going to click

**[12:40]** allow. And just like any simple OOTH

**[12:42]** screen, we're now going to be connected.

**[12:44]** So now what we can do is we can go back

**[12:45]** to the routine and then I can add the

**[12:47]** connector manually. From here, you'll be

**[12:49]** given a token. You can copy that token,

**[12:51]** store it somewhere safe. So that's what

**[12:52]** I'm going to do here. And now we

**[12:54]** basically have our skill or our routine

**[12:57]** ready to go. Okay. And then once you're

**[12:59]** done, just head over to the run now in

**[13:01]** the top right hand corner to basically

**[13:02]** start the workflow run. And uh we're

**[13:04]** just going to do this here using the GUI

**[13:06]** graphical user interface for testing

**[13:08]** purposes. But you'll see a new little

**[13:09]** run just populated. So I'm going to go

**[13:11]** down here and you'll see all we're

**[13:12]** really doing is we're just sending it

**[13:14]** this message. Once it's done, it'll use

**[13:16]** the Slack connector to send me an

**[13:17]** update. You can see it's already

**[13:18]** starting to fire off a tool search. So

**[13:20]** I'll just double back when it's done.

**[13:21]** And I should note, I mean, I'm watching

**[13:22]** it here, but the whole idea is that I

**[13:24]** don't even know that this thing's going

**[13:25]** on, right? This was triggered uh ideally

**[13:28]** on a schedule or something like that,

**[13:29]** and I just wake up in the morning to my

**[13:31]** Slack uh message with a bunch of

**[13:33]** different emails and their various

**[13:34]** drafts. If I head back over here, you

**[13:37]** can see that we actually have both of

**[13:38]** those fed in. Um, looks like somebody

**[13:40]** invited me for a podcast interview and

**[13:42]** then somebody else asked me a couple of

**[13:44]** questions about a few things here.

**[13:46]** Finally, I want to show you guys how

**[13:47]** easy it is to convert workflows that you

**[13:49]** built on third party tools like NAD, for

**[13:51]** instance, into routines. And what's

**[13:54]** really cool about NAND is they allow you

**[13:56]** just to like mouse over if you hold

**[13:57]** shift and then hold command C or just

**[14:00]** right click and press copy. And then now

**[14:02]** you basically have access to a bunch of

**[14:03]** JSON. And you could tell just by me

**[14:05]** pasting it in. This is like JSON or the

**[14:07]** syntax that these nodes are represented

**[14:09]** in if we're talking through text. Well,

**[14:11]** anyway, if I go back to anti-gravity,

**[14:13]** which contains my little cloud code

**[14:14]** window, and then I type in this JSON,

**[14:17]** and then at the very top, I say use the

**[14:19]** routine generator to turn this naden

**[14:22]** workflow into a routine. Okay, I'm just

**[14:26]** going to divide this to make it really

**[14:27]** simple. Uh what this is going to do is

**[14:29]** use the skill that I'm giving all of you

**[14:30]** guys out of the box to basically turn

**[14:32]** this into a flow that we can call just

**[14:34]** using natural language. So I'm not

**[14:36]** necessarily going to encourage you to

**[14:37]** use all of your workflows or to port

**[14:39]** them over from NADN or some other no

**[14:41]** code tool to uh claude's back end.

**[14:43]** Reason being is you know when you're

**[14:44]** dealing in the domain of tokens things

**[14:46]** are going to be a little bit more

**[14:47]** expensive than dealing entirely in the

**[14:48]** domain of compute. And really the point

**[14:50]** is not hey just turn all your nadn or

**[14:53]** make.com workflows into routines. The

**[14:55]** point is more like, you know, if you

**[14:56]** have something you can build today that

**[14:58]** previously would have taken you a couple

**[15:00]** of hours in NAN, might make more sense

**[15:01]** just to oneshot it as a routine. But,

**[15:04]** um, you know, what this will do really

**[15:05]** quickly is just go ahead and do the

**[15:06]** creation. So, as you guys can see here,

**[15:08]** it's doing some thinking. It's loading

**[15:09]** the routines. In this case, it's just

**[15:11]** going to schedule one cuz I didn't

**[15:12]** provide any context as to how I wanted

**[15:13]** to run it. Um, but yeah, here we go.

**[15:15]** It's now going to fetch stories from the

**[15:16]** HackerN Algolia API, extract the hits,

**[15:19]** format them into a markdown report, and

**[15:21]** commit it, which was what the actual

**[15:22]** flow was doing. So, just like this one

**[15:24]** here, if I click execute workflow, this

**[15:27]** goes through the scraper. It then

**[15:28]** generates a bunch of hits basically from

**[15:31]** um a website called Hacker News.

**[15:33]** HackerNews is the source here, which in

**[15:35]** this case is going to contain a bunch of

**[15:37]** different um comments like this one on

**[15:38]** how open source AI is the path forward.

**[15:41]** Certainly not when Claude drops a

**[15:42]** freaking update like this. Well, the

**[15:44]** same routine is going to work here the

**[15:46]** exact same way. And you can see it just

**[15:47]** said routine created and fired hacker

**[15:49]** use AI stories fetch, right? And what's

**[15:51]** really cool about this is I mean it's

**[15:52]** it's just so easy for me to to change

**[15:55]** things. Um so I mean right now this is

**[15:57]** obviously going to fetch that data,

**[15:58]** right? And you know fetching that data

**[16:00]** is okay, but what am I going to do with

**[16:01]** it? It's just sort of like stuck here,

**[16:03]** right? You know, if I were in NAD, I'd

**[16:04]** have to modify this. Uh it'd be

**[16:06]** significantly harder to modify this

**[16:07]** here. I can literally just go connectors

**[16:10]** Slack. Okay, save. I can then set it to

**[16:12]** run on, you know, 733 MDT or via API

**[16:17]** request, which I'm going to click done.

**[16:18]** And now what I can also do is I can go

**[16:19]** back here and I can say great, update

**[16:21]** this so that it sends me a message in

**[16:24]** Slack with the scrape after it's done.

**[16:28]** And now in 3 seconds, you know, it can

**[16:30]** make an HTTP request over to the routine

**[16:32]** and just edit it on the fly for me. I

**[16:34]** don't have to drag and drop any notes.

**[16:35]** It's much easier and much faster. Okay,

**[16:37]** so hopefully you guys can see that this

**[16:39]** has a lot of potential and you're likely

**[16:42]** to see larger and larger flows be passed

**[16:44]** off to agents in this manner. Um, I

**[16:48]** didn't really give you guys an

**[16:49]** extraordinarily comprehensive look at

**[16:50]** all the different things you could do

**[16:51]** with this, but just off the top of my

**[16:53]** head, some ways that I'm implementing

**[16:55]** this in my agency today, some ways that

**[16:57]** I've already done so, and some ways that

**[16:58]** I can I'm going to continue to do so

**[17:00]** after this video are I'm going to

**[17:02]** replace all of my proposal generators

**[17:03]** with these built-in routines. I'm going

**[17:05]** to connect a couple of additional

**[17:07]** routines so that after a call, like a a

**[17:09]** sales call with a prospect, um, I'll

**[17:12]** receive a web hook with um, essentially

**[17:14]** like a transcript. I'm going to feed

**[17:15]** that transcript into a routine that's

**[17:17]** going to generate an immediate post call

**[17:18]** email and then uh like a workflow

**[17:21]** diagram draft based on our conversations

**[17:23]** that I can also pin alongside it just

**[17:25]** for the impression of of more effort and

**[17:27]** higher perceived quality. Uh when we

**[17:29]** send out the proposal, I'm going to be

**[17:30]** monitoring to see if somebody's signed.

**[17:32]** When they do, it's going to route back

**[17:33]** to another routine via a web hook, which

**[17:35]** is going to proceed with the next step,

**[17:37]** which is sending them a message with an

**[17:38]** email with an onboarding uh you know,

**[17:40]** calendar notification, as well as

**[17:42]** congratulating them and thanking them on

**[17:43]** on coming aboard.

**[17:45]** You guys can automate more or less all

**[17:46]** of the non like human facetime steps in

**[17:49]** a business right now. And it's not like

**[17:51]** you couldn't before. It's just in order

**[17:52]** to do it before it was pretty laborious

**[17:54]** and you needed a fair amount of knowhow.

**[17:55]** Um now as long as you understand sort of

**[17:57]** the routine spec and more or less what

**[17:58]** I've showed you in this video, you guys

**[18:00]** are good to go. So it's an exciting time

**[18:02]** to be in AI and automation. Hopefully

**[18:03]** you guys appreciated this video. Looking

**[18:05]** forward to the next one. Catch y'all on

**[18:06]** it.

**[0:00]** Well, Anthropic just launched routines,

**[0:02]** which allows Claude to kick off

**[0:03]** automations via schedule, trigger, or

**[0:05]** even web hook. And this closes the loop

**[0:07]** and basically turns Claude into a

**[0:09]** dedicated automation platform competing

**[0:11]** with no code drag and drop builders like

**[0:13]** NADEN and others. In this video, I'm

**[0:15]** going to show you guys how you can build

**[0:16]** routines very quickly. I'm going to give

**[0:18]** you guys a couple of demos and I'm going

**[0:19]** to walk you through step by step setting

**[0:21]** up your own routines on both the Claude

**[0:23]** desktop interface as well as behind the

**[0:25]** scenes via API. Okay, so for the most

**[0:27]** prototypical example, I have a daily

**[0:29]** mailbox summary plus draft routine. And

**[0:32]** what I'm doing here is I just clicked

**[0:34]** run now because they have a little demo

**[0:36]** or test feature that allows you to

**[0:37]** actually run it and then see the inputs

**[0:39]** and outputs live. If I click on this

**[0:41]** little runs button, you'll see that all

**[0:43]** I've really done is I've just fed in a

**[0:44]** prompt. And this is the exact same thing

**[0:46]** as cloud code. It's just occurring on a

**[0:48]** standardized cloud container, not on my

**[0:51]** computer. And in this case, I'm just

**[0:53]** testing it using their interface, but

**[0:54]** you can also schedule it. You can have

**[0:56]** it trigger based off web hook. And then

**[0:58]** you can also send an API request to

**[1:00]** trigger it. And so you can trigger it

**[1:01]** based on incoming data. You can trigger

**[1:02]** it based off outgoing data. It's very

**[1:04]** powerful. If anybody has watched my

**[1:06]** previous video on Agentic Workflows,

**[1:08]** this is basically the standardized and

**[1:10]** enterprise version of Agentic Workflows.

**[1:13]** So this is now searching through Gmail

**[1:14]** emails. It's actually doing everything

**[1:16]** more or less that I would normally do if

**[1:18]** running this locally on my computer. The

**[1:20]** only difference being obviously that

**[1:22]** because it's occurring on the cloud,

**[1:24]** it's not something that I realistically

**[1:25]** am going to want to have to steer.

**[1:27]** Typically, you want to be a lot clear

**[1:28]** about the instructions and make sure

**[1:29]** that it has all the information that it

**[1:31]** needs. After that, it's just going to go

**[1:33]** through various tool calls and

**[1:34]** everything like that until it gets to

**[1:36]** the definition of done, which in my case

**[1:38]** is going to be, hey, once you're

**[1:39]** finished, use a Slack connector to send

**[1:40]** me an update. Now, on the Cloud Code

**[1:42]** docs page, the majority of the use cases

**[1:44]** are what I'd consider to be overly

**[1:46]** technical things like backlog

**[1:47]** maintenance, alert triage, bespoke code

**[1:50]** review. I mean, most people don't even

**[1:51]** know what any of the stuff means. Um,

**[1:53]** but I want you to know this is basically

**[1:55]** a standin replacement for automation.

**[1:57]** You can automate anything using this

**[1:59]** tool. And what's really cool is you can

**[2:01]** do it using natural language. So, what

**[2:03]** I've done is I've developed a cloud

**[2:04]** skill that you can import into your own

**[2:05]** workspace. Then you can just give that

**[2:07]** skill any pre-existing workflow whether

**[2:09]** it's in natural language written as an

**[2:11]** SOP or it's something on a no code tool

**[2:14]** like naden or make.com. Back to the

**[2:16]** skill page here. You can see it's found

**[2:18]** two unreads. The thing is I don't really

**[2:20]** care about this because if you think

**[2:21]** about it, this is the conversation

**[2:22]** thread. What I want to do is I want to

**[2:24]** see this Slack update that was sent to

**[2:26]** my DMs because you know if I'm using

**[2:27]** this like a traditional automation,

**[2:29]** that's where I'd probably be getting the

**[2:30]** notification. So, if I go, I actually

**[2:32]** see I did receive a notification at

**[2:34]** 12:01 where it pulled my own reds and

**[2:36]** then it fed me the information as well

**[2:38]** as like a highle summary along with a

**[2:40]** polite decline that it drafted as well

**[2:42]** as an acceptance for for this one. And I

**[2:45]** can go on to my email and I can actually

**[2:46]** open up the drafts and I could I could

**[2:47]** see them all as well. And just because

**[2:49]** I'm trying not to dox all of these

**[2:50]** people too hard, um, you know, in this

**[2:52]** case, I immediately drafted, hey Corey,

**[2:54]** thanks for reaching out. Tell the other

**[2:55]** Nick I own one. Happy to come on. Send

**[2:57]** over a few time slots that work on your

**[2:59]** end. Uh, and then I just removed the two

**[3:00]** email, but that was previously

**[3:01]** populated. Okay, so that's probably the

**[3:03]** simplest example of a demo. And I just

**[3:06]** did all this stuff uh live using the

**[3:08]** test feature because I wanted to show

**[3:09]** you that that's how it works. But you

**[3:11]** can also schedule it. And then you can

**[3:12]** also fire things off based off web hooks

**[3:14]** and API calls. So what I'm going to do

**[3:16]** next is I'm very quickly going to show

**[3:17]** you how the scheduling feature works.

**[3:18]** And then after I'm going to show you how

**[3:20]** you can use triggers like web hooks and

**[3:22]** so on and so forth to run your routines.

**[3:24]** Once we're done with that, I'll actually

**[3:25]** walk through like the UX and show you

**[3:27]** guys uh more of the deep dive behind how

**[3:29]** this works. So anyway, for scheduling

**[3:31]** purposes, all I need to do is go back to

**[3:33]** the routine that I made a moment ago. I

**[3:35]** click on this little button here, and

**[3:36]** then I can just select a different

**[3:38]** trigger. So in this case, I have call

**[3:39]** via API, but I could also click

**[3:42]** schedule. And as you see here, we have

**[3:43]** this little visual interface where I

**[3:45]** could select hourly, daily, and so on

**[3:46]** and so forth. Because this is going to

**[3:48]** be an email triage flow, I'm probably

**[3:49]** going to want to run this pretty early

**[3:50]** before I wake up. I'm waking up around

**[3:52]** 5:20 these days, so it'll probably be

**[3:53]** about 510. And what I should note is you

**[3:56]** can add multiple of these triggers at

**[3:57]** any point in time. So now after saving,

**[4:00]** if I go back to routines, you'll see

**[4:01]** there's a little calendar feature here.

**[4:03]** And you can now see that there's a daily

**[4:05]** mailbox summary plus draft opened at

**[4:07]** 5:10, as well as a couple of other ones

**[4:09]** that I was playing around with earlier

**[4:10]** today. You don't have to pay attention

**[4:11]** to those. What that means is without me

**[4:13]** having to do anything, the exact same

**[4:15]** exercise is going to occur. The agent is

**[4:17]** going to check my mailbox using the

**[4:19]** Gmail connector. It's going to run

**[4:20]** through whatever SOP or logic that I

**[4:22]** gave it, which in this case was just,

**[4:23]** hey, go see if we've had any previous

**[4:25]** email communicate. And then it's going

**[4:26]** to draft up the message and send it to

**[4:28]** me in Slack. Okay. What I have here is

**[4:30]** another routine. This one takes a

**[4:32]** transcript that is generated using

**[4:34]** Fireflies, which is a transcript service

**[4:36]** that joins your call, listens to what

**[4:38]** you say, and then basically stores it

**[4:40]** all as text. And essentially what I'm

**[4:42]** going to do just for the purposes of

**[4:43]** this demo is I'm going to do it via API

**[4:45]** request, but I'm going to show you guys

**[4:47]** as well how you can hook it up via web

**[4:48]** hook so it just fires automatically. So

**[4:50]** I have my transcript to proposal routine

**[4:52]** right over here. And I could click run

**[4:54]** now, but there's no actual transcript.

**[4:55]** The instructions here are I give you a

**[4:57]** transcript via API call. So what I'm

**[4:59]** going to do is I'm going to open up a

**[5:00]** cloud code instance. I'm just going to

**[5:02]** have it send an API request using uh

**[5:05]** this transcript.

**[5:07]** And then I'm just going to press enter.

**[5:09]** And I'm not going to expand this because

**[5:10]** I've just hard-coded an API key for uh

**[5:12]** demo purposes. But you can see here what

**[5:14]** it's going to start off by doing is

**[5:16]** basically sending that curl request as a

**[5:19]** text payload and then also generating

**[5:21]** the proposal entirely on its own. And

**[5:23]** when this occurs, it's actually going to

**[5:24]** trigger that routine. I guess I already

**[5:27]** just leaked my API key. Whatever the

**[5:29]** hell. Um it's going to fire that

**[5:31]** routine, which it's done right over

**[5:32]** here. And now it's actually running in

**[5:34]** the cloud with the full transcript and

**[5:35]** whatever the deal terms are of the, you

**[5:37]** know, conversation. And so I can

**[5:39]** actually open this up and then I can see

**[5:41]** what's going on. So you can see I give

**[5:42]** you a transcript via API call. I want

**[5:44]** you to create a full proposal using one

**[5:46]** of my other AI agents in a managed

**[5:48]** session. And this is where managed

**[5:49]** sessions come in handy, which if you

**[5:51]** guys didn't know is just a similar way

**[5:52]** that you could set up different

**[5:54]** endpoints out there that allow AI to

**[5:56]** basically create an an interconnected

**[5:59]** network of managed agents or agents that

**[6:01]** all have their own siloed containers

**[6:03]** both for security and then safety

**[6:05]** purposes. So, it's just verifying that

**[6:06]** we actually have what we need for Slack.

**[6:08]** And now it's going to go ahead and

**[6:09]** generate a high-quality proposal. Now, I

**[6:11]** just want to be clear about what problem

**[6:13]** exactly this solves. The old way of

**[6:15]** designing automations typically involved

**[6:17]** some sort of event or outside trigger

**[6:20]** like a schedule, maybe something that

**[6:22]** occurred, you know, at 5:00 a.m. every

**[6:24]** morning or whatever. That event would be

**[6:26]** fed into a platform like NAN, which was

**[6:29]** responsible for basically proceeding

**[6:31]** through a chain of logic that you

**[6:33]** created. You know, it' be a bunch of

**[6:35]** drag and drop uh nodes that you put

**[6:37]** together to do some function. In this

**[6:39]** case, this is a Reddit scraper for a

**[6:41]** live build that I did for one of my

**[6:42]** communities. And see this whole section

**[6:45]** in the middle here, this logic, this can

**[6:47]** take a fair amount of time to put

**[6:48]** together. You know, you have to drag and

**[6:49]** drop all these nodes, you have to set up

**[6:51]** all of these credentials, you have to do

**[6:52]** all the authentication, you got to get

**[6:54]** the data and and map the right variables

**[6:56]** and the fields. This is really like

**[6:57]** where the meat and potatoes of your work

**[6:59]** as somebody that was looking to automate

**[7:00]** your business um um came in. Okay? And

**[7:03]** then from there, your NAD system,

**[7:05]** typically, it doesn't just like work by

**[7:06]** itself. It does something to some

**[7:08]** platform, right? So it'll then grab its

**[7:10]** output and then shove that into Slack or

**[7:12]** maybe some sort of CRM somewhere or

**[7:14]** whatever it is that you do, some

**[7:15]** database. The new way is basically the

**[7:17]** exact same thing. You have an event,

**[7:19]** okay? And that event is either an API

**[7:21]** call. It's a web hook or it's some sort

**[7:23]** of schedule. So again, you know, waking

**[7:25]** it up at 5:00 a.m. every morning. It's

**[7:27]** just instead of putting that into NADN

**[7:28]** and then having to build all that stuff

**[7:30]** yourself with those drag and drop nodes,

**[7:32]** all you have to do, okay, is just give

**[7:34]** it some natural language which is far

**[7:37]** easier obviously with some very high

**[7:39]** level instructions and then it can then

**[7:41]** output things as uh ND did before to you

**[7:44]** know some other platform Slack or CRM

**[7:46]** and so the reason why I'm equating it

**[7:48]** like this is because routines

**[7:50]** effectively solve that middle problem.

**[7:52]** Uh I've made some videos in the past to

**[7:54]** the tune of N8N is over because XYZ

**[7:57]** thing is now launched and it does it way

**[7:58]** better and you know sometimes a specific

**[8:01]** feature was missing that you know N8N or

**[8:03]** some other no code platform handled. Um

**[8:05]** that didn't make it an exactly one to

**[8:06]** one overlap but routines are uh cla's

**[8:09]** literal 1 to1 overlap. It replaces the

**[8:11]** exact same functionality. It's capable

**[8:12]** of scheduling. It's capable of

**[8:14]** orchestrating workflows and so on and so

**[8:16]** forth. And it really is like the next

**[8:17]** step in agentic uh execution of

**[8:20]** knowledge tasks. When all this stuff

**[8:21]** finishes, I actually have the proposal

**[8:23]** right over here. I can take a look at

**[8:24]** that. Click this button to open it in a

**[8:26]** new page. And you can see I now have the

**[8:28]** proposal, which is just part of the

**[8:30]** template of the manage agent that

**[8:31]** generates this thing. Pull out all of

**[8:33]** the data. So, you know, we're an AI

**[8:35]** content writing marketplace that matches

**[8:37]** business clients with vetted freelancer

**[8:38]** writers. And then this is leftclick,

**[8:40]** which you know is pitching them. And so,

**[8:42]** these are the sorts of proposals that we

**[8:43]** actually send day-to-day. And hopefully

**[8:45]** you guys see how easy it is to actually

**[8:46]** like integrate a routine or some sort of

**[8:49]** API eventbased system into your

**[8:52]** infrastructure in like two minutes. Uh

**[8:55]** boy, have we come a long way from back

**[8:56]** in the day when me designing that

**[8:58]** proposal generator would have taken like

**[8:59]** 2 and 1 half to 3 hours. The current UX

**[9:02]** for routines looks like this. And in

**[9:03]** order to get there, all you have to do

**[9:05]** is type in cloud.ai/code/

**[9:08]** routines. You'll be given a page that

**[9:10]** looks something like this where you can

**[9:11]** see all routines stored in a grid-like

**[9:13]** pattern over here alongside their title,

**[9:16]** the time that they are running, and then

**[9:18]** also the the next scheduled run as well

**[9:20]** as what looks like some category listing

**[9:22]** which they provide uh with or without

**[9:24]** you. There's also a calendar view and so

**[9:26]** you can see the actual ones that are

**[9:28]** going to be executed and exactly which

**[9:29]** times they're going to be executed. And

**[9:31]** so here I created a couple of demos,

**[9:32]** daily nicks, arrive mention scan,

**[9:34]** morning inbox drafts and news video

**[9:36]** ideas. You can see that today this one's

**[9:38]** going to execute at 651, this one at

**[9:40]** 7:43, and this one at 8:17. So, you also

**[9:42]** get a little bit of a visual aspect

**[9:44]** there. When you click new routine up in

**[9:46]** the top right, it'll immediately ask you

**[9:47]** for some information like the name. So,

**[9:50]** I'm just going to provide a quick demo

**[9:51]** here called mailbox drafter. Next, you

**[9:54]** can describe what Claude should do in

**[9:55]** each session. So, this is where you

**[9:57]** basically give it a prompt. And this

**[9:58]** prompt is essentially analogous to a

**[10:00]** skill. Just like in a skill, you have a

**[10:02]** standardized list of steps that you need

**[10:04]** the model to take in order to perform

**[10:05]** some economically valuable piece of work

**[10:07]** for you. Um, so too should you construct

**[10:10]** this routine description like a list of

**[10:13]** SOPs or steps to allow it to perform uh

**[10:16]** a tasks for you. It's just my

**[10:17]** recommendation here is be a little bit

**[10:20]** more precise than you are probably in

**[10:22]** your skill because whereas in your skill

**[10:24]** you could modify things on the fly,

**[10:26]** change your trajectory of the task and

**[10:27]** so on and so forth, here the routine

**[10:29]** occurs entirely hands-off, meaning that

**[10:32]** it basically needs to work almost

**[10:33]** perfectly every time. So decrease the

**[10:36]** total scope of possible messups and

**[10:37]** screw-ups that it could make by being as

**[10:39]** clear and precise as possible. But for

**[10:41]** instance, I wrote pull all of my unreads

**[10:43]** using the provided Gmail connector. More

**[10:45]** on that in a sec. For each unread, check

**[10:47]** if there's any pre-existing

**[10:48]** conversations with that contact. If so,

**[10:50]** pull those two for context. Then draft

**[10:52]** replies based on what you know about me

**[10:54]** and the context of the task. Once done,

**[10:56]** use the Slack connector. More on that in

**[10:58]** a second to send me an update. And so,

**[11:01]** as you can see here, um, you know, you

**[11:03]** can make this about as long or as as

**[11:05]** short as you want. I don't believe

**[11:06]** there's a length limit. I went and I

**[11:07]** checked just by pasting this a bunch of

**[11:09]** times and I couldn't find anything. So,

**[11:11]** I would definitely lean on the side of

**[11:13]** more contacts as opposed to less. From

**[11:15]** there, you can select a repository. So,

**[11:17]** whatever repository you want. I'm just

**[11:18]** going to say this business one. You can

**[11:20]** select a model type. So, I'm going to

**[11:21]** use Opus 4.61 mil. And then you can also

**[11:24]** select which cloud environment you want

**[11:26]** to run it in. And so, you can hear

**[11:28]** basically create a cloud environment

**[11:29]** with a bunch of environment variables,

**[11:31]** keys, uh, you know, API credentials and

**[11:34]** so on and so forth as needed. So, in my

**[11:36]** case, I'm fine with default. I'm just

**[11:37]** going to move on. You can then select a

**[11:39]** trigger. So, you can schedule it. You

**[11:41]** can go via GitHub event or you can go

**[11:43]** via API. Now, realistically, this is

**[11:45]** probably something you're going to want

**[11:46]** to do on a schedule since we are just

**[11:48]** going to be going through our on reds

**[11:49]** and then drafting. But for demonstration

**[11:51]** purposes, I'm just going to go via API.

**[11:52]** And the whole idea is by doing this,

**[11:54]** I'll be able to very quickly call and

**[11:56]** then test in another Cloud Code instance

**[11:58]** to show you guys what's happening live.

**[12:00]** So, I'm just going to add a trigger. And

**[12:02]** then once we've added said trigger,

**[12:04]** we're going to receive a little curl

**[12:05]** request, which is a snippet of code that

**[12:07]** you can give any model. And finally, now

**[12:08]** we just need to add our connector. So,

**[12:10]** here I'm going to click add connector.

**[12:11]** And then I'm going to connect my own

**[12:12]** Gmail. By the way, if you don't have a

**[12:14]** connector, just head on down to Claude

**[12:16]** code settings, then go to connectors

**[12:18]** over here. Then you can actually add uh

**[12:20]** just clicking on this little connect

**[12:21]** button. When you do, it'll ask to

**[12:23]** connect Claude to your Gmail account.

**[12:25]** You can click continue and then you can

**[12:26]** sign into the particular one that you

**[12:27]** want. So, in my case, this I'm also

**[12:29]** going to need one other connector if you

**[12:31]** guys think about it because I'm going to

**[12:32]** want a Slack message sent. So, here I

**[12:34]** can use this little search bar and then

**[12:35]** click a plus button. Then I'll just have

**[12:37]** to perform again some OOTH in a new

**[12:38]** browser tab. Here I'm going to click

**[12:40]** allow. And just like any simple OOTH

**[12:42]** screen, we're now going to be connected.

**[12:44]** So now what we can do is we can go back

**[12:45]** to the routine and then I can add the

**[12:47]** connector manually. From here, you'll be

**[12:49]** given a token. You can copy that token,

**[12:51]** store it somewhere safe. So that's what

**[12:52]** I'm going to do here. And now we

**[12:54]** basically have our skill or our routine

**[12:57]** ready to go. Okay. And then once you're

**[12:59]** done, just head over to the run now in

**[13:01]** the top right hand corner to basically

**[13:02]** start the workflow run. And uh we're

**[13:04]** just going to do this here using the GUI

**[13:06]** graphical user interface for testing

**[13:08]** purposes. But you'll see a new little

**[13:09]** run just populated. So I'm going to go

**[13:11]** down here and you'll see all we're

**[13:12]** really doing is we're just sending it

**[13:14]** this message. Once it's done, it'll use

**[13:16]** the Slack connector to send me an

**[13:17]** update. You can see it's already

**[13:18]** starting to fire off a tool search. So

**[13:20]** I'll just double back when it's done.

**[13:21]** And I should note, I mean, I'm watching

**[13:22]** it here, but the whole idea is that I

**[13:24]** don't even know that this thing's going

**[13:25]** on, right? This was triggered uh ideally

**[13:28]** on a schedule or something like that,

**[13:29]** and I just wake up in the morning to my

**[13:31]** Slack uh message with a bunch of

**[13:33]** different emails and their various

**[13:34]** drafts. If I head back over here, you

**[13:37]** can see that we actually have both of

**[13:38]** those fed in. Um, looks like somebody

**[13:40]** invited me for a podcast interview and

**[13:42]** then somebody else asked me a couple of

**[13:44]** questions about a few things here.

**[13:46]** Finally, I want to show you guys how

**[13:47]** easy it is to convert workflows that you

**[13:49]** built on third party tools like NAD, for

**[13:51]** instance, into routines. And what's

**[13:54]** really cool about NAND is they allow you

**[13:56]** just to like mouse over if you hold

**[13:57]** shift and then hold command C or just

**[14:00]** right click and press copy. And then now

**[14:02]** you basically have access to a bunch of

**[14:03]** JSON. And you could tell just by me

**[14:05]** pasting it in. This is like JSON or the

**[14:07]** syntax that these nodes are represented

**[14:09]** in if we're talking through text. Well,

**[14:11]** anyway, if I go back to anti-gravity,

**[14:13]** which contains my little cloud code

**[14:14]** window, and then I type in this JSON,

**[14:17]** and then at the very top, I say use the

**[14:19]** routine generator to turn this naden

**[14:22]** workflow into a routine. Okay, I'm just

**[14:26]** going to divide this to make it really

**[14:27]** simple. Uh what this is going to do is

**[14:29]** use the skill that I'm giving all of you

**[14:30]** guys out of the box to basically turn

**[14:32]** this into a flow that we can call just

**[14:34]** using natural language. So I'm not

**[14:36]** necessarily going to encourage you to

**[14:37]** use all of your workflows or to port

**[14:39]** them over from NADN or some other no

**[14:41]** code tool to uh claude's back end.

**[14:43]** Reason being is you know when you're

**[14:44]** dealing in the domain of tokens things

**[14:46]** are going to be a little bit more

**[14:47]** expensive than dealing entirely in the

**[14:48]** domain of compute. And really the point

**[14:50]** is not hey just turn all your nadn or

**[14:53]** make.com workflows into routines. The

**[14:55]** point is more like, you know, if you

**[14:56]** have something you can build today that

**[14:58]** previously would have taken you a couple

**[15:00]** of hours in NAN, might make more sense

**[15:01]** just to oneshot it as a routine. But,

**[15:04]** um, you know, what this will do really

**[15:05]** quickly is just go ahead and do the

**[15:06]** creation. So, as you guys can see here,

**[15:08]** it's doing some thinking. It's loading

**[15:09]** the routines. In this case, it's just

**[15:11]** going to schedule one cuz I didn't

**[15:12]** provide any context as to how I wanted

**[15:13]** to run it. Um, but yeah, here we go.

**[15:15]** It's now going to fetch stories from the

**[15:16]** HackerN Algolia API, extract the hits,

**[15:19]** format them into a markdown report, and

**[15:21]** commit it, which was what the actual

**[15:22]** flow was doing. So, just like this one

**[15:24]** here, if I click execute workflow, this

**[15:27]** goes through the scraper. It then

**[15:28]** generates a bunch of hits basically from

**[15:31]** um a website called Hacker News.

**[15:33]** HackerNews is the source here, which in

**[15:35]** this case is going to contain a bunch of

**[15:37]** different um comments like this one on

**[15:38]** how open source AI is the path forward.

**[15:41]** Certainly not when Claude drops a

**[15:42]** freaking update like this. Well, the

**[15:44]** same routine is going to work here the

**[15:46]** exact same way. And you can see it just

**[15:47]** said routine created and fired hacker

**[15:49]** use AI stories fetch, right? And what's

**[15:51]** really cool about this is I mean it's

**[15:52]** it's just so easy for me to to change

**[15:55]** things. Um so I mean right now this is

**[15:57]** obviously going to fetch that data,

**[15:58]** right? And you know fetching that data

**[16:00]** is okay, but what am I going to do with

**[16:01]** it? It's just sort of like stuck here,

**[16:03]** right? You know, if I were in NAD, I'd

**[16:04]** have to modify this. Uh it'd be

**[16:06]** significantly harder to modify this

**[16:07]** here. I can literally just go connectors

**[16:10]** Slack. Okay, save. I can then set it to

**[16:12]** run on, you know, 733 MDT or via API

**[16:17]** request, which I'm going to click done.

**[16:18]** And now what I can also do is I can go

**[16:19]** back here and I can say great, update

**[16:21]** this so that it sends me a message in

**[16:24]** Slack with the scrape after it's done.

**[16:28]** And now in 3 seconds, you know, it can

**[16:30]** make an HTTP request over to the routine

**[16:32]** and just edit it on the fly for me. I

**[16:34]** don't have to drag and drop any notes.

**[16:35]** It's much easier and much faster. Okay,

**[16:37]** so hopefully you guys can see that this

**[16:39]** has a lot of potential and you're likely

**[16:42]** to see larger and larger flows be passed

**[16:44]** off to agents in this manner. Um, I

**[16:48]** didn't really give you guys an

**[16:49]** extraordinarily comprehensive look at

**[16:50]** all the different things you could do

**[16:51]** with this, but just off the top of my

**[16:53]** head, some ways that I'm implementing

**[16:55]** this in my agency today, some ways that

**[16:57]** I've already done so, and some ways that

**[16:58]** I can I'm going to continue to do so

**[17:00]** after this video are I'm going to

**[17:02]** replace all of my proposal generators

**[17:03]** with these built-in routines. I'm going

**[17:05]** to connect a couple of additional

**[17:07]** routines so that after a call, like a a

**[17:09]** sales call with a prospect, um, I'll

**[17:12]** receive a web hook with um, essentially

**[17:14]** like a transcript. I'm going to feed

**[17:15]** that transcript into a routine that's

**[17:17]** going to generate an immediate post call

**[17:18]** email and then uh like a workflow

**[17:21]** diagram draft based on our conversations

**[17:23]** that I can also pin alongside it just

**[17:25]** for the impression of of more effort and

**[17:27]** higher perceived quality. Uh when we

**[17:29]** send out the proposal, I'm going to be

**[17:30]** monitoring to see if somebody's signed.

**[17:32]** When they do, it's going to route back

**[17:33]** to another routine via a web hook, which

**[17:35]** is going to proceed with the next step,

**[17:37]** which is sending them a message with an

**[17:38]** email with an onboarding uh you know,

**[17:40]** calendar notification, as well as

**[17:42]** congratulating them and thanking them on

**[17:43]** on coming aboard.

**[17:45]** You guys can automate more or less all

**[17:46]** of the non like human facetime steps in

**[17:49]** a business right now. And it's not like

**[17:51]** you couldn't before. It's just in order

**[17:52]** to do it before it was pretty laborious

**[17:54]** and you needed a fair amount of knowhow.

**[17:55]** Um now as long as you understand sort of

**[17:57]** the routine spec and more or less what

**[17:58]** I've showed you in this video, you guys

**[18:00]** are good to go. So it's an exciting time

**[18:02]** to be in AI and automation. Hopefully

**[18:03]** you guys appreciated this video. Looking

**[18:05]** forward to the next one. Catch y'all on

**[18:06]** it.
