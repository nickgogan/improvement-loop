# Transcript: How to Distill Claude Fable 5 Before It Goes Offline Again

**URL:** https://www.youtube.com/watch?v=qWhSFjDS3LA
**Segments:** 275
**Channel:** Cloud Codes
**Duration:** 11:10
**Uploaded:** 2026-07-05

---

## Full Text

Three days. That is how long the most powerful AI model on Earth stayed online before the United States government reached in and switched it off. Claude Fable 5. Here on a Tuesday, dark by Friday. And the people who saw it coming did something clever. They started quietly copying its brain. Anthropic shipped Fable 5 on June 9th. It's first public Mythos class model, a full tier above Opus, the sharpest thing they had ever released. 72 hours later, it was gone. The order came straight from the Commerce Department. National security, export controls. Researchers had found a jailbreak that stripped the model's safety rails and turned it into an open cyber weapon. So, Washington pulled the plug for every user outside the country overnight. Then, 3 weeks later, it came back. The controls were lifted and Fable 5 returned to Claude and Claude code. But, read the title again before it goes offline again, because a model the government switched off once can be switched off twice. So, here's the plan. While Fable 5 is live, you capture what it does, its reasoning, its every move, and you pour that into a small model that runs on your own laptop. A model nobody can take offline. This is distillation, and today we walk it end to end. It starts with a trace. When Fable 5 solves a task, it thinks out loud and then acts, runs a command, edits a file, reads the result. Capture that whole thought and action log, and you have one trace. Thousands of them become a training set. And thousands is exactly what appeared on Hugging Face. One post drops a data set called Fable Traces. Another, Fable 5 Traces. 4,600 agent sessions packaged and ready while the model was still warm. The target is a tiny open model, Qwen 3 4 billion parameters, small enough to run on a single gaming graphics card. Fine-tune it on Fable 5's traces, and you get something people already nicknamed Queebal. Claude's brain, Quinn's body. One question hangs over all of it. When you crush a frontier model into something 400 times smaller, does the intelligence actually survive the shrink? Hold that thought. The answer is not the one the hype promised. So, here's the plan for the next 12 minutes. First, the resources that make this possible. Then the research paper that explains why it really works. And finally, the exact steps to do it yourself. It began with a single post. A developer publishes the Fable traces drop, tags the base model, and within hours the repost climb. The comments are all one question. Is this really Claude running locally for free? The screenshot said yes. Open the model card, and it is refreshingly plain. Base model, QN3 4 billion instruct, precision 16-bit, format ChatML, license Apache 2, completely open. One line spins it up, vllm serve, and it answers like a shrunk-down Fable 5. The dataset behind it is small but dense. 4,600 sessions distilled from just 60 real Claude runs inside 188 megabytes, smaller than a phone photo album. Each row keeps the context, the hidden reasoning, and the exact action the model took. And look at what those actions are. 81% of the rows are tool calls, not chit-chat. The single most common move, running a bash command, shows up 1,500 times. This is not a chatbot dataset. It is a recording of an engineer at work. One team went much bigger. They pulled 2.3 million reasoning traces out of Fable 5 and compressed all of it into that same 4 billion model. 2.3 million worked examples, like handing a student every solved problem in an entire library and saying, "Learn the pattern." And it was never just one person. Half a dozen accounts raced to capture the model before it could vanish again. Raw traces, agent logs, full coding sessions, all mirrored onto Hugging Face, a frontier model quietly backed up by strangers. So, what is distillation really? Picture a teacher and a student. The teacher is Fable 5, enormous, expensive, brilliant. The student is the little model. The teacher solves problems out loud, and the student copies not just the answers, but the way it reached them. And here is the first thing to hold onto. Distillation transfers how to reason, the shape of the thinking, not new facts. You are teaching a style of solving, not stuffing in a library. That one distinction decides everything that comes next. Now, the naive way, the way most of these data sets use, you take the teacher's traces and train the student to imitate them, line by line. It sounds obvious, but there is a trap hiding in it. The student only ever sees the teacher's perfect path and never its own mistakes, which is exactly the problem a team at Thinking Machines set out to fix in a paper simply titled On Policy Distillation. It is the missing piece in almost every Fable 5 clone shipping right now. Their fix flips the whole direction. Instead of feeding the student the teacher's answers, you let the student attempt the task itself, and the teacher grades every single token it produces. Right move, high score. Wrong move, low score. The student learns from its own walk, not a stranger's. And the payoff is real. On a brutal math benchmark, on policy distillation hit 70% at 1/10 the cost of full reinforcement learning, up to 30 times cheaper than the naive method, and 7 to 10 times faster to train. Cheaper and better. Why does grading the student's own attempts matter so much? Because when the little model drifts off course, and it will, it needs to have seen that mistake and been corrected. Copying a flawless transcript never teaches recovery, only practice does. So, keep these two words apart. Off policy, imitate the teacher's transcript, cheap and fragile. On policy, practice under the teacher's eye, a little pricier and far stronger. Same traces, completely different result. But you did not come here for theory, so let us check the receipts. One engineer took the distilled Qobol, dropped it on a single graphics card, and ran it head-to-head against the plain base model it started from. Same hardware, same settings, a fair fight. The result stings. On a live tool calling test, the untouched base scored 99. Add Opus reasoning on top, and it slipped to 98. Add the Fable 5 traces as well, it dropped again to 96. Every distillation step made the model a little worse. The coding test was harsher still. The base model fixed 19 real bugs out of 30. The Fable distilled version? 11. And it flat-out gave up on 16 of them. The clone did not gain Fable 5's power. It lost its own. And now the reason lands. A 4 billion model simply does not have the room to hold a frontier brain. So, naive imitation copies the voice, the confident tone, the shape of the answer, while the real capability leaks straight out. Style transfers, genius does not. And that is exactly the gap on policy was built to close. Which brings us to the part you actually clicked for. How to do this yourself, and do it properly. Six steps. Capture, clean, format, train, quantize, run. The first five on a rented GPU, the last one on the laptop right in front of you. Step one, capture, and it is a race against the clock. While Fable 5 is online, point Claude code at your own tasks and log every session. The prompt, the reasoning, the tool calls, the output. Every real problem you solve quietly becomes a training example for free. Step two, clean. Raw logs are filthy. Rate limit warnings, slash command menus, color codes bleeding out of the terminal. Strip all of it. The teams that did this well filtered the junk first because a model will happily learn your noise as if it were signal. Step three, format. Every trace becomes one clean example in chat ML. The context going in, the reasoning, and the action coming out. This is the exact shape the student trains on. Thousands of little context to action pairs. Each one a lesson in how Fable 5 thinks. Step four, pick your base. QN3 4B instruct is the popular choice. Small, sharp, and Apache licensed so you can share whatever you build. A bigger base has more room to absorb. A smaller base is cheaper to run. Your call. Step five, train. The cheap route is a Laura fine-tune. You freeze the base and nudge a thin new layer on top, so the whole job fits on one rented GPU for about the price of a coffee. A few hours later, you have a first QFable, and it will sound exactly like Fable 5. But if you want it to be good, not just sound good, this is where you spend the extra hour on policy distillation. Let your student attempt real tasks, have a stronger model grade each token, and train on that. This one step is the whole difference between a costume and a brain. Step six, quantize and ship. Squeeze the weights down into a 4-bit GGUF file, just a couple of gigabytes, and hand it to Ollama. One command, Ollama run, and the model pulls up on your own machine. No API key, no account, no off switch in Washington. And there it is, answering in your terminal, fully offline, on hardware you own. A shadow of Fable 5, sure, but a shadow that is yours forever, that boots on an airplane, and that no government directive can ever suspend again. Step back, and the point is bigger than one model. This is an insurance policy. When Frontier AI can be switched off by an export order or a pricing change overnight, a local copy, however rough, is the one version nobody can revoke. Just stay honest about what you are holding. You are not getting Fable 5 on a laptop. You are getting its accent, the phrasing, the format, a thin sliver of its skill. For simple, repetitive work, that is genuinely enough. For the hard problems, it is not. And the gap is closing fast. Every month the methods sharpen, the base models get stronger, and on-policy distillation packs more real ability into less space. Today, it is a souvenir. A year from now, it could be a serious tool. So, here is the whole story in four numbers: 3 days online, 4,600 traces captured, 2.3 million examples distilled, and 1/10 the cost, if you do it the right way. The lesson underneath all of it is simple. You cannot download a Frontier model, but you can download the way it thinks. And once you have that, no one can ever fully take it away. So, if the model on your screen could vanish tomorrow, would you copy its brain tonight? Tell me where you land in the comments, and I will see you in the next one.

---

## Timestamped Segments

**[0:00]** Three days. That is how long the most

**[0:02]** powerful AI model on Earth stayed online

**[0:05]** before the United States government

**[0:07]** reached in and switched it off. Claude

**[0:09]** Fable 5. Here on a Tuesday, dark by

**[0:12]** Friday. And the people who saw it coming

**[0:14]** did something clever. They started

**[0:16]** quietly copying its brain. Anthropic

**[0:19]** shipped Fable 5 on June 9th. It's first

**[0:22]** public Mythos class model, a full tier

**[0:24]** above Opus, the sharpest thing they had

**[0:27]** ever released. 72 hours later, it was

**[0:29]** gone. The order came straight from the

**[0:32]** Commerce Department. National security,

**[0:34]** export controls. Researchers had found a

**[0:37]** jailbreak that stripped the model's

**[0:39]** safety rails and turned it into an open

**[0:41]** cyber weapon. So, Washington pulled the

**[0:43]** plug for every user outside the country

**[0:45]** overnight. Then, 3 weeks later, it came

**[0:48]** back. The controls were lifted and Fable

**[0:51]** 5 returned to Claude and Claude code.

**[0:53]** But, read the title again before it goes

**[0:55]** offline again, because a model the

**[0:57]** government switched off once can be

**[0:59]** switched off twice. So, here's the plan.

**[1:02]** While Fable 5 is live, you capture what

**[1:04]** it does, its reasoning, its every move,

**[1:07]** and you pour that into a small model

**[1:09]** that runs on your own laptop. A model

**[1:11]** nobody can take offline. This is

**[1:14]** distillation, and today we walk it end

**[1:16]** to end. It starts with a trace. When

**[1:19]** Fable 5 solves a task, it thinks out

**[1:21]** loud and then acts, runs a command,

**[1:24]** edits a file, reads the result. Capture

**[1:27]** that whole thought and action log, and

**[1:28]** you have one trace. Thousands of them

**[1:31]** become a training set. And thousands is

**[1:33]** exactly what appeared on Hugging Face.

**[1:35]** One post drops a data set called Fable

**[1:37]** Traces. Another, Fable 5 Traces. 4,600

**[1:42]** agent sessions packaged and ready while

**[1:44]** the model was still warm. The target is

**[1:47]** a tiny open model, Qwen 3 4 billion

**[1:50]** parameters, small enough to run on a

**[1:52]** single gaming graphics card. Fine-tune

**[1:54]** it on Fable 5's traces, and you get

**[1:57]** something people already nicknamed

**[1:59]** Queebal.

**[2:00]** Claude's brain, Quinn's body. One

**[2:02]** question hangs over all of it. When you

**[2:05]** crush a frontier model into something

**[2:06]** 400 times smaller, does the intelligence

**[2:09]** actually survive the shrink? Hold that

**[2:11]** thought. The answer is not the one the

**[2:14]** hype promised. So, here's the plan for

**[2:16]** the next 12 minutes. First, the

**[2:18]** resources that make this possible. Then

**[2:20]** the research paper that explains why it

**[2:22]** really works. And finally, the exact

**[2:25]** steps to do it yourself. It began with a

**[2:27]** single post. A developer publishes the

**[2:29]** Fable traces drop, tags the base model,

**[2:32]** and within hours the repost climb. The

**[2:35]** comments are all one question. Is this

**[2:37]** really Claude running locally for free?

**[2:40]** The screenshot said yes. Open the model

**[2:42]** card, and it is refreshingly plain.

**[2:45]** Base model, QN3 4 billion instruct,

**[2:48]** precision 16-bit, format ChatML, license

**[2:53]** Apache 2, completely open. One line

**[2:55]** spins it up, vllm serve, and it answers

**[2:59]** like a shrunk-down Fable 5. The dataset

**[3:02]** behind it is small but dense.

**[3:04]** 4,600 sessions distilled from just 60

**[3:07]** real Claude runs inside 188 megabytes,

**[3:12]** smaller than a phone photo album. Each

**[3:14]** row keeps the context, the hidden

**[3:17]** reasoning, and the exact action the

**[3:19]** model took. And look at what those

**[3:21]** actions are. 81% of the rows are tool

**[3:24]** calls, not chit-chat. The single most

**[3:26]** common move, running a bash command,

**[3:29]** shows up 1,500 times. This is not a

**[3:31]** chatbot dataset. It is a recording of an

**[3:34]** engineer at work. One team went much

**[3:37]** bigger. They pulled 2.3 million

**[3:39]** reasoning traces out of Fable 5 and

**[3:41]** compressed all of it into that same 4

**[3:44]** billion model.

**[3:45]** 2.3 million worked examples, like

**[3:47]** handing a student every solved problem

**[3:49]** in an entire library and saying, "Learn

**[3:52]** the pattern." And it was never just one

**[3:54]** person. Half a dozen accounts raced to

**[3:56]** capture the model before it could vanish

**[3:58]** again. Raw traces, agent logs, full

**[4:01]** coding sessions, all mirrored onto

**[4:04]** Hugging Face, a frontier model quietly

**[4:06]** backed up by strangers. So, what is

**[4:08]** distillation really? Picture a teacher

**[4:11]** and a student. The teacher is Fable 5,

**[4:14]** enormous, expensive, brilliant. The

**[4:16]** student is the little model. The teacher

**[4:19]** solves problems out loud, and the

**[4:21]** student copies not just the answers, but

**[4:23]** the way it reached them. And here is the

**[4:25]** first thing to hold onto.

**[4:27]** Distillation transfers how to reason,

**[4:29]** the shape of the thinking, not new

**[4:31]** facts. You are teaching a style of

**[4:33]** solving, not stuffing in a library. That

**[4:36]** one distinction decides everything that

**[4:38]** comes next. Now, the naive way, the way

**[4:41]** most of these data sets use, you take

**[4:44]** the teacher's traces and train the

**[4:45]** student to imitate them, line by line.

**[4:48]** It sounds obvious, but there is a trap

**[4:50]** hiding in it.

**[4:52]** The student only ever sees the teacher's

**[4:53]** perfect path and never its own mistakes,

**[4:56]** which is exactly the problem a team at

**[4:58]** Thinking Machines set out to fix in a

**[5:00]** paper simply titled On Policy

**[5:03]** Distillation.

**[5:04]** It is the missing piece in almost every

**[5:06]** Fable 5 clone shipping right now. Their

**[5:09]** fix flips the whole direction. Instead

**[5:11]** of feeding the student the teacher's

**[5:13]** answers, you let the student attempt the

**[5:15]** task itself, and the teacher grades

**[5:18]** every single token it produces. Right

**[5:20]** move, high score. Wrong move, low score.

**[5:23]** The student learns from its own walk,

**[5:25]** not a stranger's. And the payoff is

**[5:27]** real. On a brutal math benchmark, on

**[5:30]** policy distillation hit 70% at 1/10 the

**[5:34]** cost of full reinforcement learning, up

**[5:36]** to 30 times cheaper than the naive

**[5:38]** method, and 7 to 10 times faster to

**[5:41]** train. Cheaper and better. Why does

**[5:44]** grading the student's own attempts

**[5:45]** matter so much? Because when the little

**[5:47]** model drifts off course, and it will, it

**[5:50]** needs to have seen that mistake and been

**[5:52]** corrected. Copying a flawless transcript

**[5:55]** never teaches recovery, only practice

**[5:57]** does. So, keep these two words apart.

**[6:00]** Off policy, imitate the teacher's

**[6:02]** transcript, cheap and fragile. On

**[6:05]** policy, practice under the teacher's

**[6:07]** eye, a little pricier and far stronger.

**[6:10]** Same traces, completely different

**[6:12]** result. But you did not come here for

**[6:14]** theory, so let us check the receipts.

**[6:17]** One engineer took the distilled Qobol,

**[6:19]** dropped it on a single graphics card,

**[6:21]** and ran it head-to-head against the

**[6:23]** plain base model it started from. Same

**[6:25]** hardware, same settings, a fair fight.

**[6:28]** The result stings. On a live tool

**[6:31]** calling test, the untouched base scored

**[6:33]** 99. Add Opus reasoning on top, and it

**[6:36]** slipped to 98. Add the Fable 5 traces as

**[6:39]** well, it dropped again to 96. Every

**[6:42]** distillation step made the model a

**[6:44]** little worse. The coding test was

**[6:46]** harsher still. The base model fixed 19

**[6:49]** real bugs out of 30. The Fable distilled

**[6:52]** version? 11. And it flat-out gave up on

**[6:55]** 16 of them. The clone did not gain Fable

**[6:58]** 5's power. It lost its own. And now the

**[7:01]** reason lands. A 4 billion model simply

**[7:04]** does not have the room to hold a

**[7:05]** frontier brain. So, naive imitation

**[7:08]** copies the voice, the confident tone,

**[7:10]** the shape of the answer, while the real

**[7:12]** capability leaks straight out. Style

**[7:15]** transfers, genius does not. And that is

**[7:17]** exactly the gap on policy was built to

**[7:19]** close.

**[7:21]** Which brings us to the part you actually

**[7:23]** clicked for. How to do this yourself,

**[7:25]** and do it properly. Six steps. Capture,

**[7:28]** clean, format, train, quantize, run. The

**[7:31]** first five on a rented GPU, the last one

**[7:34]** on the laptop right in front of you.

**[7:36]** Step one, capture, and it is a race

**[7:39]** against the clock.

**[7:41]** While Fable 5 is online, point Claude

**[7:43]** code at your own tasks and log every

**[7:45]** session. The prompt, the reasoning, the

**[7:48]** tool calls, the output. Every real

**[7:50]** problem you solve quietly becomes a

**[7:52]** training example for free. Step two,

**[7:55]** clean. Raw logs are filthy. Rate limit

**[7:58]** warnings, slash command menus, color

**[8:01]** codes bleeding out of the terminal.

**[8:03]** Strip all of it. The teams that did this

**[8:05]** well filtered the junk first because a

**[8:07]** model will happily learn your noise as

**[8:10]** if it were signal. Step three, format.

**[8:13]** Every trace becomes one clean example in

**[8:15]** chat ML. The context going in, the

**[8:18]** reasoning, and the action coming out.

**[8:20]** This is the exact shape the student

**[8:22]** trains on. Thousands of little context

**[8:24]** to action pairs. Each one a lesson in

**[8:27]** how Fable 5 thinks. Step four, pick your

**[8:30]** base. QN3 4B instruct is the popular

**[8:33]** choice. Small, sharp, and Apache

**[8:36]** licensed so you can share whatever you

**[8:38]** build. A bigger base has more room to

**[8:40]** absorb. A smaller base is cheaper to

**[8:43]** run. Your call. Step five, train. The

**[8:46]** cheap route is a Laura fine-tune. You

**[8:49]** freeze the base and nudge a thin new

**[8:51]** layer on top, so the whole job fits on

**[8:53]** one rented GPU for about the price of a

**[8:56]** coffee. A few hours later, you have a

**[8:58]** first QFable, and it will sound exactly

**[9:01]** like Fable 5. But if you want it to be

**[9:03]** good, not just sound good, this is where

**[9:06]** you spend the extra hour on policy

**[9:08]** distillation. Let your student attempt

**[9:10]** real tasks, have a stronger model grade

**[9:13]** each token, and train on that. This one

**[9:16]** step is the whole difference between a

**[9:17]** costume and a brain. Step six, quantize

**[9:21]** and ship. Squeeze the weights down into

**[9:23]** a 4-bit GGUF file, just a couple of

**[9:26]** gigabytes, and hand it to Ollama. One

**[9:29]** command, Ollama run, and the model pulls

**[9:31]** up on your own machine. No API key, no

**[9:35]** account, no off switch in Washington.

**[9:37]** And there it is, answering in your

**[9:39]** terminal, fully offline, on hardware you

**[9:42]** own. A shadow of Fable 5, sure, but a

**[9:45]** shadow that is yours forever, that boots

**[9:48]** on an airplane, and that no government

**[9:50]** directive can ever suspend again.

**[9:52]** Step back, and the point is bigger than

**[9:54]** one model. This is an insurance policy.

**[9:57]** When Frontier AI can be switched off by

**[9:59]** an export order or a pricing change

**[10:01]** overnight, a local copy, however rough,

**[10:05]** is the one version nobody can revoke.

**[10:07]** Just stay honest about what you are

**[10:08]** holding. You are not getting Fable 5 on

**[10:11]** a laptop. You are getting its accent,

**[10:14]** the phrasing, the format, a thin sliver

**[10:16]** of its skill. For simple, repetitive

**[10:19]** work, that is genuinely enough. For the

**[10:21]** hard problems, it is not. And the gap is

**[10:24]** closing fast. Every month the methods

**[10:27]** sharpen, the base models get stronger,

**[10:29]** and on-policy distillation packs more

**[10:31]** real ability into less space. Today, it

**[10:34]** is a souvenir. A year from now, it could

**[10:37]** be a serious tool. So, here is the whole

**[10:39]** story in four numbers: 3 days online,

**[10:42]** 4,600 traces captured, 2.3 million

**[10:46]** examples distilled, and 1/10 the cost,

**[10:49]** if you do it the right way.

**[10:51]** The lesson underneath all of it is

**[10:52]** simple. You cannot download a Frontier

**[10:55]** model, but you can download the way it

**[10:57]** thinks. And once you have that, no one

**[10:59]** can ever fully take it away. So, if the

**[11:02]** model on your screen could vanish

**[11:03]** tomorrow, would you copy its brain

**[11:05]** tonight? Tell me where you land in the

**[11:07]** comments, and I will see you in the next

**[11:09]** one.
