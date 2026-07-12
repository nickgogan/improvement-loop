# Transcript: Claude Fable 5 Use Cases You Must Do NOW (Or Lose Thousands in 1 Week)

**URL:** https://www.youtube.com/watch?v=lplVBFr0Ndc
**Segments:** 368
**Channel:** Chase AI
**Duration:** 11:59
**Uploaded:** 2026-07-02

---

## Full Text

The most powerful AI model ever, Fable 5 is back. But we only have a week to play around with this thing before we lose it to API pricing. So, the question you should be asking yourself is, what projects can I use Fable 5 on over the next 7 days to get the most bang for my buck? How can I actually squeeze every ounce of juice out of this model? Well, in this video, I'm going to help you out as I show you five different projects you can point Fable 5 at and get your money's worth. So, with that, let's hop in. So, the first and arguably the best use case for Fable 5 is simply cloning software that already exists out in the real world. Probably software you pay for. Well, why are we paying for it? Why don't we just build a clone ourselves and customize it to our needs? Fable 5 is great at doing this. And in this demo, let's have it clone Whisper Flow. A ton of you probably use Whisper Flow or something like it. Well, why are we paying for this? Furthermore, why are we giving our data to someone like Whisper Flow and having that information that we speak into our microphone go to some cloud server? Why don't we just create a Whisper Flow that's purely local, runs on our machine, is faster, and again, we can customize to our heart's desire. Well, that's exactly what Fable 5 can do. Now, when we work on these big projects, something we do need to keep in mind is our usage limits. Up until July 7th, we can use Fable 5 with our Max plans. However, we can only use up to 50% of the plan's weekly usage limit. So, we need to be smart about how we do this. We need to be smart about the sort of prompts we create. Does it make a lot of sense for me to just say, "Hey Fable 5, go recreate Whisper Flow."? We can probably do better than that. In fact, what we can probably do is we could use something like deep research, aka dynamic workflows inside of Claude code using a model like Opus 4.8, have it figure out a plan that actually makes sense. We could even use something like Codex to check that plan. And once we have a plan that makes sense, we hand it off to Fable 5. We do some of the upfront grunt work with Opus and let Fable 5 handle the rest. That's exactly what we're going to do. So, again, I'm on Opus 4.8. I said {forward slash} deep research. I want to come up with a plan to clone WhisperFlow. I want you to do some deep research on how WhisperFlow works, what we would need to recreate its base functionality on our computer. Furthermore, I'd like to recreate it locally. So, I want it to be a local model running on a Llama that essentially does what WhisperFlow does. So, we're going to run this. It's going to come back with a plan. And if that plan makes sense to us, we're going to go ahead and hand it to Fable 5 and have it go to work. So, went ahead and finished the deep research. It figured out, "Hey, this is what a WhisperFlow clone should look like. Here's how it would work on your computer, and here's sort of the local architecture I'm thinking about." Now, what we want to do is we want to take this whole report and we want to turn this into a prompt we can hand to Fable 5, and we can have Opus do that just fine. Ideally, we set up this prompt so it makes sense if we do {forward slash} goal. Remember, {forward slash} goal is for a long-running agentic tasks, big projects, things that are perfect for Fable 5. And with {forward slash} goal, we're saying, "Hey, this is what we want to do, and here's sort of the success criteria." And it's just going to keep working and working and working until it gets to your end state. So, perfect for things like this. So, went ahead and created that prompt for me. So, I'm just going to go ahead and copy this thing. We're then going ahead and just switch the model over to Fable 5. We pasted the prompt in there. And we just let it go to work. And after some back and forth get the visuals working, we got this, which is my version of WhisperFlow, but entirely local. Nothing leaves my computer. Doesn't have all the bells and whistles of WhisperFlow, but it does the basics. It listens to what's going on with my microphone. It transcribes it. It sends it down to the local AI model to clean it up. And when I'm done talking, it just populates it inside the text box. Let's see what it gives us. So, hey, nothing leaves the computer. It doesn't have all the bells and whistles, etc., etc., etc. So, it just took everything I said and put it inside here. Now, all that all that being said is WhisperFlow clone the craziest thing ever for Fable 5? No, it can actually do a lot more than that. But, it just sort of depends on what you want to clone. I think you sort of just use the template I gave you, which is do some deep research, figure out how that particular app actually works, figure out how you want to customize it, get your prompt in order, and then bring it to Fable 5. I definitely do not suggest using dynamic workflows with Fable 5, or you're just going to burn through all of your usage. Now, let's move into use case number two, which is using Fable 5 to do a complete teardown and diagnosis of how you use Claude code and how you can improve. Now, I'm not talking about how you use Claude code in terms of usage, I'm saying we're going to have Fable 5 look across all your previous sessions, take a look at how you use Claude in terms of your skills, your automations, your tasks, and then figure out what you're doing right, what you're doing wrong, and more importantly, what we can do to improve this. Does this mean changing our skills, creating new skills, adding new automations? So, this is essentially doing an audit of how you're using the tool itself. So, here's a look at the prompt. We're saying, "Reflect on our past Claude code sessions to find the highest leverage improvements to my setup. Use sub-agents to pull raw signals from the transcripts, you cluster them across sessions, and decide per cluster whether it needs a new skill, an automation, a fix, or nothing. Write the candidates in this MD file." And we're saying, "Hey, at first, it's just a diagnosis. I want to see what it comes back with before it executes anything." Now, if you're wondering how I'm coming up with these prompts in this prompt structure, this is coming from Anthropic's official documentation when it comes to prompting Claude Fable 5, because there are some nuances between how you want to use Fable and Mythos versus something like Opus. So, let's see what it comes back with. So, Fable 5 ran through my last 39 sessions, and this is what it came up with. It broke it out into three different batches based on how much leverage it think it would gave me, and they ranged from creating new skills to setting certain skills as automations and some simple changes to things like my Claude.md. So, this is a really simple use case to improve your workflows within Claude code and it's something you'll get a lot more out of if you fall into the power user side of the equation. So, before we jump into the next use case, I just want to give you a quick word from today's sponsor, which is me. I just released a Claude code masterclass not too long ago and it is the number one way to go from zero to AI dev especially if you don't come from a technical background. We update this every single week and all the resources you see in today's video including my Claude OS can be found here inside of Chase AI Plus. There's a link to that in the pinned comment. So, definitely check us out if you are trying to get more serious about your AI journey. Now, let's go into use case number three, which is building your own agentic OS. What you see here is one I built with Fable 5 and this essentially acts as a custom wrapper over the top of Claude code. What we see here is the visual side of it, but what's most important is what's going on under the hood and it's a perfect follow on from use case number two, which is essentially codifying everything you do in your day-to-day, your week-to-week into skills and automations. But, this gives us the additional advantages of certain visual metrics that we just can't get inside of the terminal. So, for me that includes things like content, right? What's been going on with my content game across multiple platforms. I can see things like my different like morning reports and things of that nature. This is all linked to Obsidian and I have all of my most used skills and automations over here on the right, which are just a click away. Now again, I've done deep dives on this. I'm not going to turn this into a deep dive agentic OS video, but the most important part are all those skills and automations I'm talking about. You need to use Fable 5 to come up with the skills and automations that make sense for you. For me that has to do with like research, content, things on my agency side like sales and finance. All my individual tasks Fable 5 turns into skills and turns them into automations, if that makes sense. And in certain cases, we apply loop engineering to those skills as well, but that really depends on the use case. But this sort of customize Agentyc OS is pretty simple for Fable 5 to create. And one of the best parts about this is that if you're in the AI agency game, you can package this, since it's essentially a web app that anyone can put on top of their Claude code and sell it. Or you can clone it and give this to teammates who aren't going to use the CLI or aren't going to use the Claude app, because they can add whatever they want to this and you pretty much just wire up different skills and automations that you would use, because it's just doing Claude headless -p under the hood, which luckily for us isn't pulling from API prices anymore, since Anthropic walked that back a few weeks ago. Now use case number four comes directly from Anthropic itself, and that is code review and debugging. If you have a complicated project, if you have a huge code base, now is the time to take Fable 5 and point it at that code base and see if you can figure out what code looks bad and what are actually bugs. And the prompt for this doesn't have to be complicated. Hey, so I want you to take a look at this code base and I want you to do a full code review and also let me know about any bugs you find. And it's going to come back with whatever it finds. So after about 5 minutes, it found 45 raw findings from four parallel reviewers, dedupe down to 24. And then it took those 24 and it broke it down by severity. And it gives us sort of an explanation of what's wrong at each step, kind of like where the issue is, and then it gives us a specific priority. And it's like, "Hey, do you want to go ahead and start working on these?" Now, the cool thing about this is it found all these things wrong in a code base that isn't necessarily that complicated. There's things that are infinitely more complicated than what I'm doing here. So if you are in that camp of someone who has something very complicated, there is no reason you should not be pointing Fable 5 at it and at least having it get eyes on on the work you've already done. Now use case number five is what you see right here. It's having Fable 5 create whatever custom software you want, something that is going to require a long horizon. This is a video game built in a browser running on 3.js and this looks wild. This is an insane accomplishment by Fable 5. You would not be able to create this using something like Opus 4.8 unless you knew exactly what you were doing. This is Again, this is all running on the browser. This isn't like a downloaded video game. This is all browser graphics and it's crazy. Now, I wasn't one who actually built that. This is an open-source project from Braffolk who created this using Fable 5 the first time it came out. But, I think this is a great case study for the sort of things you can create and the power here isn't just that Fable 5 built it. The power is that we can look at sort of how he created this from scratch. So, the read me talks about the one document that they gave Fable 5 in order to create this. So, the human partially wrote one document, which is this markdown file. And what is this? This is a PRD. This is a product requirements document spelling out, "Hey, here's what we want to build, right? The visual target is a current-gen Unreal Engine 5 showcase footage." And then it goes through sort of like the pillars of this application, the instructions, the constraint, the floors, etc., etc. Like I said, this was only partially written by the human. So, what you need to do if you're trying to create your own sort of software or game or whatever it is, some sort of crazy project that only Fable 5 can build, you need to nail this down. You need to nail down the PRD. Now, Fable 5 can help you, but we want to be very conscious of our usage. So, this is something Opus 4.8 can at least get it started with you, right? You should be able to create some sort of PRD with the specific instructions and with the specific requirements with Opus 4.8. Again, use something like deep research to help you do that and then bring it to Fable 5. Essentially, recreate what we did in the first use case. And after that, you pretty much just hand it to Fable 5 and you let it execute it across long autonomous sessions, exactly like the Ford /goals scenario we did earlier. In this particular setup, Phable 5 wrote 21,000 lines of TypeScript across 90 plus commits to get what you just saw. So, really cool stuff and that's just a taste of what this model is able to build for you. So, those are the five Phable 5 use cases you need to try out this week. As always, let me know what you thought about this video in the comments. Make sure to check out Chase AI Plus if you want to get your hands on the Claude Code Masterclass or my exact Claude OS setup. Besides that, I'll see you around.

---

## Timestamped Segments

**[0:00]** The most powerful AI model ever, Fable 5

**[0:02]** is back. But we only have a week to play

**[0:05]** around with this thing before we lose it

**[0:06]** to API pricing. So, the question you

**[0:09]** should be asking yourself is, what

**[0:11]** projects can I use Fable 5 on over the

**[0:14]** next 7 days to get the most bang for my

**[0:17]** buck? How can I actually squeeze every

**[0:20]** ounce of juice out of this model? Well,

**[0:22]** in this video, I'm going to help you out

**[0:24]** as I show you five different projects

**[0:26]** you can point Fable 5 at and get your

**[0:28]** money's worth. So, with that, let's hop

**[0:30]** in. So, the first and arguably the best

**[0:32]** use case for Fable 5 is simply cloning

**[0:34]** software that already exists out in the

**[0:37]** real world. Probably software you pay

**[0:38]** for. Well, why are we paying for it? Why

**[0:41]** don't we just build a clone ourselves

**[0:42]** and customize it to our needs? Fable 5

**[0:44]** is great at doing this. And in this

**[0:46]** demo, let's have it clone Whisper Flow.

**[0:49]** A ton of you probably use Whisper Flow

**[0:51]** or something like it. Well, why are we

**[0:52]** paying for this? Furthermore, why are we

**[0:54]** giving our data to someone like Whisper

**[0:56]** Flow and having that information that we

**[0:58]** speak into our microphone go to some

**[1:00]** cloud server? Why don't we just create a

**[1:02]** Whisper Flow that's purely local, runs

**[1:04]** on our machine, is faster, and again, we

**[1:06]** can customize to our heart's desire.

**[1:09]** Well, that's exactly what Fable 5 can

**[1:10]** do. Now, when we work on these big

**[1:13]** projects, something we do need to keep

**[1:15]** in mind is our usage limits. Up until

**[1:18]** July 7th, we can use Fable 5 with our

**[1:21]** Max plans. However, we can only use up

**[1:23]** to 50% of the plan's weekly usage limit.

**[1:25]** So, we need to be smart about how we do

**[1:27]** this. We need to be smart about the sort

**[1:29]** of prompts we create. Does it make a lot

**[1:31]** of sense for me to just say, "Hey Fable

**[1:33]** 5, go recreate Whisper Flow."?

**[1:35]** We can probably do better than that. In

**[1:37]** fact, what we can probably do is we

**[1:39]** could use something like deep research,

**[1:41]** aka dynamic workflows inside of Claude

**[1:44]** code using a model like Opus 4.8, have

**[1:47]** it figure out a plan that actually makes

**[1:49]** sense. We could even use something like

**[1:51]** Codex to check that plan. And once we

**[1:53]** have a plan that makes sense, we hand it

**[1:55]** off to Fable 5. We do some of the

**[1:57]** upfront grunt work with Opus and let

**[2:00]** Fable 5 handle the rest. That's exactly

**[2:01]** what we're going to do. So, again, I'm

**[2:03]** on Opus 4.8. I said {forward slash} deep

**[2:05]** research. I want to come up with a plan

**[2:07]** to clone WhisperFlow. I want you to do

**[2:08]** some deep research on how WhisperFlow

**[2:10]** works, what we would need to recreate

**[2:12]** its base functionality on our computer.

**[2:14]** Furthermore, I'd like to recreate it

**[2:15]** locally. So, I want it to be a local

**[2:18]** model running on a Llama that

**[2:19]** essentially does what WhisperFlow does.

**[2:20]** So, we're going to run this. It's going

**[2:22]** to come back with a plan. And if that

**[2:24]** plan makes sense to us, we're going to

**[2:25]** go ahead and hand it to Fable 5 and have

**[2:28]** it go to work. So, went ahead and

**[2:29]** finished the deep research. It figured

**[2:30]** out, "Hey, this is what a WhisperFlow

**[2:32]** clone should look like. Here's how it

**[2:33]** would work on your computer, and here's

**[2:34]** sort of the local architecture I'm

**[2:36]** thinking about." Now, what we want to do

**[2:38]** is we want to take this whole report and

**[2:39]** we want to turn this into a prompt we

**[2:40]** can hand to Fable 5, and we can have

**[2:42]** Opus do that just fine. Ideally, we set

**[2:44]** up this prompt so it makes sense if we

**[2:47]** do {forward slash} goal. Remember,

**[2:49]** {forward slash} goal is for a

**[2:50]** long-running agentic tasks, big

**[2:52]** projects, things that are perfect for

**[2:53]** Fable 5. And with {forward slash} goal,

**[2:56]** we're saying, "Hey, this is what we want

**[2:58]** to do, and here's sort of the success

**[2:59]** criteria." And it's just going to keep

**[3:01]** working and working and working until it

**[3:03]** gets to your end state. So, perfect for

**[3:06]** things like this. So, went ahead and

**[3:07]** created that prompt for me. So, I'm just

**[3:10]** going to go ahead and copy this thing.

**[3:12]** We're then going ahead and just switch

**[3:13]** the model

**[3:15]** over to Fable 5. We pasted the prompt in

**[3:18]** there.

**[3:20]** And we just let it go to work. And after

**[3:22]** some back and forth get the visuals

**[3:23]** working, we got this, which is my

**[3:26]** version of WhisperFlow, but entirely

**[3:28]** local. Nothing leaves my computer.

**[3:31]** Doesn't have all the bells and whistles

**[3:32]** of WhisperFlow, but it does the basics.

**[3:34]** It listens to what's going on with my

**[3:36]** microphone. It transcribes it. It sends

**[3:38]** it down to the local AI model to clean

**[3:40]** it up. And when I'm done talking, it

**[3:42]** just populates it inside the text box.

**[3:45]** Let's see what it gives us.

**[3:49]** So, hey, nothing leaves the computer. It

**[3:50]** doesn't have all the bells and whistles,

**[3:51]** etc., etc., etc. So, it just took

**[3:53]** everything I said and put it inside

**[3:55]** here.

**[3:56]** Now,

**[3:58]** all that all that being said is

**[3:59]** WhisperFlow clone the craziest thing

**[4:01]** ever for Fable 5? No, it can actually do

**[4:03]** a lot more than that. But, it just sort

**[4:04]** of depends on what you want to clone. I

**[4:07]** think you sort of just use the template

**[4:08]** I gave you, which is do some deep

**[4:10]** research, figure out how that particular

**[4:12]** app actually works, figure out how you

**[4:14]** want to customize it, get your prompt in

**[4:16]** order, and then bring it to Fable 5. I

**[4:18]** definitely do not suggest using dynamic

**[4:20]** workflows with Fable 5, or you're just

**[4:22]** going to burn through all of your usage.

**[4:24]** Now, let's move into use case number

**[4:25]** two, which is using Fable 5 to do a

**[4:28]** complete teardown and diagnosis of how

**[4:31]** you use Claude code and how you can

**[4:33]** improve. Now, I'm not talking about how

**[4:34]** you use Claude code in terms of usage,

**[4:36]** I'm saying we're going to have Fable 5

**[4:38]** look across all your previous sessions,

**[4:40]** take a look at how you use Claude in

**[4:43]** terms of your skills, your automations,

**[4:45]** your tasks, and then figure out what

**[4:47]** you're doing right, what you're doing

**[4:49]** wrong, and more importantly, what we can

**[4:51]** do to improve this. Does this mean

**[4:52]** changing our skills, creating new

**[4:54]** skills, adding new automations? So, this

**[4:56]** is essentially doing an audit of how

**[4:59]** you're using the tool itself. So, here's

**[5:00]** a look at the prompt. We're saying,

**[5:01]** "Reflect on our past Claude code

**[5:03]** sessions to find the highest leverage

**[5:04]** improvements to my setup. Use sub-agents

**[5:07]** to pull raw signals from the

**[5:08]** transcripts, you cluster them across

**[5:10]** sessions, and decide per cluster whether

**[5:12]** it needs a new skill, an automation, a

**[5:14]** fix, or nothing. Write the candidates in

**[5:17]** this MD file." And we're saying, "Hey,

**[5:19]** at first, it's just a diagnosis. I want

**[5:20]** to see what it comes back with before it

**[5:22]** executes anything." Now, if you're

**[5:23]** wondering how I'm coming up with these

**[5:24]** prompts in this prompt structure, this

**[5:26]** is coming from Anthropic's official

**[5:27]** documentation when it comes to prompting

**[5:29]** Claude Fable 5, because there are some

**[5:31]** nuances between how you want to use

**[5:33]** Fable and Mythos versus something like

**[5:35]** Opus. So, let's see what it comes back

**[5:37]** with. So, Fable 5 ran through my last 39

**[5:39]** sessions, and this is what it came up

**[5:40]** with. It broke it out into three

**[5:42]** different batches based on how much

**[5:44]** leverage it think it would gave me, and

**[5:45]** they ranged from creating new skills to

**[5:48]** setting certain skills as automations

**[5:51]** and some simple changes to things like

**[5:53]** my Claude.md. So, this is a really

**[5:55]** simple use case to improve your

**[5:56]** workflows within Claude code and it's

**[5:58]** something you'll get a lot more out of

**[6:00]** if you fall into the power user side of

**[6:03]** the equation. So, before we jump into

**[6:05]** the next use case, I just want to give

**[6:06]** you a quick word from today's sponsor,

**[6:08]** which is me. I just released a Claude

**[6:10]** code masterclass not too long ago and it

**[6:12]** is the number one way to go from zero to

**[6:14]** AI dev especially if you don't come from

**[6:16]** a technical background. We update this

**[6:18]** every single week and all the resources

**[6:20]** you see in today's video including my

**[6:21]** Claude OS can be found here inside of

**[6:24]** Chase AI Plus. There's a link to that in

**[6:26]** the pinned comment. So, definitely check

**[6:28]** us out if you are trying to get more

**[6:30]** serious about your AI journey. Now,

**[6:31]** let's go into use case number three,

**[6:33]** which is building your own agentic OS.

**[6:35]** What you see here is one I built with

**[6:37]** Fable 5 and this essentially acts as a

**[6:40]** custom wrapper over the top of Claude

**[6:42]** code. What we see here is the visual

**[6:44]** side of it, but what's most important is

**[6:46]** what's going on under the hood and it's

**[6:48]** a perfect follow on from use case number

**[6:49]** two, which is essentially codifying

**[6:52]** everything you do in your day-to-day,

**[6:54]** your week-to-week into skills and

**[6:55]** automations. But, this gives us the

**[6:57]** additional advantages of certain visual

**[6:59]** metrics that we just can't get inside of

**[7:00]** the terminal. So, for me that includes

**[7:02]** things like content, right? What's been

**[7:04]** going on with my content game across

**[7:06]** multiple platforms. I can see things

**[7:08]** like my different like morning reports

**[7:10]** and things of that nature. This is all

**[7:11]** linked to Obsidian and I have all of my

**[7:13]** most used skills and automations over

**[7:16]** here on the right, which are just a

**[7:17]** click away. Now again, I've done deep

**[7:19]** dives on this. I'm not going to turn

**[7:20]** this into a deep dive agentic OS video,

**[7:22]** but the most important part are all

**[7:24]** those skills and automations I'm talking

**[7:26]** about. You need to use Fable 5 to come

**[7:28]** up with the skills and automations that

**[7:30]** make sense for you. For me that has to

**[7:31]** do with like research, content, things

**[7:34]** on my agency side like sales and

**[7:35]** finance. All my individual tasks Fable 5

**[7:38]** turns into skills and turns them into

**[7:40]** automations, if that makes sense. And in

**[7:42]** certain cases, we apply loop engineering

**[7:45]** to those skills as well, but that really

**[7:46]** depends on the use case. But this sort

**[7:49]** of customize Agentyc OS is pretty simple

**[7:51]** for Fable 5 to create. And one of the

**[7:53]** best parts about this is that if you're

**[7:55]** in the AI agency game, you can package

**[7:57]** this, since it's essentially a web app

**[7:58]** that anyone can put on top of their

**[7:59]** Claude code and sell it. Or you can

**[8:02]** clone it and give this to teammates who

**[8:05]** aren't going to use the CLI or aren't

**[8:07]** going to use the Claude app, because

**[8:08]** they can add whatever they want to this

**[8:10]** and you pretty much just wire up

**[8:12]** different skills and automations that

**[8:14]** you would use, because it's just doing

**[8:15]** Claude headless -p under the hood, which

**[8:19]** luckily for us isn't pulling from API

**[8:21]** prices anymore, since Anthropic walked

**[8:23]** that back a few weeks ago. Now use case

**[8:25]** number four comes directly from

**[8:26]** Anthropic itself, and that is code

**[8:28]** review and debugging. If you have a

**[8:29]** complicated project, if you have a huge

**[8:31]** code base, now is the time to take Fable

**[8:33]** 5 and point it at that code base and see

**[8:35]** if you can figure out what code looks

**[8:37]** bad and what are actually bugs. And the

**[8:40]** prompt for this doesn't have to be

**[8:42]** complicated.

**[8:44]** Hey, so I want you to take a look at

**[8:46]** this code base and I want you to do a

**[8:47]** full code review and also let me know

**[8:50]** about any bugs you find. And it's going

**[8:51]** to come back with whatever it finds. So

**[8:53]** after about 5 minutes, it found 45 raw

**[8:55]** findings from four parallel reviewers,

**[8:57]** dedupe down to 24. And then it took

**[8:59]** those 24 and it broke it down by

**[9:02]** severity. And it gives us sort of an

**[9:04]** explanation of what's wrong at each

**[9:05]** step, kind of like where the issue is,

**[9:08]** and then it gives us a specific

**[9:10]** priority. And it's like, "Hey, do you

**[9:11]** want to go ahead and start working on

**[9:13]** these?" Now, the cool thing about this

**[9:14]** is it found all these things wrong in a

**[9:16]** code base that isn't necessarily that

**[9:18]** complicated. There's things that are

**[9:19]** infinitely more complicated than what

**[9:20]** I'm doing here. So if you are in that

**[9:23]** camp of someone who has something very

**[9:24]** complicated, there is no reason you

**[9:26]** should not be pointing Fable 5 at it and

**[9:28]** at least having it get eyes on on the

**[9:30]** work you've already done. Now use case

**[9:31]** number five is what you see right here.

**[9:32]** It's having Fable 5 create whatever

**[9:34]** custom software you want, something that

**[9:36]** is going to require a long horizon. This

**[9:38]** is a video game built in a browser

**[9:40]** running on 3.js and this looks wild.

**[9:43]** This is an insane accomplishment by

**[9:46]** Fable 5. You would not be able to create

**[9:48]** this

**[9:49]** using something like Opus 4.8 unless you

**[9:51]** knew exactly what you were doing. This

**[9:52]** is Again, this is all running on the

**[9:53]** browser. This isn't like a downloaded

**[9:55]** video game. This is all browser graphics

**[9:58]** and it's crazy. Now, I wasn't one who

**[10:00]** actually built that. This is an

**[10:01]** open-source project from Braffolk who

**[10:03]** created this using Fable 5 the first

**[10:05]** time it came out. But, I think this is a

**[10:07]** great case study for the sort of things

**[10:09]** you can create and the power here isn't

**[10:12]** just that Fable 5 built it. The power is

**[10:14]** that we can look at sort of

**[10:17]** how he created this from scratch. So,

**[10:19]** the read me talks about the one document

**[10:22]** that they gave Fable 5 in order to

**[10:25]** create this. So, the human partially

**[10:28]** wrote one document, which is this

**[10:29]** markdown file. And what is this? This is

**[10:31]** a PRD. This is a product requirements

**[10:33]** document spelling out, "Hey, here's what

**[10:35]** we want to build, right? The visual

**[10:37]** target is a current-gen Unreal Engine 5

**[10:40]** showcase footage." And then it goes

**[10:41]** through sort of like the pillars of this

**[10:43]** application, the instructions, the

**[10:45]** constraint, the floors, etc., etc. Like

**[10:47]** I said, this was only partially written

**[10:49]** by the human. So, what you need to do if

**[10:51]** you're trying to create your own sort of

**[10:53]** software or game or whatever it is, some

**[10:54]** sort of crazy project that only Fable 5

**[10:56]** can build, you need to nail this down.

**[10:58]** You need to nail down the PRD. Now,

**[11:00]** Fable 5 can help you, but we want to be

**[11:02]** very conscious of our usage. So, this is

**[11:04]** something Opus

**[11:06]** 4.8 can at least get it started with

**[11:08]** you, right? You should be able to create

**[11:10]** some sort of PRD with the specific

**[11:11]** instructions and with the specific

**[11:13]** requirements with Opus 4.8. Again, use

**[11:15]** something like deep research to help you

**[11:17]** do that and then bring it to Fable 5.

**[11:19]** Essentially, recreate what we did in the

**[11:21]** first use case. And after that, you

**[11:23]** pretty much just hand it to Fable 5 and

**[11:25]** you let it execute it across long

**[11:26]** autonomous sessions, exactly like the

**[11:29]** Ford /goals scenario we did earlier. In

**[11:31]** this particular setup, Phable 5 wrote

**[11:33]** 21,000 lines of TypeScript across 90

**[11:35]** plus commits to get what you just saw.

**[11:38]** So, really cool stuff and that's just a

**[11:39]** taste of what this model is able to

**[11:41]** build for you. So, those are the five

**[11:43]** Phable 5 use cases you need to try out

**[11:46]** this week. As always, let me know what

**[11:48]** you thought about this video in the

**[11:49]** comments. Make sure to check out Chase

**[11:51]** AI Plus if you want to get your hands on

**[11:52]** the Claude Code Masterclass or my exact

**[11:55]** Claude OS setup. Besides that, I'll see

**[11:58]** you around.
