# Transcript: I Tried /teach and 10x'd My Ability To Learn

**URL:** https://www.youtube.com/watch?v=lw6Ld1ZgpV8
**Segments:** 539
**Channel:** Kacper Rutkiewicz | AI Made Simple
**Duration:** 15:10
**Uploaded:** 2026-06-15

---

## Full Text

What you're looking at is a full lesson that my AI agent built for me, and it's teaching me something that I've wanted to learn for a very long time. This was all able to happen from a free skill called /teach, and it was created by Matt Pocock. You may have heard of Matt Pocock. He's created skills like Grill Me and Grill Me with Docs, and I'm a huge fan of his work. And what this /teach skill does is it literally turns your Claude Code Agent into a personal tutor that can teach you [music] anything. It can teach you about code, it can teach you about new framework, and even about open-source models, which is exactly what I'm using it for. And I don't say this lightly. It might be the most useful skill that I've installed this year. So, in today's video, I'm going to show you the actual lessons that it builds out for you, the one teaching idea that makes it work really well, and exactly how to install it and start learning in about 5 [music] minutes. So, get comfortable, grab some coffee, and let's hop straight into the video. Okay, so before we touch anything and get into any examples, let me explain to you the one idea that makes this whole entire concept actually work. Typically, when someone wants to learn something using AI, they'll open up their AI, whether that's Claude Chat, ChatGPT, Claude Code, and say, "Hey, explain this to me." And without a shadow of a doubt, you'll get an answer. But that answer is always a one-off, and if you were to ask that same question again, the answer would be completely different. It kind of feels like having a substitute teacher that's met you for the first time, and then the next day you get another substitute teacher, and you kind of have to re-explain everything once you meet that teacher. They don't know what you actually understand, they don't know what you're stuck on, and as soon as the bell rings, they completely forget about you. Every single time you come back and start a new session, you're starting directly from scratch. Or you're so far in your context window that you're not even getting the right information anymore because your agent starting to hallucinate. This /teach skill is completely different because it's stateful. So, it actually knows where you're stuck, actually knows everything that you already have learned, logs questions that you've asked so that you don't have to ask them again or you can refer to them. And so, instead of having a substitute who forgets you every single time, you have a teacher that remembers you and knows exactly where you're at. What's really cool is it's also forward-thinking, and it picks the next lesson on purpose directly on the questions that you're asking or where you think you are in that learning process. So, a stateless tool completely forgets you. A stateful tool actually teaches you and remembers you. And that's exactly why this last teach skill works so well and I've been having a ton of fun with it. And it's not remembering you in some vague way. It actually logs pretty much everything you're doing once you run this last teach command. So, if you're looking inside of my operating system here, you can see I have a tab that says learning open source models. In there, I have learning records from questions that I've asked, places that I've got stuck. I've got all the lesson plans that we've created. We're about five lessons so far. And each of these lessons build on the questions and kind of where I'm at in the process of learning about open source models. It also creates a glossary whenever I ask about a certain word and what that means. And then as the lessons grow, this glossary grows along with it. What's incredibly important is that it creates a mission statement. Because why am I actually trying to learn this? And in my case, for open source models, what happened with Claude Fable really didn't sit well with me. And if you have no idea with what happened, you can click this video right here and go take a look at that. But that's exactly why I'm trying to learn more about open source models. It also has a note section about everything about kind of me and how to operate and what kind of software I'm using, my hardware, how to actually operate with me. And then while it actually builds the lesson plans, it documents every single resource within this resources.md. So, I can actually go reference those and really understand what's happening each lesson. So, ultimately, whenever I want to pick up exactly from where I left off, I'm able to do that now. And so, I've mentioned a few times already that I'm learning about open source models. So, let's go ahead and dive into what some of these lesson plans actually look like. And as you got a quick peek of in the intro, this is one of the actual lessons that my AI agent built for me using this last teach skill. So, the first one was all about open weight models, being able to run your first model on your own machine, created a beautiful HTML file that's really easy to follow. It gave me all the install commands when I wanted to install Ollama, helped me understand why I'm installing Ollama and then putting in small models in there based on what kind of hardware I'm using. So, it really [snorts] helped me quickly pick up this simple concept of Ollama and how to actually to started with open source models. What I really like is it gives me all the commands, it gives me a simple checklist that I can check off as I'm learning, and then it gives me a self-check to make sure I'm actually learning as I'm doing these things. And what I really like is that it makes you take action. And there's no better way to learning than actually taking action and then answering questions about what you did, why you did it, and those simple things. Those create a very easy learning loop, at least for myself. So, after every single lesson, I would go ahead and answer these questions. It lets me know that it is my teacher, not just the docs, so I could ask it all these questions. It tells me what to actually let it know before I get into the next lesson. And then at the bottom here, you can see all these sources that it provides for me with Ollama docs, ollama.com/library. And then the lesson one is tied to the mission.md. And all the terms are inside of that glossary.html that you guys saw earlier, which I just realized I didn't actually show you guys, but this is what the glossary looks like. So, we have our open weights model glossary, and these are all the words that have been inside of the five lesson plans that I have, all with definitions, so I can kind of reference this. And when I see the word, I can go back and see, okay, that's what it means, and that's the context of this sentence. And this continues to grow as you get more and more lessons. Just scrolling through a couple of more examples, this is what lesson two looks like. This one's really cool because it actually gives me some math to actually understand what kind of models I can run on my hardware. I have a computer from 2019, so I can't run anything crazy. I only have 8 GB of RAM, so I got to be very flexible with which models I choose. This helps me understand better how to actually choose which model. And what's really cool is in these HTMLs, they're incredibly interactive, and that's why it makes learning so much more fun than my previous experiences. So, I could actually type in here numbers and then get answers of everything like that, and it just goes with the entire flow of my learning process. And again, it gives me immediate action to take, and then I have to do a self-check right after that. What's really fun, too, is if I'm stuck on a certain topic and I'm not just not quite understanding it yet, I'll just have it generate a HTML quiz for me, and I could just go in, quiz, ask questions about the quiz, ask questions about really anything related to that lesson plan, and it's going to create a dynamic way for me to learn that. And I mentioned previously that it documents all your learning records, and based on the questions that you ask or the situations that you're in within that learning lesson, you'll have everything documented for future lessons. So, in this case, I was verifying that my machine was 8 GB of VRAM, whatever my hardware was, so I can decide what models that I can comfortably run on this computer. And in this case scenario, I was just asking like, what is the best open-source model that I can run on this computer? I specifically asked it if I could use DeepSeek's best and it told me that I was out of my mind because I have nowhere near the hardware to actually run that model. It then brought me down a loop of explaining what distilled models are, frontier models, and how distilled models are just lowered versions of these frontier models that run on this incredible hardware, and how you're actually able to run variations of these open-source models on whatever hardware you have. But, the fact that it's tracking my real progress and gives me a good standing point of exactly where I'm at in learning about open-source models gives me a very comfortable feeling. But, what's the thing that actually makes this thing really work? This simple philosophy is what separates /teach from every other teaching AI tool that I've tried out. Matt Pocock built this on his last 10 years of experience teaching people. So, it's built on how people actually learn and not just spitting out random information. And there are three levels to this philosophy. There's knowledge, skills, and wisdom. The first thing it does is it pulls knowledge, but not from any random sources. It actually goes through high-trusted sources and vets them before embedding them into your lesson plan. Then it helps you build real practice by again, like I said before, taking action and not just reading. And then for the last part, wisdom, it actually points you towards communities to help you surround yourself with more people learning the same topic. So, if I hop over to my glossary here at the bottom, you can see that it's pointing me to the Reddit page for Olama. Because as people say all the time, you can outsource your research and all that stuff to AI, but you can never really outsource your understanding. So, getting into these communities and learning from people that have actually been in your place is incredibly important, and I love how this /teach skill implements this. But, this right here is a concept that fascinated me. We all know that we all learn things differently. Like, when I was in school, I literally could not sit still, and if I wasn't interested in a topic, I just didn't care about it. But, every lesson that this skill builds is pitched right at your level. So, they're not so easy that you're bored, and they're not so hard that you want to quit. They're pitched for exactly where you're at. Right in that sweet spot where you feel a little bit challenged, but you still really want to do it, and it gets fun. And it's able to do that because, again, it's tracking your record. Based on the questions that you're answering, it's logging all that information in those lesson records that I showed you earlier. So, every single lesson following that is calibrated to exactly where you're at in the current one. And teachers actually have a name for this concept, and it's called the zone of proximal development. And if you really want to feel like you can learn anything and just go to any topic and easily pick it up, this is a concept definitely worth knowing about. Because most of the time, any other learning tool that you use will either just dump all the information on you or baby you. This one feels like it hits the right spot every time. And then it really does something you wouldn't expect. Once it feels like you've mastered or learned these skills well enough, it'll just pass you on to a community and actually step out of the way. Which, for me, learning about open source models is actually really exciting because I definitely want to surround myself with some people that actually know a lot about it. And I love this because it's not trying to keep you dependent on the model to keep learning. It's trying to make you good enough at the topic so that you don't need it anymore. Because we don't want to become reliant on AI. And so, I know at this point you're probably eager to get this set up for yourself, so let's get exactly into that next. And if you've been following me for a long time, you know exactly how I'm going to install this, and all I'm going to do is hop over to this {slash} skills repo, grab the {slash} teach skill, and then hop right over to Claude code, say, "Please look at this skill and install it into our project." Give it the GitHub link, and then it's going to go ahead and install that skill for us. Now, I already did it, so I'm not going to enter in this prompt, but I wanted to show you guys on the screen so you can do it for yourself. And so, now let's actually run this skill. So, I'm going to go ahead and run {slash} teach on how to actually build LLMs, and then on the left-hand side here, we only have one folder right now, which is open source models, and we should get another one once this whole process is done. And so, right away it begins setting up the entire teaching workspace for this. And first it checks what actually exists already within the entire codebase. And since learning about how to build LLMs is such a vast topic, it's going to actually ask me some concise questions to really narrow down where we want to start learning. First question is the why, which is going to help us develop that mission statement. So, what's the real driver behind behind learning how to build LLMs? And that's going to be first principle mastery for me. Then the depth is going to say "How hands-on do you want to get?" I'm going to say hands-on code. I do really want to learn how to actually build these for myself. And now slowly we're going to begin building out this entire workspace. And so, it locked that plan in, and now it's immediately going and doing some web search and getting us some initial information. And a quick note, while you're running this, I'm currently running this on Opus 4.8 with high effort. Matt Pocock in his explanatory video, which will be linked in the description, ran it on medium effort. So, that's also a good default if you don't want to be spending that many tokens. If you wanted to go a little bit faster and maybe do a little bit better research, then you could just run this on the high or max effort. And I ran into a little bug, which I'm glad that actually happened, because instead of making its own workspace inside of that learning folder that I had earlier, it went ahead into the skill folder and created it inside of that, which is something I don't want. So, just make sure when you're prompting this inside of an operating system, and if you're not in a fresh folder, that you actually are very meticulous with where you're placing these folders. I'm going to wait for everything to finish, and then I'm going to show you how I merge it over back to the learning section. And so, the workspace was created, and actually created the first lesson for us. So, this first lesson is an LLM is a next token predictor, explaining us what an LLM is. We can see the four moves on how it works, the code behind it. It then gives me your turn to predict then run, which is really cool. Check for yourself. I could open these up and answer all the questions, and all these sources at the bottom. But I want to go ahead and merge this into its own workspace inside of that learning subfolder. So, I'm going to go ahead and say that. Please move this entire workspace into the learnings folder. I don't want it in the skills folder where it's currently at. So, merge this entire workspace in a subfolder under the learning folder called how to build LLMs. Then, I'm going to go ahead, send that off, and now that entire thing that it just built will merge into that learning folders, which is exactly where I want it to be. So, if you come across this, this is a simple fix, but just make sure that you guys are pretty meticulous with where you're actually asking these files to be created. And that's much better. Now, in the learning folders, we have two subfolders called how to build LLMs and open-source models. So, that's how you guys can fix that really quickly. And then it says easy as just continuing every lesson. If you're in one session, you can continue on just learning, going through the lesson plan, asking questions, everything will get tracked, and then you'll be able to start exactly where you left off from in every new session. All you'll need to do is point your agent to the specific workspace, and you'll be good to go. And of course, the reality is this isn't magic at all. And it's definitely [music] not a shortcut because at the end of the day, you're learning, and you still got to do the reps. You guys saw yourself, I'm only five lessons in to my open-source model journey, and I'm going to keep going through it lesson by lesson until I feel I'm at a good spot to get pushed to a community. And that's the entire point of this skill. It's a tutor, not a cheat code, and it makes learning way [music] more fun. But, it does not do the learning for you. And I'll say it again, you can outsource all the research with AI, but you can never outsource your understanding of AI. And if any part of this video confused you at all, don't worry cuz I got you. I created an entire free resource guide with all the install commands, some prompts in there for you guys, and everything you need to follow alongside this video. All you'll need to do is click the link down below, enter in your email, and join my free school community AI Automation Nexus. You'll get access to all the resources from this video and every single resource that I've ever created. Really hope to see some of you guys in there soon. As always, if you've got any value from this video, drop a like, hit that subscribe button. It definitely helps me out a ton. Leave a comment down below on the first thing you're going to learn using this new {slash} teach skill. I drop videos every Tuesday and Friday, but I'm going to be dropping a video every single day until July 11th. I really have fun making content for you guys. I'm definitely enjoying the process. And if you've made it this far in the video, thank you so much and I'll see you guys in the next one. God bless, guys. Hey, if you're still here, that means you've made it to the end of the video. So, first of all, thank you so much. Something I like to do at the end of all my videos is pray for you guys, my audience. I do this because I genuinely believe in the power of prayer. It's helped me get some out of some dark places in my life and I can only extend that belief to you guys and I really do love you guys and appreciate the fact that you guys watch my videos every single day and actually enjoy my content. If this makes you feel uncomfortable at all, please feel free to click off the video. I'm not here to force anything on you, but just know that Jesus loves you. But, I'm going to go ahead and pray for you guys. Heavenly Father, thank you so much for this day. Thank you so much for giving us the breath of life today to chase opportunity and become better versions of ourselves every single day and glorify you. Lord, I just want to pray a blessing over my audience, a blessing of wisdom. Lord, just continue to have them come to you and ask you questions and ask to receive wisdom because you will give it to them and just continue, Lord, to put it in their hearts to serve their neighbor, love their neighbor, love their families, provide for their children and then just be good people with good hearts. Lord, in everything that we do, may we glorify you and honor you. Lord, we thank you for your sovereignty, your peace and your love. And Lord, just continue to make us think and be where our feet are. Lord, [snorts] don't let us make plans for the future. Can let us be present in every single moment of every single day and just continue to better our lives. Lord, we thank you for everything. Lord, we thank you for your son Jesus and his sacrifice on the cross and we just continue to praise you, love you and glorify you. And it's in your name that we pray. Amen. Now, go have a great day, guys. I'll see you tomorrow.

---

## Timestamped Segments

**[0:00]** What you're looking at is a full lesson

**[0:01]** that my AI agent built for me, and it's

**[0:03]** teaching me something that I've wanted

**[0:05]** to learn for a very long time. This was

**[0:06]** all able to happen from a free skill

**[0:08]** called /teach, and it was created by

**[0:11]** Matt Pocock. You may have heard of Matt

**[0:12]** Pocock. He's created skills like Grill

**[0:14]** Me and Grill Me with Docs, and I'm a

**[0:15]** huge fan of his work. And what this

**[0:17]** /teach skill does is it literally turns

**[0:19]** your Claude Code Agent into a personal

**[0:21]** tutor that can teach you [music]

**[0:23]** anything. It can teach you about code,

**[0:24]** it can teach you about new framework,

**[0:26]** and even about open-source models, which

**[0:28]** is exactly what I'm using it for. And I

**[0:29]** don't say this lightly. It might be the

**[0:31]** most useful skill that I've installed

**[0:33]** this year. So, in today's video, I'm

**[0:34]** going to show you the actual lessons

**[0:35]** that it builds out for you, the one

**[0:37]** teaching idea that makes it work really

**[0:38]** well, and exactly how to install it and

**[0:40]** start learning in about 5 [music]

**[0:42]** minutes. So, get comfortable, grab some

**[0:44]** coffee, and let's hop straight into the

**[0:45]** video. Okay, so before we touch anything

**[0:47]** and get into any examples, let me

**[0:49]** explain to you the one idea that makes

**[0:51]** this whole entire concept actually work.

**[0:53]** Typically, when someone wants to learn

**[0:54]** something using AI, they'll open up

**[0:56]** their AI, whether that's Claude Chat,

**[0:58]** ChatGPT, Claude Code, and say, "Hey,

**[1:00]** explain this to me." And without a

**[1:02]** shadow of a doubt, you'll get an answer.

**[1:04]** But that answer is always a one-off, and

**[1:05]** if you were to ask that same question

**[1:07]** again, the answer would be completely

**[1:08]** different. It kind of feels like having

**[1:10]** a substitute teacher that's met you for

**[1:11]** the first time, and then the next day

**[1:12]** you get another substitute teacher, and

**[1:14]** you kind of have to re-explain

**[1:15]** everything once you meet that teacher.

**[1:16]** They don't know what you actually

**[1:17]** understand, they don't know what you're

**[1:18]** stuck on, and as soon as the bell rings,

**[1:20]** they completely forget about you. Every

**[1:21]** single time you come back and start a

**[1:23]** new session, you're starting directly

**[1:24]** from scratch. Or you're so far in your

**[1:26]** context window that you're not even

**[1:27]** getting the right information anymore

**[1:29]** because your agent starting to

**[1:30]** hallucinate. This /teach skill is

**[1:31]** completely different because it's

**[1:33]** stateful. So, it actually knows where

**[1:34]** you're stuck, actually knows everything

**[1:36]** that you already have learned, logs

**[1:38]** questions that you've asked so that you

**[1:39]** don't have to ask them again or you can

**[1:40]** refer to them. And so, instead of having

**[1:42]** a substitute who forgets you every

**[1:44]** single time, you have a teacher that

**[1:45]** remembers you and knows exactly where

**[1:47]** you're at. What's really cool is it's

**[1:48]** also forward-thinking, and it picks the

**[1:50]** next lesson on purpose directly on the

**[1:52]** questions that you're asking or where

**[1:54]** you think you are in that learning

**[1:55]** process. So, a stateless tool completely

**[1:58]** forgets you. A stateful tool actually

**[2:00]** teaches you and remembers you. And

**[2:02]** that's exactly why this last teach skill

**[2:03]** works so well and I've been having a ton

**[2:05]** of fun with it. And it's not remembering

**[2:07]** you in some vague way. It actually logs

**[2:09]** pretty much everything you're doing once

**[2:10]** you run this last teach command. So, if

**[2:12]** you're looking inside of my operating

**[2:13]** system here, you can see I have a tab

**[2:15]** that says learning open source models.

**[2:17]** In there, I have learning records from

**[2:19]** questions that I've asked, places that

**[2:20]** I've got stuck. I've got all the lesson

**[2:22]** plans that we've created. We're about

**[2:23]** five lessons so far. And each of these

**[2:26]** lessons build on the questions and kind

**[2:28]** of where I'm at in the process of

**[2:29]** learning about open source models. It

**[2:31]** also creates a glossary whenever I ask

**[2:33]** about a certain word and what that

**[2:35]** means. And then as the lessons grow,

**[2:37]** this glossary grows along with it.

**[2:38]** What's incredibly important is that it

**[2:40]** creates a mission statement. Because why

**[2:41]** am I actually trying to learn this? And

**[2:43]** in my case, for open source models, what

**[2:45]** happened with Claude Fable really didn't

**[2:46]** sit well with me. And if you have no

**[2:48]** idea with what happened, you can click

**[2:49]** this video right here and go take a look

**[2:50]** at that. But that's exactly why I'm

**[2:52]** trying to learn more about open source

**[2:54]** models. It also has a note section about

**[2:56]** everything about kind of me and how to

**[2:57]** operate and what kind of software I'm

**[2:59]** using, my hardware, how to actually

**[3:01]** operate with me. And then while it

**[3:03]** actually builds the lesson plans, it

**[3:04]** documents every single resource within

**[3:07]** this resources.md. So, I can actually go

**[3:09]** reference those and really understand

**[3:10]** what's happening each lesson. So,

**[3:12]** ultimately, whenever I want to pick up

**[3:13]** exactly from where I left off, I'm able

**[3:15]** to do that now. And so, I've mentioned a

**[3:17]** few times already that I'm learning

**[3:18]** about open source models. So, let's go

**[3:19]** ahead and dive into what some of these

**[3:21]** lesson plans actually look like. And as

**[3:22]** you got a quick peek of in the intro,

**[3:24]** this is one of the actual lessons that

**[3:25]** my AI agent built for me using this last

**[3:27]** teach skill. So, the first one was all

**[3:29]** about open weight models, being able to

**[3:31]** run your first model on your own

**[3:32]** machine, created a beautiful HTML file

**[3:34]** that's really easy to follow. It gave me

**[3:36]** all the install commands when I wanted

**[3:38]** to install Ollama, helped me understand

**[3:40]** why I'm installing Ollama and then

**[3:42]** putting in small models in there based

**[3:43]** on what kind of hardware I'm using. So,

**[3:45]** it really [snorts] helped me quickly

**[3:46]** pick up this simple concept of Ollama

**[3:49]** and how to actually to started with open

**[3:51]** source models. What I really like is it

**[3:52]** gives me all the commands, it gives me a

**[3:54]** simple checklist that I can check off as

**[3:55]** I'm learning, and then it gives me a

**[3:57]** self-check to make sure I'm actually

**[3:58]** learning as I'm doing these things. And

**[4:00]** what I really like is that it makes you

**[4:02]** take action. And there's no better way

**[4:03]** to learning than actually taking action

**[4:05]** and then answering questions about what

**[4:07]** you did, why you did it, and those

**[4:08]** simple things. Those create a very easy

**[4:10]** learning loop, at least for myself. So,

**[4:12]** after every single lesson, I would go

**[4:13]** ahead and answer these questions. It

**[4:14]** lets me know that it is my teacher, not

**[4:16]** just the docs, so I could ask it all

**[4:17]** these questions. It tells me what to

**[4:19]** actually let it know before I get into

**[4:21]** the next lesson. And then at the bottom

**[4:22]** here, you can see all these sources that

**[4:24]** it provides for me with Ollama docs,

**[4:26]** ollama.com/library.

**[4:28]** And then the lesson one is tied to the

**[4:30]** mission.md. And all the terms are inside

**[4:32]** of that glossary.html that you guys saw

**[4:33]** earlier, which I just realized I didn't

**[4:35]** actually show you guys, but this is what

**[4:36]** the glossary looks like. So, we have our

**[4:38]** open weights model glossary, and these

**[4:40]** are all the words that have been inside

**[4:41]** of the five lesson plans that I have,

**[4:43]** all with definitions, so I can kind of

**[4:45]** reference this. And when I see the word,

**[4:47]** I can go back and see, okay, that's what

**[4:48]** it means, and that's the context of this

**[4:50]** sentence. And this continues to grow as

**[4:52]** you get more and more lessons. Just

**[4:53]** scrolling through a couple of more

**[4:54]** examples, this is what lesson two looks

**[4:56]** like. This one's really cool because it

**[4:58]** actually gives me some math to actually

**[4:59]** understand what kind of models I can run

**[5:02]** on my hardware. I have a computer from

**[5:03]** 2019, so I can't run anything crazy. I

**[5:06]** only have 8 GB of RAM, so I got to be

**[5:08]** very flexible with which models I

**[5:10]** choose. This helps me understand better

**[5:11]** how to actually choose which model. And

**[5:13]** what's really cool is in these HTMLs,

**[5:15]** they're incredibly interactive, and

**[5:16]** that's why it makes learning so much

**[5:18]** more fun than my previous experiences.

**[5:20]** So, I could actually type in here

**[5:21]** numbers and then get answers of

**[5:23]** everything like that, and it just goes

**[5:25]** with the entire flow of my learning

**[5:27]** process. And again, it gives me

**[5:28]** immediate action to take, and then I

**[5:30]** have to do a self-check right after

**[5:31]** that. What's really fun, too, is if I'm

**[5:33]** stuck on a certain topic and I'm not

**[5:35]** just not quite understanding it yet,

**[5:36]** I'll just have it generate a HTML quiz

**[5:38]** for me, and I could just go in, quiz,

**[5:40]** ask questions about the quiz, ask

**[5:42]** questions about really anything related

**[5:44]** to that lesson plan, and it's going to

**[5:46]** create a dynamic way for me to learn

**[5:47]** that. And I mentioned previously that it

**[5:49]** documents all your learning records, and

**[5:51]** based on the questions that you ask or

**[5:53]** the situations that you're in within

**[5:54]** that learning lesson, you'll have

**[5:56]** everything documented for future

**[5:58]** lessons. So, in this case, I was

**[6:00]** verifying that my machine was 8 GB of

**[6:02]** VRAM, whatever my hardware was, so I can

**[6:05]** decide what models that I can

**[6:06]** comfortably run on this computer. And in

**[6:08]** this case scenario, I was just asking

**[6:10]** like, what is the best open-source model

**[6:11]** that I can run on this computer? I

**[6:13]** specifically asked it if I could use

**[6:15]** DeepSeek's best and it told me that I

**[6:16]** was out of my mind because I have

**[6:18]** nowhere near the hardware to actually

**[6:19]** run that model. It then brought me down

**[6:21]** a loop of explaining what distilled

**[6:23]** models are, frontier models, and how

**[6:25]** distilled models are just lowered

**[6:27]** versions of these frontier models that

**[6:29]** run on this incredible hardware, and how

**[6:31]** you're actually able to run variations

**[6:33]** of these open-source models on whatever

**[6:34]** hardware you have. But, the fact that

**[6:36]** it's tracking my real progress and gives

**[6:38]** me a good standing point of exactly

**[6:39]** where I'm at in learning about

**[6:41]** open-source models gives me a very

**[6:42]** comfortable feeling. But, what's the

**[6:44]** thing that actually makes this thing

**[6:45]** really work? This simple philosophy is

**[6:47]** what separates /teach from every other

**[6:49]** teaching AI tool that I've tried out.

**[6:51]** Matt Pocock built this on his last 10

**[6:53]** years of experience teaching people. So,

**[6:55]** it's built on how people actually learn

**[6:57]** and not just spitting out random

**[6:59]** information. And there are three levels

**[7:00]** to this philosophy. There's knowledge,

**[7:03]** skills, and wisdom. The first thing it

**[7:04]** does is it pulls knowledge, but not from

**[7:06]** any random sources. It actually goes

**[7:08]** through high-trusted sources and vets

**[7:10]** them before embedding them into your

**[7:11]** lesson plan. Then it helps you build

**[7:13]** real practice by again, like I said

**[7:14]** before, taking action and not just

**[7:17]** reading. And then for the last part,

**[7:18]** wisdom, it actually points you towards

**[7:20]** communities to help you surround

**[7:21]** yourself with more people learning the

**[7:23]** same topic. So, if I hop over to my

**[7:24]** glossary here at the bottom, you can see

**[7:26]** that it's pointing me to the Reddit page

**[7:28]** for Olama. Because as people say all the

**[7:29]** time, you can outsource your research

**[7:31]** and all that stuff to AI, but you can

**[7:32]** never really outsource your

**[7:33]** understanding. So, getting into these

**[7:35]** communities and learning from people

**[7:36]** that have actually been in your place is

**[7:38]** incredibly important, and I love how

**[7:40]** this /teach skill implements this. But,

**[7:42]** this right here is a concept that

**[7:43]** fascinated me. We all know that we all

**[7:45]** learn things differently. Like, when I

**[7:47]** was in school, I literally could not sit

**[7:49]** still, and if I wasn't interested in a

**[7:50]** topic, I just didn't care about it. But,

**[7:52]** every lesson that this skill builds is

**[7:54]** pitched right at your level. So, they're

**[7:56]** not so easy that you're bored, and

**[7:58]** they're not so hard that you want to

**[7:59]** quit. They're pitched for exactly where

**[8:00]** you're at. Right in that sweet spot

**[8:02]** where you feel a little bit challenged,

**[8:03]** but you still really want to do it, and

**[8:05]** it gets fun. And it's able to do that

**[8:07]** because, again, it's tracking your

**[8:08]** record. Based on the questions that

**[8:09]** you're answering, it's logging all that

**[8:11]** information in those lesson records that

**[8:12]** I showed you earlier. So, every single

**[8:14]** lesson following that is calibrated to

**[8:16]** exactly where you're at in the current

**[8:18]** one. And teachers actually have a name

**[8:19]** for this concept, and it's called the

**[8:20]** zone of proximal development. And if you

**[8:22]** really want to feel like you can learn

**[8:23]** anything and just go to any topic and

**[8:25]** easily pick it up, this is a concept

**[8:27]** definitely worth knowing about. Because

**[8:28]** most of the time, any other learning

**[8:30]** tool that you use will either just dump

**[8:32]** all the information on you or baby you.

**[8:34]** This one feels like it hits the right

**[8:35]** spot every time. And then it really does

**[8:37]** something you wouldn't expect. Once it

**[8:39]** feels like you've mastered or learned

**[8:40]** these skills well enough, it'll just

**[8:42]** pass you on to a community and actually

**[8:44]** step out of the way. Which, for me,

**[8:45]** learning about open source models is

**[8:47]** actually really exciting because I

**[8:48]** definitely want to surround myself with

**[8:49]** some people that actually know a lot

**[8:51]** about it. And I love this because it's

**[8:52]** not trying to keep you dependent on the

**[8:54]** model to keep learning. It's trying to

**[8:55]** make you good enough at the topic so

**[8:57]** that you don't need it anymore. Because

**[8:59]** we don't want to become reliant on AI.

**[9:01]** And so, I know at this point you're

**[9:02]** probably eager to get this set up for

**[9:03]** yourself, so let's get exactly into that

**[9:05]** next. And if you've been following me

**[9:06]** for a long time, you know exactly how

**[9:08]** I'm going to install this, and all I'm

**[9:09]** going to do is hop over to this {slash}

**[9:11]** skills repo, grab the {slash} teach

**[9:13]** skill, and then hop right over to Claude

**[9:14]** code, say, "Please look at this skill

**[9:16]** and install it into our project." Give

**[9:18]** it the GitHub link, and then it's going

**[9:20]** to go ahead and install that skill for

**[9:21]** us. Now, I already did it, so I'm not

**[9:23]** going to enter in this prompt, but I

**[9:24]** wanted to show you guys on the screen so

**[9:25]** you can do it for yourself. And so, now

**[9:27]** let's actually run this skill. So, I'm

**[9:28]** going to go ahead and run {slash} teach

**[9:29]** on how to actually build LLMs, and then

**[9:32]** on the left-hand side here, we only have

**[9:33]** one folder right now, which is open

**[9:35]** source models, and we should get another

**[9:36]** one once this whole process is done. And

**[9:38]** so, right away it begins setting up the

**[9:40]** entire teaching workspace for this. And

**[9:42]** first it checks what actually exists

**[9:44]** already within the entire codebase. And

**[9:46]** since learning about how to build LLMs

**[9:48]** is such a vast topic, it's going to

**[9:49]** actually ask me some concise questions

**[9:51]** to really narrow down where we want to

**[9:53]** start learning. First question is the

**[9:55]** why, which is going to help us develop

**[9:56]** that mission statement. So, what's the

**[9:58]** real driver behind behind learning how

**[10:00]** to build LLMs? And that's going to be

**[10:02]** first principle mastery for me. Then the

**[10:04]** depth is going to say "How hands-on do

**[10:05]** you want to get?" I'm going to say

**[10:07]** hands-on code. I do really want to learn

**[10:08]** how to actually build these for myself.

**[10:10]** And now slowly we're going to begin

**[10:11]** building out this entire workspace. And

**[10:13]** so, it locked that plan in, and now it's

**[10:14]** immediately going and doing some web

**[10:16]** search and getting us some initial

**[10:17]** information. And a quick note, while

**[10:19]** you're running this, I'm currently

**[10:20]** running this on Opus 4.8 with high

**[10:22]** effort. Matt Pocock in his explanatory

**[10:24]** video, which will be linked in the

**[10:25]** description, ran it on medium effort.

**[10:27]** So, that's also a good default if you

**[10:29]** don't want to be spending that many

**[10:30]** tokens. If you wanted to go a little bit

**[10:31]** faster and maybe do a little bit better

**[10:33]** research, then you could just run this

**[10:35]** on the high or max effort. And I ran

**[10:36]** into a little bug, which I'm glad that

**[10:38]** actually happened, because instead of

**[10:39]** making its own workspace inside of that

**[10:42]** learning folder that I had earlier, it

**[10:44]** went ahead into the skill folder and

**[10:46]** created it inside of that, which is

**[10:47]** something I don't want. So, just make

**[10:49]** sure when you're prompting this inside

**[10:50]** of an operating system, and if you're

**[10:52]** not in a fresh folder, that you actually

**[10:54]** are very meticulous with where you're

**[10:56]** placing these folders. I'm going to wait

**[10:58]** for everything to finish, and then I'm

**[10:59]** going to show you how I merge it over

**[11:00]** back to the learning section. And so,

**[11:02]** the workspace was created, and actually

**[11:03]** created the first lesson for us. So,

**[11:05]** this first lesson is an LLM is a next

**[11:07]** token predictor, explaining us what an

**[11:09]** LLM is. We can see the four moves on how

**[11:11]** it works, the code behind it. It then

**[11:14]** gives me your turn to predict then run,

**[11:16]** which is really cool. Check for

**[11:17]** yourself. I could open these up and

**[11:19]** answer all the questions, and all these

**[11:21]** sources at the bottom. But I want to go

**[11:22]** ahead and merge this into its own

**[11:24]** workspace inside of that learning

**[11:25]** subfolder. So, I'm going to go ahead and

**[11:27]** say that. Please move this entire

**[11:28]** workspace into the learnings folder. I

**[11:31]** don't want it in the skills folder where

**[11:33]** it's currently at. So, merge this entire

**[11:35]** workspace in a subfolder under the

**[11:37]** learning folder called how to build

**[11:39]** LLMs. Then, I'm going to go ahead, send

**[11:41]** that off, and now that entire thing that

**[11:43]** it just built will merge into that

**[11:44]** learning folders, which is exactly where

**[11:46]** I want it to be. So, if you come across

**[11:47]** this, this is a simple fix, but just

**[11:49]** make sure that you guys are pretty

**[11:50]** meticulous with where you're actually

**[11:52]** asking these files to be created. And

**[11:53]** that's much better. Now, in the learning

**[11:55]** folders, we have two subfolders called

**[11:56]** how to build LLMs and open-source

**[11:58]** models. So, that's how you guys can fix

**[12:00]** that really quickly. And then it says

**[12:01]** easy as just continuing every lesson. If

**[12:03]** you're in one session, you can continue

**[12:05]** on just learning, going through the

**[12:07]** lesson plan, asking questions,

**[12:09]** everything will get tracked, and then

**[12:10]** you'll be able to start exactly where

**[12:12]** you left off from in every new session.

**[12:14]** All you'll need to do is point your

**[12:15]** agent to the specific workspace, and

**[12:17]** you'll be good to go. And of course, the

**[12:19]** reality is this isn't magic at all. And

**[12:21]** it's definitely [music] not a shortcut

**[12:22]** because at the end of the day, you're

**[12:23]** learning, and you still got to do the

**[12:24]** reps. You guys saw yourself, I'm only

**[12:26]** five lessons in to my open-source model

**[12:28]** journey, and I'm going to keep going

**[12:29]** through it lesson by lesson until I feel

**[12:31]** I'm at a good spot to get pushed to a

**[12:33]** community. And that's the entire point

**[12:34]** of this skill. It's a tutor, not a cheat

**[12:36]** code, and it makes learning way [music]

**[12:38]** more fun. But, it does not do the

**[12:39]** learning for you. And I'll say it again,

**[12:41]** you can outsource all the research with

**[12:43]** AI, but you can never outsource your

**[12:45]** understanding of AI. And if any part of

**[12:46]** this video confused you at all, don't

**[12:48]** worry cuz I got you. I created an entire

**[12:50]** free resource guide with all the install

**[12:52]** commands, some prompts in there for you

**[12:53]** guys, and everything you need to follow

**[12:55]** alongside this video. All you'll need to

**[12:57]** do is click the link down below, enter

**[12:58]** in your email, and join my free school

**[13:00]** community AI Automation Nexus. You'll

**[13:02]** get access to all the resources from

**[13:03]** this video and every single resource

**[13:05]** that I've ever created. Really hope to

**[13:07]** see some of you guys in there soon. As

**[13:08]** always, if you've got any value from

**[13:09]** this video, drop a like, hit that

**[13:11]** subscribe button. It definitely helps me

**[13:12]** out a ton. Leave a comment down below on

**[13:14]** the first thing you're going to learn

**[13:16]** using this new {slash} teach skill. I

**[13:18]** drop videos every Tuesday and Friday,

**[13:19]** but I'm going to be dropping a video

**[13:21]** every single day until July 11th. I

**[13:23]** really have fun making content for you

**[13:24]** guys. I'm definitely enjoying the

**[13:25]** process. And if you've made it this far

**[13:27]** in the video, thank you so much and I'll

**[13:29]** see you guys in the next one. God bless,

**[13:32]** guys.

**[13:35]** Hey, if you're still here, that means

**[13:36]** you've made it to the end of the video.

**[13:37]** So, first of all, thank you so much.

**[13:39]** Something I like to do at the end of all

**[13:41]** my videos is pray for you guys, my

**[13:42]** audience. I do this because I genuinely

**[13:44]** believe in the power of prayer. It's

**[13:46]** helped me get some out of some dark

**[13:47]** places in my life and I can only extend

**[13:49]** that belief to you guys and I really do

**[13:51]** love you guys and appreciate the fact

**[13:52]** that you guys watch my videos every

**[13:54]** single day and actually enjoy my

**[13:56]** content. If this makes you feel

**[13:57]** uncomfortable at all, please feel free

**[13:59]** to click off the video. I'm not here to

**[14:01]** force anything on you, but just know

**[14:03]** that Jesus loves you. But, I'm going to

**[14:04]** go ahead and pray for you guys.

**[14:08]** Heavenly Father, thank you so much for

**[14:09]** this day. Thank you so much for giving

**[14:11]** us the breath of life today to chase

**[14:12]** opportunity and become better versions

**[14:14]** of ourselves every single day and

**[14:16]** glorify you. Lord, I just want to pray a

**[14:18]** blessing over my audience, a blessing of

**[14:20]** wisdom. Lord, just continue to have them

**[14:22]** come to you and ask you questions and

**[14:24]** ask to receive wisdom because you will

**[14:26]** give it to them and just continue, Lord,

**[14:28]** to put it in their hearts to serve their

**[14:30]** neighbor, love their neighbor, love

**[14:32]** their families, provide for their

**[14:33]** children and then just be good people

**[14:36]** with good hearts. Lord, in everything

**[14:38]** that we do, may we glorify you and honor

**[14:40]** you. Lord, we thank you for your

**[14:41]** sovereignty, your peace and your love.

**[14:44]** And Lord, just continue to make us think

**[14:46]** and be where our feet are. Lord,

**[14:48]** [snorts] don't let us make plans for the

**[14:49]** future. Can let us be present in every

**[14:51]** single moment of every single day and

**[14:53]** just continue to better our lives. Lord,

**[14:55]** we thank you for everything. Lord, we

**[14:57]** thank you for your son Jesus and his

**[14:58]** sacrifice on the cross and we just

**[15:00]** continue to praise you, love you and

**[15:02]** glorify you. And it's in your name that

**[15:04]** we pray.

**[15:05]** Amen.

**[15:06]** Now, go have a great day, guys. I'll see

**[15:08]** you tomorrow.
