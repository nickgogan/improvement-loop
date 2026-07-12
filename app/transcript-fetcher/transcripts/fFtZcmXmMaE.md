# Transcript: Claude Code's Leak Changes Everything..

**URL:** https://www.youtube.com/watch?v=fFtZcmXmMaE
**Segments:** 296
**Channel:** Agentic Lab
**Duration:** 10:57
**Uploaded:** 2026-04-02

---

## Full Text

Claude Code had its full source code leaked totaling 512,000 lines of TypeScript. I boiled down all of it, and after 2,000 plus hours building in Claude Code, I knew exactly which patterns matter. Here's what really changed without all the hype. And we'll start with the first pattern that directly impacts how you manage your repos while working in Claude Code. Every time you send a message before your words reach the model, thousands of tokens you can't see enter the model's context. The source code officially revealed two interesting additions. First of all, and very simply, the current date. This is a huge quality of life boost since LLMs have training data typically over 6 months old. They have no idea what the current date is unless you tell them. The second is Git status. Your entire Git status gets dumped into context at the start of every conversation totaling up to a cap of 2,000 characters of raw Git status output, which is approximately 500 tokens of context distracting your model at all times. So, if you're working in a messy repo with 50 untracked files, it might be time to clean that up. Another interesting fact is if you're using Claude Code through VS Code or JetBrains, every line you highlight and every file you open gets silently streamed to the model. I knew about Git status injection before the leak because I asked Claude Code what was in its context, and it told me. You can always just ask the model what it sees. Luckily for us, this leak confirms exactly how it works down to the source code. So, the takeaway here is to keep your Git status clean by committing often. Post-session hooks, which automatically push to a branch after every Claude Code session, can be a fantastic way to autonomously manage version control. A lot of the coverage of this leak talks about five compaction strategies, like they're all running right now. Most of these are behind feature flags that are actually off by default. So, one of the examples was very interesting, though. It's called micro compact, which would remove stale tool calls, meaning calls that are older than the most recent five, from the memory of agents or the context of agents, which as we know, tool calls are the most context dense part of Claude Code. I just wanted to mention this since most people are talking about this as if it's a live feature. It is not yet live. Another interesting fact from the comments of the code is that 18% of all file reads in Claude Code are duplicates, meaning that Claude Code frequently rereads files. So, they built a deduplication system. If the file hasn't changed since the last read, it returns a one-line stub instead of the full content of the tool call. This saves 2.6% of fleet-wide token costs, which is actually quite a bit. So, this is an extremely important pattern to remember for those of you that are interested in building your own harness or utilizing third-party harnesses. In another part of the code base, an agent awaiting release is in the works. This is a separate verification agent, which can only read files and run commands. It cannot edit or write. This reflects a core pattern that I've been investigating for a while now. Performing verification is in the same context window as generation, i.e., generating code and then asking the same agent to verify the code it just wrote, results in frequently biased verification. One thing that I've been doing lately is asking my Claude Code to spawn a sub-agent to verify its work, or I even put verifier sub-agents in many of my autonomous pipelines. Now, this solves context pollution, where the builder agent is convinced its own work is correct while verifying. So, you can easily copy the verifier agent pattern for yourself before it even releases. Trust me, this will change the game for the quality of your verification gates. So, this is the entire verification agent prompt distilled into seven core patterns that we can use when making our own verification agents. And for anyone writing any code, they should seriously consider these verification agents, also known as LLM as a judge. So, for number one and number four, notice that it's trying to actively break what was written. It has an adversarial framing. So, it's not just testing if it works or confirming it, it's actively trying to break it. And it does that through possible concurrency, boundary values, idempotency, or orphan operations. And [snorts] it has to check one of those before it can even issue a pass. Then for number two, notice that it can not edit, write, or create files. So, this allows it to not do any damage to the code while looking over it because it's meant to just be a verification agent. It's not actually meant to edit the code. And then notice for number three, solid logging is one of the keys in all agentic pipelines. But specifically in this case, verification, because you have to actually see what the verification agent was up to and why it decided what it decided with actual test logs. And for number five, notice that this one is talking about how tests that were potentially written by an LLM could prove nothing because they would already be biased. So, this is that unbiased layer in the pipeline that's supposed to make its own tests. And number six is by far the most important pattern here, and you need this. The idea behind number six is that we have binary criteria, meaning that it is pass or fail, which allows the agent to actually choose a side instead of just going on vibes. It doesn't allow any room for hallucinations, bloviating, or guessing. In this case, there's also a partial option, but that's only when the verification agent was actually unable to complete its verification tasks due to environmental limitations. Then finally, for number seven, this showcases the core pattern in LLMs where frequently they get lazy and decide to skip things. This is a prompt that's trying to prevent that. Speaking of features in the works, there's a feature flag called fork_subagent, which when released will be a huge shift in how we can utilize sub-agents. It's fully built out in the code, and all it would take is setting the feature flag to true. Right now, when you spawn a sub-agent, it starts fresh with none of your session history and context. But with this flag, you could spawn a sub-agent that has the exact full session context of what you've been working on thus far, which makes for a very different dynamic. And we know this can work because it already is how /btw works. /btw simply forks your context and allows you to question the model in real time. Then you can just trim the branched context that was created, which is done automatically with /btw, and continue on the main task. But here's why this actually matters. A sub-agent with your full context is the same thing as a fork. And forks mean that you can explore different trajectories in parallel, meaning you can have your agent forms different solutions to the same problem in parallel. You can spin up three forks, give each one a different approach, and watch which one lands, and then feed that winning path back to the orchestrator and continue on the winning path. So, this is basically a genetic algorithm, but for agents. This is fundamentally what I call trajectory engineering, which is the practice of exploring the output trajectory of the LLM through different context inputs. The infrastructure for this is fully built, and my guess is that it's coming soon. I'm personally considering this as a leaked feature. Now, here's the big one. There's a /pay command in Claude Code, and a /wallet command, and a /x402 command. So, these commands have sets of argument that allow you to set up and configure a Coinbase wallet such that your agent can pay for certain APIs or pay other agents. This is an absolutely huge leak because it shows that Anthropic is planning to move further along with agent-to-agent payment structure. So, you fund the wallet and configure how much it can spend per session, and then your agent can actually pay for stuff. It can also pay other agents. So, based on the code, it's definitely very early, and there are still bugs, but this is going to be a big shift to the economy in general. And it's finally an official thing that Anthropic is taking part in. Technically, it's more of an unofficial thing, but it's, you know, officially unofficially going to happen because it's in the source code. They're at the very least experimenting with this. And they're using Coinbase as their outlet. Now, Claude Code is not just a thin wrapper. As you can see, it's a deeply engineered multi-model system with tons of functionalities. The source code allows us to treat it like a glass box and actually review what is going on and how. For example, the context injection allows us to see how tools like Claude Code are injecting context into the model that we may or may not want. And this allows us to turn that type of stuff off. Then we have compaction, which is one of the most interesting variables that's yet to be solved. So, you can see that there are strategies coming, especially for real-time compaction, which will be particularly interesting. Then we have file deduplication. The big thing there is that it was proven that 18% of reads are duplicates. That's actually a huge statistic because it means any harness without the file deduplication is missing out. But this leak also shows that they're experimenting. We have a verification agent coming soon, which as a user, as a power user, you can actually build this yourself based on watching this video and reviewing the code. Then you have fork sub-agent, which we all knew was coming eventually, but it's confirmed now that it's actually in the code, and all you have to do is turn a flag on, and it would actually be able to fork its own context. And then finally, we have a crypto wallet, which will be a paradigm shift in how agents actually pay for stuff. This has always been possible, but now that Anthropic to be experimenting with it officially, that could mean a huge leap for the crypto ecosystem. After boiling down all 512,000 lines of code, I wrote up an 80-page document summarizing the code base and the core patterns you might need to know in more detail according to their actual implementation. You can find it free in my school community, which is the number one agentic coding community on school. I'll see you in there.

---

## Timestamped Segments

**[0:00]** Claude Code had its full source code

**[0:02]** leaked totaling 512,000 lines of

**[0:06]** TypeScript. I boiled down all of it, and

**[0:09]** after 2,000 plus hours building in

**[0:11]** Claude Code, I knew exactly which

**[0:13]** patterns matter. Here's what really

**[0:15]** changed without all the hype.

**[0:18]** And we'll start with the first pattern

**[0:19]** that directly impacts how you manage

**[0:21]** your repos while working in Claude Code.

**[0:23]** Every time you send a message before

**[0:25]** your words reach the model, thousands of

**[0:27]** tokens you can't see enter the model's

**[0:29]** context. The source code officially

**[0:32]** revealed two interesting additions.

**[0:34]** First of all, and very simply, the

**[0:36]** current date. This is a huge quality of

**[0:38]** life boost since LLMs have training data

**[0:40]** typically over 6 months old. They have

**[0:43]** no idea what the current date is unless

**[0:45]** you tell them.

**[0:46]** The second is Git status. Your entire

**[0:49]** Git status gets dumped into context at

**[0:51]** the start of every conversation totaling

**[0:54]** up to a cap of 2,000 characters of raw

**[0:56]** Git status output, which is

**[0:58]** approximately 500 tokens of context

**[1:01]** distracting your model at all times.

**[1:04]** So, if you're working in a messy repo

**[1:06]** with 50 untracked files, it might be

**[1:08]** time to clean that up. Another

**[1:10]** interesting fact is if you're using

**[1:12]** Claude Code through VS Code or

**[1:14]** JetBrains, every line you highlight and

**[1:16]** every file you open gets silently

**[1:18]** streamed to the model.

**[1:20]** I knew about Git status injection before

**[1:23]** the leak because I asked Claude Code

**[1:25]** what was in its context, and it told me.

**[1:28]** You can always just ask the model what

**[1:30]** it sees. Luckily for us, this leak

**[1:32]** confirms exactly how it works down to

**[1:35]** the source code.

**[1:36]** So, the takeaway here is to keep your

**[1:38]** Git status clean by committing often.

**[1:40]** Post-session hooks, which automatically

**[1:42]** push to a branch after every Claude Code

**[1:44]** session, can be a fantastic way to

**[1:47]** autonomously manage version control.

**[1:50]** A lot of the coverage of this leak talks

**[1:52]** about five compaction strategies, like

**[1:54]** they're all running right now. Most of

**[1:57]** these are behind feature flags that are

**[1:59]** actually off by default. So, one of the

**[2:01]** examples was very interesting, though.

**[2:03]** It's called micro compact, which would

**[2:05]** remove stale tool calls, meaning calls

**[2:09]** that are older than the most recent

**[2:11]** five, from the memory of agents or the

**[2:13]** context of agents, which as we know,

**[2:15]** tool calls are the most context dense

**[2:18]** part of Claude Code. I just wanted to

**[2:20]** mention this since most people are

**[2:22]** talking about this as if it's a live

**[2:24]** feature. It is not yet live.

**[2:27]** Another interesting fact from the

**[2:29]** comments of the code is that 18% of all

**[2:32]** file reads in Claude Code are

**[2:33]** duplicates, meaning that Claude Code

**[2:35]** frequently rereads files. So, they built

**[2:38]** a deduplication system. If the file

**[2:40]** hasn't changed since the last read, it

**[2:43]** returns a one-line stub instead of the

**[2:45]** full content of the tool call. This

**[2:47]** saves 2.6% of fleet-wide token costs,

**[2:51]** which is actually quite a bit. So, this

**[2:53]** is an extremely important pattern to

**[2:55]** remember for those of you that are

**[2:57]** interested in building your own harness

**[2:59]** or utilizing third-party harnesses.

**[3:02]** In another part of the code base, an

**[3:04]** agent awaiting release is in the works.

**[3:07]** This is a separate verification agent,

**[3:09]** which can only read files and run

**[3:11]** commands. It cannot edit or write. This

**[3:14]** reflects a core pattern that I've been

**[3:16]** investigating for a while now.

**[3:17]** Performing verification is in the same

**[3:20]** context window as generation, i.e.,

**[3:22]** generating code and then asking the same

**[3:24]** agent to verify the code it just wrote,

**[3:26]** results in frequently biased

**[3:28]** verification. One thing that I've been

**[3:30]** doing lately is asking my Claude Code to

**[3:32]** spawn a sub-agent to verify its work,

**[3:36]** or I even put verifier sub-agents in

**[3:38]** many of my autonomous pipelines.

**[3:41]** Now, this solves context pollution,

**[3:44]** where the builder agent is convinced its

**[3:46]** own work is correct while verifying. So,

**[3:49]** you can easily copy the verifier agent

**[3:52]** pattern for yourself before it even

**[3:53]** releases. Trust me, this will change the

**[3:56]** game for the quality of your

**[3:57]** verification gates.

**[4:00]** So, this is the entire verification

**[4:02]** agent prompt distilled into seven core

**[4:04]** patterns that we can use when making our

**[4:06]** own verification agents.

**[4:08]** And for anyone writing any code, they

**[4:11]** should seriously consider these

**[4:12]** verification agents, also known as LLM

**[4:15]** as a judge.

**[4:16]** So, for number one and number four,

**[4:18]** notice that it's trying to actively

**[4:20]** break what was written. It has an

**[4:22]** adversarial framing. So, it's not just

**[4:24]** testing if it works or confirming it,

**[4:26]** it's actively trying to break it. And it

**[4:29]** does that through possible concurrency,

**[4:30]** boundary values, idempotency, or orphan

**[4:33]** operations.

**[4:35]** And [snorts] it has to check one of

**[4:36]** those before it can even issue a pass.

**[4:39]** Then for number two, notice that it can

**[4:41]** not edit, write, or create files. So,

**[4:44]** this allows it to not do any damage

**[4:47]** to the code while looking over it

**[4:50]** because it's meant to just be a

**[4:51]** verification agent. It's not actually

**[4:53]** meant to edit the code.

**[4:55]** And then notice for number three, solid

**[4:57]** logging is one of the keys in all

**[4:59]** agentic pipelines.

**[5:01]** But specifically in this case,

**[5:03]** verification, because you have to

**[5:05]** actually see what the verification agent

**[5:07]** was up to and why it decided what it

**[5:09]** decided with actual test logs.

**[5:12]** And for number five, notice that this

**[5:14]** one is talking about how tests that were

**[5:16]** potentially written by an LLM could

**[5:18]** prove nothing because they would already

**[5:20]** be biased.

**[5:22]** So, this is that unbiased layer in the

**[5:23]** pipeline that's supposed to make its own

**[5:25]** tests.

**[5:26]** And number six is by far the most

**[5:28]** important pattern here, and you need

**[5:30]** this.

**[5:30]** The idea behind number six is that we

**[5:33]** have binary criteria, meaning that it is

**[5:36]** pass or fail, which allows the agent to

**[5:38]** actually choose a side instead of just

**[5:40]** going on vibes.

**[5:42]** It doesn't allow any room for

**[5:43]** hallucinations, bloviating, or guessing.

**[5:46]** In this case, there's also a partial

**[5:48]** option, but that's only when the

**[5:50]** verification agent was actually unable

**[5:52]** to complete its verification tasks due

**[5:55]** to environmental limitations. Then

**[5:57]** finally, for number seven, this

**[5:59]** showcases the core pattern in LLMs where

**[6:01]** frequently they get lazy and decide to

**[6:03]** skip things. This is a prompt that's

**[6:06]** trying to prevent that.

**[6:08]** Speaking of features in the works,

**[6:10]** there's a feature flag called

**[6:11]** fork_subagent,

**[6:13]** which when released will be a huge shift

**[6:16]** in how we can utilize sub-agents. It's

**[6:18]** fully built out in the code, and all it

**[6:20]** would take is setting the feature flag

**[6:22]** to true.

**[6:23]** Right now, when you spawn a sub-agent,

**[6:25]** it starts fresh with none of your

**[6:27]** session history and context. But with

**[6:29]** this flag, you could spawn a sub-agent

**[6:32]** that has the exact full session context

**[6:34]** of what you've been working on thus far,

**[6:36]** which makes for a very different

**[6:37]** dynamic.

**[6:38]** And we know this can work because it

**[6:40]** already is how /btw works. /btw simply

**[6:45]** forks your context and allows you to

**[6:47]** question the model in real time. Then

**[6:50]** you can just trim the branched context

**[6:52]** that was created, which is done

**[6:53]** automatically with /btw, and continue on

**[6:56]** the main task.

**[6:58]** But here's why this actually matters. A

**[6:59]** sub-agent with your full context is the

**[7:01]** same thing as a fork. And forks mean

**[7:04]** that you can explore different

**[7:06]** trajectories in parallel, meaning you

**[7:08]** can have your agent forms different

**[7:11]** solutions to the same problem in

**[7:13]** parallel. You can spin up three forks,

**[7:16]** give each one a different approach, and

**[7:18]** watch which one lands, and then feed

**[7:20]** that winning path back to the

**[7:22]** orchestrator and continue on the winning

**[7:23]** path. So, this is basically a genetic

**[7:26]** algorithm, but for agents.

**[7:28]** This is fundamentally what I call

**[7:30]** trajectory engineering, which is the

**[7:32]** practice of exploring the output

**[7:34]** trajectory of the LLM through different

**[7:37]** context inputs.

**[7:38]** The infrastructure for this is fully

**[7:40]** built, and my guess is that it's coming

**[7:42]** soon. I'm personally considering this as

**[7:44]** a leaked feature.

**[7:47]** Now, here's the big one. There's a /pay

**[7:50]** command in Claude Code, and a /wallet

**[7:53]** command, and a /x402 command. So, these

**[7:57]** commands have sets of argument that

**[7:59]** allow you to set up and configure a

**[8:01]** Coinbase wallet such that your agent can

**[8:04]** pay for certain APIs or pay other

**[8:06]** agents. This is an absolutely huge leak

**[8:09]** because it shows that Anthropic is

**[8:11]** planning to move further along with

**[8:13]** agent-to-agent payment structure.

**[8:15]** So, you fund the wallet and configure

**[8:17]** how much it can spend per session, and

**[8:19]** then your agent can actually pay for

**[8:21]** stuff. It can also pay other agents. So,

**[8:24]** based on the code, it's definitely very

**[8:26]** early, and there are still bugs, but

**[8:28]** this is going to be a big shift to the

**[8:30]** economy in general.

**[8:32]** And it's finally an official thing that

**[8:34]** Anthropic is taking part in.

**[8:38]** Technically, it's more of an unofficial

**[8:40]** thing, but it's, you know, officially

**[8:42]** unofficially going to happen because

**[8:45]** it's in the source code. They're at the

**[8:47]** very least experimenting with this.

**[8:49]** And they're using Coinbase as their

**[8:51]** outlet.

**[8:54]** Now, Claude Code is not just a thin

**[8:56]** wrapper. As you can see, it's a deeply

**[8:58]** engineered multi-model system with tons

**[9:01]** of functionalities.

**[9:03]** The source code allows us to treat it

**[9:05]** like a glass box and actually review

**[9:07]** what is going on and how.

**[9:09]** For example, the context injection

**[9:11]** allows us to see how tools like Claude

**[9:14]** Code are injecting context into the

**[9:16]** model that we may or may not want. And

**[9:19]** this allows us to turn that type of

**[9:21]** stuff off.

**[9:22]** Then we have compaction, which is one of

**[9:24]** the most interesting variables that's

**[9:26]** yet to be solved. So, you can see that

**[9:28]** there are strategies coming, especially

**[9:30]** for real-time compaction, which will be

**[9:32]** particularly interesting.

**[9:35]** Then we have file deduplication. The big

**[9:37]** thing there is that it was proven that

**[9:39]** 18% of reads are duplicates. That's

**[9:42]** actually a huge statistic because it

**[9:44]** means any harness without the file

**[9:46]** deduplication is missing out.

**[9:49]** But this leak also shows that they're

**[9:51]** experimenting. We have a verification

**[9:54]** agent coming soon, which as a user, as a

**[9:56]** power user, you can actually build this

**[9:58]** yourself based on watching this video

**[10:00]** and reviewing the code.

**[10:02]** Then you have fork sub-agent, which we

**[10:04]** all knew was coming eventually, but it's

**[10:06]** confirmed now that it's actually in the

**[10:09]** code, and all you have to do is turn a

**[10:11]** flag on, and it would actually be able

**[10:13]** to fork its own context. And then

**[10:16]** finally, we have a crypto wallet, which

**[10:19]** will be a paradigm shift in how agents

**[10:21]** actually pay for stuff.

**[10:23]** This has always been possible, but now

**[10:25]** that Anthropic to be experimenting with

**[10:28]** it officially,

**[10:30]** that could mean a huge leap for the

**[10:32]** crypto ecosystem.

**[10:35]** After boiling down all 512,000

**[10:38]** lines of code, I wrote up an 80-page

**[10:41]** document summarizing the code base and

**[10:43]** the core patterns you might need to know

**[10:45]** in more detail according to their actual

**[10:48]** implementation. You can find it free in

**[10:50]** my school community, which is the number

**[10:52]** one agentic coding community on school.

**[10:55]** I'll see you in there.
