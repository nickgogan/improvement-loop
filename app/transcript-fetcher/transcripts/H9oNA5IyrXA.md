# Transcript: Apple, Anthropic, And OpenAI Just Made The Same Move. Nobody Noticed.

**URL:** https://www.youtube.com/watch?v=H9oNA5IyrXA
**Segments:** 459
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 17:13
**Uploaded:** 2026-06-29

---

## Full Text

Open AI just released chat GPT 5.6 but not in the normal way. For now, access is restricted to a small group of government-approved partners while Washington reviews the cybersecurity risk. That's not a cancellation, but it's a tremendous slowdown in frontier availability. And by the end of this video, I want you to understand why that delay, the new Siri, Claude Tag, GLN 5.2, and Codex are all about the same underlying thing: a battle for the part of your brain that understands work. Not your brain in the sci-fi mind control sense. The everyday part. Which message matters? Which file is current? What the customer actually meant? What the team decided? What can be shared? What can't be shared? What counts as done? Because if frontier intelligence slows down, even for a few weeks, the next advantage is not owning the newest model. It's having the context that makes any good model useful. Look at the week through that lens, and the news starts to rhyme. Apple's trying to fix Siri by giving it access to your messages and photos and email and notes and screen and apps. Anthropic has launched Claude Tag in Slack, where a team can give Claude access to selected channels and tools and data and code bases. Z.ai's GLN 5.2 has made cheap, open, frontier-ish intelligence feel much closer to a reality than it did just a few weeks ago. And Open AI has a Codex paper showing that inside Open AI, Codex has become the dominant surface for work-related AI output. And those really do sound like completely different stories. I get it. Open AI being told to slow the rollout, Apple trying to make Siri less embarrassing, Anthropic putting Claude into Slack. How are these related? The The problem is the same underneath all of them. The model can be smart and still not know what's going on. If you use AI every day, you already know the feeling. You can open Codex or ChatGPT or Claude or Gemini, and and the model's very capable, right? It can write, it can reason, it can summarize, it can help you think. But before it can do something useful, you have to carry that entire situation into the context window, often through uploading files to the chat box. You paste the email, you paste the memo, you explain who the client is, you explain which version of the deck is current, you explain that the Slack thread from yesterday changed that decision. This is what prompting has become as we've asked these models to do more. And then after all of that, when you put all of that in, the AI finally becomes extremely useful. And that's a really big friction point. And that is what we've described as an agent problem, right? A problem that you want agents to fix by going after the context window. And that's the promise that we've all been trying to realize with agents for the last few months. So I'm going to walk you through three surfaces here. I'm going to walk you through Apple's Siri, Claude tag, and Codex in terms of execution inside OpenAI. And I'm going to walk you through the pressure points around them. GLM 5.2 on the one hand, the delay of ChatGPT 5.6 on the other, and throughout we're going to uncover the story of why intelligence is getting cheaper, the newest frontier intelligence is coming out more slowly, and what that means for all of us as far as context goes. Fundamentally, the next useful AI product is probably not going to be the one that wins a benchmark. It's going to be the one that knows where the work is, what it's allowed to see, what it's allowed to do, and it's going to be something that knows that seamlessly. So let's start with Siri because Siri is something that for better or worse we all understand. Siri has been bad for so long that it's become a punchline. You can ask it something normal and half the time it either misunderstands the question or gives you a web search that makes you wonder why you bothered speaking out loud. So the easy headline for a long time has been Apple's finally trying to do something with Siri. We don't know if it's actually good or not. We have a little skepticism, but Apple's relaunching Siri effectively. And I get where that story exists, right? Apple itself is talking about Siri as a conversational AI assistant, is promising more natural conversations, richer answers, a dedicated Siri app. And that's all a part of the story, and it may well work. I've gotten my hands on it a little bit. I've played with it, but I don't think that Siri becomes Chat GPT is the story here. I think the story here is that Apple is trying to make Siri useful by connecting it to the context in your life. Like, when is my mom landing on the plane requires context from calendar, flight number, email confirmation, uh whether another family member said they might go pick up mom instead, whether the airplane uh is late or not. And so, the challenge for Apple is to find a way to privately and securely connect Siri to where the context lives on your phone, right? Photos, calendar, notes, email, app state, screen, etc. And if Siri can do that, Siri's intelligence level doesn't have to be super high for Siri to be incredibly useful. Ultimately, the question of Siri's capability may be the wrong one. And Apple's answer is not a capability answer. It's a context answer. It's an answer about where intelligence lives, and they're trying to push it as close to your systems as possible. So, on-device processing is Apple's goal wherever possible, and then private cloud where it's not. So, one of the things that's really interesting from a product shape here for Apple's solution is that Apple is essentially saying your assistant gets better when it's close to you, and very conveniently, when it's close to you, we can construct a privacy architecture that means it's only yours. And that's a consumer answer to this context problem, right? It's an answer where Siri doesn't have to be able to be that smart to use your phone to be extremely useful. And so, suddenly, instead of Apple's advantage coming from the App Store ecosystem or from the hardware, Apple's advantage comes from the fact that we have Apple products, and we have context that lives inside the iPhone, and Apple can access that context in ways that are very useful to us. Keep that in mind as we walk over to the work site and we talk about Claude Tag. Now, Anthropic's product announcement is pretty plain on the surface. Claude Tag starts in Slack, a team can grant Claude access to selected channels, to tools, to data, to code bases it can tag it in, and then Claude just works through tasks and stages as it's tagged in and it can respond in the thread, it can remember relevant information from channels it's in and it can operate inside of particular permission scopes, particular spend limits, particular logs it can touch. That sounds like a Slack bot, but don't say that too fast because Slack has had bots for a long time and the interesting thing is that Anthropic is trying to put the assistant inside your team's context. So, on your phone the context is private and messy because it's your life. In a company the context is shared and permissioned and political and stale and half-written and in six places. And so, the thing that's interesting about all of this is that work is happening in those messy places and for a long time AI has been kind of separate from that except in a few instances. Devin has been very successful with this from a coding perspective, but there's not a lot of great off-the-shelf instances for really intelligent AI coming into that kind of messy context. And so, when Anthropic says Claude Tag can build context over time, that is not only a real claim, but the heart of where the company is going to go. It's a very powerful and dangerous statement because the more useful Claude becomes in Slack, the more it need access to messy stuff companies are bad at governing like engineering decisions and customer tickets and pricing debates and people information. And Anthropic knows this which is why the launch language spends so much time on scopes and permissions, on admin controls, on channel defined memories. Uh they recognize that they're going to have to earn that trust because if you put an AI teammate in Slack and it breaks boundaries, you've created a context leak, you've created a corporate liability. And so, what Anthropic is saying is, you can trust us with this context because you're in charge the whole time. And I think that Claude tag is a much better signal than most out there of this whole AI co-worker phenomenon. Because we have a lot of startups that are in this space, and one of the things that Anthropic is doing very intentionally here is they're saying, you fed us formal context through prompts, uh through co-work, through Claude code for a while. Now trust us with informal context, and enable us to be a co-worker that's more useful as a result. And no other company can say that in the same way. This is Anthropic doing for work what Apple is doing for your phone. Now let's bring in Codex. Now a Codex study is easy to dismiss. It doesn't feel like it's news. But I think the Codex paper is really useful in this conversation because software is showing us the assistant context problem in its cleanest form. And Codex is a piece of software, and the study that's released is essentially how actual employees at OpenAI chose or did not choose to adopt Codex over the course of time, and what they used Codex for. In other words, what context did they trust Codex with? And this is fascinating to me because you might think that at OpenAI, it's a requirement and everyone's mandated to use Codex. That wasn't how it worked. Codex had to earn everyone's trust. Codex had to earn trust first with engineers, and then with other knowledge workers at OpenAI. And so, the thing that matters the most to me when I read this study is that even at a company that is one of the most AI native companies on the planet, you still have to think about where you trust a particular AI application with context, and it's not a zero-to-one light flip switch. But, it is true that you can see tipping points. And one of the tipping points that's evident in the data from OpenAI and that I have seen personally is that Codex got a lot more useful in the last couple months after 5.5 was released. And you can see that in the adoption data that shows that the popular adoption of Codex after 5.5 in non-tech circles in OpenAI skyrocketed. Now, the thing that stands out to me when you put that in the context conversation we've been having is that Codex has with 5.5 earned the trust to get legal stuff, recruiting stuff, sales stuff, like all of that dirty context fed into it in the way it earned trust with engineers for code. And there's a lot more in that study. I encourage you to read it. I can link it. Uh Codex is doing the opposite of Claude tag. So, if Claude tag is basically saying, "You work in Slack, so tag Claude in." Codex is saying, "Your work is sensitive. Your work is important. Make sure you point Codex at the local files you care about for that work, and Codex can take care of the rest." And so, that's a frame that has Codex as your launchpad, Codex as your headquarters. Whereas, Claude's frame is more let Claude come to where you already are, and you can give it the messy context. In both cases, there's some mess, but Claude is saying that they can tackle the human conversation and the context and still do useful work. And Codex is saying, "You know what? Give us the files, give us the jobs, and we can produce great outputs for you, whether you're in legal or sales or HR." I love that distinction, not because I don't think that OpenAI will release a tag Codex soon. These models tend to copy each other. But, because I think it shows the difference in product shape around context that these two labs have. Claude has always been a we come to you, we wrap our interface around you kind of products. Uh Claude code was really exciting and co-work was really exciting partly because they basically said just type what you want into the terminal, type what you want into co-work, uh and we will just take care of it for you. Now they're taking the next step in this slack. It's in a sandbox, it's just going to do the work there, and then you'll get an output. It's almost like bring your wheelbarrow of work and let us do the work and then we'll we'll give you an output. And it's gotten much more wide-ranging as computer uses come in in the last couple months and that's made it much more useful and you can see that in the study, but it's still fundamentally a file-shaped tool. And Claude is kind of a chat-shaped tool. And I realize that that is a gross simplification because both of them tackle files, both of them do chat, right? So I'm not saying it's one or the other. It's not a light bulb on-off conversation. Claude has for a long time thought of the problem of context as conversational in the way they've designed their products. And Codex for a long time has thought about the problem of context in terms of files and has been a file-shaped answer. And you can still see the legacy of that context in these moments this week. Now, this brings us to the next Open AI story, which is around this chat GPT 5.6 delay. If a frontier model spends the next few weeks or months in a restricted preview, which it looks like almost all of them will, we in the world do not pause and wait. Companies still have Claude and they have Open AI models and they now have GLM 5.2 and they'll have whatever new open-source model is coming right after that, maybe a a new deep seek, who knows. And they will have a anticipation but not the reality of future frontier work from Anthropic and Open AI, which by the way are still developing and still accumulating knowledge very rapidly internally. They're just not able to release it as fast. And so the government restriction is putting friction at the frontier of intelligence, and it means that there is more pressure on Anthropic and OpenAI to release features like Claude tag because you have to increase the utility of the intelligence you already have to bring it closer to context so that you get more value for the customer. If you can spend, you know, 2 minutes tagging in Claude or 30 seconds tagging in Claude instead of 10 minutes briefing the AI, you've saved yourself a lot of time. You can add that up, right? If it's something where it becomes a seamless part of your work, then you perceive a lot more utility from that even if the model didn't get smarter. What that means is that we are in the middle of a context war, and that is the way you should read the news for the next few weeks, I think. You should be looking at and saying Apple is battling for your personal context, which because we bring our devices to work becomes a work context conversation. Uh Anthropic and OpenAI are definitely battling over work context. They have different shapes for how they do that. And one of the most interesting things here is that effectively the government slowdown is giving open-source models time to catch up in public even if they're not catching up in private. So Anthropic and OpenAI may maintain their 6 7 8-month lead over open-source models privately, but the public models we have access to may start to close because the US government is slowing down frontier model releases. And that leads to a tremendous amount of pressure on utility in the context there. There's going to be a huge war over how quickly and easily an AI model can apply intelligence to that context. And so look at Apple and Anthropic and OpenAI as being in the same boat, even though we don't typically put them in that boat. And think about your context. Think about what context you're comfortable giving to these companies. Think about what context you want to retain, and think about whether you are willing to put the time in to actually build elements of a harness that allow you to decide where to route your context. And so, when I've talked about Open Brain and and Open Engine most recently, a lot of what I'm doing is basically building pieces of a harness in public so that you have more choices. And I'm not the only one doing it. There are others who are doing it. It's a good work. I'm glad it's widespread. There's There's a big movement around this. I think it's important that we have choice. We shouldn't have to feel like we're locked in to any given model provider. We should have the option to retain our context and use intelligence in order to get meaningful work done. And I think the more we look at the story going forward, the more it's a story of the intelligence wars shifting into the context wars. It's going to be less about Windows 5.6 come out, and it will eventually. Windows Fable come out, and it will eventually. And more about when can we make the next step in applying intelligence so that it's useful. And the story of Siri really shows us, pardon me, Apple, that you don't have to have an incredibly intelligent model to have incredible utility. Like, your model doesn't have to max out the benchmarks. That's not what Siri is going to do. But Siri applied across your context on your phone seamlessly can still be incredibly powerful. So, that's the story under the story this week. Pay attention to the context layer. It's going to matter a lot. And if you want more stories under the story, I do them every week, subscribe for more.

---

## Timestamped Segments

**[0:00]** Open AI just released chat GPT 5.6 but

**[0:02]** not in the normal way. For now, access

**[0:04]** is restricted to a small group of

**[0:06]** government-approved partners while

**[0:07]** Washington reviews the cybersecurity

**[0:09]** risk. That's not a cancellation, but

**[0:11]** it's a tremendous slowdown in frontier

**[0:13]** availability. And by the end of this

**[0:15]** video, I want you to understand why that

**[0:17]** delay, the new Siri, Claude Tag, GLN

**[0:21]** 5.2, and Codex are all about the same

**[0:23]** underlying thing: a battle for the part

**[0:26]** of your brain that understands work. Not

**[0:28]** your brain in the sci-fi mind control

**[0:30]** sense. The everyday part. Which message

**[0:32]** matters? Which file is current? What the

**[0:33]** customer actually meant? What the team

**[0:36]** decided? What can be shared? What can't

**[0:37]** be shared? What counts as done? Because

**[0:40]** if frontier intelligence slows down,

**[0:42]** even for a few weeks, the next advantage

**[0:45]** is not owning the newest model. It's

**[0:47]** having the context that makes any good

**[0:49]** model useful. Look at the week through

**[0:51]** that lens, and the news starts to rhyme.

**[0:53]** Apple's trying to fix Siri by giving it

**[0:55]** access to your messages and photos and

**[0:56]** email and notes and screen and apps.

**[0:58]** Anthropic has launched Claude Tag in

**[1:00]** Slack, where a team can give Claude

**[1:01]** access to selected channels and tools

**[1:03]** and data and code bases. Z.ai's GLN 5.2

**[1:07]** has made cheap, open, frontier-ish

**[1:09]** intelligence feel much closer to a

**[1:11]** reality than it did just a few weeks

**[1:12]** ago. And Open AI has a Codex paper

**[1:15]** showing that inside Open AI, Codex has

**[1:17]** become the dominant surface for

**[1:18]** work-related AI output. And those really

**[1:21]** do sound like completely different

**[1:22]** stories. I get it. Open AI being told to

**[1:24]** slow the rollout, Apple trying to make

**[1:26]** Siri less embarrassing, Anthropic

**[1:28]** putting Claude into Slack. How are these

**[1:30]** related? The The problem is the same

**[1:32]** underneath all of them. The model can be

**[1:34]** smart and still not know what's going

**[1:37]** on. If you use AI every day, you already

**[1:39]** know the feeling. You can open Codex or

**[1:41]** ChatGPT or Claude or Gemini, and and the

**[1:43]** model's very capable, right? It can

**[1:45]** write, it can reason, it can summarize,

**[1:47]** it can help you think. But before it can

**[1:49]** do something useful, you have to carry

**[1:51]** that entire situation into the context

**[1:54]** window, often through uploading files to

**[1:55]** the chat box. You paste the email, you

**[1:58]** paste the memo, you explain who the

**[2:00]** client is, you explain which version of

**[2:01]** the deck is current, you explain that

**[2:03]** the Slack thread from yesterday changed

**[2:04]** that decision. This is what prompting

**[2:07]** has become as we've asked these models

**[2:09]** to do more.

**[2:10]** And then after all of that, when you put

**[2:12]** all of that in, the AI finally becomes

**[2:14]** extremely useful. And that's a really

**[2:16]** big friction point. And that is what

**[2:18]** we've described as an agent problem,

**[2:21]** right? A problem that you want agents to

**[2:22]** fix by going after the context window.

**[2:25]** And that's the promise that we've all

**[2:27]** been trying to realize with agents for

**[2:30]** the last few months. So I'm going to

**[2:31]** walk you through three surfaces here.

**[2:33]** I'm going to walk you through Apple's

**[2:34]** Siri, Claude tag, and Codex in terms of

**[2:37]** execution inside OpenAI. And I'm going

**[2:40]** to walk you through the pressure points

**[2:41]** around them. GLM 5.2 on the one hand,

**[2:43]** the delay of ChatGPT 5.6 on the other,

**[2:46]** and throughout we're going to uncover

**[2:48]** the story of why intelligence is getting

**[2:51]** cheaper, the newest frontier

**[2:53]** intelligence is coming out more slowly,

**[2:55]** and what that means for all of us as far

**[2:58]** as context goes. Fundamentally, the next

**[3:01]** useful AI product is probably not going

**[3:03]** to be the one that wins a benchmark.

**[3:04]** It's going to be the one that knows

**[3:06]** where the work is, what it's allowed to

**[3:08]** see, what it's allowed to do, and it's

**[3:10]** going to be something that knows that

**[3:11]** seamlessly. So let's start with Siri

**[3:13]** because Siri is something that for

**[3:15]** better or worse we all understand. Siri

**[3:17]** has been bad for so long that it's

**[3:19]** become a punchline. You can ask it

**[3:21]** something normal and half the time it

**[3:22]** either misunderstands the question or

**[3:24]** gives you a web search that makes you

**[3:25]** wonder why you bothered speaking out

**[3:27]** loud. So the easy headline for a long

**[3:29]** time has been Apple's finally trying to

**[3:31]** do something with Siri. We don't know if

**[3:34]** it's actually good or not. We have a

**[3:35]** little skepticism, but Apple's

**[3:36]** relaunching Siri effectively. And I get

**[3:38]** where that story exists, right? Apple

**[3:40]** itself is talking about Siri as a

**[3:42]** conversational AI assistant, is

**[3:44]** promising more natural conversations,

**[3:46]** richer answers, a dedicated Siri app.

**[3:49]** And that's all a part of the story, and

**[3:51]** it may well work. I've gotten my hands

**[3:53]** on it a little bit. I've played with it,

**[3:55]** but I don't think that Siri becomes Chat

**[3:57]** GPT is the story here. I think the story

**[4:00]** here is that Apple is trying to make

**[4:02]** Siri useful by connecting it to the

**[4:05]** context in your life. Like, when is my

**[4:07]** mom landing on the plane requires

**[4:10]** context from calendar, flight number,

**[4:12]** email confirmation, uh whether another

**[4:15]** family member said they might go pick up

**[4:17]** mom instead, whether the airplane uh is

**[4:20]** late or not. And so, the challenge for

**[4:23]** Apple is to find a way to privately and

**[4:26]** securely connect Siri to where the

**[4:29]** context lives on your phone, right?

**[4:30]** Photos, calendar, notes, email, app

**[4:32]** state, screen, etc. And if Siri can do

**[4:35]** that, Siri's intelligence level doesn't

**[4:38]** have to be super high for Siri to be

**[4:41]** incredibly useful. Ultimately, the

**[4:44]** question of Siri's capability may be the

**[4:46]** wrong one. And Apple's answer is not a

**[4:49]** capability answer. It's a context

**[4:51]** answer. It's an answer about where

**[4:53]** intelligence lives, and they're trying

**[4:55]** to push it as close to your systems as

**[4:57]** possible. So, on-device processing is

**[4:59]** Apple's goal wherever possible, and then

**[5:01]** private cloud where it's not. So, one of

**[5:04]** the things that's really interesting

**[5:05]** from a product shape here for Apple's

**[5:07]** solution is that Apple is essentially

**[5:09]** saying your assistant gets better when

**[5:10]** it's close to you, and very

**[5:12]** conveniently, when it's close to you, we

**[5:14]** can construct a privacy architecture

**[5:16]** that means it's only yours. And that's a

**[5:19]** consumer answer to this context problem,

**[5:21]** right? It's an answer where Siri doesn't

**[5:23]** have to be able to be that smart to use

**[5:25]** your phone to be extremely useful. And

**[5:28]** so, suddenly, instead of Apple's

**[5:29]** advantage coming from the App Store

**[5:31]** ecosystem or from the hardware, Apple's

**[5:33]** advantage comes from the fact that we

**[5:35]** have Apple products, and we have context

**[5:38]** that lives inside the iPhone, and Apple

**[5:40]** can access that context in ways that are

**[5:42]** very useful to us. Keep that in mind as

**[5:45]** we walk over to the work site and we

**[5:47]** talk about Claude Tag. Now, Anthropic's

**[5:49]** product announcement is pretty plain on

**[5:51]** the surface. Claude Tag starts in Slack,

**[5:54]** a team can grant Claude access to

**[5:56]** selected channels, to tools, to data, to

**[5:58]** code bases it can tag it in, and then

**[6:00]** Claude just works through tasks and

**[6:02]** stages as it's tagged in and it can

**[6:03]** respond in the thread, it can remember

**[6:05]** relevant information from channels it's

**[6:07]** in and it can operate inside of

**[6:10]** particular permission scopes, particular

**[6:12]** spend limits, particular logs it can

**[6:15]** touch. That sounds like a Slack bot, but

**[6:17]** don't say that too fast because Slack

**[6:19]** has had bots for a long time and the

**[6:21]** interesting thing is that Anthropic is

**[6:23]** trying to put the assistant inside your

**[6:25]** team's context. So, on your phone the

**[6:28]** context is private and messy because

**[6:30]** it's your life. In a company the context

**[6:32]** is shared and permissioned and political

**[6:34]** and stale and half-written and in six

**[6:36]** places. And so, the thing that's

**[6:39]** interesting about all of this is that

**[6:41]** work is happening in those messy places

**[6:44]** and for a long time AI has been kind of

**[6:46]** separate from that except in a few

**[6:48]** instances. Devin has been very

**[6:49]** successful with this from a coding

**[6:51]** perspective, but there's not a lot of

**[6:52]** great off-the-shelf instances for really

**[6:55]** intelligent AI coming into that kind of

**[6:57]** messy context. And so, when Anthropic

**[7:00]** says Claude Tag can build context over

**[7:03]** time, that is not only a real claim, but

**[7:07]** the heart of where the company is going

**[7:09]** to go. It's a very powerful and

**[7:11]** dangerous statement because the more

**[7:13]** useful Claude becomes in Slack, the more

**[7:16]** it need access to messy stuff companies

**[7:19]** are bad at governing like engineering

**[7:21]** decisions and customer tickets and

**[7:22]** pricing debates and people information.

**[7:25]** And Anthropic knows this which is why

**[7:26]** the launch language spends so much time

**[7:28]** on scopes and permissions, on admin

**[7:31]** controls, on channel defined memories.

**[7:33]** Uh they recognize that they're going to

**[7:35]** have to earn that trust because if you

**[7:37]** put an AI teammate in Slack and it

**[7:39]** breaks boundaries, you've created a

**[7:41]** context leak, you've created a corporate

**[7:43]** liability. And so, what Anthropic is

**[7:46]** saying is, you can trust us with this

**[7:48]** context because you're in charge the

**[7:50]** whole time. And I think that Claude tag

**[7:52]** is a much better signal than most out

**[7:54]** there of this whole AI co-worker

**[7:56]** phenomenon. Because we have a lot of

**[7:58]** startups that are in this space, and one

**[8:01]** of the things that Anthropic is doing

**[8:04]** very intentionally here is they're

**[8:06]** saying, you fed us formal context

**[8:09]** through prompts, uh through co-work,

**[8:11]** through Claude code for a while. Now

**[8:13]** trust us with informal context, and

**[8:17]** enable us to be a co-worker that's more

**[8:19]** useful as a result. And no other company

**[8:21]** can say that in the same way. This is

**[8:24]** Anthropic doing for work what Apple is

**[8:27]** doing for your phone. Now let's bring in

**[8:29]** Codex. Now a Codex study is easy to

**[8:32]** dismiss. It doesn't feel like it's news.

**[8:34]** But I think the Codex paper is really

**[8:37]** useful in this conversation because

**[8:39]** software is showing us the assistant

**[8:41]** context problem in its cleanest form.

**[8:44]** And Codex is a piece of software, and

**[8:46]** the study that's released is essentially

**[8:48]** how actual employees at OpenAI chose or

**[8:51]** did not choose to adopt Codex over the

**[8:54]** course of time, and what they used Codex

**[8:56]** for. In other words, what context did

**[8:59]** they trust Codex with? And this is

**[9:02]** fascinating to me because you might

**[9:04]** think that at OpenAI, it's a requirement

**[9:06]** and everyone's mandated to use Codex.

**[9:08]** That wasn't how it worked. Codex had to

**[9:11]** earn everyone's trust. Codex had to earn

**[9:14]** trust first with engineers, and then

**[9:17]** with other knowledge workers at OpenAI.

**[9:19]** And so, the thing that matters the most

**[9:22]** to me when I read this study is that

**[9:24]** even at a company that is one of the

**[9:27]** most AI native companies on the planet,

**[9:30]** you still have to think about where you

**[9:34]** trust a particular AI application with

**[9:37]** context, and it's not a zero-to-one

**[9:40]** light flip switch. But, it is true that

**[9:42]** you can see tipping points. And one of

**[9:44]** the tipping points that's evident in the

**[9:46]** data from OpenAI and that I have seen

**[9:48]** personally is that Codex got a lot more

**[9:51]** useful in the last couple months after

**[9:53]** 5.5 was released. And you can see that

**[9:56]** in the adoption data that shows that the

**[9:59]** popular adoption of Codex after 5.5 in

**[10:03]** non-tech circles in OpenAI skyrocketed.

**[10:07]** Now, the thing that stands out to me

**[10:08]** when you put that in the context

**[10:10]** conversation we've been having is that

**[10:13]** Codex has with 5.5 earned the trust to

**[10:17]** get legal stuff, recruiting stuff, sales

**[10:21]** stuff, like all of that dirty context

**[10:23]** fed into it in the way it earned trust

**[10:26]** with engineers for code. And there's a

**[10:28]** lot more in that study. I encourage you

**[10:30]** to read it. I can link it. Uh Codex is

**[10:33]** doing the opposite of Claude tag. So, if

**[10:35]** Claude tag is basically saying, "You

**[10:36]** work in Slack, so tag Claude in." Codex

**[10:40]** is saying, "Your work is sensitive. Your

**[10:42]** work is important. Make sure you point

**[10:45]** Codex at the local files you care about

**[10:47]** for that work, and Codex can take care

**[10:49]** of the rest." And so, that's a frame

**[10:51]** that has Codex as your launchpad, Codex

**[10:54]** as your headquarters. Whereas, Claude's

**[10:56]** frame is more let Claude come to where

**[10:58]** you already are, and you can give it the

**[11:00]** messy context. In both cases, there's

**[11:03]** some mess, but Claude is saying that

**[11:06]** they can tackle the human conversation

**[11:09]** and the context and still do useful

**[11:11]** work. And Codex is saying, "You know

**[11:13]** what? Give us the files, give us the

**[11:15]** jobs, and we can produce great outputs

**[11:18]** for you, whether you're in legal or

**[11:19]** sales or HR." I love that distinction,

**[11:22]** not because I don't think that OpenAI

**[11:24]** will release a tag Codex soon. These

**[11:26]** models tend to copy each other. But,

**[11:28]** because I think it shows the difference

**[11:31]** in product shape around context that

**[11:33]** these two labs have. Claude has always

**[11:37]** been a we come to you, we wrap our

**[11:40]** interface around you kind of products.

**[11:43]** Uh Claude code was really exciting and

**[11:45]** co-work was really exciting partly

**[11:46]** because they basically said just type

**[11:49]** what you want into the terminal, type

**[11:50]** what you want into co-work, uh and we

**[11:52]** will just take care of it for you. Now

**[11:53]** they're taking the next step in this

**[11:55]** slack. It's in a sandbox, it's just

**[11:56]** going to do the work there, and then

**[11:58]** you'll get an output. It's almost like

**[12:00]** bring your wheelbarrow of work and let

**[12:02]** us do the work and then we'll we'll give

**[12:03]** you an output. And it's gotten much more

**[12:06]** wide-ranging as computer uses come in in

**[12:09]** the last couple months and that's made

**[12:10]** it much more useful and you can see that

**[12:12]** in the study, but it's still

**[12:14]** fundamentally a file-shaped tool. And

**[12:17]** Claude is kind of a chat-shaped tool.

**[12:22]** And I realize that that is a gross

**[12:23]** simplification because both of them

**[12:25]** tackle files, both of them do chat,

**[12:27]** right? So I'm not saying it's one or the

**[12:29]** other. It's not a light bulb on-off

**[12:31]** conversation. Claude has for a long time

**[12:34]** thought of the problem of context as

**[12:36]** conversational in the way they've

**[12:38]** designed their products. And Codex for a

**[12:40]** long time has thought about the problem

**[12:43]** of context in terms of files and has

**[12:45]** been a file-shaped answer. And you can

**[12:48]** still see the legacy of that context in

**[12:50]** these moments this week. Now, this

**[12:52]** brings us to the next Open AI story,

**[12:54]** which is around this chat GPT 5.6 delay.

**[12:57]** If a frontier model spends the next few

**[13:00]** weeks or months in a restricted preview,

**[13:01]** which it looks like almost all of them

**[13:03]** will, we in the world do not pause and

**[13:06]** wait. Companies still have Claude and

**[13:08]** they have Open AI models and they now

**[13:10]** have GLM 5.2 and they'll have whatever

**[13:12]** new open-source model is coming right

**[13:14]** after that, maybe a a new deep seek, who

**[13:15]** knows. And they will have a anticipation

**[13:20]** but not the reality of future frontier

**[13:22]** work from Anthropic and Open AI, which

**[13:24]** by the way are still developing and

**[13:25]** still accumulating knowledge very

**[13:28]** rapidly internally. They're just not

**[13:30]** able to release it as fast. And so the

**[13:32]** government restriction is putting

**[13:34]** friction at the frontier of

**[13:36]** intelligence, and it means that there is

**[13:38]** more pressure on Anthropic and OpenAI to

**[13:42]** release features like Claude tag because

**[13:44]** you have to increase the utility of the

**[13:47]** intelligence you already have to bring

**[13:50]** it closer to context so that you get

**[13:53]** more value for the customer. If you can

**[13:56]** spend, you know, 2 minutes tagging in

**[13:59]** Claude or 30 seconds tagging in Claude

**[14:01]** instead of 10 minutes briefing the AI,

**[14:03]** you've saved yourself a lot of time. You

**[14:05]** can add that up, right? If it's

**[14:07]** something where it becomes a seamless

**[14:08]** part of your work, then you perceive a

**[14:11]** lot more utility from that even if the

**[14:14]** model didn't get smarter. What that

**[14:17]** means is that we are in the middle of a

**[14:20]** context war, and that is the way you

**[14:22]** should read the news for the next few

**[14:24]** weeks, I think. You should be looking at

**[14:26]** and saying Apple is battling for your

**[14:28]** personal context, which because we bring

**[14:30]** our devices to work becomes a work

**[14:32]** context conversation. Uh Anthropic and

**[14:35]** OpenAI are definitely battling over work

**[14:38]** context. They have different shapes for

**[14:39]** how they do that. And one of the most

**[14:41]** interesting things here is that

**[14:43]** effectively the government slowdown is

**[14:45]** giving open-source models time to catch

**[14:49]** up in public even if they're not

**[14:51]** catching up in private. So Anthropic and

**[14:53]** OpenAI may maintain their 6 7 8-month

**[14:56]** lead over open-source models privately,

**[14:58]** but the public models we have access to

**[15:00]** may start to close because the US

**[15:03]** government is slowing down frontier

**[15:04]** model releases. And that leads to a

**[15:06]** tremendous amount of pressure on utility

**[15:09]** in the context there. There's going to

**[15:10]** be a huge war over how quickly and

**[15:13]** easily an AI model can apply

**[15:15]** intelligence to that context. And so

**[15:18]** look at Apple and Anthropic and OpenAI

**[15:21]** as being in the same boat, even though

**[15:23]** we don't typically put them in that

**[15:24]** boat. And think about your context.

**[15:27]** Think about what context you're

**[15:29]** comfortable giving to these companies.

**[15:31]** Think about what context you want to

**[15:33]** retain, and think about whether you are

**[15:37]** willing to put the time in to actually

**[15:40]** build elements of a harness that allow

**[15:43]** you to decide where to route your

**[15:45]** context. And so, when I've talked about

**[15:47]** Open Brain and and Open Engine most

**[15:49]** recently, a lot of what I'm doing is

**[15:51]** basically building pieces of a harness

**[15:54]** in public so that you have more choices.

**[15:56]** And I'm not the only one doing it. There

**[15:58]** are others who are doing it. It's a good

**[15:59]** work. I'm glad it's widespread. There's

**[16:01]** There's a big movement around this. I

**[16:03]** think it's important that we have

**[16:06]** choice. We shouldn't have to feel like

**[16:08]** we're locked in to any given model

**[16:10]** provider. We should have the option to

**[16:13]** retain our context and use intelligence

**[16:16]** in order to get meaningful work done.

**[16:18]** And I think the more we look at the

**[16:21]** story going forward, the more it's a

**[16:23]** story of the intelligence wars shifting

**[16:26]** into the context wars. It's going to be

**[16:29]** less about Windows 5.6 come out, and it

**[16:32]** will eventually. Windows Fable come out,

**[16:34]** and it will eventually. And more about

**[16:37]** when can we make the next step in

**[16:41]** applying intelligence so that it's

**[16:43]** useful. And the story of Siri really

**[16:46]** shows us, pardon me, Apple, that you

**[16:48]** don't have to have an incredibly

**[16:50]** intelligent model to have incredible

**[16:53]** utility. Like, your model doesn't have

**[16:54]** to max out the benchmarks. That's not

**[16:56]** what Siri is going to do. But Siri

**[16:59]** applied across your context on your

**[17:00]** phone seamlessly can still be incredibly

**[17:02]** powerful. So, that's the story under the

**[17:05]** story this week. Pay attention to the

**[17:06]** context layer. It's going to matter a

**[17:08]** lot. And if you want more stories under

**[17:10]** the story, I do them every week,

**[17:12]** subscribe for more.
