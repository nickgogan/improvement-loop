# Transcript: Agent Loop Explained in 10 Minutes...

**URL:** https://www.youtube.com/watch?v=Vwn19n8W-qE
**Segments:** 248
**Channel:** Cloud Codes
**Duration:** 9:51
**Uploaded:** 2026-07-06

---

## Full Text

You give an AI agent a single sentence, fix the failing test, refactor this file, book the flight, and then something strange happens. It goes quiet and it works. It reads your files, runs commands, hits errors, tries again, and a few minutes later hands you the finished thing with no further instructions. So, what is actually running in that gap? Here is the honest answer. There is no magic in there. Underneath every agent you have ever used is one small idea repeated, a loop. The model takes a step, looks at the result, and decides the next step over and over until the job is done. To see why the loop matters, start with the model on its own. A language model is basically a function. Text goes in, text comes out, and then it forgets everything. It has no memory of a minute ago, and it cannot touch a single file. Powerful, but frozen, a brain in a jar. The loop is what breaks it out of the jar, and in code it is almost embarrassingly simple. While the task is not done, ask the model what to do, do that one thing, feed the result back, and ask again. That tiny while loop is the entire difference between a chatbot and an agent. Anthropic describes that loop in three moves, gather context, take action, then verify the work, and repeat. Almost every serious agent today, from coding tools to research assistants, is running some version of these three steps in a circle. Watch one lap. The task is to fix a failing test. The model thinks, then acts. It calls a tool to run the tests. It reads the red output, reasons about the cause, edits a line, and runs the test again. Green. Only now does it stop. Think, act, observe, repeat. And notice the part most people miss. The agent checked its own work. Its first attempt was wrong. The tests caught it, and it looped back and fixed it with nobody watching. That single ability to catch its own mistakes and try again is what separates a real agent from a lucky guess. Of course, a loop that never stops is a nightmare. So, every agent carries a stop condition. Quit when the task succeeds, quit when it is truly stuck, or quit when it runs out of budget, a cap on steps, on tokens, or on dollars. Knowing when to stop is a feature, not an afterthought. Why does this suddenly matter so much? Because the loop is scaling fast. Researchers at METR found the length of tasks an agent can finish on its own has been doubling roughly every 7 months. Agents went from handling a few seconds of work to running unattended for hours. So, let us take the loop completely apart in three chapters. First, the four parts every loop is built from. Then, the three phases in detail, gather, act, and verify. And finally, where the loop breaks and how real systems keep it on the rails. Part one, tools. On its own, the model can only produce text. So, we hand it a menu of functions it is allowed to call. Read a file, run a shell command, search the web, edit code. Each tool has a name and a set of arguments. Tools are the hands. Without them, the model can think, but never act. Part two, context. Every turn, the loop keeps a running transcript, the original task, each action it took, and everything it observed. That growing record is the agent's short-term memory. It is the only reason step 10 has any idea what happened back at step one. Put it together, and every agent is really just four moving parts, the model that decides, the tools that act, the context that remembers, and the stop condition that ends it. Swap the model for a smarter one, add new tools, change the goal, the loop wrapped around them stays exactly the same. That is why one good harness can run a hundred different agents. Phase one, in depth, gather context. Before touching anything, a good agent goes and finds what it needs. It grabs the code base, opens the failing file, reads the error, pulls the relevant docs. It does not dump the whole repository into its head. It pulls in just the few pieces that matter for this exact step. The folder structure itself becomes a kind of memory the agent can search on demand. And when there is simply too much to read, it delegates. The main agent spins up sub agents in parallel, each with its own clean context, each chasing one narrow question. And they report back only the useful sentence, not the entire haystack. It is how an agent searches a mountain without drowning in it. Before diving in, the more capable agents also make a plan. They write themselves a short to-do list, then work it item by item, checking each one off as it lands. It sounds trivial, but that little checklist is what keeps a long loop from wandering off and losing the thread halfway through. Phase two, take action. And this is the actual handshake. The model does not run anything itself. It emits a structured request naming a tool and its arguments. The harness around it runs that tool, captures the output, and hands the result back as the next observation. Then the loop turns again. Most of those tools are small and specific, and that is on purpose. A few sharp, well-named tools beat a hundred vague ones the model has to squint at. But one tool is a universal key, the shell. Give an agent bash, and it can run almost any command a human developer could. A fast agent also does not wait in line. When several tool calls do not depend on each other, read three files, run two searches, it fires them all at once and reads the results together. Same loop, just wider and often several times quicker. To reach the outside world, Slack, GitHub, Google Drive, your database, agents increasingly speak one shared protocol called MCP. Instead of handwriting a fragile integration for every service, you plug in an MCP server and its tools simply appear in the menu, authentication and all. Phase three, verify. The best feedback is cold hard rules. Run the linter, run the tests, compile the types. If anything fails, the agent gets the exact error and loops again. This is why an agent that writes TypeScript and tests it is far more reliable than one that just emits code and hopes. Some work cannot be checked with a test, so the agent takes a screenshot of the page it built and actually looks at it. Is the layout right? Is anything overlapping? Then fixes what it sees. And for fuzzy things like whether an email sounds right, a second model can act as a judge and grade the answer. Now the hard part, because a loop is not automatically smart. Its greatest weakness is that errors compound. One wrong observation quietly poisons the next decision, which poisons the one after that. And 10 steps later, the agent is marching confidently in completely the wrong direction, and worse, it has no idea anything went wrong. Every mistake becomes the ground truth for the next step. The other silent killer is context rot. That transcript never stops growing, and once it fills most of the window, Anthropic starts compacting at around 167,000 tokens of a 200,000 token window, the model begins losing the thread and misreading its own history. The fix is compaction. When the context gets close to full, the agent summarizes everything so far into a tight recap, throws away the raw history, and starts a fresh window from that summary. It is how an agent can keep working for hours on end without simply forgetting the plan. And for anything that has to outlive the window entirely, the agent writes notes to a file, a scratchpad, a memory file, and reads them back later. Context is the short-term memory that fills up and gets wiped. The file system is the long-term memory that stays. You also fence the loop in with hard limits, a ceiling on steps, on tokens, on money, and on wall clock time. If any of them runs out, the loop stops and reports back. Think of it as a seatbelt. It will not make the agent smarter, but it stops a confused one from running all night. And for anything dangerous, you keep a human in the loop. Reading a file can happen freely, but deleting data, deploying to production, or spending money pauses the loop and asks for a yes. The agent proposes, a person approves, a autonomy where it is cheap, and permission where it is costly. One last honest point, not every problem needs a full agent. If the steps are fixed and known ahead of time, a plain workflow, do this, then this, then this, is cheaper, faster, and more predictable. The loop is for open-ended work where you genuinely cannot script the path in advance. Use the least power that solves the job. So, that is the whole machine. Gather context, take action, verify, and repeat. A model to decide, tools to act, context to remember, and a stop condition to end it. Wrap those four in a while loop, add a few guardrails so it cannot hurt itself, and you have an agent. Everything fancier is just a variation on this one shape. The model gets the headlines and the benchmark scores. But the thing that turns a clever text predictor into something that can fix a bug, research a question, or run for an hour on its own is the humble loop wrapped around it. Understand the loop and you understand every agent there is. If this made the agent loop finally click, subscribe. That is exactly what this channel does, one system at a time. I will see you in the next

---

## Timestamped Segments

**[0:00]** You give an AI agent a single sentence,

**[0:02]** fix the failing test, refactor this

**[0:05]** file, book the flight, and then

**[0:07]** something strange happens. It goes quiet

**[0:10]** and it works. It reads your files, runs

**[0:13]** commands, hits errors, tries again, and

**[0:15]** a few minutes later hands you the

**[0:17]** finished thing with no further

**[0:19]** instructions. So, what is actually

**[0:21]** running in that gap? Here is the honest

**[0:23]** answer. There is no magic in there.

**[0:26]** Underneath every agent you have ever

**[0:27]** used is one small idea repeated, a loop.

**[0:31]** The model takes a step, looks at the

**[0:33]** result, and decides the next step over

**[0:36]** and over until the job is done. To see

**[0:39]** why the loop matters, start with the

**[0:41]** model on its own. A language model is

**[0:43]** basically a function. Text goes in, text

**[0:46]** comes out, and then it forgets

**[0:48]** everything. It has no memory of a minute

**[0:50]** ago, and it cannot touch a single file.

**[0:53]** Powerful, but frozen, a brain in a jar.

**[0:57]** The loop is what breaks it out of the

**[0:58]** jar, and in code it is almost

**[1:00]** embarrassingly simple.

**[1:02]** While the task is not done, ask the

**[1:04]** model what to do, do that one thing,

**[1:06]** feed the result back, and ask again.

**[1:09]** That tiny while loop is the entire

**[1:11]** difference between a chatbot and an

**[1:13]** agent. Anthropic describes that loop in

**[1:16]** three moves, gather context, take

**[1:18]** action, then verify the work, and

**[1:20]** repeat. Almost every serious agent

**[1:23]** today, from coding tools to research

**[1:25]** assistants, is running some version of

**[1:27]** these three steps in a circle. Watch one

**[1:30]** lap. The task is to fix a failing test.

**[1:33]** The model thinks, then acts. It calls a

**[1:36]** tool to run the tests. It reads the red

**[1:38]** output, reasons about the cause, edits a

**[1:41]** line, and runs the test again. Green.

**[1:44]** Only now does it stop. Think, act,

**[1:46]** observe, repeat. And notice the part

**[1:49]** most people miss. The agent checked its

**[1:51]** own work.

**[1:53]** Its first attempt was wrong. The tests

**[1:55]** caught it, and it looped back and fixed

**[1:57]** it with nobody watching. That single

**[2:00]** ability to catch its own mistakes and

**[2:02]** try again is what separates a real agent

**[2:05]** from a lucky guess. Of course, a loop

**[2:07]** that never stops is a nightmare. So,

**[2:09]** every agent carries a stop condition.

**[2:12]** Quit when the task succeeds, quit when

**[2:14]** it is truly stuck, or quit when it runs

**[2:16]** out of budget, a cap on steps, on

**[2:19]** tokens, or on dollars. Knowing when to

**[2:21]** stop is a feature, not an afterthought.

**[2:24]** Why does this suddenly matter so much?

**[2:26]** Because the loop is scaling fast.

**[2:28]** Researchers at METR found the length of

**[2:31]** tasks an agent can finish on its own has

**[2:34]** been doubling roughly every 7 months.

**[2:36]** Agents went from handling a few seconds

**[2:38]** of work to running unattended for hours.

**[2:42]** So, let us take the loop completely

**[2:43]** apart in three chapters. First, the four

**[2:47]** parts every loop is built from. Then,

**[2:49]** the three phases in detail, gather, act,

**[2:52]** and verify. And finally, where the loop

**[2:55]** breaks and how real systems keep it on

**[2:57]** the rails. Part one, tools. On its own,

**[3:00]** the model can only produce text. So, we

**[3:02]** hand it a menu of functions it is

**[3:04]** allowed to call. Read a file, run a

**[3:07]** shell command, search the web, edit

**[3:09]** code. Each tool has a name and a set of

**[3:12]** arguments. Tools are the hands. Without

**[3:15]** them, the model can think, but never

**[3:17]** act. Part two, context. Every turn, the

**[3:21]** loop keeps a running transcript, the

**[3:23]** original task, each action it took, and

**[3:26]** everything it observed. That growing

**[3:28]** record is the agent's short-term memory.

**[3:30]** It is the only reason step 10 has any

**[3:32]** idea what happened back at step one.

**[3:35]** Put it together, and every agent is

**[3:37]** really just four moving parts, the model

**[3:40]** that decides, the tools that act, the

**[3:42]** context that remembers, and the stop

**[3:45]** condition that ends it. Swap the model

**[3:47]** for a smarter one, add new tools, change

**[3:50]** the goal, the loop wrapped around them

**[3:52]** stays exactly the same. That is why one

**[3:55]** good harness can run a hundred different

**[3:56]** agents. Phase one, in depth, gather

**[3:59]** context. Before touching anything, a

**[4:02]** good agent goes and finds what it needs.

**[4:05]** It grabs the code base, opens the

**[4:07]** failing file, reads the error, pulls the

**[4:09]** relevant docs.

**[4:11]** It does not dump the whole repository

**[4:13]** into its head. It pulls in just the few

**[4:15]** pieces that matter for this exact step.

**[4:18]** The folder structure itself becomes a

**[4:20]** kind of memory the agent can search on

**[4:22]** demand. And when there is simply too

**[4:24]** much to read, it delegates.

**[4:27]** The main agent spins up sub agents in

**[4:29]** parallel, each with its own clean

**[4:31]** context, each chasing one narrow

**[4:33]** question. And they report back only the

**[4:36]** useful sentence, not the entire

**[4:38]** haystack. It is how an agent searches a

**[4:40]** mountain without drowning in it. Before

**[4:42]** diving in, the more capable agents also

**[4:45]** make a plan. They write themselves a

**[4:47]** short to-do list, then work it item by

**[4:50]** item, checking each one off as it lands.

**[4:52]** It sounds trivial, but that little

**[4:54]** checklist is what keeps a long loop from

**[4:56]** wandering off and losing the thread

**[4:58]** halfway through. Phase two, take action.

**[5:02]** And this is the actual handshake. The

**[5:04]** model does not run anything itself. It

**[5:06]** emits a structured request naming a tool

**[5:09]** and its arguments. The harness around it

**[5:11]** runs that tool, captures the output, and

**[5:14]** hands the result back as the next

**[5:15]** observation. Then the loop turns again.

**[5:18]** Most of those tools are small and

**[5:20]** specific, and that is on purpose. A few

**[5:23]** sharp, well-named tools beat a hundred

**[5:25]** vague ones the model has to squint at.

**[5:28]** But one tool is a universal key, the

**[5:30]** shell. Give an agent bash, and it can

**[5:33]** run almost any command a human developer

**[5:35]** could.

**[5:36]** A fast agent also does not wait in line.

**[5:39]** When several tool calls do not depend on

**[5:41]** each other, read three files, run two

**[5:44]** searches, it fires them all at once and

**[5:46]** reads the results together. Same loop,

**[5:49]** just wider and often several times

**[5:51]** quicker. To reach the outside world,

**[5:54]** Slack, GitHub, Google Drive, your

**[5:56]** database, agents increasingly speak one

**[5:59]** shared protocol called MCP. Instead of

**[6:02]** handwriting a fragile integration for

**[6:04]** every service, you plug in an MCP server

**[6:07]** and its tools simply appear in the menu,

**[6:09]** authentication and all. Phase three,

**[6:12]** verify. The best feedback is cold hard

**[6:15]** rules. Run the linter, run the tests,

**[6:18]** compile the types. If anything fails,

**[6:21]** the agent gets the exact error and loops

**[6:23]** again. This is why an agent that writes

**[6:26]** TypeScript and tests it is far more

**[6:28]** reliable than one that just emits code

**[6:30]** and hopes. Some work cannot be checked

**[6:33]** with a test, so the agent takes a

**[6:35]** screenshot of the page it built and

**[6:37]** actually looks at it. Is the layout

**[6:39]** right? Is anything overlapping? Then

**[6:41]** fixes what it sees. And for fuzzy things

**[6:44]** like whether an email sounds right, a

**[6:47]** second model can act as a judge and

**[6:48]** grade the answer. Now the hard part,

**[6:51]** because a loop is not automatically

**[6:53]** smart. Its greatest weakness is that

**[6:55]** errors compound.

**[6:57]** One wrong observation quietly poisons

**[6:59]** the next decision, which poisons the one

**[7:02]** after that. And 10 steps later, the

**[7:04]** agent is marching confidently in

**[7:06]** completely the wrong direction, and

**[7:08]** worse, it has no idea anything went

**[7:10]** wrong. Every mistake becomes the ground

**[7:13]** truth for the next step. The other

**[7:15]** silent killer is context rot. That

**[7:17]** transcript never stops growing, and once

**[7:19]** it fills most of the window, Anthropic

**[7:22]** starts compacting at around 167,000

**[7:25]** tokens of a 200,000 token window, the

**[7:28]** model begins losing the thread and

**[7:30]** misreading its own history. The fix is

**[7:33]** compaction.

**[7:34]** When the context gets close to full, the

**[7:36]** agent summarizes everything so far into

**[7:39]** a tight recap, throws away the raw

**[7:41]** history, and starts a fresh window from

**[7:43]** that summary.

**[7:45]** It is how an agent can keep working for

**[7:47]** hours on end without simply forgetting

**[7:49]** the plan.

**[7:50]** And for anything that has to outlive the

**[7:52]** window entirely, the agent writes notes

**[7:54]** to a file, a scratchpad, a memory file,

**[7:58]** and reads them back later. Context is

**[8:00]** the short-term memory that fills up and

**[8:02]** gets wiped. The file system is the

**[8:04]** long-term memory that stays. You also

**[8:07]** fence the loop in with hard limits, a

**[8:09]** ceiling on steps, on tokens, on money,

**[8:12]** and on wall clock time. If any of them

**[8:15]** runs out, the loop stops and reports

**[8:17]** back. Think of it as a seatbelt. It will

**[8:20]** not make the agent smarter, but it stops

**[8:23]** a confused one from running all night.

**[8:25]** And for anything dangerous, you keep a

**[8:27]** human in the loop. Reading a file can

**[8:29]** happen freely, but deleting data,

**[8:32]** deploying to production, or spending

**[8:34]** money pauses the loop and asks for a

**[8:36]** yes. The agent proposes, a person

**[8:38]** approves, a autonomy where it is cheap,

**[8:41]** and permission where it is costly. One

**[8:43]** last honest point, not every problem

**[8:46]** needs a full agent. If the steps are

**[8:48]** fixed and known ahead of time, a plain

**[8:50]** workflow, do this, then this, then this,

**[8:53]** is cheaper, faster, and more

**[8:55]** predictable. The loop is for open-ended

**[8:58]** work where you genuinely cannot script

**[8:59]** the path in advance. Use the least power

**[9:02]** that solves the job. So, that is the

**[9:04]** whole machine. Gather context, take

**[9:07]** action, verify, and repeat. A model to

**[9:10]** decide, tools to act, context to

**[9:12]** remember, and a stop condition to end

**[9:14]** it. Wrap those four in a while loop, add

**[9:17]** a few guardrails so it cannot hurt

**[9:19]** itself, and you have an agent.

**[9:21]** Everything fancier is just a variation

**[9:23]** on this one shape. The model gets the

**[9:25]** headlines and the benchmark scores. But

**[9:28]** the thing that turns a clever text

**[9:29]** predictor into something that can fix a

**[9:31]** bug, research a question, or run for an

**[9:34]** hour on its own is the humble loop

**[9:37]** wrapped around it. Understand the loop

**[9:39]** and you understand every agent there is.

**[9:42]** If this made the agent loop finally

**[9:44]** click, subscribe. That is exactly what

**[9:46]** this channel does, one system at a time.

**[9:49]** I will see you in the next
