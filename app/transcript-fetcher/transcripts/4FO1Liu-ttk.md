# Transcript: Caveman Claude Code Is the New Meta (Here's the Science)

**URL:** https://www.youtube.com/watch?v=4FO1Liu-ttk
**Segments:** 307
**Channel:** Chase AI
**Duration:** 10:36
**Uploaded:** 2026-04-07

---

## Full Text

Making Claude code talk like a cave man, might not only save you tokens, it could actually improve your performance as well. Now, on the surface, this sounds like a complete meme. We have a GitHub repo called cave man that's gotten 5,000 stars in 72 hours, and all it does is force Claude code to talk like a Neanderthal. It trims out all the filler. The idea is that by making it more concise, we save a ton of tokens in the process. But buried in this repo is a link to this research paper that just came out a few weeks ago, which tells us if we force our large language models to be more concise, we not only save tokens, but we can dramatically improve their performance. So, today I'm going to break down this entire cave man skill. I'm going to explain what it actually buys you, because the numbers in the repo are a little misleading, and we're going to talk through this research paper so you can understand what this actually means for you. So, this is cave man, our why say many word when few word do trick repo. Now, right off the bat, what is it doing? Pretty simple, cutting out the filler. Claude code now talks like a cave man. It gives us some before and after examples, shows us the token difference, and even has a full benchmark list showing the task it gave Claude code, explain react render bug, the normal tokens being used, the cave man tokens, and the amount saved. Now, the numbers put forth in this repo are kind of insane. So, they are claiming that with the skill, we are going to cut 75% of output tokens while keeping full technical accuracy. This cave man does not change how Claude code reasons under the hood. It doesn't change how it actually generates code. None of that gets changed. It's just the output, what you see as a response. It also includes a companion tool that compresses your memory files, think Claude.md into cave man speak, and that is supposed to reduce our input tokens by 45% every session. Now, let's be clear. You are not cutting 75% of your output tokens at large and 45% of your input tokens at large at all. That is completely not true. Even though we can see these things that say, "Hey, it saves 87% of tokens on how it explains a react render bug." The prompt you get back from Claude code, the response itself, the text, is just a small portion of the output tokens at large. Just like the memory files, like Claude.md, is just a small portion of the input at large. So, let's be very clear about what this is actually buying us on a token scale. You are not saving 80% of your total tokens. And to make it a little more clear, let's break down your average 100,000 token Claude code session. Now, I understand every session is a little different, but just work with me here. We have a 100,000 token session, and it's broken up into two parts, the input, which is the lion's share, that's 75,000 tokens, and the output, which is 25%. Now, cave man is claiming we're going to reduce output by 75%. That is not true. If we take a look at output, it's really in three parts, right? We have tool calls taking up a portion of it, code blocks like the actual code generation taking a portion of it, and then the actual prose responses. This response, that text response in the terminal, that's what cave man is adjusting. That's what it's reducing. It can reduce 75% of that. You know, if we go down here, we can see, okay, so normally the prose takes up 6K tokens, with cave man we save 4,000 tokens. So, we get a 4% reduction. That's still really good. If we're saving 4% of our total tokens over the course of the week, that certainly adds up, especially in the current environment where we are all so conscious of our usage. But understand, this is not 87%. It's 70%, 60% of one portion of one portion of the total session. Furthermore, if you look at the inputs, and it talks about the cave man compression saving 45%, again, not really. We're talking about the system prompt area, and only certain parts of the system prompt. So, total here, right? We're saving what? Maybe 1,000 tokens, maybe 2,000 tokens. And over the course, again, of an entire session, if I save 5,000 tokens, 5% of every session, that's great. Good stuff. But it's not these gaudy numbers. So, understand that going in. This is an on the margin play. This isn't totally You're not going to be able to go from basically 5x max plan to 20x max plan because we're saving 75%. No, no, no, no. But there's still tons of value to be added here, and even more value to be extracted once we take a look at the study. It's kind of buried in here. There's There's one little section dedicated to it. But this is a study called brevity constraints reverse performance hierarchies in language models, and this came out in early March of this year. So, I'll put a link to the study down in the description if you want to check it out. But let's just talk about it really quick, because this is really interesting. Because the idea and the expectation is bigger model better than smaller model, always. Well, not exactly, not according to this study. So, in this study, they evaluated 31 models across 1,500 problems, and they identified the mechanism as spontaneous scale dependent verbosity that introduces errors through over elaboration. What the heck does that mean? That means on nearly 8% of the problems across these 1,500 problems and 31 models, the larger language models, the ones with more parameters, underperformed smaller ones by 28 percentage points despite 100 times more parameters in some cases. So, you had scenarios where, again, this is with all open weight models, you had a 2 billion parameter model outperforming a 400 billion parameter model. And this happened multiple times. This is crazy. Why is this? Well, they propose it that the reason why is because these large language models talk too damn much. They are over verbose to the point that they pretty much spin themselves into circles and get the wrong answer because of it. And in the study, they found that by constraining large models to produce brief responses, cave man responses, improves accuracy by 26 percentage points and reduces performance gaps by up to 2/3. And in many cases, by forcing these large language models to become more concise, more cave man like, switched that dynamic to where before they were losing to some of these smaller models, and now they were defeating them. That's kind of wild, especially in context of this GitHub repo. Now, obviously, these are open weight models. This isn't Opus 4.6. This isn't Codex 5.4. Do these frontier models exhibit this exact same sort of behavior? We don't necessarily know for sure, but if you've seen any of these studies, you understand usually what you see here tends to be repeated on some level with the frontier models. Maybe it's not this extreme, but there's probably something to it. Now, the rest of the study goes into a lot of detail about how they run the tests, how they're trying to break out correlation versus causation, and why they think this is a problem. And like I said before, they hypothesize that large models generate excessively verbose responses that obscure correct reasoning, a phenomenon they termed overthinking. It's just trying to put too much out there. Instead of just giving you the answer and getting out of its own way, it talks itself into the wrong answer, literally. And they specifically say the learned tendency towards thoroughness becomes counterproductive introducing error accumulation. Brevity constraints help large models dramatically while barely affecting the smaller models. And an obvious question you should have is, well, why why is this even the case? Why are these larger models having this issue? They point towards reinforcement learning. So, when you train a new model, so imagine Opus 5.0 is in the process of being trained, part of what they do is reinforcement learning. Now, I don't know if Anthropic does it specifically, but this is how it's done for many models. Essentially, they take the new model and they bring in a human to grade its answers. They show multiple answers and says, "I like this one more than this one." And they're saying in the study, chances are humans tend to like more verbose answers, more thorough answers, and because of that, these larger models are essentially trained to be more verbose rather than concise and even correct in some instances. But the big takeaway here is this, is that brevity constraints completely reversed the performance hierarchies. So, where they were losing before, now they were winning simply by telling them to be more concise. They didn't change how they thought, they didn't change anything under the hood, they just said, "Be a cave man." Now, they weren't literally using this GitHub, but same exact thing. So, this is why I think this is actually kind of interesting, not just a complete meme. You know, beyond the fact that there are some token, you know, positives here. Saving 5% of tokens is nothing to laugh at, especially if you are not on a max 20 plan. But if there's a potential scenario where we're actually getting better outputs because of it, especially on more straightforward questions, because if you dive into that study, it kind of breaks out like which questions they kind of had this issue with in this dynamic. It's interesting, very interesting, which is why I think this is kind of worth looking at. And it's also super simple to use. It's just a set of skills. Installing this literally is one line, and then running it, we either invoke it with {slash} cave man, or just say something like talk like a cave man, cave man mode, or less tokens, please. There's also levels to it, so we can go like ultra cave man, right? We like just came out of the ocean, we barely can stand up straight, and then we have full and light. So, you can get different levels of cave man throughout the years. And it isn't a blanket thing either. Things like error messages are quoted exactly, and again, anything to do with code, anything to do with generation, anything under the hood, stays the same. We're not changing how it really thinks. So, overall, I think this is worth trying out. It's a single skill, it saves tokens, and there's no real downside, and based on the study, there's actually potential upside here in terms of outputs. And if you don't like the whole cave man thing, I think this points towards at the very least putting some sort of line in your Claude.md that says, "Be concise. No filler. Straight to the point. Use less words. Because clearly there's an advantage to that, not just in tokens, like we saw, potentially the actual answers it gives us. So, that's where I'm going to leave you guys for today. What looked like on the surface to be just like a complete meme project, Caveman Claude, actually has some weight to it, some actual, you know, scientific rigor behind the why, which I think actually makes this something worth worth actually implementing. So, as always, let me know in the comments what you thought. Make sure to check out Chase AI Plus if you want to get your hands on my Claude code masterclass. Got more updates dropping in that space in the next couple days. But besides that, I'll see you guys around.

---

## Timestamped Segments

**[0:00]** Making Claude code talk like a cave man,

**[0:02]** might not only save you tokens, it could

**[0:05]** actually improve your performance as

**[0:06]** well. Now, on the surface, this sounds

**[0:08]** like a complete meme. We have a GitHub

**[0:10]** repo called cave man that's gotten 5,000

**[0:13]** stars in 72 hours, and all it does is

**[0:16]** force Claude code to talk like a

**[0:18]** Neanderthal. It trims out all the

**[0:20]** filler. The idea is that by making it

**[0:23]** more concise, we save a ton of tokens in

**[0:26]** the process. But buried in this repo is

**[0:28]** a link to this research paper that just

**[0:30]** came out a few weeks ago, which tells us

**[0:33]** if we force our large language models to

**[0:34]** be more concise, we not only save

**[0:36]** tokens, but we can dramatically improve

**[0:39]** their performance. So, today I'm going

**[0:40]** to break down this entire cave man

**[0:42]** skill. I'm going to explain what it

**[0:44]** actually buys you, because the numbers

**[0:45]** in the repo are a little misleading, and

**[0:48]** we're going to talk through this

**[0:48]** research paper so you can understand

**[0:51]** what this actually means for you. So,

**[0:53]** this is cave man, our why say many word

**[0:56]** when few word do trick repo.

**[0:59]** Now, right off the bat, what is it

**[1:01]** doing? Pretty simple, cutting out the

**[1:03]** filler. Claude code now talks like a

**[1:06]** cave man. It gives us some before and

**[1:08]** after examples, shows us the token

**[1:10]** difference, and even has a full

**[1:12]** benchmark list showing the task it gave

**[1:15]** Claude code, explain react render bug,

**[1:17]** the normal tokens being used, the cave

**[1:19]** man tokens, and the amount saved. Now,

**[1:21]** the numbers put forth in this repo are

**[1:22]** kind of insane.

**[1:23]** So, they are claiming that with the

**[1:25]** skill, we are going to cut 75% of output

**[1:29]** tokens while keeping full technical

**[1:30]** accuracy. This cave man does not change

**[1:33]** how Claude code reasons under the hood.

**[1:35]** It doesn't change how it actually

**[1:36]** generates code. None of that gets

**[1:38]** changed. It's just the output, what you

**[1:40]** see as a response. It also includes a

**[1:42]** companion tool that compresses your

**[1:44]** memory files, think Claude.md into cave

**[1:46]** man speak, and that is supposed to

**[1:49]** reduce our input tokens by 45% every

**[1:51]** session.

**[1:52]** Now, let's be clear. You are not cutting

**[1:55]** 75% of your output tokens at large and

**[1:57]** 45% of your input tokens at large at

**[1:59]** all. That is completely not true. Even

**[2:01]** though we can see these things that say,

**[2:02]** "Hey, it saves 87% of tokens on how it

**[2:05]** explains a react render bug." The prompt

**[2:08]** you get back from Claude code, the

**[2:10]** response itself, the text, is just a

**[2:12]** small portion of the output tokens at

**[2:15]** large. Just like the memory files, like

**[2:17]** Claude.md, is just a small portion of

**[2:20]** the input at large. So, let's be very

**[2:22]** clear about what this is actually buying

**[2:24]** us on a token scale. You are not saving

**[2:25]** 80% of your total tokens. And to make it

**[2:27]** a little more clear, let's break down

**[2:29]** your average 100,000 token Claude code

**[2:31]** session. Now, I understand every session

**[2:34]** is a little different, but just work

**[2:36]** with me here. We have a 100,000 token

**[2:38]** session, and it's broken up into two

**[2:39]** parts, the input, which is the lion's

**[2:42]** share, that's 75,000 tokens, and the

**[2:44]** output, which is 25%. Now, cave man is

**[2:48]** claiming we're going to reduce output by

**[2:50]** 75%. That is not true. If we take a look

**[2:53]** at output, it's really in three parts,

**[2:56]** right? We have tool calls taking up a

**[2:58]** portion of it, code blocks like the

**[2:59]** actual code generation taking a portion

**[3:01]** of it, and then the actual prose

**[3:03]** responses. This response, that text

**[3:06]** response in the terminal, that's what

**[3:09]** cave man is adjusting. That's what it's

**[3:10]** reducing. It can reduce 75% of that. You

**[3:13]** know, if we go down here, we can see,

**[3:15]** okay, so normally the prose takes up 6K

**[3:18]** tokens, with cave man we save 4,000

**[3:21]** tokens. So, we get a 4% reduction.

**[3:23]** That's still really good.

**[3:25]** If we're saving 4% of our total tokens

**[3:28]** over the course of the week, that

**[3:29]** certainly adds up, especially in the

**[3:30]** current environment where we are all so

**[3:32]** conscious of our usage. But understand,

**[3:34]** this is not 87%. It's 70%, 60% of one

**[3:39]** portion of one portion of the total

**[3:42]** session.

**[3:43]** Furthermore, if you look at the inputs,

**[3:45]** and it talks about the cave man

**[3:47]** compression saving 45%, again, not

**[3:50]** really. We're talking about the system

**[3:51]** prompt area, and only certain parts of

**[3:54]** the system prompt. So, total here,

**[3:56]** right? We're saving what? Maybe 1,000

**[3:58]** tokens, maybe 2,000 tokens. And over the

**[4:01]** course, again, of an entire session, if

**[4:03]** I save 5,000 tokens, 5% of every

**[4:05]** session, that's great. Good stuff. But

**[4:08]** it's not

**[4:09]** these gaudy numbers. So, understand that

**[4:12]** going in. This is an on the margin play.

**[4:14]** This isn't totally You're not going to

**[4:16]** be able to go from basically 5x max plan

**[4:18]** to 20x max plan because we're saving

**[4:20]** 75%. No, no, no, no. But there's still

**[4:23]** tons of value to be added here, and even

**[4:24]** more value to be extracted once we take

**[4:27]** a look at the study. It's kind of buried

**[4:29]** in here. There's There's one little

**[4:30]** section dedicated to it. But this is a

**[4:32]** study called brevity constraints reverse

**[4:34]** performance hierarchies in language

**[4:36]** models, and this came out in early March

**[4:38]** of this year. So, I'll put a link to the

**[4:39]** study down in the description if you

**[4:41]** want to check it out. But let's just

**[4:42]** talk about it really quick, because this

**[4:44]** is really interesting. Because the idea

**[4:46]** and the expectation is

**[4:48]** bigger model better than smaller model,

**[4:51]** always.

**[4:53]** Well, not exactly, not according to this

**[4:55]** study. So, in this study, they evaluated

**[4:58]** 31 models across 1,500 problems, and

**[5:02]** they identified the mechanism as

**[5:04]** spontaneous scale dependent verbosity

**[5:07]** that introduces errors through over

**[5:08]** elaboration. What the heck does that

**[5:10]** mean? That means on nearly 8% of the

**[5:14]** problems across these 1,500 problems and

**[5:16]** 31 models, the larger language models,

**[5:19]** the ones with more parameters,

**[5:21]** underperformed smaller ones by 28

**[5:24]** percentage points despite 100 times more

**[5:27]** parameters in some cases. So, you had

**[5:29]** scenarios where, again, this is with all

**[5:31]** open weight models, you had a 2 billion

**[5:34]** parameter model outperforming a 400

**[5:36]** billion parameter model.

**[5:39]** And this happened multiple times. This

**[5:41]** is crazy. Why is this? Well,

**[5:44]** they

**[5:45]** propose it that the reason why is

**[5:47]** because these large language models talk

**[5:50]** too damn much. They are over verbose to

**[5:53]** the point that they pretty much spin

**[5:54]** themselves into circles and get the

**[5:56]** wrong answer because of it. And in the

**[5:58]** study, they found that by constraining

**[6:00]** large models to produce brief responses,

**[6:02]** cave man responses, improves accuracy by

**[6:05]** 26 percentage points and reduces

**[6:07]** performance gaps by up to 2/3. And in

**[6:09]** many cases, by forcing these large

**[6:11]** language models to become more concise,

**[6:14]** more cave man like, switched that

**[6:16]** dynamic to where before they were losing

**[6:19]** to some of these smaller models, and now

**[6:20]** they were defeating them.

**[6:22]** That's kind of wild, especially in

**[6:23]** context of this GitHub repo. Now,

**[6:26]** obviously, these are open weight models.

**[6:27]** This isn't Opus 4.6. This isn't Codex

**[6:29]** 5.4. Do these frontier models exhibit

**[6:32]** this exact same sort of behavior? We

**[6:34]** don't necessarily know for sure, but if

**[6:36]** you've seen any of these studies, you

**[6:38]** understand usually what you see here

**[6:41]** tends to be repeated on some level with

**[6:43]** the frontier models. Maybe it's not this

**[6:45]** extreme, but there's probably something

**[6:47]** to it. Now, the rest of the study goes

**[6:48]** into a lot of detail about how they run

**[6:50]** the tests, how they're trying to break

**[6:52]** out correlation versus causation, and

**[6:54]** why they think this is a problem. And

**[6:56]** like I said before, they hypothesize

**[6:58]** that large models generate excessively

**[7:00]** verbose responses that obscure correct

**[7:02]** reasoning, a phenomenon they termed

**[7:05]** overthinking. It's just trying to put

**[7:06]** too much out there. Instead of just

**[7:08]** giving you the answer and getting out of

**[7:09]** its own way, it talks itself into the

**[7:11]** wrong answer, literally. And they

**[7:13]** specifically say the learned tendency

**[7:16]** towards thoroughness becomes

**[7:17]** counterproductive

**[7:19]** introducing error accumulation. Brevity

**[7:21]** constraints help large models

**[7:23]** dramatically while barely affecting the

**[7:25]** smaller models. And an obvious question

**[7:27]** you should have is, well, why why is

**[7:28]** this even the case? Why are these larger

**[7:30]** models having this issue? They point

**[7:32]** towards reinforcement learning. So, when

**[7:35]** you train a new model, so imagine Opus

**[7:37]** 5.0 is in the process of being trained,

**[7:40]** part of what they do is reinforcement

**[7:42]** learning. Now, I don't know if Anthropic

**[7:43]** does it specifically, but this is how

**[7:44]** it's done for many models. Essentially,

**[7:46]** they take the new model and they bring

**[7:48]** in a human to grade its answers. They

**[7:50]** show multiple answers and says, "I like

**[7:53]** this one more than this one." And

**[7:54]** they're saying in the study, chances are

**[7:56]** humans tend to like more verbose

**[7:59]** answers, more thorough answers, and

**[8:00]** because of that, these larger models are

**[8:02]** essentially trained to be more verbose

**[8:05]** rather than concise and even correct in

**[8:07]** some instances. But the big takeaway

**[8:09]** here is this, is that brevity

**[8:10]** constraints completely reversed the

**[8:12]** performance hierarchies. So, where they

**[8:13]** were losing before, now they were

**[8:15]** winning simply by telling them to be

**[8:17]** more concise. They didn't change how

**[8:18]** they thought, they didn't change

**[8:19]** anything under the hood, they just said,

**[8:22]** "Be a cave man." Now, they weren't

**[8:23]** literally using this GitHub, but same

**[8:26]** exact thing. So, this is why I think

**[8:29]** this is actually kind of interesting,

**[8:31]** not just a complete meme. You know,

**[8:32]** beyond the fact that there are some

**[8:34]** token,

**[8:35]** you know, positives here. Saving 5% of

**[8:37]** tokens is nothing to laugh at,

**[8:39]** especially if you are not on a max 20

**[8:41]** plan. But if there's a potential

**[8:42]** scenario where we're actually getting

**[8:43]** better outputs because of it, especially

**[8:45]** on more straightforward questions,

**[8:47]** because if you dive into that study, it

**[8:49]** kind of breaks out like which questions

**[8:51]** they kind of had this issue with in this

**[8:53]** dynamic.

**[8:55]** It's interesting, very interesting,

**[8:57]** which is why I think this is kind of

**[8:58]** worth looking at. And it's also super

**[8:59]** simple to use. It's just a set of

**[9:01]** skills. Installing this literally is one

**[9:04]** line, and then running it, we either

**[9:06]** invoke it with {slash} cave man, or just

**[9:08]** say something like talk like a cave man,

**[9:10]** cave man mode, or less tokens, please.

**[9:12]** There's also levels to it, so we can go

**[9:14]** like ultra cave man, right? We like just

**[9:16]** came out of the ocean, we barely can

**[9:18]** stand up straight, and then we have full

**[9:21]** and light. So, you can get different

**[9:22]** levels of cave man throughout the years.

**[9:24]** And it isn't a blanket thing either.

**[9:26]** Things like error messages are quoted

**[9:28]** exactly, and again, anything to do with

**[9:30]** code, anything to do with generation,

**[9:31]** anything under the hood, stays the same.

**[9:33]** We're not changing how it really thinks.

**[9:35]** So, overall, I think this is worth

**[9:36]** trying out. It's a single skill, it

**[9:38]** saves tokens, and there's no real

**[9:40]** downside, and based on the study,

**[9:42]** there's actually potential upside here

**[9:44]** in terms of outputs. And if you don't

**[9:46]** like the whole cave man thing, I think

**[9:48]** this points towards at the very least

**[9:51]** putting some sort of line in your

**[9:52]** Claude.md that says, "Be concise. No

**[9:55]** filler. Straight to the point. Use less

**[9:58]** words.

**[10:00]** Because clearly there's an advantage to

**[10:01]** that, not just in tokens, like we saw,

**[10:04]** potentially the actual answers it gives

**[10:05]** us. So, that's where I'm going to leave

**[10:06]** you guys for today. What looked like on

**[10:08]** the surface to be just like a complete

**[10:10]** meme project, Caveman Claude,

**[10:13]** actually has some weight to it, some

**[10:14]** actual, you know, scientific rigor

**[10:16]** behind the why, which I think actually

**[10:18]** makes this something worth worth

**[10:20]** actually implementing. So, as always,

**[10:23]** let me know in the comments what you

**[10:24]** thought. Make sure to check out Chase AI

**[10:26]** Plus if you want to get your hands on my

**[10:28]** Claude code masterclass. Got more

**[10:29]** updates dropping in that space in the

**[10:32]** next couple days.

**[10:33]** But besides that, I'll see you guys

**[10:35]** around.
