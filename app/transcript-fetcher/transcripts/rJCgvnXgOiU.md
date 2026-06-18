# Transcript: rJCgvnXgOiU

**URL:** https://www.youtube.com/watch?v=rJCgvnXgOiU
**Segments:** 545

---

## Full Text

Almost every rag system suffers from the exact same problem. They can only handle text documents. So if you try to give it images, charts, graphs, whatever, most rag systems just can't handle it. And when I showed you light rag yesterday, it suffered from the exact same problem. But today, I'm going to show you the fix. And that fix is rag anything. Rag anything solves this document problem for us. It can handle images. It can handle charts. It can handle graphs. And it allows us to create a rag system that actually deals with the documents you use. Rag anything is from the same team that built light rag. It plugs in directly into the light rag system we already built yesterday. So it's really easy to introduce this into our stack. And so today I'm going to show you exactly how to set it up and how it works under the hood so you can begin using one of the most powerful rag systems out there. So in case it wasn't obvious enough from the opener, I'm going to assume you've already watched yesterday's light rag video. I'll put a link above if you haven't done that already because today I'm going to assume you've already set up your light rag server. You understand how rag works and you understand this whole knowledge graph thing because rag anything is essentially going to be a wrapper around light rag. We're still going to have the same light rag web UI with some differences but everything that gets pushed into rag anything you know these non-ext documents eventually find their way to the same knowledge graph. We're going to be asking it the same questions. We're going to be using the same API to query it through cloud code that we did yesterday. And the functionality we are going to be adding today is significant. It's not enough to build a rag system that is purely text. We don't operate in a world that's purely text. How many of you have been given a PDF document that isn't even technically text? It's just scanned. Light rag can't really handle that. Rag anything can. Now, we will go a little technical today. We'll get under the hood and I'll explain exactly how this whole system works. But big picture, what is it doing? Rag anything is just looking at the documents that aren't text, it's basically doing exactly what light rag does except to these non-ext documents. And after it creates its own knowledge graph in its own vector database, it merges it with the light rag one, which is why everything ends up being in one nice neat little place for us to ask questions about. Now, the only downsides about rag anything is it's a bit heavier. We have to download some models that live on our computer that help parse some of these non-ext documents. And when it comes to actually ingesting non-ext documents, we can't do it really through the light rag UI. We have to use a script. Luckily, this is where cloud code comes in. So for you, the user, after you set all this up, all you have to do to ingest non-ext documents is tell cloud code, hey, go ahead, use the rag anything skill and ingest this document. It's that simple. And you ask the questions the same way you did before. So really not too bad. And again, you get all this functionality just by doing that. Now, before we go into how Rag Anything actually works, just want to give a quick plug for my Claude Code Masterass. Just came out a couple weeks ago, and it's the number one place to go from zero to AI dev, especially if you don't come from technical background. I update this literally every week. There's a new update coming tomorrow. So, if you're someone who is really trying to master cloud code and has no idea where to start, well, this is for you. There's a link to that in the comments. It's inside Chase AI Plus. I also have the free Chase AI community. if this is just too much for you, you're just getting started, link to that is in the description. That is where you also will find the prompts and the skills that I'm going to talk about today. So, make sure you check that out regardless. Now, let's talk about Rag Anything and how this thing actually works. To be honest, it's pretty simple, pretty self-explanatory. So, not to waste your time, I'm just going to keep this image up for like 10 seconds and then we'll move on to the next thing. All right, pretty good, right? Let's move on. I'm just kidding. [laughter] It's it's there's actually a bit going on. This image makes it more confusing than it actually is. And if you understand what we did the other day with light rag, remember all this conversation, you're going to be good. Rag anything kind of operates in a similar fashion just with a few extra steps. And I want to go through because I think it's important to understand how these things work. You know, I think in AI in general, it's easy to become like super practical focused like I just want to know how I install it Chase and then how to use it. That's fine. You can skip ahead if that's you. But I think if you want to become a more mature AI dev and you kind of want to separate yourself from the monkey I could replace you with that just hits accept accept accept and copies prompts and skills then I think it's important to have some you know understanding of architecture because this is what's going to separate you from other people and not just in terms of like how you can use this rag system but in bigger level and higher level bigger projects right this is how you begin to sort of like create your own skills like actually become good at this stuff so let's talk about it so rag anything. Let's talk about the problem, right? The problem is I have a PDF that is a scanned PDF and it's not really text and yet I need to put it into my rag system. Light rag can't handle it. So, in comes Rag Anything, right? It's got the cool llama with the six shades. So, the first thing that happens is I'm going to ingest this document into rag anything. And the first thing it's going to do is it's going to use a program called MinerU, which runs on your computer completely locally for free. And it's going to essentially break down this document into its component parts. Minor U is an open- source project. Again, it's essentially a document parser that includes a bunch of like miniature specialized models. All you need to know is if you're scared of this, it's open source. I'll put a link down below. And again, this is what's going to be running and doing most of the work for us today. So minor U is looking at this document and it says okay this is a header. It creates a box around the header. It says this is text. It says this is a chart. It says this is an image of a bar graph and it says this is an equation written in latex. What it's done is it's looked at the document and it's broken it out okay into its special parts. Minor U doesn't understand what's inside here. Minor U isn't reading the text. It doesn't get the text. It doesn't understand what the chart is about. It just knows chart text image. Okay. From there, it's going to send these component parts to individual specialized models that are part of minor U. So, this is all invisible to you. This is all happening automatically under the hood. So, the model, one of the models is called like paddle OCR. That's what's going to look at the text. So minor is sending this text block to paddle OCR on your computer and it's going to pull out the text. Okay. So now instead of being scan text, it's actual text that reads company X reported strong Q323 results with revenue growth blah blah blah blah blah, right? Same for this text. Same for the chart, right? It's also going to turn it into text, right? Something an LLM can handle. Same thing with latex equations. It has a whole model that handles that, right? This is now no longer latex. it's actually text except for images. So whether this is a bar chart or just it's really anything that it can't transform to text. What it's going to do instead is it's going to take a screenshot of it. And this is important. All right. So now this is a screenshot. It's an image. Screenshot. Love that. So what do we have? We inserted a non-ext document. It's been identified into its component parts. And we've taken those component parts and we've broken it down into two buckets, right? We have the text bucket and we have the image bucket. It's important to realize this. There's two paths that can go down. Image or text. All right, you with me? So, what it's going to do now is we're done using these internal models. Now, we need to bring in the big boys. Now, we need to bring in something like GPT 5.4 mini. Of note, that isn't necessarily the case. You could keep this all local if you wanted to. You could use something like Olama. So now I take the text bucket and I push it to GPT 5.4 mini and I include a prompt that says I want you to break out this text for two things. I want you to take that text and break it out into entities and relationships. Remember entities and relationships. Remember our knowledge graph entity entity and sort of the relationship between them. Okay? And I want you to break it out into what will be embeddings for a vector database. So embeddings embed and then I'm just going to say entities plus relationships. Now thinking ahead, what's going to happen there? Well, the embeddings are going to become embeddings in a vector database and the entities and relationships are going to become a knowledge graph just like we did with light rag, right? Same thing. Same thing except now now it's from the text bucket. But what about those images we had, right? What are we going to do with these guys? Same thing. This is going to get pushed to 5.4 as well, but it's going to be as a screenshot, as an OCR. So, we're telling GBT 5.4, take a look at this screenshot and break it out into two things, right? Embeddings and also entities plus relationships. Now, why do we do that? Why don't we just shove it all into the same exact prompt and have it just OCR this entire thing, right? Why don't we just treat this entire thing as a screenshot? Because it's expensive and slow. What Rag Anything decided to do, and I think it's kind of smart, is it kind of takes a scalpel to this on your computer at the local level, breaking it out into text, breaking out into screenshots. So, when we go through these two paths, you're saving a ton of money and time. Because imagine you were trying to have chat GPT look at 10,000 screenshots and then break out all the text and from the text break it out into embeddings and entities and relationships. It take a lot of time and money. This is smarter. So entities and relationships from the image side same exact thing. It also gets a vector database and it also gets a knowledge graph. So what does that mean? That means from one document we've now created four kind of things, right? We have two vector databases and we have two knowledge graphs from our single non-ext document. You with me? Now, what do we have to do? Well, it's kind of obvious. We need to merge these. So, it's going to take these four things and just push them together, right? They're going to pretty much overlay on top of one another. It's going to match them based on entities essentially. And you're just going to get, you know, at the end one vector database and one knowledge graph. Pretty much the exact same thing we did up here with lighter rag. Simple enough. If we were just using rag anything, that would kind of be the extent of it. However, remember, we're trying to lay rag anything on top of light rag. I want all the power of light rag and I want all the power of rag anything. So what happens now? Well, what happens is just a repeat of what you just saw. So let's kind of bring this guy down. So now we have our rag anything set with a vector database and a knowledge graph and we have our light rag set. So what do we do? We just merge those together. So then what happens is we get the rag everything and the light rag combined which gives us finally one vector database and one knowledge graph and from there it's just like it was before with light rag on its own right you ask a question about whatever that get that question gets turned into a vector up here it pulls the relevant vectors and then it also goes down here finds the correct entity and then takes a look at what's nearby. Okay, maybe that was a little confusing. I hope I explained that. Okay, the kind of recap to confuse you even more. What happens when I add a document that cannot be text? It goes into rag anything. Rag anything breaks out what text it can and then breaks out what images it can as well. It sends both of those to chat GPT or whatever AI system you want. It breaks that out into embeddings, entities, and relationships. Those get turned into knowledge graphs and vector databases. We then merge those together. We now have one vector database and one knowledge graph for rag anything. And since we've already been running this in light rag or if you've added any more documents on top of that, you have an existing vector database and an existing knowledge graph. To solve that, we simply merge them. And in the end, you didn't notice a dang thing. Again, as the user, all of this is invisible to you. Okay? None of this really matters to you. The only thing that might matter to you is what's happening over here with GBD 5.4 cuz it's going to cost you some money. But for educational purposes, that is how the rag anything system integrates with the light rag system. And at the end of the day, it just means that you have a rag system that can handle non-ext documents. And if you're still around after all that, now we can go into how you actually install this thing and use it. So now let's talk about the install and how to actually use it and a couple things you need to watch out for. So I created a oneshot prompt that you can give Claude Code that will install everything for you and update the proper models and all of that. All you need to do is just make sure you're in your light rag directory when you run this. So there's really three things it's going to be doing. First of all, it's going to make sure we update that correct storage path since you already have a Docker light rag instance running. Two, we want to update the model because based on the GitHub, it, you know, was created a little while ago originally. So all the example scripts and all that use things like GPT 40 mini. So I have it on 5.4 nano. Understand you can change that if you want to, but I had it use 5.4 nano as well as keep text embedding 3 large so that we can just use OpenAI for everything. It just keeps it simple. Play with it as you wish. Lastly, since we're using rag anything as essentially a wrapper on top of light rag, some of the example scripts given in the GitHub repo are kind of wrong. So there's like this embedding double wrap bug which again we just tell cloud code to fix and it will fix it. So you're just going to use this prompt again. It is inside the free school community link is in the description. Just look up rag anything and you will find it there. And once you run that prompt, it will begin downloading everything. and understand it's a little heavier because it needs to download minor u and all those dependencies as well. Now let's talk about ingesting documents cuz this is kind of annoying and a pain in the butt. In a perfect world, the lightrag plus rag anything situation would be very streamlined and I could dump whatever I wanted to into light rag/rag anything through a singular interface. I could come into the UI, I could go to upload and I could do that. You really can't with rag anything with light rag. You can still do this for text documents. So you can still do the normal workflow that I showed in the previous video where you go to the UI or you use the light rag skill to upload documents. You can't do that with rag anything. It has to go down essentially a different tunnel, a different pathway. But that different pathway with rag anything is a Python script. There's no UI. There's no button to press. It's literally a script. It's code you have to run. Now, luckily, this is where cloud code comes in and makes it very simple because we're just going to turn that script inside of the repo into a skill. So, for you, once that skill is created, all you have to do is say, "Claude code, use the rag anything skill to upload all these documents, all these non-ext documents." And when it does that, it will go through the minor u process. It will take some time because it has to do all these you know things to it like we explained in the kind of technical section but it will upload it to light rag and it will show up inside of your documents and inside of your knowledge graph. Okay, that's the only weird part you need to know. The other weird part to be honest is once you do that it also requires you to restart the docker container but as part of the skill that happens automatically. So again from your point of view as the user the only difference is you just need to invoke the skill. Now this skill the rag anything upload skill is also inside the free community. So just download it and then put it in your dotcloud folder and then it will work just fine. Now the one note on minor u taking a while that's because the way rag anything works when you download it it's going to run on your CPU. If you want it to run on your GPU you have to have a different version of pietorch. If that all went over your head, just if it's too slow for you, just tell cloud code, hey, can we run PyTorch, can we run minor U on our GPU? And it will walk you through it. Or in fact, it'll just do it all on its own. But by default, it's just going to run on your CPU. So just know that. So let's see an example of this in action. So one of the documents we ingested was this PDF of Novatech, right? SAS revenue analysis. It's totally fake. But the point is we ingested something that has this sorted bar chart, right? So this is something that obviously would have been pulled out as an image sent to chat GBT yada yada yada. Normally light rag wouldn't be able to handle this because it's just an image. It's charts. It's hard for it to sort of break that out. But since we ran this through rag anything, we can now ask a question via cloud code about this. So I asked Claude code, can we query our lighter rag database about the monthly revenue trend for Novatech Inc. for January through September 2025? You can see here it actually didn't even use the skill. It just straight up did the API request, which is fine as well with the query. What was the monthly revenue trend for Novatech Inc. from blah blah blah blah blah. Now, it gave a full response. So, I can take a look at the raw response if I wanted to. But what did it do? It came back with the full monthly breakdowns. We see January 4.6, 4.6, February 4.9, 4.9, March 5.4, 5.4, on and on and on. So, in terms of asking questions about these new documents, same thing as before. The only difference is the upload. All you need to do is to invoke that skill that I'm giving you and then tell Claude Code what you want to put in there. You could point it at a whole folder. You can point it at a specific download. It's just this easy. This is the only really weird thing you got to get used to is these two upload paths. But the actual question and answer, it's just plain language. Plain language. Even if you have you have the skills as well, which I also gave in the last video, but Cloud Code's also smart enough to understand the API structure of this whole thing because it's it's local. It's on your computer. So that's really it when it comes to rag anything. I know the majority of this video was focused sort of on the technical aspects, but as you see once we built that light rag foundation, actually adding rag anything on top of it isn't too hard, especially if we just use that oneshot prompt I gave you. There are some things you can tweak along the edges like anything when it comes to quering it, but really with claude code, it's kind of in charge of all the weights that you can tune inside of light rag. And for that I'm talking about if we go to the retrieval section all the parameters here on the right. Again claude code knows which ones tend to be best for you. So overall I hope this kind of explained how easy it is to set up rag anything and also how easy it is to add this level of functionality to your rag systems which in many rag systems just isn't possible or it's very expensive. And this is relatively cheap especially with that whole minor u local parsing system we're able to set up. So as always let me know what you thought. Make sure to check out Chase AI Plus if you want to get your hands on that cloud code master class and I'll see you

---

## Timestamped Segments

**[0:00]** Almost every rag system suffers from the

**[0:02]** exact same problem. They can only handle

**[0:05]** text documents. So if you try to give it

**[0:07]** images, charts, graphs, whatever, most

**[0:10]** rag systems just can't handle it. And

**[0:12]** when I showed you light rag yesterday,

**[0:14]** it suffered from the exact same problem.

**[0:16]** But today, I'm going to show you the

**[0:18]** fix. And that fix is rag anything. Rag

**[0:21]** anything solves this document problem

**[0:22]** for us. It can handle images. It can

**[0:24]** handle charts. It can handle graphs. And

**[0:26]** it allows us to create a rag system that

**[0:28]** actually deals with the documents you

**[0:30]** use. Rag anything is from the same team

**[0:32]** that built light rag. It plugs in

**[0:34]** directly into the light rag system we

**[0:36]** already built yesterday. So it's really

**[0:38]** easy to introduce this into our stack.

**[0:40]** And so today I'm going to show you

**[0:41]** exactly how to set it up and how it

**[0:43]** works under the hood so you can begin

**[0:45]** using one of the most powerful rag

**[0:47]** systems out there. So in case it wasn't

**[0:49]** obvious enough from the opener, I'm

**[0:50]** going to assume you've already watched

**[0:52]** yesterday's light rag video. I'll put a

**[0:54]** link above if you haven't done that

**[0:55]** already because today I'm going to

**[0:57]** assume you've already set up your light

**[0:59]** rag server. You understand how rag works

**[1:01]** and you understand this whole knowledge

**[1:02]** graph thing because rag anything is

**[1:04]** essentially going to be a wrapper around

**[1:06]** light rag. We're still going to have the

**[1:08]** same light rag web UI with some

**[1:10]** differences but everything that gets

**[1:12]** pushed into rag anything you know these

**[1:14]** non-ext documents eventually find their

**[1:16]** way to the same knowledge graph. We're

**[1:17]** going to be asking it the same

**[1:19]** questions. We're going to be using the

**[1:20]** same API to query it through cloud code

**[1:23]** that we did yesterday. And the

**[1:24]** functionality we are going to be adding

**[1:26]** today is significant. It's not enough to

**[1:28]** build a rag system that is purely text.

**[1:30]** We don't operate in a world that's

**[1:31]** purely text. How many of you have been

**[1:33]** given a PDF document that isn't even

**[1:35]** technically text? It's just scanned.

**[1:36]** Light rag can't really handle that. Rag

**[1:38]** anything can. Now, we will go a little

**[1:40]** technical today. We'll get under the

**[1:41]** hood and I'll explain exactly how this

**[1:43]** whole system works. But big picture,

**[1:45]** what is it doing? Rag anything is just

**[1:48]** looking at the documents that aren't

**[1:49]** text, it's basically doing exactly what

**[1:52]** light rag does except to these non-ext

**[1:54]** documents. And after it creates its own

**[1:56]** knowledge graph in its own vector

**[1:57]** database, it merges it with the light

**[2:00]** rag one, which is why everything ends up

**[2:02]** being in one nice neat little place for

**[2:05]** us to ask questions about. Now, the only

**[2:06]** downsides about rag anything is it's a

**[2:09]** bit heavier. We have to download some

**[2:11]** models that live on our computer that

**[2:12]** help parse some of these non-ext

**[2:14]** documents. And when it comes to actually

**[2:16]** ingesting non-ext documents, we can't do

**[2:19]** it really through the light rag UI. We

**[2:22]** have to use a script. Luckily, this is

**[2:24]** where cloud code comes in. So for you,

**[2:26]** the user, after you set all this up, all

**[2:29]** you have to do to ingest non-ext

**[2:30]** documents is tell cloud code, hey, go

**[2:33]** ahead, use the rag anything skill and

**[2:35]** ingest this document. It's that simple.

**[2:37]** And you ask the questions the same way

**[2:38]** you did before. So really not too bad.

**[2:40]** And again, you get all this

**[2:41]** functionality just by doing that. Now,

**[2:43]** before we go into how Rag Anything

**[2:45]** actually works, just want to give a

**[2:46]** quick plug for my Claude Code Masterass.

**[2:49]** Just came out a couple weeks ago, and

**[2:50]** it's the number one place to go from

**[2:51]** zero to AI dev, especially if you don't

**[2:54]** come from technical background. I update

**[2:56]** this literally every week. There's a new

**[2:58]** update coming tomorrow. So, if you're

**[3:00]** someone who is really trying to master

**[3:01]** cloud code and has no idea where to

**[3:02]** start, well, this is for you. There's a

**[3:05]** link to that in the comments. It's

**[3:07]** inside Chase AI Plus. I also have the

**[3:10]** free Chase AI community. if this is just

**[3:12]** too much for you, you're just getting

**[3:13]** started, link to that is in the

**[3:15]** description. That is where you also will

**[3:17]** find the prompts and the skills that I'm

**[3:19]** going to talk about today. So, make sure

**[3:20]** you check that out regardless. Now,

**[3:22]** let's talk about Rag Anything and how

**[3:24]** this thing actually works. To be honest,

**[3:26]** it's pretty simple, pretty

**[3:26]** self-explanatory. So, not to waste your

**[3:29]** time, I'm just going to keep this image

**[3:30]** up for like 10 seconds and then we'll

**[3:32]** move on to the next thing.

**[3:37]** All right, pretty good, right? Let's

**[3:40]** move on. I'm just kidding. [laughter]

**[3:42]** It's it's there's actually a bit going

**[3:44]** on. This image makes it more confusing

**[3:46]** than it actually is. And if you

**[3:47]** understand what we did the other day

**[3:49]** with light rag, remember all this

**[3:51]** conversation, you're going to be good.

**[3:52]** Rag anything kind of operates in a

**[3:54]** similar fashion just with a few extra

**[3:56]** steps. And I want to go through because

**[3:57]** I think it's important to understand how

**[3:59]** these things work. You know, I think in

**[4:01]** AI in general, it's easy to become like

**[4:03]** super practical focused like I just want

**[4:04]** to know how I install it Chase and then

**[4:06]** how to use it. That's fine. You can skip

**[4:07]** ahead if that's you. But I think if you

**[4:09]** want to become a more mature AI dev and

**[4:11]** you kind of want to separate yourself

**[4:13]** from the monkey I could replace you with

**[4:15]** that just hits accept accept accept and

**[4:16]** copies prompts and skills then I think

**[4:18]** it's important to have some you know

**[4:21]** understanding of architecture because

**[4:22]** this is what's going to separate you

**[4:23]** from other people and not just in terms

**[4:25]** of like how you can use this rag system

**[4:27]** but in bigger level and higher level

**[4:29]** bigger projects right this is how you

**[4:31]** begin to sort of like

**[4:33]** create your own skills like actually

**[4:34]** become good at this stuff so let's talk

**[4:36]** about it so rag anything. Let's talk

**[4:39]** about the problem, right? The problem is

**[4:41]** I have a PDF that is a scanned PDF and

**[4:44]** it's not really text and yet I need to

**[4:45]** put it into my rag system. Light rag

**[4:47]** can't handle it. So, in comes Rag

**[4:50]** Anything, right? It's got the cool llama

**[4:52]** with the six shades.

**[4:54]** So, the first thing that happens is I'm

**[4:56]** going to ingest this document into rag

**[5:00]** anything. And the first thing it's going

**[5:01]** to do is it's going to use a program

**[5:03]** called MinerU, which runs on your

**[5:06]** computer completely locally for free.

**[5:08]** And it's going to essentially break down

**[5:10]** this document into its component parts.

**[5:12]** Minor U is an open- source project.

**[5:14]** Again, it's essentially a document

**[5:16]** parser that includes a bunch of like

**[5:17]** miniature specialized models. All you

**[5:19]** need to know is if you're scared of

**[5:21]** this, it's open source. I'll put a link

**[5:23]** down below. And again, this is what's

**[5:24]** going to be running and doing most of

**[5:25]** the work for us today. So minor U is

**[5:27]** looking at this document and it says

**[5:29]** okay this is a header. It creates a box

**[5:33]** around the header. It says this is text.

**[5:36]** It says this is a chart. It says this is

**[5:40]** an image of a bar graph and it says this

**[5:42]** is an equation written in latex. What

**[5:45]** it's done is it's looked at the document

**[5:47]** and it's broken it out okay into its

**[5:49]** special parts. Minor U doesn't

**[5:51]** understand what's inside here. Minor U

**[5:52]** isn't reading the text. It doesn't get

**[5:54]** the text. It doesn't understand what the

**[5:56]** chart is about. It just knows chart text

**[5:59]** image. Okay. From there, it's going to

**[6:03]** send these component parts to individual

**[6:07]** specialized models that are part of

**[6:09]** minor U. So, this is all invisible to

**[6:12]** you. This is all happening automatically

**[6:14]** under the hood. So, the model, one of

**[6:18]** the models is called like paddle OCR.

**[6:20]** That's what's going to look at the text.

**[6:21]** So minor is sending this text block to

**[6:23]** paddle OCR on your computer and it's

**[6:26]** going to pull out the text. Okay. So now

**[6:28]** instead of being scan text, it's actual

**[6:31]** text that reads company X reported

**[6:32]** strong Q323 results with revenue growth

**[6:35]** blah blah blah blah blah, right? Same

**[6:37]** for this

**[6:39]** text. Same for the chart, right? It's

**[6:42]** also going to turn it into text, right?

**[6:43]** Something an LLM can handle. Same thing

**[6:45]** with latex equations. It has a whole

**[6:47]** model that handles that, right? This is

**[6:49]** now no longer latex. it's actually text

**[6:52]** except for images. So whether this is a

**[6:56]** bar chart or just it's really anything

**[6:58]** that it can't transform to text. What

**[7:00]** it's going to do instead is it's going

**[7:02]** to take a screenshot of it. And this is

**[7:04]** important. All right. So now this is a

**[7:06]** screenshot. It's an image. Screenshot.

**[7:10]** Love that. So what do we have? We

**[7:14]** inserted a non-ext document. It's been

**[7:17]** identified into its component parts. And

**[7:19]** we've taken those component parts and

**[7:20]** we've broken it down into two buckets,

**[7:22]** right? We have the text bucket and we

**[7:25]** have the image bucket. It's important to

**[7:27]** realize this. There's two paths that can

**[7:29]** go down. Image or text. All right, you

**[7:31]** with me? So, what it's going to do now

**[7:34]** is we're done using these internal

**[7:35]** models. Now, we need to bring in the big

**[7:37]** boys. Now, we need to bring in something

**[7:38]** like GPT 5.4 mini. Of note, that isn't

**[7:42]** necessarily the case. You could keep

**[7:43]** this all local if you wanted to. You

**[7:44]** could use something like Olama. So now I

**[7:46]** take the text bucket and I push it to

**[7:48]** GPT 5.4 mini and I include a prompt that

**[7:51]** says I want you to break out this text

**[7:53]** for two things. I want you to take that

**[7:56]** text and break it out into entities and

**[8:00]** relationships. Remember entities and

**[8:02]** relationships. Remember our knowledge

**[8:04]** graph entity entity and sort of the

**[8:08]** relationship between them. Okay? And

**[8:12]** I want you to break it out into what

**[8:14]** will be embeddings for a vector

**[8:16]** database. So embeddings

**[8:20]** embed and then I'm just going to say

**[8:23]** entities plus relationships. Now

**[8:27]** thinking ahead, what's going to happen

**[8:28]** there? Well, the embeddings are going to

**[8:31]** become embeddings in a vector database

**[8:33]** and the entities and relationships are

**[8:35]** going to become a knowledge graph just

**[8:37]** like we did with light rag, right? Same

**[8:40]** thing. Same thing except now now it's

**[8:43]** from the text bucket.

**[8:45]** But what about those images we had,

**[8:47]** right? What are we going to do with

**[8:48]** these guys? Same thing. This is going to

**[8:50]** get pushed to 5.4 as well, but it's

**[8:52]** going to be as a screenshot, as an OCR.

**[8:55]** So, we're telling GBT 5.4, take a look

**[8:58]** at this screenshot and break it out into

**[9:00]** two things, right? Embeddings

**[9:03]** and also entities plus relationships.

**[9:06]** Now, why do we do that? Why don't we

**[9:08]** just shove it all into the same exact

**[9:09]** prompt and have it just OCR this entire

**[9:11]** thing, right? Why don't we just treat

**[9:12]** this entire thing as a screenshot?

**[9:14]** Because it's expensive and slow. What

**[9:16]** Rag Anything decided to do, and I think

**[9:18]** it's kind of smart, is it kind of takes

**[9:20]** a scalpel to this on your computer at

**[9:21]** the local level, breaking it out into

**[9:23]** text, breaking out into screenshots. So,

**[9:25]** when we go through these two paths,

**[9:27]** you're saving a ton of money and time.

**[9:29]** Because imagine you were trying to have

**[9:30]** chat GPT look at 10,000 screenshots and

**[9:33]** then break out all the text and from the

**[9:35]** text break it out into embeddings and

**[9:36]** entities and relationships. It take a

**[9:37]** lot of time and money. This is smarter.

**[9:40]** So entities and relationships from the

**[9:43]** image side same exact thing. It also

**[9:46]** gets a vector database and it also gets

**[9:50]** a knowledge graph. So what does that

**[9:53]** mean? That means from one document we've

**[9:56]** now created four kind of things, right?

**[9:59]** We have two vector databases and we have

**[10:02]** two knowledge graphs from our single

**[10:06]** non-ext document. You with me? Now, what

**[10:10]** do we have to do? Well, it's kind of

**[10:11]** obvious. We need to merge these. So,

**[10:13]** it's going to take these four things and

**[10:16]** just push them together, right? They're

**[10:18]** going to pretty much overlay on top of

**[10:19]** one another. It's going to match them

**[10:20]** based on entities essentially. And

**[10:22]** you're just going to get, you know,

**[10:26]** at the end one vector database and one

**[10:30]** knowledge graph. Pretty much the exact

**[10:32]** same thing we did up here with lighter

**[10:33]** rag. Simple enough. If we were just

**[10:36]** using rag anything, that would kind of

**[10:39]** be the extent of it. However, remember,

**[10:41]** we're trying to lay rag anything on top

**[10:45]** of light rag. I want all the power of

**[10:47]** light rag and I want all the power of

**[10:49]** rag anything. So what happens now? Well,

**[10:52]** what happens is just a repeat of what

**[10:53]** you just saw. So let's kind of bring

**[10:55]** this guy down. So now we have

**[11:00]** our rag anything set with a vector

**[11:02]** database and a knowledge graph and we

**[11:05]** have our light rag set. So what do we

**[11:07]** do? We just merge those together. So

**[11:10]** then what happens is we get the rag

**[11:12]** everything and the light rag combined

**[11:15]** which gives us finally one vector

**[11:19]** database and one knowledge graph and

**[11:21]** from there it's just like it was before

**[11:24]** with light rag on its own right you ask

**[11:28]** a question about whatever that get that

**[11:31]** question gets turned into a vector up

**[11:33]** here it pulls the relevant vectors and

**[11:35]** then it also goes down here finds the

**[11:38]** correct entity and then takes a look at

**[11:40]** what's nearby. Okay, maybe that was a

**[11:44]** little confusing. I hope I explained

**[11:45]** that. Okay, the kind of recap

**[11:49]** to confuse you even more. What happens

**[11:51]** when I add a document that cannot be

**[11:53]** text? It goes into rag anything. Rag

**[11:56]** anything breaks out what text it can and

**[11:58]** then breaks out what images it can as

**[12:00]** well. It sends both of those to chat GPT

**[12:02]** or whatever AI system you want. It

**[12:05]** breaks that out into embeddings,

**[12:07]** entities, and relationships. Those get

**[12:10]** turned into knowledge graphs and vector

**[12:12]** databases. We then merge those together.

**[12:15]** We now have one vector database and one

**[12:17]** knowledge graph for rag anything. And

**[12:20]** since we've already been running this in

**[12:21]** light rag or if you've added any more

**[12:23]** documents on top of that, you have an

**[12:25]** existing vector database and an existing

**[12:28]** knowledge graph. To solve that, we

**[12:30]** simply merge them. And in the end, you

**[12:33]** didn't notice a dang thing. Again, as

**[12:36]** the user, all of this is invisible to

**[12:38]** you. Okay? None of this really matters

**[12:41]** to you. The only thing that might matter

**[12:42]** to you is what's happening over here

**[12:43]** with GBD 5.4 cuz it's going to cost you

**[12:46]** some money. But for educational

**[12:50]** purposes, that is how the rag anything

**[12:53]** system integrates with the light rag

**[12:55]** system. And at the end of the day, it

**[12:57]** just means that you have a rag system

**[12:58]** that can handle non-ext documents. And

**[13:00]** if you're still around after all that,

**[13:03]** now we can go into how you actually

**[13:06]** install this thing and use it. So now

**[13:08]** let's talk about the install and how to

**[13:09]** actually use it and a couple things you

**[13:11]** need to watch out for. So I created a

**[13:12]** oneshot prompt that you can give Claude

**[13:14]** Code that will install everything for

**[13:16]** you and update the proper models and all

**[13:18]** of that. All you need to do is just make

**[13:20]** sure you're in your light rag directory

**[13:22]** when you run this. So there's really

**[13:24]** three things it's going to be doing.

**[13:25]** First of all, it's going to make sure we

**[13:27]** update that correct storage path since

**[13:29]** you already have a Docker light rag

**[13:31]** instance running. Two, we want to update

**[13:33]** the model because based on the GitHub,

**[13:35]** it, you know, was created a little while

**[13:36]** ago originally. So all the example

**[13:38]** scripts and all that use things like GPT

**[13:40]** 40 mini. So I have it on 5.4 nano.

**[13:43]** Understand you can change that if you

**[13:44]** want to, but I had it use 5.4 nano as

**[13:47]** well as keep text embedding 3 large so

**[13:49]** that we can just use OpenAI for

**[13:51]** everything. It just keeps it simple.

**[13:52]** Play with it as you wish. Lastly, since

**[13:54]** we're using rag anything as essentially

**[13:56]** a wrapper on top of light rag, some of

**[13:58]** the example scripts given in the GitHub

**[14:01]** repo are kind of wrong. So there's like

**[14:03]** this embedding double wrap bug which

**[14:06]** again we just tell cloud code to fix and

**[14:08]** it will fix it. So you're just going to

**[14:11]** use this prompt again. It is inside the

**[14:13]** free school community link is in the

**[14:15]** description. Just look up rag anything

**[14:17]** and you will find it there. And once you

**[14:18]** run that prompt, it will begin

**[14:20]** downloading everything. and understand

**[14:21]** it's a little heavier because it needs

**[14:22]** to download minor u and all those

**[14:24]** dependencies as well. Now let's talk

**[14:25]** about ingesting documents cuz this is

**[14:27]** kind of annoying and a pain in the butt.

**[14:28]** In a perfect world, the lightrag plus

**[14:31]** rag anything situation would be very

**[14:34]** streamlined and I could dump whatever I

**[14:36]** wanted to into light rag/rag anything

**[14:40]** through a singular interface. I could

**[14:42]** come into the UI, I could go to upload

**[14:44]** and I could do that. You really can't

**[14:46]** with rag anything with light rag. You

**[14:48]** can still do this for text documents. So

**[14:50]** you can still do the normal workflow

**[14:52]** that I showed in the previous video

**[14:53]** where you go to the UI or you use the

**[14:57]** light rag skill to upload documents. You

**[14:59]** can't do that with rag anything. It has

**[15:01]** to go down essentially a different

**[15:03]** tunnel, a different pathway. But that

**[15:05]** different pathway with rag anything is a

**[15:07]** Python script. There's no UI. There's no

**[15:10]** button to press. It's literally a

**[15:12]** script. It's code you have to run. Now,

**[15:14]** luckily, this is where cloud code comes

**[15:16]** in and makes it very simple because

**[15:18]** we're just going to turn that script

**[15:20]** inside of the repo into a skill. So, for

**[15:24]** you, once that skill is created, all you

**[15:25]** have to do is say, "Claude code, use the

**[15:28]** rag anything skill to upload all these

**[15:32]** documents, all these non-ext documents."

**[15:34]** And when it does that, it will go

**[15:35]** through the minor u process. It will

**[15:36]** take some time because it has to do all

**[15:38]** these you know things to it like we

**[15:41]** explained in the kind of technical

**[15:42]** section but it will upload it to light

**[15:45]** rag and it will show up inside of your

**[15:46]** documents and inside of your knowledge

**[15:49]** graph. Okay, that's the only weird part

**[15:50]** you need to know. The other weird part

**[15:52]** to be honest is once you do that it also

**[15:55]** requires you to restart the docker

**[15:57]** container but as part of the skill that

**[15:59]** happens automatically. So again from

**[16:02]** your point of view as the user the only

**[16:04]** difference is you just need to invoke

**[16:05]** the skill. Now this skill the rag

**[16:07]** anything upload skill is also inside the

**[16:09]** free community. So just download it and

**[16:11]** then put it in your dotcloud folder and

**[16:13]** then it will work just fine. Now the one

**[16:15]** note on minor u taking a while that's

**[16:17]** because the way rag anything works when

**[16:19]** you download it it's going to run on

**[16:22]** your CPU. If you want it to run on your

**[16:24]** GPU you have to have a different version

**[16:26]** of pietorch. If that all went over your

**[16:28]** head, just if it's too slow for you,

**[16:31]** just tell cloud code, hey, can we run

**[16:34]** PyTorch, can we run minor U on our GPU?

**[16:36]** And it will walk you through it. Or in

**[16:38]** fact, it'll just do it all on its own.

**[16:39]** But by default, it's just going to run

**[16:41]** on your CPU. So just know that. So let's

**[16:43]** see an example of this in action. So one

**[16:45]** of the documents we ingested was this

**[16:48]** PDF of Novatech, right? SAS revenue

**[16:51]** analysis. It's totally fake. But the

**[16:53]** point is we ingested something that has

**[16:55]** this sorted bar chart, right? So this is

**[16:57]** something that obviously would have been

**[16:58]** pulled out as an image sent to chat GBT

**[17:00]** yada yada yada. Normally light rag

**[17:02]** wouldn't be able to handle this because

**[17:04]** it's just an image. It's charts. It's

**[17:05]** hard for it to sort of break that out.

**[17:07]** But since we ran this through rag

**[17:09]** anything, we can now ask a question via

**[17:12]** cloud code about this. So I asked Claude

**[17:14]** code, can we query our lighter rag

**[17:15]** database about the monthly revenue trend

**[17:17]** for Novatech Inc. for January through

**[17:18]** September 2025? You can see here it

**[17:21]** actually didn't even use the skill. It

**[17:22]** just straight up did the API request,

**[17:24]** which is fine as well with the query.

**[17:26]** What was the monthly revenue trend for

**[17:28]** Novatech Inc. from blah blah blah blah

**[17:30]** blah. Now, it gave a full response. So,

**[17:32]** I can take a look at the raw response if

**[17:34]** I wanted to. But what did it do? It came

**[17:36]** back with the full monthly breakdowns.

**[17:39]** We see January 4.6, 4.6, February 4.9,

**[17:42]** 4.9, March 5.4, 5.4, on and on and on.

**[17:46]** So, in terms of asking questions about

**[17:47]** these new documents, same thing as

**[17:49]** before. The only difference is the

**[17:50]** upload. All you need to do is to invoke

**[17:53]** that skill that I'm giving you and then

**[17:55]** tell Claude Code what you want to put in

**[17:56]** there. You could point it at a whole

**[17:57]** folder. You can point it at a specific

**[17:59]** download. It's just this easy. This is

**[18:01]** the only really weird thing you got to

**[18:03]** get used to is these two upload paths.

**[18:05]** But the actual question and answer, it's

**[18:07]** just plain language. Plain language.

**[18:10]** Even if you have you have the skills as

**[18:11]** well, which I also gave in the last

**[18:13]** video, but Cloud Code's also smart

**[18:14]** enough to understand the API structure

**[18:16]** of this whole thing because it's it's

**[18:17]** local. It's on your computer. So that's

**[18:19]** really it when it comes to rag anything.

**[18:21]** I know the majority of this video was

**[18:22]** focused sort of on the technical

**[18:24]** aspects, but as you see once we built

**[18:27]** that light rag foundation, actually

**[18:29]** adding rag anything on top of it isn't

**[18:31]** too hard, especially if we just use that

**[18:33]** oneshot prompt I gave you. There are

**[18:35]** some things you can tweak along the

**[18:36]** edges like anything when it comes to

**[18:38]** quering it, but really with claude code,

**[18:41]** it's kind of in charge of all the

**[18:42]** weights that you can tune inside of

**[18:44]** light rag. And for that I'm talking

**[18:45]** about if we go to the retrieval section

**[18:47]** all the parameters here on the right.

**[18:49]** Again claude code knows which ones tend

**[18:51]** to be best for you. So overall I hope

**[18:54]** this kind of explained how easy it is to

**[18:57]** set up rag anything and also how easy it

**[19:00]** is to add this level of functionality to

**[19:02]** your rag systems which in many rag

**[19:03]** systems just isn't possible or it's very

**[19:05]** expensive. And this is relatively cheap

**[19:08]** especially with that whole minor u local

**[19:10]** parsing system we're able to set up. So

**[19:12]** as always let me know what you thought.

**[19:14]** Make sure to check out Chase AI Plus if

**[19:16]** you want to get your hands on that cloud

**[19:17]** code master class and I'll see you
