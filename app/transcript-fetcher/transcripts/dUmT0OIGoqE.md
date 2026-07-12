# Transcript: dUmT0OIGoqE

**URL:** https://www.youtube.com/watch?v=dUmT0OIGoqE
**Segments:** 160

---

## Full Text

The number of AI agents on the internet is increasing at such an insane rate. I don't think I've seen anything like this. This is crazy. And this is an area that is quite new, and the technology is still pretty rough. Improving rapidly, but pretty rough. And the promise of agents is incredible. It would book the cheapest plane ticket for you, or run 24 hours a day to manage your schedule, submit insurance claims, continuously scan a codebase for vulnerabilities and patch it. Well, this is the good, but at the same time, you get so many news headlines about spam, security issues, and system breakdowns. And it gets even tougher when you have not one agent, but multiple agents. Imagine two agents organizing a holiday for you. The flight agent hallucinates a cheaper airport 400 miles away from your real destination. Then, the hotel agent says, "Let's book something super cheap nearby." Well, super cheap is often non-refundable. And now, congratulations. You now have a non-refundable room you will never see. And so many of these problems come from the fact that agent coordination is super difficult. Now, check out what this paper says we should do. Here is a math problem. First agent writes a plan. The next one critiques it, and the third one solves the problem. And at this point, I said, "Okay. I see nothing interesting here. This is what everyone does with agents." Yes, but here's the key. Most agents communicate a bit like we do, in words. Wait a second. Why should we do that? Look at this neural interface for brain-to-text communication. Yes, this really works. You just think about a letter in the alphabet, and it magically appears. And if you keep doing this a lot, you start asking. The alphabet is optimized for writing. Why use that? Why not use one that is optimized for thinking? And what would that even look like? Hint, it would look like this. We talked about this 500 videos ago, paper in the description. Now, if you look at the agents, the first one does some work, packs it up, and passes it to the next one. So do the second and the third ones. Every [clears throat] time an agent wants to communicate something, it has to write out full sentences, decode tokens one by one, and the next guy has to read and re-encode the whole thing. Why are we doing that? Who said they should talk in plain English? And this is the part where I fell off the chair. Now, hold on to your papers, fellow scholars, because this work says, "Huh, forget English. You know what? Forget letters entirely." It says, "Instead, let's link up their brains." Kind of. Instead of using English words, they pass raw undecoded numbers directly to the next agent. Send raw brain signals, if you will. Call it cross-agent latent state transfer. So, the theory is that these three agents can work together round one, round two, and round three much cheaper than the text-based agents. They refine an answer, and you get better answers with the same amount of computation. So, is it better? Hmm, let's see. Dear fellow scholars, this is Two Minute Papers with Dr. Károly Zsolnai Fehér. Well, when given competition-level math questions, it goes from 73% to 86%. That is crazy. We are talking free sub-10 billion parameter models, not expensive frontier systems. And here is where it gets the Michelin star status. Look at that. Ooh. Token usage down 75%. They all evaporated into the latent space. Loving it. So, this can improve smaller systems to be in striking distance of much bigger, more expensive models on difficult math problems. So, I bet it costs a fortune to train, right? Well, look at that. Four bucks. Basically, you spend your coffee money on these agents and in return they punch a hole in space-time. Love it. Additionally, it might even unlock Wait, wait, wait. I shouldn't say unlock. That's AI speak. So, it might give us a new scaling law. More rounds, better results. And at this point, I thought we might have a deadly flaw here. And it's really subtle. So, the training for each agent's role is written by a giant AI model. So, if they perform well, you have to ask, are things better because of the brain linking or is it good distillation from an excellent teacher? So, which one is it? A good teacher or a good architecture? Well, fellow scholars, we are in luck. This is a really good paper. So, the scientists thought about this too. And look, goodness, a controlled comparison gives the same teacher to other architectures and this one. And the new one still outperforms. So, yes, the brain linking really works. What a time to be alive. Okay, now, let's not get too excited. This is two-minute papers and we respect the science here. Limitations. One, tests were on smaller models. We don't yet know how these insights scale up to bigger ones. If they don't, then this puts small models on steroids. Still good. If yes, potential huge game-changer. Two, there is an optimal latent thought length, and that is about 80 steps. This is somewhat of a limit on how much thinking an agent can do per round. >> [clears throat] >> I am thinking, you know, if it solves a mathematical Olympiad problems already, how bad can that be? And sure enough, after 80, you don't get a lot of value anyway, but I wanted to mention it. Okay? So, code and models are available for free. Note that this is still very rough, very early, but it shows potential. And this is still research. Please do not think you just plug this in and everything will fly immediately. We need new tools for the era of LLMs, and Weights & Biases now has Weave, a lightweight toolkit to confidently iterate on LLM applications. Use traces to debug how data flows through each step of your app, and use evaluations to measure your progress. It is the best. Try it out now at wnb.me/papers, or click the link in the description below.

---

## Timestamped Segments

**[0:00]** The number of AI agents on the internet

**[0:02]** is increasing at such an insane rate. I

**[0:06]** don't think I've seen anything like

**[0:07]** this. This is crazy. And this is an area

**[0:10]** that is quite new, and the technology is

**[0:12]** still pretty rough. Improving rapidly,

**[0:15]** but pretty rough. And the promise of

**[0:17]** agents is incredible. It would book the

**[0:19]** cheapest plane ticket for you, or run 24

**[0:22]** hours a day to manage your schedule,

**[0:24]** submit insurance claims, continuously

**[0:27]** scan a codebase for vulnerabilities and

**[0:29]** patch it. Well, this is the good, but at

**[0:31]** the same time, you get so many news

**[0:34]** headlines about spam, security issues,

**[0:36]** and system breakdowns. And it gets even

**[0:39]** tougher when you have not one agent, but

**[0:42]** multiple agents. Imagine two agents

**[0:45]** organizing a holiday for you. The flight

**[0:47]** agent hallucinates a cheaper airport 400

**[0:51]** miles away from your real destination.

**[0:53]** Then, the hotel agent says, "Let's book

**[0:56]** something super cheap nearby." Well,

**[0:59]** super cheap is often non-refundable. And

**[1:02]** now, congratulations.

**[1:04]** You now have a non-refundable room you

**[1:07]** will never see.

**[1:09]** And so many of these problems come from

**[1:11]** the fact that agent coordination is

**[1:13]** super difficult. Now, check out what

**[1:16]** this paper says we should do. Here is a

**[1:18]** math problem. First agent writes a plan.

**[1:21]** The next one critiques it, and the third

**[1:24]** one solves the problem. And at this

**[1:26]** point, I said, "Okay.

**[1:28]** I see nothing interesting here. This is

**[1:31]** what everyone does with agents." Yes,

**[1:34]** but here's the key. Most agents

**[1:36]** communicate a bit like we do, in words.

**[1:40]** Wait a second. Why should we do that?

**[1:42]** Look at this neural interface for

**[1:45]** brain-to-text communication. Yes, this

**[1:48]** really works. You just think about a

**[1:50]** letter in the alphabet, and it magically

**[1:53]** appears. And if you keep doing this a

**[1:55]** lot, you start asking. The alphabet is

**[1:58]** optimized for writing.

**[2:00]** Why use that? Why not use one that is

**[2:03]** optimized for thinking? And what would

**[2:05]** that even look like? Hint, it would look

**[2:08]** like this. We talked about this 500

**[2:10]** videos ago, paper in the description.

**[2:13]** Now, if you look at the agents, the

**[2:15]** first one does some work, packs it up,

**[2:17]** and passes it to the next one. So do the

**[2:20]** second and the third ones. Every

**[2:22]** [clears throat] time an agent wants to

**[2:24]** communicate something, it has to write

**[2:26]** out full sentences, decode tokens one by

**[2:30]** one, and the next guy has to read and

**[2:33]** re-encode the whole thing.

**[2:36]** Why are we doing that? Who said they

**[2:38]** should talk in plain English? And this

**[2:41]** is the part where I fell off the chair.

**[2:43]** Now, hold on to your papers, fellow

**[2:44]** scholars, because this work says, "Huh,

**[2:47]** forget English. You know what? Forget

**[2:49]** letters entirely." It says, "Instead,

**[2:52]** let's link up their brains." Kind of.

**[2:56]** Instead of using English words, they

**[2:58]** pass raw undecoded numbers directly to

**[3:01]** the next agent. Send raw brain signals,

**[3:04]** if you will. Call it cross-agent latent

**[3:07]** state transfer. So, the theory is that

**[3:10]** these three agents can work together

**[3:12]** round one, round two, and round three

**[3:15]** much cheaper than the text-based agents.

**[3:18]** They refine an answer, and you get

**[3:20]** better answers with the same amount of

**[3:22]** computation. So, is it better? Hmm,

**[3:26]** let's see. Dear fellow scholars, this is

**[3:28]** Two Minute Papers with Dr. Károly

**[3:30]** Zsolnai Fehér. Well, when given

**[3:32]** competition-level math questions, it

**[3:34]** goes from 73% to 86%.

**[3:38]** That is crazy.

**[3:40]** We are talking free sub-10 billion

**[3:42]** parameter models, not expensive frontier

**[3:45]** systems. And here is where it gets the

**[3:48]** Michelin star status. Look at that.

**[3:52]** Ooh.

**[3:53]** Token usage down 75%.

**[3:57]** They all evaporated into the latent

**[4:00]** space. Loving it. So, this can improve

**[4:03]** smaller systems to be in striking

**[4:05]** distance of much bigger, more expensive

**[4:08]** models on difficult math problems. So, I

**[4:11]** bet it costs a fortune to train, right?

**[4:14]** Well, look at that.

**[4:17]** Four bucks. Basically, you spend your

**[4:19]** coffee money on these agents and in

**[4:21]** return they punch a hole in space-time.

**[4:25]** Love it. Additionally, it might even

**[4:27]** unlock Wait, wait, wait. I shouldn't say

**[4:30]** unlock. That's AI speak. So, it might

**[4:33]** give us a new scaling law. More rounds,

**[4:37]** better results. And at this point, I

**[4:39]** thought we might have a deadly flaw

**[4:41]** here. And it's really subtle. So, the

**[4:44]** training for each agent's role is

**[4:47]** written by a giant AI model. So, if they

**[4:50]** perform well, you have to ask, are

**[4:53]** things better because of the brain

**[4:55]** linking or is it good distillation from

**[4:58]** an excellent teacher? So, which one is

**[5:01]** it? A good teacher or a good

**[5:03]** architecture? Well, fellow scholars, we

**[5:06]** are in luck. This is a really good

**[5:08]** paper. So, the scientists thought about

**[5:11]** this too. And look, goodness, a

**[5:14]** controlled comparison gives the same

**[5:16]** teacher to other architectures and this

**[5:19]** one. And the new one still outperforms.

**[5:22]** So, yes, the brain linking really works.

**[5:26]** What a time to be alive. Okay, now,

**[5:29]** let's not get too excited. This is

**[5:31]** two-minute papers and we respect the

**[5:33]** science here. Limitations. One, tests

**[5:36]** were on smaller models. We don't yet

**[5:39]** know how these insights scale up to

**[5:41]** bigger ones. If they don't, then this

**[5:44]** puts small models on steroids.

**[5:47]** Still good. If yes, potential huge

**[5:50]** game-changer. Two, there is an optimal

**[5:52]** latent thought length, and that is about

**[5:55]** 80 steps. This is somewhat of a limit on

**[5:58]** how much thinking an agent can do per

**[6:01]** round.

**[6:02]** >> [clears throat]

**[6:02]** >> I am thinking, you know, if it solves a

**[6:04]** mathematical Olympiad problems already,

**[6:07]** how bad can that be? And sure enough,

**[6:10]** after 80, you don't get a lot of value

**[6:12]** anyway, but I wanted to mention it.

**[6:14]** Okay? So, code and models are available

**[6:17]** for free. Note that this is still very

**[6:20]** rough, very early, but it shows

**[6:22]** potential. And this is still research.

**[6:25]** Please do not think you just plug this

**[6:27]** in and everything will fly immediately.

**[6:30]** We need new tools for the era of LLMs,

**[6:33]** and Weights & Biases now has Weave, a

**[6:36]** lightweight toolkit to confidently

**[6:38]** iterate on LLM applications. Use traces

**[6:41]** to debug how data flows through each

**[6:43]** step of your app, and use evaluations to

**[6:46]** measure your progress. It is the best.

**[6:49]** Try it out now at wnb.me/papers,

**[6:53]** or click the link in the description

**[6:55]** below.
