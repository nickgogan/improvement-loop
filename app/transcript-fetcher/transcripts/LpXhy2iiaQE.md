# Transcript: DeepSeek’s New AI Is A Game Changer

**URL:** https://www.youtube.com/watch?v=LpXhy2iiaQE
**Segments:** 176
**Channel:** Two Minute Papers
**Duration:** 7:43
**Uploaded:** 2026-05-22

---

## Full Text

Hmm, why does this deep sea quirk exist? I mean, it adds vision capabilities to the deep sea AI system, but that's not new. A lot of other AI systems have vision capabilities. You just drop an image here and it works. Even video and even for open models. So, why do we need this paper? Well, they did something incredible here and it is an absolute game changer. Why? You see, if you ask a previous technique to count the number of people in this photo, it will think something like this. Okay, there are people on the upper left and a bunch of stripy guys in two rows. That is kind of three rows. Some of them are standing, some of them are sitting. Ah, it's just so confusing to just count them up using only words. Two problems with this one. One, this is prone to error. Two, you have to think a lot. Just describing stuff. Why? What would we, humans, do? Of course, we would use our finger and would point at the image. One, two, three, and so on. Done. Don't describe images like a poet. Point like a human. Now, that is exactly what this new technique does. It allows an AI system to point at things while thinking and it is absolutely brilliant. This makes it more accurate and it also makes it faster. In a world where hardware and tokens cost a fortune, it is fantastic to have something that gives us results faster and cheaper. But, it turns out thinking with visual primitives has even more advantages. It can also do topological reasoning. For instance, if you give it a maze with a start and end point, you not only get a correct answer to your questions, but you can also trace back the whole thought process visually. I love that. Also, here you can ask where the crown connects and look. To the octopus. Yeah, it answers correctly, but you can also see how it came to that conclusion. Now, make no mistake. These are simple examples. I'll show you in a moment if it is as good as these billion-dollar frontier models. Also, if something goes wrong, this will make it easier to find mistakes and fix them to create an even better model. This puts us one step closer to AI systems we can actually understand that do not just give us a soup of numbers. So good. So, how good is it? Well, hold on to your papers, fellow scholars, and I dropped my papers here. Look, it needs about 90% fewer visual tokens than most frontier models. Now, wait, wait, wait. It doesn't matter how little you think if you just say three as an answer without thinking. Thinking time doesn't matter if it is incorrect. So, how accurate is it? Are you kidding me? This free system matches or beats almost everything. And once again, we are talking about this, which is free, going up against billion-dollar systems here. Wow. Now, we are fellow scholars here, so at this point we ask, are these results real? You know, benchmarks are being gamed left and right. Now, here is what many people missed. Average over seven benchmarks, but in-house benchmarks excluded. That is the key. They did not rig their own benchmarks. You know why? Well, everyone loves it because it's one of the oldest tricks in the book. If you are not performing well, just create a new benchmark that fits you. Let's make a YUNUS benchmark. You will always be world first in being you. And this is not the case here. Amazing. This is free and open research. So, this technique can potentially be added to many existing models, including free ones. This paper does not have a model attached that I know of. It describes the concept of how to do it in detail. It's a blueprint, if you will. More intelligence for all of us for free. The world needs more papers like this. Love it. But, this all sounds like magic. How did they do this? Well, look, this is their own policy distillation objective. We need exactly this. You see, normally, we have a bunch of expert AI models. Now, at the risk of simplifying things, imagine that one of these guys is great at boxes. Nobody does boxes better than this guy. The other one is great at tracing mazes with points. But, that's not what we want. What we want is one AI that can do all of these things. And that is where this comes into play. We train a student model that learns from all of these teachers. It says what it would try to do, then the teachers say, "Okay, here's what I would have done." Do this enough and the student will be pretty good at all of these different kinds of visual thinking. This is why they used the name distilling the knowledge of a bunch of expert teachers into a student. So, where does this put us? Okay, so here's what I think. Dear fellow scholars, this is Two Minute Papers with Dr. Károly Zsolnai-Fehér. You know, we always thought that we would make AI systems smarter by giving it higher resolution images to train on. More pixels, more smarts. It turns out not true. Sometimes, that's not what we need at all. Deep Seek just cut down those visual tokens by 90% and still beat frontier models. Less is more. Now, is this perfect? All problems solved? No. Limitations. One, the AI does not automatically do this kind of pointy thinking. It needs a word as a cue for this kind of thinking. Two, bounding boxes are nice for people, but if you are counting blades of grass or strands of hair, now, in this case, not having those in very high resolution is a problem. >> [laughter] >> Yep, once again, the two-minute papers special, thin structures. Every time, man. It's so painful. And three, this kind of topological reasoning does not generalize as well as we'd like. It might not be as robust when you show it something completely new. So, careful with the misleading media headlines, careful with the hype everywhere. There is still plenty to improve here. But, I feel that this might be a breakthrough. And that makes it maybe the third one this month in AI research. What a time to be alive. Also, with large AI companies going to IPO, they are about to become ventures that look to maximize their profits. More money needed every quarter. So, it's going to become more and more crucial to own your own AI systems with free open weights models. And this one makes them better. Love it. Here you see me running the full DeepSeek AI model through Lambda GPU Cloud. 671 billion parameters running super fast and super reliably. This is insane. I love it and I use it on a regular basis. Lambda provides you with powerful Nvidia GPUs to run your own chatbots and experiments. Seriously, try it out now at lambda.ai/papers or click the link in the description.

---

## Timestamped Segments

**[0:00]** Hmm, why does this deep sea quirk exist?

**[0:02]** I mean, it adds vision capabilities to

**[0:05]** the deep sea AI system, but that's not

**[0:07]** new. A lot of other AI systems have

**[0:10]** vision capabilities. You just drop an

**[0:12]** image here and it works. Even video and

**[0:15]** even for open models. So, why do we need

**[0:18]** this paper? Well, they did something

**[0:21]** incredible here and it is an absolute

**[0:24]** game changer. Why? You see, if you ask a

**[0:27]** previous technique to count the number

**[0:29]** of people in this photo, it will think

**[0:32]** something like this. Okay, there are

**[0:34]** people on the upper left and a bunch of

**[0:36]** stripy guys in two rows. That is kind of

**[0:40]** three rows. Some of them are standing,

**[0:42]** some of them are sitting.

**[0:44]** Ah, it's just so confusing to just count

**[0:46]** them up using only words. Two problems

**[0:49]** with this one. One, this is prone to

**[0:51]** error. Two, you have to think a lot.

**[0:55]** Just describing stuff. Why? What would

**[0:58]** we, humans, do? Of course, we would use

**[1:01]** our finger and would point at the image.

**[1:04]** One, two, three, and so on.

**[1:07]** Done. Don't describe images like a poet.

**[1:10]** Point like a human. Now, that is exactly

**[1:13]** what this new technique does. It allows

**[1:16]** an AI system to point at things while

**[1:19]** thinking and it is absolutely brilliant.

**[1:22]** This makes it more accurate and it also

**[1:25]** makes it faster. In a world where

**[1:27]** hardware and tokens cost a fortune, it

**[1:30]** is fantastic to have something that

**[1:33]** gives us results faster and cheaper.

**[1:35]** But, it turns out thinking with visual

**[1:38]** primitives has even more advantages. It

**[1:41]** can also do topological reasoning. For

**[1:43]** instance, if you give it a maze with a

**[1:46]** start and end point, you not only get a

**[1:49]** correct answer to your questions, but

**[1:51]** you can also trace back the whole

**[1:54]** thought process visually.

**[1:56]** I love that. Also, here you can ask

**[1:59]** where the crown connects and look.

**[2:02]** To the octopus. Yeah, it answers

**[2:05]** correctly, but you can also see how it

**[2:08]** came to that conclusion. Now, make no

**[2:11]** mistake. These are simple examples. I'll

**[2:14]** show you in a moment if it is as good as

**[2:16]** these billion-dollar frontier models.

**[2:19]** Also, if something goes wrong, this will

**[2:21]** make it easier to find mistakes and fix

**[2:24]** them to create an even better model.

**[2:26]** This puts us one step closer to AI

**[2:29]** systems we can actually understand that

**[2:32]** do not just give us a soup of numbers.

**[2:34]** So good. So, how good is it? Well, hold

**[2:38]** on to your papers, fellow scholars, and

**[2:41]** I dropped my papers here. Look, it needs

**[2:43]** about 90% fewer visual tokens than most

**[2:47]** frontier models. Now, wait, wait, wait.

**[2:50]** It doesn't matter how little you think

**[2:52]** if you just say three as an answer

**[2:55]** without thinking. Thinking time doesn't

**[2:57]** matter if it is incorrect. So, how

**[3:00]** accurate is it?

**[3:02]** Are you kidding me? This free system

**[3:04]** matches or beats almost everything. And

**[3:08]** once again, we are talking about this,

**[3:10]** which is free, going up against

**[3:12]** billion-dollar systems here. Wow. Now,

**[3:16]** we are fellow scholars here, so at this

**[3:18]** point we ask, are these results real?

**[3:21]** You know, benchmarks are being gamed

**[3:23]** left and right. Now, here is what many

**[3:26]** people missed. Average over seven

**[3:29]** benchmarks, but in-house benchmarks

**[3:31]** excluded.

**[3:33]** That is the key. They did not rig their

**[3:35]** own benchmarks. You know why? Well,

**[3:38]** everyone loves it because it's one of

**[3:40]** the oldest tricks in the book. If you

**[3:42]** are not performing well, just create a

**[3:45]** new benchmark that fits you. Let's make

**[3:47]** a YUNUS benchmark. You will always be

**[3:50]** world first in being you. And this is

**[3:53]** not the case here. Amazing. This is free

**[3:56]** and open research. So, this technique

**[3:58]** can potentially be added to many

**[4:00]** existing models, including free ones.

**[4:03]** This paper does not have a model

**[4:05]** attached that I know of. It describes

**[4:07]** the concept of how to do it in detail.

**[4:10]** It's a blueprint, if you will. More

**[4:12]** intelligence for all of us for free.

**[4:16]** The world needs more papers like this.

**[4:18]** Love it. But, this all sounds like

**[4:21]** magic. How did they do this? Well, look,

**[4:23]** this is their own policy distillation

**[4:26]** objective. We need exactly this. You

**[4:29]** see, normally, we have a bunch of expert

**[4:32]** AI models. Now, at the risk of

**[4:34]** simplifying things, imagine that one of

**[4:37]** these guys is great at boxes. Nobody

**[4:40]** does boxes better than this guy. The

**[4:42]** other one is great at tracing mazes with

**[4:45]** points. But, that's not what we want.

**[4:48]** What we want is one AI that can do all

**[4:51]** of these things. And that is where this

**[4:53]** comes into play. We train a student

**[4:56]** model that learns from all of these

**[4:58]** teachers. It says what it would try to

**[5:01]** do, then the teachers say, "Okay, here's

**[5:04]** what I would have done." Do this enough

**[5:06]** and the student will be pretty good at

**[5:09]** all of these different kinds of visual

**[5:11]** thinking. This is why they used the name

**[5:13]** distilling the knowledge of a bunch of

**[5:15]** expert teachers into a student. So,

**[5:19]** where does this put us? Okay, so here's

**[5:21]** what I think. Dear fellow scholars, this

**[5:23]** is Two Minute Papers with Dr. Károly

**[5:25]** Zsolnai-Fehér. You know, we always

**[5:27]** thought that we would make AI systems

**[5:29]** smarter by giving it higher resolution

**[5:32]** images to train on. More pixels, more

**[5:34]** smarts. It turns out not true.

**[5:37]** Sometimes, that's not what we need at

**[5:39]** all. Deep Seek just cut down those

**[5:42]** visual tokens by 90% and still beat

**[5:45]** frontier models. Less is more. Now, is

**[5:48]** this perfect? All problems solved? No.

**[5:52]** Limitations. One, the AI does not

**[5:55]** automatically do this kind of pointy

**[5:57]** thinking. It needs a word as a cue for

**[6:00]** this kind of thinking. Two, bounding

**[6:03]** boxes are nice for people, but if you

**[6:05]** are counting blades of grass or strands

**[6:08]** of hair, now, in this case, not having

**[6:11]** those in very high resolution is a

**[6:13]** problem.

**[6:15]** >> [laughter]

**[6:15]** >> Yep, once again, the two-minute papers

**[6:18]** special, thin structures. Every time,

**[6:22]** man. It's so painful. And three, this

**[6:25]** kind of topological reasoning does not

**[6:27]** generalize as well as we'd like. It

**[6:30]** might not be as robust when you show it

**[6:32]** something completely new. So, careful

**[6:35]** with the misleading media headlines,

**[6:37]** careful with the hype everywhere. There

**[6:39]** is still plenty to improve here. But, I

**[6:42]** feel that this might be a breakthrough.

**[6:44]** And that makes it

**[6:46]** maybe the third one this month in AI

**[6:48]** research. What a time to be alive. Also,

**[6:52]** with large AI companies going to IPO,

**[6:55]** they are about to become ventures that

**[6:57]** look to maximize their profits. More

**[6:59]** money needed every quarter. So, it's

**[7:02]** going to become more and more crucial to

**[7:05]** own your own AI systems with free open

**[7:07]** weights models. And this one makes them

**[7:10]** better.

**[7:11]** Love it. Here you see me running the

**[7:13]** full DeepSeek AI model through Lambda

**[7:16]** GPU Cloud. 671

**[7:20]** billion parameters running super fast

**[7:22]** and super reliably. This is insane. I

**[7:26]** love it and I use it on a regular basis.

**[7:29]** Lambda provides you with powerful Nvidia

**[7:32]** GPUs to run your own chatbots and

**[7:35]** experiments. Seriously, try it out now

**[7:37]** at lambda.ai/papers

**[7:40]** or click the link in the description.
