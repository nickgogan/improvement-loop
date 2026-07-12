# Transcript: DeepSeek Just Solved AI's Billion Dollar Problem

**URL:** https://www.youtube.com/watch?v=mG4SmhWyeFA
**Segments:** 131
**Channel:** Two Minute Papers
**Duration:** 5:50
**Uploaded:** 2026-06-22

---

## Full Text

Scientists at Deep Seek have invented something amazing and exactly at the right time when we need it most. You see, we are entering the age of AI. But, I am really surprised. I just found out that the way these AI systems run on our computers is incredibly inefficient. So, if you want your AI assistant to answer quicker, you need more compute power, clear as day. But, you may find that as you add more compute, it does not get faster. But, how can that be? You know, it's kind of shocking given that companies are paying billions and billions of dollars for more compute to run these AI systems. How is this possible? Imagine reading a book and now imagine that every time you turn the page, you forget about the characters. That's not a great way to read books, right? Here is what happens in practice. Assume we have a huge brain the size of a mountain and we want to talk about a book. If the book is one page, we just memorize that one page and just talk about it, quick and easy. Now, imagine that the book grows. It is now huge and since we forget about everything the moment we turn the page, ouch. If we want to talk about it, we have to reread it all the time. So, our brain is huge and hungry, but there is a problem. Information is coming in through a straw. So then, we spend most of our time not thinking, but reading slowly. And that is exactly what the graphics cards of today are doing when you run an agentic AI system on hard problems. All those billions of dollars sitting at 40% utilization. This is a horror story. That's a tough problem. So, what is the solution? Well, of course, you don't need all those GPUs. So, send them to me. Problem solved. >> [laughter] >> Okay, so how did scientists at Deep Seek solve it? Dear fellow scholars, this is Two Minute Papers with Dr. Károly Zsolnai Féhér. Now, of course, they say you don't need a bigger brain. You need a bigger straw. So, in today's systems, there are AI chips that do the reading. We call them prefill machines. They are the straws, and they are completely jammed. But, there are also different kinds of machines in the network, the decoding machines. And their straws are nearly completely empty. They just sit there, often unused. So, they say, "Use those to do the reading, and have it take a second path to the prefill machines." Finally, it's a clever detour that lets the brain do its job. But, there is a problem. This shortcut takes the same high-speed roads that the AI needs for thinking. If we don't do this well, "Hooray, we solved the traffic jam." And when they ask us how, well, >> [laughter] >> by introducing another traffic jam. Okay, so what is the solution for that? Well, traffic control. On these roads, thinking traffic gets priority. Memory traffic, however, gets leftover space. This is absolute genius because it does not give you more compute. No, it gives you access to the compute that you already have. Okay, so what is the key result? Well, hold on to your papers, fellow scholars, because it speeds up this whole network from 40% utilization to about 80% utilization. In practice, almost twice as much work from the machine you already bought. That is an insane jump in just one paper. I am completely stunned. And the main use case for this is when you have long multi-turn agentic workloads. And they give this technique away for all of us for free forever. Woof. Now, it is not a magic bullet for all AI agents to run twice as fast. No, no. It is situational. But it helps exactly in the hardest situations where we need them most. Long conversations, lots of data. That's when things really slow down. Also, note that this is not a shiny new AI system that you can easily write headlines about. It's not the brain. It's a better road system to the brain. It's something that you implement in a data center when you serve these AI systems. So, you don't see a lot of headlines on this because it's not the shiny thing that is easy to sell. But it is absolutely brilliant. And I really wanted to show it to you. And all of us get value out of this kind of open science. If this idea makes it to real serving systems, it might lead to cheaper AI inference for all of us in the future. And they don't close it down and keep this knowledge to themselves. They give it all to us as a gift. How cool is that? That is the power of the papers. What a time to be alive. A word of optimism and joy in a world where you hear about doom coming from every direction. Subscribe and hit the bell if you enjoyed this. Here you see me running the full DeepSeek AI model through Lambda GPU Cloud. 671 billion parameters running super fast and super reliably. This is insane. I love it. And I use it on a regular basis. Lambda provides you with powerful Nvidia GPUs to run your own chatbots and experiments. Seriously, try it out now at lambda.ai/papers or click the link in the description.

---

## Timestamped Segments

**[0:00]** Scientists at Deep Seek have invented

**[0:02]** something amazing and exactly at the

**[0:05]** right time when we need it most. You

**[0:07]** see, we are entering the age of AI. But,

**[0:10]** I am really surprised. I just found out

**[0:13]** that the way these AI systems run on our

**[0:15]** computers is incredibly inefficient. So,

**[0:19]** if you want your AI assistant to answer

**[0:21]** quicker, you need more compute power,

**[0:24]** clear as day. But, you may find that as

**[0:27]** you add more compute, it does not get

**[0:29]** faster. But, how can that be? You know,

**[0:32]** it's kind of shocking given that

**[0:34]** companies are paying billions and

**[0:36]** billions of dollars for more compute to

**[0:39]** run these AI systems. How is this

**[0:41]** possible? Imagine reading a book and now

**[0:44]** imagine that every time you turn the

**[0:46]** page, you forget about the characters.

**[0:49]** That's not a great way to read books,

**[0:50]** right? Here is what happens in practice.

**[0:53]** Assume we have a huge brain the size of

**[0:57]** a mountain and we want to talk about a

**[0:59]** book. If the book is one page, we just

**[1:02]** memorize that one page and just talk

**[1:04]** about it, quick and easy. Now, imagine

**[1:07]** that the book grows. It is now huge and

**[1:11]** since we forget about everything the

**[1:13]** moment we turn the page, ouch. If we

**[1:16]** want to talk about it, we have to reread

**[1:18]** it all the time. So, our brain is huge

**[1:22]** and hungry, but there is a problem.

**[1:24]** Information is coming in through a

**[1:27]** straw. So then, we spend most of our

**[1:29]** time not thinking, but reading slowly.

**[1:33]** And that is exactly what the graphics

**[1:35]** cards of today are doing when you run an

**[1:38]** agentic AI system on hard problems. All

**[1:41]** those billions of dollars sitting at 40%

**[1:45]** utilization.

**[1:47]** This is a horror story. That's a tough

**[1:49]** problem. So, what is the solution?

**[1:52]** Well, of course, you don't need all

**[1:55]** those GPUs. So, send them to me.

**[1:59]** Problem solved.

**[2:01]** >> [laughter]

**[2:01]** >> Okay, so how did scientists at Deep Seek

**[2:04]** solve it? Dear fellow scholars, this is

**[2:07]** Two Minute Papers with Dr. Károly

**[2:08]** Zsolnai Féhér. Now, of course, they say

**[2:11]** you don't need a bigger brain. You need

**[2:14]** a bigger straw. So, in today's systems,

**[2:17]** there are AI chips that do the reading.

**[2:20]** We call them prefill machines. They are

**[2:22]** the straws, and they are completely

**[2:26]** jammed. But, there are also different

**[2:27]** kinds of machines in the network, the

**[2:30]** decoding machines. And their straws are

**[2:32]** nearly completely empty. They just sit

**[2:35]** there, often unused. So, they say, "Use

**[2:39]** those to do the reading, and have it

**[2:41]** take a second path to the prefill

**[2:44]** machines." Finally, it's a clever detour

**[2:47]** that lets the brain do its job. But,

**[2:50]** there is a problem. This shortcut takes

**[2:52]** the same high-speed roads that the AI

**[2:55]** needs for thinking. If we don't do this

**[2:57]** well, "Hooray, we solved the traffic

**[3:00]** jam." And when they ask us how, well,

**[3:03]** >> [laughter]

**[3:03]** >> by introducing another traffic jam.

**[3:07]** Okay, so what is the solution for that?

**[3:10]** Well, traffic control. On these roads,

**[3:13]** thinking traffic gets priority. Memory

**[3:16]** traffic, however, gets leftover space.

**[3:19]** This is absolute genius because it does

**[3:22]** not give you more compute. No, it gives

**[3:25]** you access to the compute that you

**[3:27]** already have. Okay, so what is the key

**[3:30]** result? Well, hold on to your papers,

**[3:32]** fellow scholars, because it speeds up

**[3:34]** this whole network from 40% utilization

**[3:37]** to about 80% utilization. In practice,

**[3:42]** almost twice as much work from the

**[3:44]** machine you already bought. That is an

**[3:47]** insane jump in just one paper. I am

**[3:50]** completely stunned. And the main use

**[3:52]** case for this is when you have long

**[3:55]** multi-turn agentic workloads. And they

**[3:57]** give this technique away for all of us

**[4:00]** for free forever. Woof. Now, it is not a

**[4:04]** magic bullet for all AI agents to run

**[4:06]** twice as fast. No, no. It is

**[4:09]** situational. But it helps exactly in the

**[4:12]** hardest situations where we need them

**[4:14]** most. Long conversations, lots of data.

**[4:17]** That's when things really slow down.

**[4:20]** Also, note that this is not a shiny new

**[4:23]** AI system that you can easily write

**[4:25]** headlines about. It's not the brain.

**[4:28]** It's a better road system to the brain.

**[4:30]** It's something that you implement in a

**[4:32]** data center when you serve these AI

**[4:34]** systems. So, you don't see a lot of

**[4:36]** headlines on this because it's not the

**[4:38]** shiny thing that is easy to sell. But it

**[4:42]** is absolutely brilliant. And I really

**[4:44]** wanted to show it to you. And all of us

**[4:47]** get value out of this kind of open

**[4:49]** science. If this idea makes it to real

**[4:51]** serving systems, it might lead to

**[4:54]** cheaper AI inference for all of us in

**[4:57]** the future. And they don't close it down

**[4:59]** and keep this knowledge to themselves.

**[5:01]** They give it all to us as a gift. How

**[5:04]** cool is that? That is the power of the

**[5:07]** papers. What a time to be alive. A word

**[5:10]** of optimism and joy in a world where you

**[5:13]** hear about doom coming from every

**[5:15]** direction. Subscribe and hit the bell if

**[5:17]** you enjoyed this. Here you see me

**[5:19]** running the full DeepSeek AI model

**[5:22]** through Lambda GPU Cloud. 671

**[5:26]** billion parameters running super fast

**[5:29]** and super reliably. This is insane. I

**[5:33]** love it. And I use it on a regular

**[5:35]** basis. Lambda provides you with powerful

**[5:38]** Nvidia GPUs to run your own chatbots and

**[5:41]** experiments. Seriously, try it out now

**[5:44]** at lambda.ai/papers or click the link in

**[5:46]** the description.
