# Transcript: Apple WWDC 2026: The AI Story Everyone is Missing

**URL:** https://www.youtube.com/watch?v=t7L6-fMpxFc
**Segments:** 519
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 18:34
**Uploaded:** 2026-06-11

---

## Full Text

Apple used WWDC to show Siri AI, confirmed the Google Gemini Apple Alliance story, and to expand private cloud compute into Google Cloud using Nvidia GPUs. And that sounds like it's three separate headlines, doesn't it? But I think it is Apple answering the question that may decide who becomes the first trillionaire in AI history. When AI starts doing real work for you all day long, where does that work run? Does it run in a chatbot tab? Does it run in a giant cloud service where every serious task burns tokens and GPU time and power and data center capacity? Or does more of it start inside the computer you already bought? The iPhone in your hand, the Mac on your desk, the chip inside that Mac, the operating system, the apps, the files, the photos, the messages, the screen, and then private cloud behind it when the device is not enough. That is Apple's vision. That is the WWDC story. Sure, the feature list is Siri AI and Apple Intelligence and Google Gemini family tech and app intents and foundation models and visual intelligence. The list goes on. But the story is that Apple is trying to turn AI from something you rent in the cloud into something built into the computer you bought. And that is why this WWDC matters. Because if you were trying to understand AI without turning your life into a model provider spreadsheet, this gives you a clean map to the future. So, stop asking which AI model is ahead or if Siri is catching up. Ask who owns the place where AI sees your work and touches your apps and remembers your context and does something. If you run a team, this changes the budget conversation. It is not just should we buy ChatGPT or should we buy Claude or Gemini? It's where does our work live? Which systems can AI safely touch? What has to stay private? Who gets permission to act, right? Those are the larger questions for 2026. If you build software, this changes the product conversation. It's not enough to bolt AI onto the app. Obviously, the app has to be legible to the operating system. That's the new challenge, and that's the challenge Apple is going after with WWDC. If you're drowning in email and tabs and files and passwords and copying and pasting, then this is the part that matters. That's the fight Apple picked at WWDC. So, this is the story of what Apple announced, what Siri now sits on top of, why the developer layer matters, why Google and Nvidia make the story more interesting, and what this changes if you are trying to make AI useful in actual work. Let's start with the announcements. Apple announced the next version of Apple Intelligence, new Siri AI, new Apple Foundation models, new on-device models, new server models running through private cloud compute, Google Gemini family tech underneath part of the model stack, and a private cloud compute expansion into Google Cloud with Nvidia GPUs. They also announced App Intents becoming much more important to Siri and Apple Intelligence, uh Foundation models as a developer framework, Core AI so developers can run local models in apps using Apple silicon, and Xcode agents with model choice. Natural language shortcuts, Safari features that can watch web pages and organize tabs, passwords doing more adjunctive work to fix your weak accounts, and then they did the normal WWDC platform stuff, too, right? New OS versions, design refinements, performance improvements, search improvements, betas now, final releases in the fall. So, yes, so many announcements it's easy to lose track of it all. But, the AI announcements all point in the same direction. Apple is trying to make AI part of the computer again. Not a separate chat tab, not a model picker, not some cloud product that you visit. The computer That's Apple's vision. The thing in your hand, the apps you use, the files, the photos, the message, the password, the calendar, the browser, the screen context where your life already is. That's the AI. And that's a very different strategy than build the best chatbot. And that is where most of the seems to be missing the point because the easy WWDC question is did Siri get smarter? It's a fair question, right? Siri matters. Normal people are going to judge Apple AI through Siri. If Siri feels dumb as it has, the whole thing feels dumb. But Siri's not the AI strategy for Apple. Siri's just the face. The better question is what is Siri sitting on top of, right? And the answer gets really interesting. Siri now sits on top of personal context and screen awareness and app actions and spotlight semantic index and Apple foundation models and private cloud compute and app intents. And that's not just a voice assistant story. That's Apple trying to make the operating system itself feel agentic. And by that I mean something really simple, right? Can the system see your screen? Can it understand your files and photos? Can it talk to the apps where your work happens? Can it take action and do it without spraying your life into a random cloud service? That is the product they're trying to build. It's not some benchmark they're hitting. It's not a demo they want to sort of make flashy even though WWDC has demos. The real product is whether your computer can finally take the hint, right? Can it find the thing? Can it move the file? Can it watch the page? Can it build the shortcut? Can it draft the message in the app where it will actually be sent? This is what ordinary consumers want, right? It's what my aunt wants. They don't want to manage six models or or think about tokens or context windows or local versus cloud. None of that matters. They want the computer to do the right thing and not leak their life in the process. Apple's always been good about it. That is an Apple problem. It's a better problem for Apple than beating OpenAI at frontier model speed. Look, Apple has not had the best assistant. Apple has not had the best model. They don't have those today. But you don't need to be the best frontier lab if you own the place where personal AI becomes useful. And that's what's going to matter to my aunt and and my cousins and people who are not deep in AI. The AI industry has trained us to think the model is the product. But for most consumer AI, I think the product is the model plus context plus permissions and interface and actions and trust in a package you believe in. That's what Apple is trying to own. And that brings us to the developer story, which is probably the least sexy part of the keynote and maybe the most important one, too. App Intents is how developers make their apps contents and actions available to the system. In plain English, it is how an app tells Apple Intelligence, here's what I have, here's what the user can do with it, and here are the actions you are allowed to take. That matters because an AI assistant that cannot act inside apps is not really an assistant, is it? It can just suggest things, advise on things, write things, summarize things, but all the work lives elsewhere. Apple spent the last 15 or 20 years teaching every company on Earth to become an app. And you see that even now when people are vibe coding and the number of apps in the App Store is skyrocketing. But usage isn't, right? Apple knows that. Now it's trying to teach the operating system to do the thing the app used to do. Apple's trying to self-destruct. The old world was open the app, learn the interface, tap around, do the thing. The agentic OS world is ask the system and the system uses the app for you. That is Apple trying to move past the app world it built. But the catch is this, it can't move too far because the app ecosystem is also the tollbooth. So App Intents is the compromise architecture, right? Apple gets to make apps callable by the OS while keeping the app, the developer relationship, permission layer, the App Store with all that money, and the distribution inside Apple gray. That is why this is not actually Apple killing apps. It is Apple turning apps into things the operating system can call. And this changes what developers ought to care about. For the last couple of years, a lot of AI product strategy has been, you know, you have to at least add a chatbot. And if you think I'm making that up, I have sat in rooms where people say, "Well, at at a minimum we have to do that." And it really is something people have done, and everything gets AI-washed, right? And everything gets AI-washed, right? Now now we can put AI in the headline, we can write a press release, we're done. So much of that is lazy, right? The Apple version of AI here is a lot more than a lazy press release. Apple is getting very structural with their approach to AI. If the OS is becoming an AI surface, your app has to become legible to the OS. So, for developers, your data model matters, your permissions matter, your actions matter, your integration with Spotlight and Siri and shortcuts matters a lot. The winning apps might not be the apps with the flashiest chatbot. They might be the apps whose data and actions are clean enough that Apple intelligence can actually use them. And that is not super exciting to demo, but it's super important in practice. And foundation models matter for the same reason. Apple is opening model access through a native Swift framework, right? On-device Apple models, private cloud compute models, and other providers that conform to that framework. Apple is not saying we built every model and you should only use us. Apple is saying we want to own the native model interface on Apple platforms. It's a different kind of control, right? Core AI matters because it gives developers a path to run other local models using Apple silicon. Xcode agents matter because Apple's pushing the same agent story into the developer workflow itself. So, this is not a story about Siri. It is Apple trying to make AI native across the platform, consumer surface, developer surface, app surface, device surface. The deeper WWDC story is that Apple is turning everything in the system into a pipeline to enable an AI layer for consumers over the existing Apple OS. And they're betting that that's enough to self-disrupt. I don't know if it is. And the question around whether Apple is doing enough brings us to the Google Gemini piece of this story. A lot of people are going to treat this as humiliating for Apple. At some level, it is, right? Apple would obviously prefer the clean mythology, the clean story. Our hardware, our software, our chips, our models, our magic. Instead, the story is the next generation of Apple foundation models was built in collaboration with Google using Gemini family tech. That's significant, right? But the cheap take is not as strong as it sounds. The cheap take is Apple failed and had to use Google. I think the stronger take is Apple may not care who supplies raw model capability. It's commoditizing. Apple wants to own the layer the user touches. Who owns the device, the OS, the app platform, the permission prompts, the Siri surface. Apple wants to own that. So, yeah, they'll let Google provide the model capability. Nvidia can provide the private cloud infrastructure. Apple still wants to own the experience and they're betting they can. You can source model capability. You cannot easily source a billion devices, a mature operating system, a developer ecosystem, and the trust people have in the computer they carry around. Now, private cloud compute is where that argument gets a little bit more complex. Follow me here, right? The super easy version is the Apple hardware thesis is local AI inference moves off the cloud, it moves onto the device. You have Apple silicon with unified memory and neural engines. You have local models, it's all fixed cost. That is still a part of the story. But WWDC made it clear that the larger version of that story is really a device plus private cloud. Apple is saying run what you can on the device and when the request is too difficult, trust us, we'll route it to private cloud compute. And now private cloud compute is expanding beyond Apple's own data centers into Google Cloud using Nvidia GPUs for really hard workloads, including agentic tool use and complicated reasoning. This puts Jensen in a very interesting position. Nvidia may still be inside the infrastructure, Google may still supply the model capability, the cloud may still handle the hardest workloads, but Apple wants to be the front door and stay the front door. The device is going to decide what runs locally. The OS is going to decide when context is available, the app layer exposes the actions, private cloud compute is relegated to handling overflow. Apple is going for one of the two core bottlenecks in AI here, right? In AI we have at least two major bottlenecks. One bottleneck, of course, is raw compute. GPUs and power in data centers and networking and memory bandwidth, all that stuff that Nvidia is incredible at. And that's a very real bottleneck. The other bottleneck is the trusted action surface. That's what's getting fought over now. Where does the AI meet the user? Where does the AI touch apps? Where does the AI get permission to act? And that bottleneck is real, too, and Apple's trying to own that one. And that is that is a trillionaire question, people. It's not who has the cleanest demo, it's not who has the best frontier model, it's who owns the default meter for everyday intelligence. If the future of AI is mostly bigger models and bigger data centers, Jensen wins and keeps on winning. Nvidia becomes the tax collector on intelligence. That That is just one path, but if a huge amount of useful personal AI happens through the device and operating system, the economics get a lot more complicated for Jensen. The device becomes the default, the cloud becomes a specialist, the thing in your pocket becomes just part of the larger AI compute experience, and that's a very different world. And if Apple pulls that off, it changes who gets paid at scale. Sure, Nvidia still wins in frontier training and enterprise inference and robotics and scientific computing and data centers, and that build-out is is real, but Apple can shift a meaningful part of the consumer AI value chain toward hardware it sells, toward software controls, and toward services it can meter or bundle through iCloud and the App Store. This is why we're talking about trillionaire level territory here. Because the first trillionaire is probably not just the person with the smartest model. It is the person who owns the meter when intelligence becomes economically unavoidable. Maybe that's Jensen because every path runs through GPUs. Maybe that's Apple because personal AI becomes native to Apple devices and Apple turns the iPhone upgrade cycle into the AI upgrade cycle. And maybe it's both. WWDC is trying to give us a flashlight to get through that fog. It's trying to give us clarity around what ordinary folks around the Thanksgiving dinner table are going to talk about as AI. And if you want to get ahead of that story, I would encourage you to watch the surfaces, right? Watch device surfaces, OS surfaces, browser and search surfaces, how files are handled. This tells you more about where personal AI is going than another leaderboard argument or even than the press releases around WWDC. If you already use ChatGPT as a billion people do just about or Gemini and you're trying to turn that into real work, the takeaway is even more blunt. Look, Apple is not all the way there. But WWDC is about building the rails to make that kind of default experience possible. Because if your day is full of context switching, if it's full of email and Slack and documents and tabs and you're always going back and forth, those boring features that make life feel seamless with AI really matters. Because really the value of AI is not I wrote a paragraph, the value is intelligence that lets you get more work done with less context switching, less handoff, fewer administrative papercuts. The computer just notices that the page changed. The password is weak, so the computer fixed it. The shortcut gets built in plain English so you can understand what the computer is doing. None of this is AGI, right? It is just the machine becoming less useless at the work sitting in front of you. Apple's whole product claim is the claim that the computer can now know a lot about you without making you feel like you're being stripped mine for data. And I got to ask, do you think Open AI is someone you trust with that? Does is Anthropic a company you trust like that? I don't know. People tend to have different answers to those questions. But that's the lane we're talking about. And that trust lane is extremely valuable as AI agents start touching more and more of our work. And if you're building software in this space, right? If you're building in the Apple ecosystem anywhere, the future of an app on Apple platforms is not going to be can I get this app launched and get it approved? It's going to be can I expose the actions? Can I clean up permissions? Can I make the workflow safe? Can I expose the objects so app intents work? The apps that win are not the ones with the flashiest demos. It's going to be the apps work that have data and and actions that are clean enough for the operating system to actually operate them. And the question from a brand perspective is are you stuck enough in people's heads that they will actually ask for you by name when they talk to Apple. So sure, the surface WWDC story is about Google sucking the AI features in Siri AI. The bigger story is that Apple is trying to turn the iPhone and Mac and iPad into the default place for consumers where personal AI runs and sees and decides and acts. And by the way, if it's default for consumers, it may well become default for workers because we all bring our own devices everywhere. And so the question is going to become if it's that seamless on Apple, are you going to start demanding that kind of seamlessness at work? That's the play. It's not Apple built the smartest model. It's not Apple killed Nvidia. It's not everything runs locally. The play is Apple wants to own the computer where personal AI becomes useful and by extension Apple wants to own the computer where AI is valuable. And and if that works, the AI race stops being only about who has the biggest cloud cluster. It's it's about who owns the trust in the system. Who owns the surface that agent works against. And that that is why Jensen should be watching. And frankly, the other major AI player should have been paying attention here. Because I don't think the first trillionaire is going to get decided by who IPOs this summer. I think it's going to be more useful to ask ourselves, if you want to create lasting wealth from AI, who is going to own the surface that a billion people touch AI through? Apple has a path to that. Apple is building that path. WWDC exposed for all of us the roadmap they're using to build that path. Pay attention. Because if you don't, you're going to get distracted by the headlines tomorrow and the next day and the next day about frontier model this and that. Apple wants to be synonymous with AI for billion people. If they are, the rest of the AI race is going to change entirely because they will have won the last mile that drives actual trust. So, let me know what you think in the comments and I'll see you next time.

---

## Timestamped Segments

**[0:00]** Apple used WWDC to show Siri AI,

**[0:02]** confirmed the Google Gemini Apple

**[0:05]** Alliance story, and to expand private

**[0:07]** cloud compute into Google Cloud using

**[0:09]** Nvidia GPUs. And that sounds like it's

**[0:11]** three separate headlines, doesn't it?

**[0:13]** But I think it is Apple answering the

**[0:15]** question that may decide who becomes the

**[0:17]** first trillionaire in AI history. When

**[0:19]** AI starts doing real work for you all

**[0:21]** day long, where does that work run? Does

**[0:25]** it run in a chatbot tab? Does it run in

**[0:27]** a giant cloud service where every

**[0:29]** serious task burns tokens and GPU time

**[0:31]** and power and data center capacity? Or

**[0:33]** does more of it start inside the

**[0:35]** computer you already bought? The iPhone

**[0:37]** in your hand, the Mac on your desk, the

**[0:39]** chip inside that Mac, the operating

**[0:41]** system, the apps, the files, the photos,

**[0:43]** the messages, the screen, and then

**[0:46]** private cloud behind it when the device

**[0:48]** is not enough. That is Apple's vision.

**[0:51]** That is the WWDC story. Sure, the

**[0:54]** feature list is Siri AI and Apple

**[0:56]** Intelligence and Google Gemini family

**[0:58]** tech and app intents and foundation

**[1:00]** models and visual intelligence. The list

**[1:02]** goes on. But the story is that Apple is

**[1:05]** trying to turn AI from something you

**[1:07]** rent in the cloud into something built

**[1:09]** into the computer you bought. And that

**[1:12]** is why this WWDC matters. Because if you

**[1:14]** were trying to understand AI without

**[1:16]** turning your life into a model provider

**[1:18]** spreadsheet, this gives you a clean map

**[1:22]** to the future. So, stop asking which AI

**[1:26]** model is ahead or if Siri is catching

**[1:27]** up. Ask who owns the place where AI sees

**[1:30]** your work and touches your apps and

**[1:32]** remembers your context and does

**[1:34]** something. If you run a team, this

**[1:37]** changes the budget conversation. It is

**[1:39]** not just should we buy ChatGPT or should

**[1:42]** we buy Claude or Gemini? It's where does

**[1:44]** our work live? Which systems can AI

**[1:46]** safely touch? What has to stay private?

**[1:48]** Who gets permission to act, right? Those

**[1:51]** are the larger questions for 2026. If

**[1:53]** you build software, this changes the

**[1:55]** product conversation. It's not enough to

**[1:57]** bolt AI onto the app. Obviously, the app

**[2:00]** has to be legible to the operating

**[2:01]** system. That's the new challenge, and

**[2:03]** that's the challenge Apple is going

**[2:04]** after with WWDC. If you're drowning in

**[2:07]** email and tabs and files and passwords

**[2:09]** and copying and pasting, then this is

**[2:11]** the part that matters. That's the fight

**[2:14]** Apple picked at WWDC. So, this is the

**[2:16]** story of what Apple announced, what Siri

**[2:18]** now sits on top of, why the developer

**[2:21]** layer matters, why Google and Nvidia

**[2:23]** make the story more interesting, and

**[2:24]** what this changes if you are trying to

**[2:26]** make AI useful in actual work.

**[2:29]** Let's start with the announcements.

**[2:31]** Apple announced the next version of

**[2:32]** Apple Intelligence, new Siri AI, new

**[2:34]** Apple Foundation models, new on-device

**[2:36]** models, new server models running

**[2:38]** through private cloud compute, Google

**[2:40]** Gemini family tech underneath part of

**[2:42]** the model stack, and a private cloud

**[2:44]** compute expansion into Google Cloud with

**[2:46]** Nvidia GPUs. They also announced App

**[2:49]** Intents becoming much more important to

**[2:50]** Siri and Apple Intelligence, uh

**[2:52]** Foundation models as a developer

**[2:54]** framework, Core AI so developers can run

**[2:56]** local models in apps using Apple

**[2:58]** silicon, and Xcode agents with model

**[3:01]** choice. Natural language shortcuts,

**[3:03]** Safari features that can watch web pages

**[3:05]** and organize tabs, passwords doing more

**[3:07]** adjunctive work to fix your weak

**[3:09]** accounts, and then they did the normal

**[3:10]** WWDC platform stuff, too, right? New OS

**[3:13]** versions, design refinements,

**[3:15]** performance improvements, search

**[3:16]** improvements, betas now, final releases

**[3:18]** in the fall. So, yes, so many

**[3:20]** announcements it's easy to lose track of

**[3:22]** it all. But, the AI announcements all

**[3:24]** point in the same direction. Apple is

**[3:27]** trying to make AI part of the computer

**[3:29]** again. Not a separate chat tab, not a

**[3:32]** model picker, not some cloud product

**[3:34]** that you visit. The computer That's

**[3:36]** Apple's vision. The thing in your hand,

**[3:38]** the apps you use, the files, the photos,

**[3:40]** the message, the password, the calendar,

**[3:42]** the browser, the screen context where

**[3:44]** your life already is. That's the AI. And

**[3:47]** that's a very different strategy than

**[3:49]** build the best chatbot. And that is

**[3:51]** where most of the

**[3:53]** seems to be missing the point because

**[3:55]** the easy WWDC question is did Siri get

**[3:58]** smarter? It's a fair question, right?

**[4:00]** Siri matters. Normal people are going to

**[4:01]** judge Apple AI through Siri. If Siri

**[4:04]** feels dumb as it has, the whole thing

**[4:06]** feels dumb. But Siri's not the AI

**[4:08]** strategy for Apple. Siri's just the

**[4:10]** face. The better question is what is

**[4:12]** Siri sitting on top of, right? And the

**[4:14]** answer gets really interesting. Siri now

**[4:17]** sits on top of personal context and

**[4:19]** screen awareness and app actions and

**[4:21]** spotlight semantic index and Apple

**[4:23]** foundation models and private cloud

**[4:25]** compute and app intents. And that's not

**[4:27]** just a voice assistant story. That's

**[4:29]** Apple trying to make the operating

**[4:31]** system itself feel agentic. And by that

**[4:33]** I mean something really simple, right?

**[4:35]** Can the system see your screen? Can it

**[4:37]** understand your files and photos? Can it

**[4:40]** talk to the apps where your work

**[4:41]** happens? Can it take action and do it

**[4:43]** without spraying your life into a random

**[4:45]** cloud service? That is the product

**[4:47]** they're trying to build. It's not some

**[4:49]** benchmark they're hitting. It's not a

**[4:50]** demo they want to sort of make flashy

**[4:53]** even though WWDC has demos. The real

**[4:56]** product is whether your computer can

**[4:58]** finally take the hint, right? Can it

**[5:00]** find the thing? Can it move the file?

**[5:02]** Can it watch the page? Can it build the

**[5:03]** shortcut? Can it draft the message in

**[5:05]** the app where it will actually be sent?

**[5:07]** This is what ordinary consumers want,

**[5:10]** right? It's what my aunt wants. They

**[5:12]** don't want to manage six models or or

**[5:14]** think about tokens or context windows or

**[5:17]** local versus cloud. None of that

**[5:19]** matters. They want the computer to do

**[5:21]** the right thing and not leak their life

**[5:23]** in the process. Apple's always been good

**[5:25]** about it. That is an Apple problem. It's

**[5:27]** a better problem for Apple than beating

**[5:29]** OpenAI at frontier model speed. Look,

**[5:31]** Apple has not had the best assistant.

**[5:34]** Apple has not had the best model. They

**[5:36]** don't have those today. But you don't

**[5:38]** need to be the best frontier lab if you

**[5:41]** own the place where personal AI becomes

**[5:43]** useful. And that's what's going to

**[5:44]** matter to my aunt and and my cousins and

**[5:47]** people who are not deep in AI. The AI

**[5:49]** industry has trained us to think the

**[5:51]** model is the product. But for most

**[5:53]** consumer AI, I think the product is the

**[5:55]** model plus context plus permissions and

**[5:58]** interface and actions and trust in a

**[5:59]** package you believe in. That's what

**[6:02]** Apple is trying to own. And that brings

**[6:04]** us to the developer story, which is

**[6:06]** probably the least sexy part of the

**[6:07]** keynote and maybe the most important

**[6:09]** one, too. App Intents is how developers

**[6:12]** make their apps contents and actions

**[6:14]** available to the system. In plain

**[6:16]** English, it is how an app tells Apple

**[6:18]** Intelligence, here's what I have, here's

**[6:20]** what the user can do with it, and here

**[6:21]** are the actions you are allowed to take.

**[6:24]** That matters because an AI assistant

**[6:26]** that cannot act inside apps is not

**[6:28]** really an assistant, is it? It can just

**[6:30]** suggest things, advise on things, write

**[6:32]** things, summarize things, but all the

**[6:34]** work lives elsewhere. Apple spent the

**[6:36]** last 15 or 20 years teaching every

**[6:38]** company on Earth to become an app. And

**[6:41]** you see that even now when people are

**[6:43]** vibe coding and the number of apps in

**[6:45]** the App Store is skyrocketing. But usage

**[6:48]** isn't, right? Apple knows that. Now it's

**[6:50]** trying to teach the operating system to

**[6:52]** do the thing the app used to do. Apple's

**[6:55]** trying to self-destruct. The old world

**[6:57]** was open the app, learn the interface,

**[6:59]** tap around, do the thing. The agentic OS

**[7:01]** world is ask the system and the system

**[7:03]** uses the app for you. That is Apple

**[7:06]** trying to move past the app world it

**[7:08]** built. But the catch is this, it can't

**[7:10]** move too far because the app ecosystem

**[7:13]** is also the tollbooth.

**[7:15]** So App Intents is the compromise

**[7:17]** architecture, right? Apple gets to make

**[7:19]** apps callable by the OS while keeping

**[7:21]** the app, the developer relationship,

**[7:24]** permission layer, the App Store with all

**[7:26]** that money, and the distribution inside

**[7:27]** Apple gray. That is why this is not

**[7:30]** actually Apple killing apps. It is Apple

**[7:32]** turning apps into things the operating

**[7:34]** system can call. And this changes what

**[7:36]** developers ought to care about. For the

**[7:37]** last couple of years, a lot of AI

**[7:39]** product strategy has been, you know, you

**[7:42]** have to at least add a chatbot. And if

**[7:44]** you think I'm making that up, I have sat

**[7:46]** in rooms where people say, "Well, at at

**[7:47]** a minimum we have to do that." And it

**[7:49]** really is something people have done,

**[7:51]** and everything gets AI-washed, right?

**[7:53]** And everything gets AI-washed, right?

**[7:54]** Now now we can put AI in the headline,

**[7:56]** we can write a press release, we're

**[7:57]** done.

**[7:58]** So much of that is lazy, right? The

**[8:02]** Apple version of AI here is a lot more

**[8:04]** than a lazy press release. Apple is

**[8:06]** getting very structural with their

**[8:07]** approach to AI. If the OS is becoming an

**[8:11]** AI surface, your app has to become

**[8:13]** legible to the OS. So, for developers,

**[8:16]** your data model matters, your

**[8:17]** permissions matter, your actions matter,

**[8:19]** your integration with Spotlight and Siri

**[8:21]** and shortcuts matters a lot. The winning

**[8:24]** apps might not be the apps with the

**[8:26]** flashiest chatbot. They might be the

**[8:28]** apps whose data and actions are clean

**[8:30]** enough that Apple intelligence can

**[8:32]** actually use them. And that is not super

**[8:34]** exciting to demo, but it's super

**[8:37]** important in practice.

**[8:39]** And foundation models matter for the

**[8:40]** same reason. Apple is opening model

**[8:42]** access through a native Swift framework,

**[8:44]** right? On-device Apple models, private

**[8:46]** cloud compute models, and other

**[8:47]** providers that conform to that

**[8:50]** framework.

**[8:50]** Apple is not saying we built every model

**[8:52]** and you should only use us. Apple is

**[8:54]** saying we want to own the native model

**[8:56]** interface on Apple platforms. It's a

**[8:58]** different kind of control, right?

**[9:00]** Core AI matters because it gives

**[9:02]** developers a path to run other local

**[9:04]** models using Apple silicon. Xcode agents

**[9:07]** matter because Apple's pushing the same

**[9:09]** agent story into the developer workflow

**[9:11]** itself. So, this is not a story about

**[9:14]** Siri. It is Apple trying to make AI

**[9:16]** native across the platform, consumer

**[9:18]** surface, developer surface, app surface,

**[9:20]** device surface.

**[9:21]** The deeper WWDC story is that Apple is

**[9:24]** turning everything in the system into a

**[9:28]** pipeline to enable an AI layer for

**[9:31]** consumers over the existing Apple OS.

**[9:35]** And they're betting that that's enough

**[9:37]** to self-disrupt. I don't know if it is.

**[9:39]** And the question around whether Apple is

**[9:41]** doing enough brings us to the Google

**[9:43]** Gemini piece of this story. A lot of

**[9:45]** people are going to treat this as

**[9:47]** humiliating for Apple. At some level, it

**[9:50]** is, right? Apple would obviously prefer

**[9:52]** the clean mythology, the clean story.

**[9:54]** Our hardware, our software, our chips,

**[9:56]** our models, our magic. Instead, the

**[9:58]** story is the next generation of Apple

**[10:01]** foundation models was built in

**[10:03]** collaboration with Google using Gemini

**[10:05]** family tech. That's significant, right?

**[10:08]** But the cheap take is not as strong as

**[10:10]** it sounds. The cheap take is Apple

**[10:11]** failed and had to use Google. I think

**[10:13]** the stronger take is Apple may not care

**[10:16]** who supplies raw model capability. It's

**[10:18]** commoditizing. Apple wants to own the

**[10:21]** layer the user touches. Who owns the

**[10:23]** device, the OS, the app platform, the

**[10:25]** permission prompts, the Siri surface.

**[10:27]** Apple wants to own that. So, yeah,

**[10:29]** they'll let Google provide the model

**[10:30]** capability. Nvidia can provide the

**[10:32]** private cloud infrastructure. Apple

**[10:34]** still wants to own the experience and

**[10:36]** they're betting they can. You can source

**[10:38]** model capability. You cannot easily

**[10:40]** source a billion devices, a mature

**[10:42]** operating system, a developer ecosystem,

**[10:44]** and the trust people have in the

**[10:45]** computer they carry around. Now, private

**[10:48]** cloud compute is where that argument

**[10:49]** gets a little bit more complex. Follow

**[10:51]** me here, right? The super easy version

**[10:53]** is the Apple hardware thesis is local AI

**[10:56]** inference moves off the cloud, it moves

**[10:57]** onto the device. You have Apple silicon

**[10:59]** with unified memory and neural engines.

**[11:01]** You have local models, it's all fixed

**[11:03]** cost. That is still a part of the story.

**[11:06]** But WWDC made it clear that the larger

**[11:09]** version of that story is really a device

**[11:11]** plus private cloud. Apple is saying run

**[11:14]** what you can on the device and when the

**[11:16]** request is too difficult, trust us,

**[11:18]** we'll route it to private cloud compute.

**[11:20]** And now private cloud compute is

**[11:21]** expanding beyond Apple's own data

**[11:23]** centers into Google Cloud using Nvidia

**[11:25]** GPUs for really hard workloads,

**[11:27]** including agentic tool use and

**[11:28]** complicated reasoning. This puts Jensen

**[11:30]** in a very interesting position. Nvidia

**[11:33]** may still be inside the infrastructure,

**[11:35]** Google may still supply the model

**[11:36]** capability, the cloud may still handle

**[11:38]** the hardest workloads, but Apple wants

**[11:40]** to be the front door and stay the front

**[11:42]** door. The device is going to decide what

**[11:44]** runs locally. The OS is going to decide

**[11:46]** when context is available, the app layer

**[11:48]** exposes the actions, private cloud

**[11:51]** compute is relegated to handling

**[11:53]** overflow. Apple is going for one of the

**[11:55]** two core bottlenecks in AI here, right?

**[11:57]** In AI we have at least two major

**[11:59]** bottlenecks. One bottleneck, of course,

**[12:00]** is raw compute. GPUs and power in data

**[12:04]** centers and networking and memory

**[12:05]** bandwidth, all that stuff that Nvidia is

**[12:08]** incredible at.

**[12:09]** And that's a very real bottleneck. The

**[12:11]** other bottleneck is the trusted action

**[12:14]** surface. That's what's getting fought

**[12:16]** over now. Where does the AI meet the

**[12:18]** user? Where does the AI touch apps?

**[12:20]** Where does the AI get permission to act?

**[12:23]** And that bottleneck is real, too, and

**[12:25]** Apple's trying to own that one. And that

**[12:27]** is that is a trillionaire question,

**[12:29]** people. It's not who has the cleanest

**[12:32]** demo, it's not who has the best frontier

**[12:33]** model, it's who owns the default meter

**[12:36]** for everyday intelligence. If the future

**[12:39]** of AI is mostly bigger models and bigger

**[12:41]** data centers, Jensen wins and keeps on

**[12:44]** winning.

**[12:45]** Nvidia becomes the tax collector on

**[12:47]** intelligence. That That is just one

**[12:50]** path, but if a huge amount of useful

**[12:52]** personal AI happens through the device

**[12:54]** and operating system, the economics get

**[12:57]** a lot more complicated for Jensen. The

**[12:58]** device becomes the default, the cloud

**[13:00]** becomes a specialist, the thing in your

**[13:03]** pocket becomes just part of the larger

**[13:05]** AI compute experience, and that's a very

**[13:07]** different world. And if Apple pulls that

**[13:09]** off, it changes who gets paid at scale.

**[13:12]** Sure, Nvidia still wins in frontier

**[13:14]** training and enterprise inference and

**[13:16]** robotics and scientific computing and

**[13:18]** data centers, and that build-out is is

**[13:20]** real, but Apple can shift a meaningful

**[13:23]** part of the consumer AI value chain

**[13:26]** toward hardware it sells, toward

**[13:27]** software controls, and toward services

**[13:30]** it can meter or bundle through iCloud

**[13:31]** and the App Store. This is why we're

**[13:34]** talking about trillionaire level

**[13:35]** territory here. Because the first

**[13:36]** trillionaire is probably not just the

**[13:39]** person with the smartest model. It is

**[13:41]** the person who owns the meter when

**[13:44]** intelligence becomes economically

**[13:46]** unavoidable. Maybe that's Jensen because

**[13:48]** every path runs through GPUs. Maybe

**[13:51]** that's Apple because personal AI becomes

**[13:54]** native to Apple devices and Apple turns

**[13:56]** the iPhone upgrade cycle into the AI

**[13:58]** upgrade cycle. And maybe it's both. WWDC

**[14:02]** is trying to give us a flashlight to get

**[14:04]** through that fog. It's trying to give us

**[14:06]** clarity around what ordinary folks

**[14:08]** around the Thanksgiving dinner table are

**[14:10]** going to talk about as AI. And if you

**[14:13]** want to get ahead of that story, I would

**[14:14]** encourage you to watch the surfaces,

**[14:16]** right? Watch device surfaces, OS

**[14:18]** surfaces, browser and search surfaces,

**[14:21]** how files are handled. This tells you

**[14:23]** more about where personal AI is going

**[14:26]** than another leaderboard argument or

**[14:28]** even than the press releases around

**[14:29]** WWDC.

**[14:31]** If you already use ChatGPT as a billion

**[14:34]** people do just about or Gemini and

**[14:36]** you're trying to turn that into real

**[14:38]** work, the takeaway is even more blunt.

**[14:41]** Look, Apple is not all the way there.

**[14:44]** But WWDC is about building the rails to

**[14:46]** make that kind of default experience

**[14:48]** possible. Because if your day is full of

**[14:51]** context switching, if it's full of email

**[14:53]** and Slack and documents and tabs and

**[14:55]** you're always going back and forth,

**[14:56]** those boring features that make life

**[14:59]** feel seamless with AI really matters.

**[15:01]** Because really the value of AI is not I

**[15:04]** wrote a paragraph, the value is

**[15:06]** intelligence that lets you get more work

**[15:08]** done with less context switching, less

**[15:10]** handoff, fewer administrative papercuts.

**[15:13]** The computer just notices that the page

**[15:15]** changed. The password is weak, so the

**[15:17]** computer fixed it. The shortcut gets

**[15:19]** built in plain English so you can

**[15:22]** understand what the computer is doing.

**[15:23]** None of this is AGI, right? It is just

**[15:25]** the machine becoming less useless at the

**[15:27]** work sitting in front of you. Apple's

**[15:29]** whole product claim is the claim that

**[15:31]** the computer can now know a lot about

**[15:33]** you without making you feel like you're

**[15:35]** being stripped mine for data. And I got

**[15:37]** to ask, do you think Open AI is someone

**[15:39]** you trust with that? Does is Anthropic a

**[15:41]** company you trust like that? I don't

**[15:43]** know. People tend to have different

**[15:44]** answers to those questions. But that's

**[15:46]** the lane we're talking about. And that

**[15:48]** trust lane is extremely valuable as AI

**[15:51]** agents start touching more and more of

**[15:52]** our work.

**[15:54]** And if you're building software in this

**[15:56]** space, right? If you're building in the

**[15:57]** Apple ecosystem anywhere, the future of

**[16:00]** an app on Apple platforms is not going

**[16:03]** to be can I get this app launched and

**[16:05]** get it approved? It's going to be can I

**[16:07]** expose the actions? Can I clean up

**[16:09]** permissions? Can I make the workflow

**[16:11]** safe? Can I expose the objects so app

**[16:13]** intents work? The apps that win are not

**[16:16]** the ones with the flashiest demos. It's

**[16:17]** going to be the apps work that have data

**[16:19]** and and actions that are clean enough

**[16:21]** for the operating system to actually

**[16:23]** operate them. And the question from a

**[16:25]** brand perspective is are you stuck

**[16:27]** enough in people's heads that they will

**[16:29]** actually ask for you by name when they

**[16:31]** talk to Apple. So sure, the surface WWDC

**[16:35]** story is about Google sucking the AI

**[16:36]** features in Siri AI.

**[16:38]** The bigger story is that Apple is trying

**[16:41]** to turn the iPhone and Mac and iPad into

**[16:44]** the default place for consumers where

**[16:46]** personal AI runs and sees and decides

**[16:48]** and acts. And by the way, if it's

**[16:51]** default for consumers, it may well

**[16:53]** become default for workers because we

**[16:55]** all bring our own devices everywhere.

**[16:57]** And so the question is going to become

**[16:59]** if it's that seamless on Apple, are you

**[17:01]** going to start demanding that kind of

**[17:03]** seamlessness at work?

**[17:05]** That's the play.

**[17:06]** It's not Apple built the smartest model.

**[17:09]** It's not Apple killed Nvidia. It's not

**[17:11]** everything runs locally. The play is

**[17:13]** Apple wants to own the computer where

**[17:15]** personal AI becomes useful and by

**[17:18]** extension Apple wants to own the

**[17:20]** computer where AI is valuable.

**[17:23]** And and if that works, the AI race stops

**[17:26]** being only about who has the biggest

**[17:27]** cloud cluster. It's it's about who owns

**[17:30]** the trust in the system. Who owns the

**[17:33]** surface that agent works against. And

**[17:35]** that that is why Jensen should be

**[17:38]** watching. And frankly, the other major

**[17:41]** AI player should have been paying

**[17:42]** attention here. Because I don't think

**[17:44]** the first trillionaire is going to get

**[17:45]** decided by who IPOs this summer. I think

**[17:49]** it's going to be more useful to ask

**[17:51]** ourselves, if you want to create lasting

**[17:53]** wealth from AI, who is going to own the

**[17:56]** surface that a billion people touch AI

**[17:59]** through?

**[18:00]** Apple has a path to that. Apple is

**[18:02]** building that path. WWDC exposed for all

**[18:05]** of us the roadmap they're using to build

**[18:08]** that path. Pay attention.

**[18:10]** Because if you don't, you're going to

**[18:12]** get distracted by the headlines tomorrow

**[18:14]** and the next day and the next day about

**[18:16]** frontier model this and that. Apple

**[18:18]** wants to be synonymous with AI for

**[18:20]** billion people. If they are, the rest of

**[18:24]** the AI race is going to change entirely

**[18:26]** because they will have won the last mile

**[18:28]** that drives actual trust.

**[18:30]** So, let me know what you think in the

**[18:31]** comments and I'll see you next time.
