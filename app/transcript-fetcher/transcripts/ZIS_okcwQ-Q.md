# Transcript: I Distilled all of AI Engineering Expertise into a single Tool

**URL:** https://www.youtube.com/watch?v=ZIS_okcwQ-Q
**Segments:** 914
**Channel:** Jacob Dietle
**Duration:** 13:27
**Uploaded:** 2026-04-15

---

## Full Text

I built a tool that lets you distill tens of thousands of hours of the best AI engineers learnings and apply it directly to your AI and context engineering problems. I'm going to show you what it is, what makes it special and how to use it. Today, to solve your specific domain problems using Go to Market Engineering as an example. So what did I build? I built something called tastematter. Tastematter is a contents graph pulling in newsletters, tweets, YouTube videos, research papers, basically everything I consider high signal in the AI, and context engineering space. And a little bit beyond that, it is my attempt. So I originally built this because I was feeling very overwhelmed, trying to keep up to date with everything, all the time. and I decided that I was using this thing. I was using this thing so often, I was reading this thing every single day. I figured it'd be useful to other people. So, first part of it is this daily brief, and the second part is the actual context graph itself. So this graph is what I check every single day. It pulls in net new  articles, or I guess whatever, right? It's not just articles. We said tweets, whatever. it checks them against the graph. As you can see, it contradict it. It'll check  and see how these relate. So the concept graph will pull in an article, bucket it into a topic and then check it against the graph. So it's doing a lot more than just summarization. It's actually intelligently seeing where these concepts fit together, whether they support each other or contradict each other and then using that to generate a brief that is meant to be directly actionable every single day. So right here, right, this is like the main takeaway. Every single one of these signals has a specific action item you can take away and the supporting, context around it. So using this signal as an example, memory architecture is the actual lock. In choosing, cloud code or OpenAI isn't selecting a model, it's choosing your team's accumulated intelligence. it's pulling out to here, this post from, let's see, two days ago, where it's citing, or it's retweeting. This is the creator blank chain. And it's also, tagging the team at leda. This is like active discourse. not everything is this up to date. It's going to pull in from the past several months. Over time you build up this, archive. But the idea is that it's very much timely, relevant, actionable, with the long tail persisted into the context graph for you to look at later. so going to that graph itself. You'll see here that the graph shows only a small number of the concepts covered. Because if we go to the concept list, right, we have 289 concepts. this is partially from a long tail of bloat that, that's kind of popped up in the last couple days of running this thing since I have this actually doing it, running a self organizing taxonomy. probably need to clean this up. But the graph is meant to show you how certain topics fit together, where they support one another, they contradict one another. And it's meant to actually, instead of saying hey, this is just you know, a summarized version of it. It's meant to kind of as much as you can actually capture wisdom, in a system like this, it's meant to capture it and make it immediately applicable for your agents to use in your own agentic engineering. And that's what the concept graph is really for. The actual graph itself, if you were to visualize this, it will not fit on the screen. there would be too many concepts, too many  underlying articles and too many connections between them. But  this is kind of, this is meant to give you an idea of what we're working with and make it tangible. Getting on to the actual graph itself that is accessible via an MCP server. So to access the graph you just need to sign up for beta access, put in your email, subscribe and then you can go and copy. This is added to cloud code. I'm just going to use regular cloud web app. for the example today. Okay, here's how you're going to add it. You're going to add go to Settings connectors, add custom connector taste matter graph and you're going to put in this URL. Now when you do this, if you're logging in for the first time, it's going to redirect you to a login page. All you have to do is provide your email. It'll send you one time code for me, I've already done this so remembers me. and then you can see here configure. It has two tools. This is using something called code mode. It's hyper context efficient and allows you to get way more out of the graph. So I'll show you that right now. So using, I'm going to use an incognito window or not Window chat, incognito chat. So it doesn't use any of my, saved context. so you can see it working on its own. say, tell me, use the context, or, excuse me, use the Taste matter graph to tell me what is going on in Context Engineering right now as an example. so first I'm going to show you this. I want to show you the code mode execution because it's interesting itself. And then I'm going to show you, how it applies to a specific domain. This case being go to Market Engineering. So you see here it's loading a tool up. it basically says, hey, what tools do I have? Search, and execute, the core, innovation. I wish you could take credit for this. I can't. This Cloudflare created this language models are exceptionally good at writing code. So rather than giving them an arbitrary list of tools, you just have them write code and it drops content consumption by like 90%, makes it far faster and far smarter. So going into here to load the tools up and then it'll run a search, say, hey, what's the graph look like? And runs basically what looks like SQL, but then it comes back with, RAW access to the graph or full access to the graph, and it can synthesize that into insight. right here, this is from today, right? So this is basically mirroring, the graph from today because I asked it what's going on today, but it's pulling in like specific Twitter handles. We saw Sarah Let. Not Sarah Letta, Sarah Waters, who works at Leta or founded Letta, up here. And this is like a live look at what's happening in the space right now. So I know this is, it looks cool, it's pulling in stuff, it's like surfacing very deep. niche tips like disabling telemetry apparently degrades your cache rate. I want to take a step back and acknowledge that this is very in the weeds abstract. And if we're not looking at this stuff all day long like I am, it may seem like it's a lot, it is, but it's structured in a way that it's, you can point this whole cumulative knowledge base knowledge graph at your specific problems and get direct answers back that are grounded in it and also don't they're, they're grounded in a way that makes it so you can make a real trade off decision. I think most people take for granted, so much of engineering is around making trade offs and by having the full attribution chain of hey, this is what happens when you use a multi agent system versus single agent system. And this is what other people have found for example, right? You get far better design, outcomes. You get better outcomes. Yeah, that makes sense. Anyway, so like I'm going to say here like  I am building a signal machine using multiple agents, multiple agents for my GTM engineering work. What have others tried, and learned building systems like systems like this. and that's actually like obviously there's not a lot of context here. I'm not giving it much to work from. So the more you give it the more you're going to get back. but this is to show like you can go and ask very specific questions and get very specific, hopefully for you, relevant and valuable results back. Right. And it'll go and just run this like  recursive search against the graph and say hey, this is what Google found. So it's taking a second here, I'll cut this. So you can see it's streaming across right now. It ran a bunch of searches. this is actually a lot of context pulled in And it's providing multiple specific points of view that people, real people have, come up with for, different patterns to use. So am I seeing this for the first time myself? Is actually really interesting. hey, Jordan, Doug, you guys gotta. I guess you guys are in this thing now too. but like, I love how this has a full chain all the way from someone who's working on something, in public or they're publishing about it. It can synthesize those, learnings and insights into real concepts in the graph and then say, hey, this is what that person has done, and what's working for them and what's not. Right. So that's cool. Yeah, see, there's a ton here. and like, I'll try another one. Let's say, my agents are. This is something I've been having a problem with recently, myself losing coherence, and can't follow their own logic. What could be some sources, we'll say, my development agents, we'll say root cause is better. So I actually know the answer, this one already because I kind of, solutioned it generally less context. And if this is actually a specific issue in cloud code right now. Right. Roll back to the last model. but I don't know, I'm just kind of having fun at this point. Let's see. Do you see here? It's running the search to get a. Basically this is telling it the schema and how to sort through. that one didn't work. What happened there? Yeah, so it, ran it improperly. But I, think you guys get the point. I'll let this one run. so I want you to think of it this way. This is like very specific deep first principles, all the best practices, all the learnings about how to use AI. And what this can do for you is you have to give it the unique constraints, of your domain. So for go to market engineering, it might be list building or it might be ICP definitions or it's talking to customers or whatever it is. this can help you do all of that stuff far more effectively because you don't have to get in the weeds of learning about different agent, architectures or what's working or what. Not unless you want to. Obviously, I'm someone who wants to. I love this stuff. But this is really meant to let you offload a lot of that complexity, and literally have the agent do it for you, because it can talk to this knowledge graph. Just to show you that end, end result here. context rot. Yep, yep. Compaction, coherence. These are all real problems I've seen. And like, I'm reading it for the first time. Sorry. I think. I think in this case, the example I was thinking about, it's really this one. I actually post about this yesterday, but I just want to show you that as proof of work. So here's my call to action. Want to be meta about it? Go use the graph today. I'm going to iterate on this a ton. Part of the value of this for me personally beyond building I guess the taste matter brand or whatever itself is using all of my most advanced context engineering techniques that I need to test bed for. So this concepts thing being self organizing, it was working really great and then like over the weekend it exploded. Right. So you see this like super long tail, this is super valuable test data for me and the more people using it, the more people getting value out of it, the better. So you can go subscribe. Obviously the briefs are the daily roll up thing. I might do weekly version of it as well just to kind of do a higher signal version, that's actually curated by me. and then the VMCP access is free as well for right now. I have a few dozen more spots left. Cloudflare's access policy has 50 slots, so once that runs out, that's the cap for now. but I hope this is useful for you and please send all of the feedback. I really appreciate it and I really appreciate your time today. Thanks so much. Bye. I built a tool that lets you distill tens of thousands of hours of the best AI engineers learnings and apply it directly to your AI and context engineering problems. I'm going to show you what it is, what makes it special and how to use it. Today, to solve your specific domain problems using Go to Market Engineering as an example. So what did I build? I built something called tastematter. Tastematter is a contents graph pulling in newsletters, tweets, YouTube videos, research papers, basically everything I consider high signal in the AI, and context engineering space. And a little bit beyond that, it is my attempt. So I originally built this because I was feeling very overwhelmed, trying to keep up to date with everything, all the time. and I decided that I was using this thing. I was using this thing so often, I was reading this thing every single day. I figured it'd be useful to other people. So, first part of it is this daily brief, and the second part is the actual context graph itself. So this graph is what I check every single day. It pulls in net new  articles, or I guess whatever, right? It's not just articles. We said tweets, whatever. it checks them against the graph. As you can see, it contradict it. It'll check  and see how these relate. So the concept graph will pull in an article, bucket it into a topic and then check it against the graph. So it's doing a lot more than just summarization. It's actually intelligently seeing where these concepts fit together, whether they support each other or contradict each other and then using that to generate a brief that is meant to be directly actionable every single day. So right here, right, this is like the main takeaway. Every single one of these signals has a specific action item you can take away and the supporting, context around it. So using this signal as an example, memory architecture is the actual lock. In choosing, cloud code or OpenAI isn't selecting a model, it's choosing your team's accumulated intelligence. it's pulling out to here, this post from, let's see, two days ago, where it's citing, or it's retweeting. This is the creator blank chain. And it's also, tagging the team at leda. This is like active discourse. not everything is this up to date. It's going to pull in from the past several months. Over time you build up this, archive. But the idea is that it's very much timely, relevant, actionable, with the long tail persisted into the context graph for you to look at later. so going to that graph itself. You'll see here that the graph shows only a small number of the concepts covered. Because if we go to the concept list, right, we have 289 concepts. this is partially from a long tail of bloat that, that's kind of popped up in the last couple days of running this thing since I have this actually doing it, running a self organizing taxonomy. probably need to clean this up. But the graph is meant to show you how certain topics fit together, where they support one another, they contradict one another. And it's meant to actually, instead of saying hey, this is just you know, a summarized version of it. It's meant to kind of as much as you can actually capture wisdom, in a system like this, it's meant to capture it and make it immediately applicable for your agents to use in your own agentic engineering. And that's what the concept graph is really for. The actual graph itself, if you were to visualize this, it will not fit on the screen. there would be too many concepts, too many  underlying articles and too many connections between them. But  this is kind of, this is meant to give you an idea of what we're working with and make it tangible. Getting on to the actual graph itself that is accessible via an MCP server. So to access the graph you just need to sign up for beta access, put in your email, subscribe and then you can go and copy. This is added to cloud code. I'm just going to use regular cloud web app. for the example today. Okay, here's how you're going to add it. You're going to add go to Settings connectors, add custom connector taste matter graph and you're going to put in this URL. Now when you do this, if you're logging in for the first time, it's going to redirect you to a login page. All you have to do is provide your email. It'll send you one time code for me, I've already done this so remembers me. and then you can see here configure. It has two tools. This is using something called code mode. It's hyper context efficient and allows you to get way more out of the graph. So I'll show you that right now. So using, I'm going to use an incognito window or not Window chat, incognito chat. So it doesn't use any of my, saved context. so you can see it working on its own. say, tell me, use the context, or, excuse me, use the Taste matter graph to tell me what is going on in Context Engineering right now as an example. so first I'm going to show you this. I want to show you the code mode execution because it's interesting itself. And then I'm going to show you, how it applies to a specific domain. This case being go to Market Engineering. So you see here it's loading a tool up. it basically says, hey, what tools do I have? Search, and execute, the core, innovation. I wish you could take credit for this. I can't. This Cloudflare created this language models are exceptionally good at writing code. So rather than giving them an arbitrary list of tools, you just have them write code and it drops content consumption by like 90%, makes it far faster and far smarter. So going into here to load the tools up and then it'll run a search, say, hey, what's the graph look like? And runs basically what looks like SQL, but then it comes back with, RAW access to the graph or full access to the graph, and it can synthesize that into insight. right here, this is from today, right? So this is basically mirroring, the graph from today because I asked it what's going on today, but it's pulling in like specific Twitter handles. We saw Sarah Let. Not Sarah Letta, Sarah Waters, who works at Leta or founded Letta, up here. And this is like a live look at what's happening in the space right now. So I know this is, it looks cool, it's pulling in stuff, it's like surfacing very deep. niche tips like disabling telemetry apparently degrades your cache rate. I want to take a step back and acknowledge that this is very in the weeds abstract. And if we're not looking at this stuff all day long like I am, it may seem like it's a lot, it is, but it's structured in a way that it's, you can point this whole cumulative knowledge base knowledge graph at your specific problems and get direct answers back that are grounded in it and also don't they're, they're grounded in a way that makes it so you can make a real trade off decision. I think most people take for granted, so much of engineering is around making trade offs and by having the full attribution chain of hey, this is what happens when you use a multi agent system versus single agent system. And this is what other people have found for example, right? You get far better design, outcomes. You get better outcomes. Yeah, that makes sense. Anyway, so like I'm going to say here like  I am building a signal machine using multiple agents, multiple agents for my GTM engineering work. What have others tried, and learned building systems like systems like this. and that's actually like obviously there's not a lot of context here. I'm not giving it much to work from. So the more you give it the more you're going to get back. but this is to show like you can go and ask very specific questions and get very specific, hopefully for you, relevant and valuable results back. Right. And it'll go and just run this like  recursive search against the graph and say hey, this is what Google found. So it's taking a second here, I'll cut this. So you can see it's streaming across right now. It ran a bunch of searches. this is actually a lot of context pulled in And it's providing multiple specific points of view that people, real people have, come up with for, different patterns to use. So am I seeing this for the first time myself? Is actually really interesting. hey, Jordan, Doug, you guys gotta. I guess you guys are in this thing now too. but like, I love how this has a full chain all the way from someone who's working on something, in public or they're publishing about it. It can synthesize those, learnings and insights into real concepts in the graph and then say, hey, this is what that person has done, and what's working for them and what's not. Right. So that's cool. Yeah, see, there's a ton here. and like, I'll try another one. Let's say, my agents are. This is something I've been having a problem with recently, myself losing coherence, and can't follow their own logic. What could be some sources, we'll say, my development agents, we'll say root cause is better. So I actually know the answer, this one already because I kind of, solutioned it generally less context. And if this is actually a specific issue in cloud code right now. Right. Roll back to the last model. but I don't know, I'm just kind of having fun at this point. Let's see. Do you see here? It's running the search to get a. Basically this is telling it the schema and how to sort through. that one didn't work. What happened there? Yeah, so it, ran it improperly. But I, think you guys get the point. I'll let this one run. so I want you to think of it this way. This is like very specific deep first principles, all the best practices, all the learnings about how to use AI. And what this can do for you is you have to give it the unique constraints, of your domain. So for go to market engineering, it might be list building or it might be ICP definitions or it's talking to customers or whatever it is. this can help you do all of that stuff far more effectively because you don't have to get in the weeds of learning about different agent, architectures or what's working or what. Not unless you want to. Obviously, I'm someone who wants to. I love this stuff. But this is really meant to let you offload a lot of that complexity, and literally have the agent do it for you, because it can talk to this knowledge graph. Just to show you that end, end result here. context rot. Yep, yep. Compaction, coherence. These are all real problems I've seen. And like, I'm reading it for the first time. Sorry. I think. I think in this case, the example I was thinking about, it's really this one. I actually post about this yesterday, but I just want to show you that as proof of work. So here's my call to action. Want to be meta about it? Go use the graph today. I'm going to iterate on this a ton. Part of the value of this for me personally beyond building I guess the taste matter brand or whatever itself is using all of my most advanced context engineering techniques that I need to test bed for. So this concepts thing being self organizing, it was working really great and then like over the weekend it exploded. Right. So you see this like super long tail, this is super valuable test data for me and the more people using it, the more people getting value out of it, the better. So you can go subscribe. Obviously the briefs are the daily roll up thing. I might do weekly version of it as well just to kind of do a higher signal version, that's actually curated by me. and then the VMCP access is free as well for right now. I have a few dozen more spots left. Cloudflare's access policy has 50 slots, so once that runs out, that's the cap for now. but I hope this is useful for you and please send all of the feedback. I really appreciate it and I really appreciate your time today. Thanks so much. Bye.

---

## Timestamped Segments

**[0:00]** I built a tool that lets you distill tens of

**[0:02]** thousands of hours of the best AI engineers

**[0:04]** learnings and apply it directly to your AI and

**[0:07]** context engineering problems.

**[0:08]** I'm going to show you what it is,

**[0:09]** what makes it special and how to use it.

**[0:11]** Today,

**[0:11]** to solve your specific domain problems using Go to

**[0:14]** Market Engineering as an example.

**[0:15]** So what did I build?

**[0:16]** I built something called tastematter.

**[0:19]** Tastematter is a contents graph pulling in

**[0:23]** newsletters,

**[0:24]** tweets,

**[0:25]** YouTube videos,

**[0:26]** research papers,

**[0:28]** basically everything I consider high signal in

**[0:31]** the AI,

**[0:32]** and context engineering space.

**[0:33]** And a little bit beyond that,

**[0:36]** it is my attempt.

**[0:37]** So I originally built this

**[0:39]** because I was feeling very overwhelmed,

**[0:40]** trying to keep up to date with everything,

**[0:42]** all the time.

**[0:44]** and I decided that

**[0:46]** I was using this thing.

**[0:47]** I was using this thing so often,

**[0:49]** I was reading this thing every single day.

**[0:51]** I figured it'd be useful to other people.

**[0:54]** So,

**[0:54]** first part of it is this daily brief,

**[0:56]** and the second part is the actual context graph

**[0:58]** itself.

**[1:00]** So this graph is what I check every single day.

**[1:02]** It pulls in net new  articles,

**[1:04]** or I guess whatever,

**[1:05]** right?

**[1:06]** It's not just articles.

**[1:06]** We said tweets,

**[1:07]** whatever.

**[1:08]** it checks them against the graph.

**[1:09]** As you can see,

**[1:10]** it contradict it.

**[1:11]** It'll check  and see how these relate.

**[1:14]** So

**[1:15]** the concept graph will pull in

**[1:17]** an article,

**[1:19]** bucket it into a topic and then check it against

**[1:22]** the graph.

**[1:22]** So it's doing a lot more than just summarization.

**[1:25]** It's actually intelligently seeing where these

**[1:27]** concepts fit together,

**[1:28]** whether they support each other or contradict each

**[1:30]** other and then using that to generate a brief that

**[1:32]** is meant to be directly actionable every single

**[1:35]** day.

**[1:35]** So right here,

**[1:37]** right,

**[1:37]** this is like the main takeaway.

**[1:38]** Every single one of these signals has a specific

**[1:40]** action item you can take away and the supporting,

**[1:43]** context around it.

**[1:45]** So using this signal as an example,

**[1:46]** memory architecture is the actual lock.

**[1:48]** In

**[1:49]** choosing,

**[1:49]** cloud code or OpenAI isn't selecting a model,

**[1:52]** it's choosing

**[1:53]** your team's accumulated intelligence.

**[1:55]** it's pulling out to here,

**[1:57]** this post from,

**[2:00]** let's see,

**[2:03]** two days ago,

**[2:04]** where it's citing,

**[2:05]** or it's retweeting.

**[2:06]** This is the creator blank chain.

**[2:08]** And it's also,

**[2:10]** tagging the team at leda.

**[2:12]** This is like active discourse.

**[2:14]** not everything is this up to date.

**[2:16]** It's going to pull in from the past several

**[2:18]** months.

**[2:19]** Over time

**[2:20]** you build up this,

**[2:21]** archive.

**[2:23]** But the idea is that it's very much

**[2:26]** timely,

**[2:26]** relevant,

**[2:27]** actionable,

**[2:28]** with the long tail persisted into the context

**[2:30]** graph for you to look at later.

**[2:33]** so going to that graph itself.

**[2:37]** You'll see here that the graph

**[2:40]** shows only a small number of the

**[2:43]** concepts covered.

**[2:44]** Because if we go to the concept list,

**[2:45]** right,

**[2:46]** we have 289 concepts.

**[2:49]** this is partially from a long tail of bloat that,

**[2:52]** that's kind of popped up in the last couple days

**[2:55]** of running this thing since I have this actually

**[2:56]** doing it,

**[2:57]** running a self organizing taxonomy.

**[3:00]** probably need to clean this up.

**[3:01]** But

**[3:02]** the graph is meant to show you how certain topics

**[3:06]** fit together,

**[3:07]** where they support one another,

**[3:08]** they contradict one another.

**[3:10]** And it's meant to actually,

**[3:11]** instead of saying hey,

**[3:12]** this is just

**[3:15]** you know,

**[3:15]** a summarized version of it.

**[3:16]** It's meant to kind of as much as you can actually

**[3:19]** capture wisdom,

**[3:21]** in a system like this,

**[3:23]** it's meant to capture it and make it immediately

**[3:25]** applicable

**[3:26]** for your agents to use in your own agentic

**[3:28]** engineering.

**[3:29]** And that's what the concept graph is really for.

**[3:31]** The actual graph itself,

**[3:32]** if you were to visualize this,

**[3:33]** it will not fit on the screen.

**[3:35]** there would be too many concepts,

**[3:37]** too many  underlying articles and too many

**[3:39]** connections between them.

**[3:41]** But  this is kind of,

**[3:43]** this is meant to give you an idea of what we're

**[3:45]** working with and make it tangible.

**[3:47]** Getting on to the actual graph itself

**[3:49]** that is accessible via an MCP server.

**[3:52]** So to access the graph you just need to sign up

**[3:54]** for beta access,

**[3:55]** put in your email,

**[3:58]** subscribe

**[4:00]** and then you can go and copy.

**[4:01]** This is added to cloud code.

**[4:03]** I'm just going to use regular cloud web app.

**[4:05]** for the example today.

**[4:07]** Okay,

**[4:07]** here's how you're going to add it.

**[4:08]** You're going to add go to Settings

**[4:11]** connectors,

**[4:13]** add custom connector

**[4:16]** taste matter graph and you're going to put in this

**[4:19]** URL.

**[4:19]** Now when you do this,

**[4:21]** if you're logging in for the first time,

**[4:22]** it's going to redirect you to a login page.

**[4:24]** All you have to do is provide your email.

**[4:25]** It'll send you one time code for me,

**[4:27]** I've already done this so remembers me.

**[4:30]** and then you can see here configure.

**[4:32]** It has two tools.

**[4:34]** This is using something called code mode.

**[4:36]** It's hyper context efficient and allows you to get

**[4:38]** way more out of the graph.

**[4:39]** So I'll show you that right now.

**[4:42]** So using,

**[4:43]** I'm going to use an incognito window or not Window

**[4:46]** chat,

**[4:48]** incognito chat.

**[4:49]** So it doesn't use any of my,

**[4:50]** saved context.

**[4:52]** so you can see it working on its own.

**[4:54]** say,

**[4:55]** tell me,

**[4:56]** use the context,

**[4:58]** or,

**[4:59]** excuse me,

**[4:59]** use the Taste matter graph to

**[5:02]** tell me what is

**[5:04]** going on

**[5:05]** in

**[5:06]** Context Engineering right now

**[5:09]** as an example.

**[5:12]** so first I'm going to show you this.

**[5:13]** I want to show you

**[5:14]** the code mode execution because it's interesting

**[5:17]** itself.

**[5:17]** And then I'm going to show you,

**[5:19]** how it applies to a specific domain.

**[5:21]** This case being go to Market Engineering.

**[5:24]** So you see here it's loading a tool up.

**[5:27]** it basically says,

**[5:28]** hey,

**[5:28]** what tools do I have?

**[5:29]** Search,

**[5:30]** and execute,

**[5:32]** the core,

**[5:33]** innovation.

**[5:34]** I wish you could take credit for this.

**[5:35]** I can't.

**[5:36]** This Cloudflare created this language models are

**[5:38]** exceptionally good at writing code.

**[5:40]** So rather than giving them an arbitrary list of

**[5:42]** tools,

**[5:43]** you just have them write code and it drops content

**[5:45]** consumption by like 90%,

**[5:47]** makes it far faster and far smarter.

**[5:50]** So going into here

**[5:51]** to load the tools up and then it'll run a search,

**[5:53]** say,

**[5:54]** hey,

**[5:54]** what's the graph look like?

**[5:55]** And runs basically what looks like

**[5:57]** SQL,

**[5:58]** but then it comes back with,

**[6:02]** RAW access to the graph or full access to the

**[6:04]** graph,

**[6:04]** and it can synthesize that into insight.

**[6:07]** right here,

**[6:08]** this is from today,

**[6:09]** right?

**[6:10]** So this is basically mirroring,

**[6:12]** the graph from today because I asked it

**[6:14]** what's going on today,

**[6:16]** but it's pulling in like specific Twitter handles.

**[6:18]** We saw Sarah Let.

**[6:19]** Not Sarah Letta,

**[6:21]** Sarah Waters,

**[6:22]** who works at Leta or founded Letta,

**[6:23]** up here.

**[6:24]** And this is like a live look at what's happening

**[6:26]** in the space right now.

**[6:30]** So

**[6:31]** I know this is,

**[6:34]** it looks

**[6:35]** cool,

**[6:35]** it's pulling in stuff,

**[6:36]** it's like surfacing

**[6:38]** very deep.

**[6:39]** niche tips like disabling telemetry

**[6:42]** apparently degrades your

**[6:44]** cache rate.

**[6:46]** I want to take a step back and

**[6:49]** acknowledge that this is very in the weeds

**[6:51]** abstract.

**[6:52]** And if we're not looking at this stuff all day

**[6:54]** long like I am,

**[6:55]** it may seem like it's a lot,

**[6:58]** it is,

**[6:59]** but

**[7:00]** it's structured in a way that it's,

**[7:02]** you can point this whole

**[7:05]** cumulative knowledge base knowledge graph at your

**[7:08]** specific problems and get direct answers back that

**[7:11]** are grounded in it and also don't

**[7:16]** they're,

**[7:17]** they're grounded in a way that makes it

**[7:19]** so you can make a real trade off decision.

**[7:21]** I think most people take for granted,

**[7:23]** so much of engineering

**[7:26]** is around making trade offs and by having the

**[7:29]** full attribution chain of hey,

**[7:31]** this is what happens when you use a multi agent

**[7:34]** system versus single agent system.

**[7:35]** And this is what other people have found for

**[7:37]** example,

**[7:38]** right?

**[7:38]** You get far better

**[7:40]** design,

**[7:40]** outcomes.

**[7:42]** You get better outcomes.

**[7:43]** Yeah,

**[7:43]** that makes sense.

**[7:44]** Anyway,

**[7:45]** so like I'm going to say here like  I am building

**[7:48]** a signal machine

**[7:50]** using multiple agents,

**[7:53]** multiple agents for my GTM

**[7:58]** engineering

**[8:00]** work.

**[8:01]** What have

**[8:03]** others

**[8:03]** tried,

**[8:05]** and

**[8:08]** learned

**[8:08]** building

**[8:09]** systems

**[8:10]** like systems like this.

**[8:13]** and that's actually like obviously there's not a

**[8:15]** lot of context here.

**[8:16]** I'm not giving it much to work from.

**[8:18]** So the more you give it the more you're going to

**[8:19]** get back.

**[8:21]** but this is to show like you can go and ask very

**[8:24]** specific questions and get very specific,

**[8:27]** hopefully for you,

**[8:28]** relevant and valuable results back.

**[8:31]** Right.

**[8:31]** And it'll go and just run this like  recursive

**[8:35]** search against the graph and say hey,

**[8:36]** this is what Google found.

**[8:38]** So it's taking a second here,

**[8:39]** I'll cut this.

**[8:41]** So you can see it's streaming across right now.

**[8:43]** It ran a bunch of searches.

**[8:46]** this is actually a lot of context pulled in

**[8:50]** And it's providing multiple specific points of

**[8:53]** view

**[8:54]** that

**[8:55]** people,

**[8:55]** real people have,

**[8:56]** come up with

**[8:58]** for,

**[8:59]** different patterns to use.

**[9:00]** So am I seeing this for the first time myself?

**[9:02]** Is actually really interesting.

**[9:06]** hey,

**[9:07]** Jordan,

**[9:07]** Doug,

**[9:08]** you guys gotta.

**[9:09]** I guess you guys are in this thing now too.

**[9:13]** but like,

**[9:14]** I love how this has a full chain all the way from

**[9:18]** someone who's working on something,

**[9:20]** in public or they're publishing about it.

**[9:24]** It can synthesize those,

**[9:25]** learnings and insights into real concepts in the

**[9:28]** graph and then say,

**[9:29]** hey,

**[9:29]** this is what that person has done,

**[9:31]** and what's working for them and what's not.

**[9:34]** Right.

**[9:35]** So

**[9:36]** that's cool.

**[9:38]** Yeah,

**[9:38]** see,

**[9:38]** there's a ton here.

**[9:41]** and like,

**[9:41]** I'll try another one.

**[9:42]** Let's say,

**[9:44]** my agents are.

**[9:47]** This is something I've been having a problem with

**[9:49]** recently,

**[9:50]** myself

**[9:50]** losing coherence,

**[9:54]** and can't

**[9:56]** follow

**[9:57]** their own logic.

**[9:59]** What could be some

**[10:01]** sources,

**[10:02]** we'll say,

**[10:02]** my development agents,

**[10:07]** we'll say root cause is better.

**[10:13]** So I actually know the answer,

**[10:14]** this one already because I kind of,

**[10:17]** solutioned it generally less context.

**[10:19]** And if this is actually a specific issue in cloud

**[10:21]** code right now.

**[10:22]** Right.

**[10:22]** Roll back to the last model.

**[10:24]** but I don't know,

**[10:26]** I'm just kind of having fun at this point.

**[10:27]** Let's see.

**[10:31]** Do you see here?

**[10:32]** It's running the search to get a.

**[10:36]** Basically this is telling it the schema

**[10:38]** and how to sort through.

**[10:39]** that one didn't work.

**[10:40]** What happened there?

**[10:42]** Yeah,

**[10:43]** so it,

**[10:43]** ran it improperly.

**[10:45]** But

**[10:46]** I,

**[10:46]** think you guys get the point.

**[10:47]** I'll let this one run.

**[10:53]** so

**[10:53]** I want you to think of it this way.

**[10:54]** This is like

**[10:56]** very specific deep

**[10:59]** first principles,

**[11:00]** all the best practices,

**[11:02]** all the learnings about how to use AI.

**[11:05]** And what this can do for you

**[11:07]** is you have to give it the unique constraints,

**[11:11]** of your domain.

**[11:12]** So for go to market engineering,

**[11:13]** it might be list building or it might be ICP

**[11:15]** definitions or it's talking to customers or

**[11:17]** whatever it is.

**[11:20]** this can help you do all of that stuff far more

**[11:23]** effectively

**[11:24]** because you don't have to get in the weeds of

**[11:27]** learning about different agent,

**[11:29]** architectures or what's working or what.

**[11:31]** Not unless you want to.

**[11:32]** Obviously,

**[11:32]** I'm someone who wants to.

**[11:33]** I love this stuff.

**[11:34]** But this is really meant to let you offload a lot

**[11:37]** of that complexity,

**[11:38]** and literally have the agent do it for you,

**[11:40]** because it can talk to this knowledge graph.

**[11:45]** Just to show you that end,

**[11:46]** end result here.

**[11:49]** context rot.

**[11:51]** Yep,

**[11:51]** yep.

**[11:51]** Compaction,

**[11:52]** coherence.

**[11:53]** These are all real problems I've seen.

**[11:55]** And like,

**[11:56]** I'm reading it for the first time.

**[11:59]** Sorry.

**[12:01]** I think.

**[12:02]** I think in this case,

**[12:03]** the example I was thinking about,

**[12:05]** it's really

**[12:06]** this one.

**[12:07]** I actually post about this yesterday,

**[12:10]** but I just want to show you that as proof of work.

**[12:13]** So here's my call to action.

**[12:14]** Want to be meta about it?

**[12:16]** Go use the graph today.

**[12:18]** I'm going to iterate on this a ton.

**[12:19]** Part of the value of this for me personally beyond

**[12:23]** building I guess the taste matter brand or

**[12:26]** whatever itself is using all of my most advanced

**[12:30]** context engineering techniques that I need to test

**[12:32]** bed for.

**[12:33]** So

**[12:34]** this concepts thing being self organizing,

**[12:36]** it was working really great and then like over the

**[12:38]** weekend it exploded.

**[12:39]** Right.

**[12:40]** So you see this like super long tail,

**[12:43]** this is super valuable test data for me and the

**[12:46]** more people using it,

**[12:47]** the more people getting value out of it,

**[12:50]** the better.

**[12:51]** So you can go subscribe.

**[12:53]** Obviously the briefs are the daily

**[12:55]** roll up thing.

**[12:56]** I might do weekly version of it as well just to

**[12:58]** kind of do a

**[12:59]** higher signal

**[13:00]** version,

**[13:01]** that's actually curated by me.

**[13:04]** and then the VMCP access is free as well for right

**[13:08]** now.

**[13:09]** I have a few dozen more spots left.

**[13:12]** Cloudflare's

**[13:14]** access policy has 50 slots,

**[13:15]** so once that runs out,

**[13:16]** that's the cap for now.

**[13:18]** but I hope this is useful for you and please send

**[13:21]** all of the feedback.

**[13:22]** I really appreciate it and I really appreciate

**[13:24]** your time today.

**[13:25]** Thanks so much.

**[13:26]** Bye.

**[0:00]** I built a tool that lets you distill tens of

**[0:02]** thousands of hours of the best AI engineers

**[0:04]** learnings and apply it directly to your AI and

**[0:07]** context engineering problems.

**[0:08]** I'm going to show you what it is,

**[0:09]** what makes it special and how to use it.

**[0:11]** Today,

**[0:11]** to solve your specific domain problems using Go to

**[0:14]** Market Engineering as an example.

**[0:15]** So what did I build?

**[0:16]** I built something called tastematter.

**[0:19]** Tastematter is a contents graph pulling in

**[0:23]** newsletters,

**[0:24]** tweets,

**[0:25]** YouTube videos,

**[0:26]** research papers,

**[0:28]** basically everything I consider high signal in

**[0:31]** the AI,

**[0:32]** and context engineering space.

**[0:33]** And a little bit beyond that,

**[0:36]** it is my attempt.

**[0:37]** So I originally built this

**[0:39]** because I was feeling very overwhelmed,

**[0:40]** trying to keep up to date with everything,

**[0:42]** all the time.

**[0:44]** and I decided that

**[0:46]** I was using this thing.

**[0:47]** I was using this thing so often,

**[0:49]** I was reading this thing every single day.

**[0:51]** I figured it'd be useful to other people.

**[0:54]** So,

**[0:54]** first part of it is this daily brief,

**[0:56]** and the second part is the actual context graph

**[0:58]** itself.

**[1:00]** So this graph is what I check every single day.

**[1:02]** It pulls in net new  articles,

**[1:04]** or I guess whatever,

**[1:05]** right?

**[1:06]** It's not just articles.

**[1:06]** We said tweets,

**[1:07]** whatever.

**[1:08]** it checks them against the graph.

**[1:09]** As you can see,

**[1:10]** it contradict it.

**[1:11]** It'll check  and see how these relate.

**[1:14]** So

**[1:15]** the concept graph will pull in

**[1:17]** an article,

**[1:19]** bucket it into a topic and then check it against

**[1:22]** the graph.

**[1:22]** So it's doing a lot more than just summarization.

**[1:25]** It's actually intelligently seeing where these

**[1:27]** concepts fit together,

**[1:28]** whether they support each other or contradict each

**[1:30]** other and then using that to generate a brief that

**[1:32]** is meant to be directly actionable every single

**[1:35]** day.

**[1:35]** So right here,

**[1:37]** right,

**[1:37]** this is like the main takeaway.

**[1:38]** Every single one of these signals has a specific

**[1:40]** action item you can take away and the supporting,

**[1:43]** context around it.

**[1:45]** So using this signal as an example,

**[1:46]** memory architecture is the actual lock.

**[1:48]** In

**[1:49]** choosing,

**[1:49]** cloud code or OpenAI isn't selecting a model,

**[1:52]** it's choosing

**[1:53]** your team's accumulated intelligence.

**[1:55]** it's pulling out to here,

**[1:57]** this post from,

**[2:00]** let's see,

**[2:03]** two days ago,

**[2:04]** where it's citing,

**[2:05]** or it's retweeting.

**[2:06]** This is the creator blank chain.

**[2:08]** And it's also,

**[2:10]** tagging the team at leda.

**[2:12]** This is like active discourse.

**[2:14]** not everything is this up to date.

**[2:16]** It's going to pull in from the past several

**[2:18]** months.

**[2:19]** Over time

**[2:20]** you build up this,

**[2:21]** archive.

**[2:23]** But the idea is that it's very much

**[2:26]** timely,

**[2:26]** relevant,

**[2:27]** actionable,

**[2:28]** with the long tail persisted into the context

**[2:30]** graph for you to look at later.

**[2:33]** so going to that graph itself.

**[2:37]** You'll see here that the graph

**[2:40]** shows only a small number of the

**[2:43]** concepts covered.

**[2:44]** Because if we go to the concept list,

**[2:45]** right,

**[2:46]** we have 289 concepts.

**[2:49]** this is partially from a long tail of bloat that,

**[2:52]** that's kind of popped up in the last couple days

**[2:55]** of running this thing since I have this actually

**[2:56]** doing it,

**[2:57]** running a self organizing taxonomy.

**[3:00]** probably need to clean this up.

**[3:01]** But

**[3:02]** the graph is meant to show you how certain topics

**[3:06]** fit together,

**[3:07]** where they support one another,

**[3:08]** they contradict one another.

**[3:10]** And it's meant to actually,

**[3:11]** instead of saying hey,

**[3:12]** this is just

**[3:15]** you know,

**[3:15]** a summarized version of it.

**[3:16]** It's meant to kind of as much as you can actually

**[3:19]** capture wisdom,

**[3:21]** in a system like this,

**[3:23]** it's meant to capture it and make it immediately

**[3:25]** applicable

**[3:26]** for your agents to use in your own agentic

**[3:28]** engineering.

**[3:29]** And that's what the concept graph is really for.

**[3:31]** The actual graph itself,

**[3:32]** if you were to visualize this,

**[3:33]** it will not fit on the screen.

**[3:35]** there would be too many concepts,

**[3:37]** too many  underlying articles and too many

**[3:39]** connections between them.

**[3:41]** But  this is kind of,

**[3:43]** this is meant to give you an idea of what we're

**[3:45]** working with and make it tangible.

**[3:47]** Getting on to the actual graph itself

**[3:49]** that is accessible via an MCP server.

**[3:52]** So to access the graph you just need to sign up

**[3:54]** for beta access,

**[3:55]** put in your email,

**[3:58]** subscribe

**[4:00]** and then you can go and copy.

**[4:01]** This is added to cloud code.

**[4:03]** I'm just going to use regular cloud web app.

**[4:05]** for the example today.

**[4:07]** Okay,

**[4:07]** here's how you're going to add it.

**[4:08]** You're going to add go to Settings

**[4:11]** connectors,

**[4:13]** add custom connector

**[4:16]** taste matter graph and you're going to put in this

**[4:19]** URL.

**[4:19]** Now when you do this,

**[4:21]** if you're logging in for the first time,

**[4:22]** it's going to redirect you to a login page.

**[4:24]** All you have to do is provide your email.

**[4:25]** It'll send you one time code for me,

**[4:27]** I've already done this so remembers me.

**[4:30]** and then you can see here configure.

**[4:32]** It has two tools.

**[4:34]** This is using something called code mode.

**[4:36]** It's hyper context efficient and allows you to get

**[4:38]** way more out of the graph.

**[4:39]** So I'll show you that right now.

**[4:42]** So using,

**[4:43]** I'm going to use an incognito window or not Window

**[4:46]** chat,

**[4:48]** incognito chat.

**[4:49]** So it doesn't use any of my,

**[4:50]** saved context.

**[4:52]** so you can see it working on its own.

**[4:54]** say,

**[4:55]** tell me,

**[4:56]** use the context,

**[4:58]** or,

**[4:59]** excuse me,

**[4:59]** use the Taste matter graph to

**[5:02]** tell me what is

**[5:04]** going on

**[5:05]** in

**[5:06]** Context Engineering right now

**[5:09]** as an example.

**[5:12]** so first I'm going to show you this.

**[5:13]** I want to show you

**[5:14]** the code mode execution because it's interesting

**[5:17]** itself.

**[5:17]** And then I'm going to show you,

**[5:19]** how it applies to a specific domain.

**[5:21]** This case being go to Market Engineering.

**[5:24]** So you see here it's loading a tool up.

**[5:27]** it basically says,

**[5:28]** hey,

**[5:28]** what tools do I have?

**[5:29]** Search,

**[5:30]** and execute,

**[5:32]** the core,

**[5:33]** innovation.

**[5:34]** I wish you could take credit for this.

**[5:35]** I can't.

**[5:36]** This Cloudflare created this language models are

**[5:38]** exceptionally good at writing code.

**[5:40]** So rather than giving them an arbitrary list of

**[5:42]** tools,

**[5:43]** you just have them write code and it drops content

**[5:45]** consumption by like 90%,

**[5:47]** makes it far faster and far smarter.

**[5:50]** So going into here

**[5:51]** to load the tools up and then it'll run a search,

**[5:53]** say,

**[5:54]** hey,

**[5:54]** what's the graph look like?

**[5:55]** And runs basically what looks like

**[5:57]** SQL,

**[5:58]** but then it comes back with,

**[6:02]** RAW access to the graph or full access to the

**[6:04]** graph,

**[6:04]** and it can synthesize that into insight.

**[6:07]** right here,

**[6:08]** this is from today,

**[6:09]** right?

**[6:10]** So this is basically mirroring,

**[6:12]** the graph from today because I asked it

**[6:14]** what's going on today,

**[6:16]** but it's pulling in like specific Twitter handles.

**[6:18]** We saw Sarah Let.

**[6:19]** Not Sarah Letta,

**[6:21]** Sarah Waters,

**[6:22]** who works at Leta or founded Letta,

**[6:23]** up here.

**[6:24]** And this is like a live look at what's happening

**[6:26]** in the space right now.

**[6:30]** So

**[6:31]** I know this is,

**[6:34]** it looks

**[6:35]** cool,

**[6:35]** it's pulling in stuff,

**[6:36]** it's like surfacing

**[6:38]** very deep.

**[6:39]** niche tips like disabling telemetry

**[6:42]** apparently degrades your

**[6:44]** cache rate.

**[6:46]** I want to take a step back and

**[6:49]** acknowledge that this is very in the weeds

**[6:51]** abstract.

**[6:52]** And if we're not looking at this stuff all day

**[6:54]** long like I am,

**[6:55]** it may seem like it's a lot,

**[6:58]** it is,

**[6:59]** but

**[7:00]** it's structured in a way that it's,

**[7:02]** you can point this whole

**[7:05]** cumulative knowledge base knowledge graph at your

**[7:08]** specific problems and get direct answers back that

**[7:11]** are grounded in it and also don't

**[7:16]** they're,

**[7:17]** they're grounded in a way that makes it

**[7:19]** so you can make a real trade off decision.

**[7:21]** I think most people take for granted,

**[7:23]** so much of engineering

**[7:26]** is around making trade offs and by having the

**[7:29]** full attribution chain of hey,

**[7:31]** this is what happens when you use a multi agent

**[7:34]** system versus single agent system.

**[7:35]** And this is what other people have found for

**[7:37]** example,

**[7:38]** right?

**[7:38]** You get far better

**[7:40]** design,

**[7:40]** outcomes.

**[7:42]** You get better outcomes.

**[7:43]** Yeah,

**[7:43]** that makes sense.

**[7:44]** Anyway,

**[7:45]** so like I'm going to say here like  I am building

**[7:48]** a signal machine

**[7:50]** using multiple agents,

**[7:53]** multiple agents for my GTM

**[7:58]** engineering

**[8:00]** work.

**[8:01]** What have

**[8:03]** others

**[8:03]** tried,

**[8:05]** and

**[8:08]** learned

**[8:08]** building

**[8:09]** systems

**[8:10]** like systems like this.

**[8:13]** and that's actually like obviously there's not a

**[8:15]** lot of context here.

**[8:16]** I'm not giving it much to work from.

**[8:18]** So the more you give it the more you're going to

**[8:19]** get back.

**[8:21]** but this is to show like you can go and ask very

**[8:24]** specific questions and get very specific,

**[8:27]** hopefully for you,

**[8:28]** relevant and valuable results back.

**[8:31]** Right.

**[8:31]** And it'll go and just run this like  recursive

**[8:35]** search against the graph and say hey,

**[8:36]** this is what Google found.

**[8:38]** So it's taking a second here,

**[8:39]** I'll cut this.

**[8:41]** So you can see it's streaming across right now.

**[8:43]** It ran a bunch of searches.

**[8:46]** this is actually a lot of context pulled in

**[8:50]** And it's providing multiple specific points of

**[8:53]** view

**[8:54]** that

**[8:55]** people,

**[8:55]** real people have,

**[8:56]** come up with

**[8:58]** for,

**[8:59]** different patterns to use.

**[9:00]** So am I seeing this for the first time myself?

**[9:02]** Is actually really interesting.

**[9:06]** hey,

**[9:07]** Jordan,

**[9:07]** Doug,

**[9:08]** you guys gotta.

**[9:09]** I guess you guys are in this thing now too.

**[9:13]** but like,

**[9:14]** I love how this has a full chain all the way from

**[9:18]** someone who's working on something,

**[9:20]** in public or they're publishing about it.

**[9:24]** It can synthesize those,

**[9:25]** learnings and insights into real concepts in the

**[9:28]** graph and then say,

**[9:29]** hey,

**[9:29]** this is what that person has done,

**[9:31]** and what's working for them and what's not.

**[9:34]** Right.

**[9:35]** So

**[9:36]** that's cool.

**[9:38]** Yeah,

**[9:38]** see,

**[9:38]** there's a ton here.

**[9:41]** and like,

**[9:41]** I'll try another one.

**[9:42]** Let's say,

**[9:44]** my agents are.

**[9:47]** This is something I've been having a problem with

**[9:49]** recently,

**[9:50]** myself

**[9:50]** losing coherence,

**[9:54]** and can't

**[9:56]** follow

**[9:57]** their own logic.

**[9:59]** What could be some

**[10:01]** sources,

**[10:02]** we'll say,

**[10:02]** my development agents,

**[10:07]** we'll say root cause is better.

**[10:13]** So I actually know the answer,

**[10:14]** this one already because I kind of,

**[10:17]** solutioned it generally less context.

**[10:19]** And if this is actually a specific issue in cloud

**[10:21]** code right now.

**[10:22]** Right.

**[10:22]** Roll back to the last model.

**[10:24]** but I don't know,

**[10:26]** I'm just kind of having fun at this point.

**[10:27]** Let's see.

**[10:31]** Do you see here?

**[10:32]** It's running the search to get a.

**[10:36]** Basically this is telling it the schema

**[10:38]** and how to sort through.

**[10:39]** that one didn't work.

**[10:40]** What happened there?

**[10:42]** Yeah,

**[10:43]** so it,

**[10:43]** ran it improperly.

**[10:45]** But

**[10:46]** I,

**[10:46]** think you guys get the point.

**[10:47]** I'll let this one run.

**[10:53]** so

**[10:53]** I want you to think of it this way.

**[10:54]** This is like

**[10:56]** very specific deep

**[10:59]** first principles,

**[11:00]** all the best practices,

**[11:02]** all the learnings about how to use AI.

**[11:05]** And what this can do for you

**[11:07]** is you have to give it the unique constraints,

**[11:11]** of your domain.

**[11:12]** So for go to market engineering,

**[11:13]** it might be list building or it might be ICP

**[11:15]** definitions or it's talking to customers or

**[11:17]** whatever it is.

**[11:20]** this can help you do all of that stuff far more

**[11:23]** effectively

**[11:24]** because you don't have to get in the weeds of

**[11:27]** learning about different agent,

**[11:29]** architectures or what's working or what.

**[11:31]** Not unless you want to.

**[11:32]** Obviously,

**[11:32]** I'm someone who wants to.

**[11:33]** I love this stuff.

**[11:34]** But this is really meant to let you offload a lot

**[11:37]** of that complexity,

**[11:38]** and literally have the agent do it for you,

**[11:40]** because it can talk to this knowledge graph.

**[11:45]** Just to show you that end,

**[11:46]** end result here.

**[11:49]** context rot.

**[11:51]** Yep,

**[11:51]** yep.

**[11:51]** Compaction,

**[11:52]** coherence.

**[11:53]** These are all real problems I've seen.

**[11:55]** And like,

**[11:56]** I'm reading it for the first time.

**[11:59]** Sorry.

**[12:01]** I think.

**[12:02]** I think in this case,

**[12:03]** the example I was thinking about,

**[12:05]** it's really

**[12:06]** this one.

**[12:07]** I actually post about this yesterday,

**[12:10]** but I just want to show you that as proof of work.

**[12:13]** So here's my call to action.

**[12:14]** Want to be meta about it?

**[12:16]** Go use the graph today.

**[12:18]** I'm going to iterate on this a ton.

**[12:19]** Part of the value of this for me personally beyond

**[12:23]** building I guess the taste matter brand or

**[12:26]** whatever itself is using all of my most advanced

**[12:30]** context engineering techniques that I need to test

**[12:32]** bed for.

**[12:33]** So

**[12:34]** this concepts thing being self organizing,

**[12:36]** it was working really great and then like over the

**[12:38]** weekend it exploded.

**[12:39]** Right.

**[12:40]** So you see this like super long tail,

**[12:43]** this is super valuable test data for me and the

**[12:46]** more people using it,

**[12:47]** the more people getting value out of it,

**[12:50]** the better.

**[12:51]** So you can go subscribe.

**[12:53]** Obviously the briefs are the daily

**[12:55]** roll up thing.

**[12:56]** I might do weekly version of it as well just to

**[12:58]** kind of do a

**[12:59]** higher signal

**[13:00]** version,

**[13:01]** that's actually curated by me.

**[13:04]** and then the VMCP access is free as well for right

**[13:08]** now.

**[13:09]** I have a few dozen more spots left.

**[13:12]** Cloudflare's

**[13:14]** access policy has 50 slots,

**[13:15]** so once that runs out,

**[13:16]** that's the cap for now.

**[13:18]** but I hope this is useful for you and please send

**[13:21]** all of the feedback.

**[13:22]** I really appreciate it and I really appreciate

**[13:24]** your time today.

**[13:25]** Thanks so much.

**[13:26]** Bye.
