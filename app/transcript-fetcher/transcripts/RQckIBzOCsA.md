# Transcript: The Folder Structure That Makes AI Build Better Software

**URL:** https://www.youtube.com/watch?v=RQckIBzOCsA
**Segments:** 360
**Channel:** AI Code That Works
**Duration:** 14:24
**Uploaded:** 2026-06-21

---

## Full Text

Quad code is not a magic AI brain. It's a folder structure. That's it. And the day that finally clicked for me is the day my whole stack stopped flaking out because I quit trying to make the AI smarter and started building the folders it reads instead. Here's the part nobody tells you. The single most powerful piece of infrastructure in the whole setup isn't a model. Isn't a plugin. Isn't some $40 a month tool. It's the shape of your project on disk. The folders, the files, what sits where. Get it right and regular AI does brilliant work session after session. Get it wrong and the smartest model on earth guesses, drifts, and quietly wrecks your project while swearing everything is fine. So, stick with me. I'm going to show you the exact skeleton I run. The one file at the root that does most of the work, the four folders around it, and the rules that keep it from rotting. By the end, you'll be able to start layering it into your own project tonight. [music] Hi, I'm Alex Brockway and a year ago, I couldn't write a single line of code. Today, real companies run on software that I built. And on this channel, I show you exactly how it's done. Start with the problem because if you've coded with AI for more than a week, you've already felt it. You just didn't have a name for it. An AI agent is only as good as the context it's holding right this second. That's the whole ball game. And there are [music] two opposite ways to get it wrong. Some dump everything into one enormous prompt, every rule, every fact, every preference. A wall of text a mile long. And the AI drowns in it. It can't tell what matters. So, it half reads it and guesses. The other camp gives it almost nothing. A one-line ask, and the AI fills the silence with whatever it invents. Too much, and it drowns. Too little, and it guesses. [music] Both end in the same place. Code that compiles, looks plausible, and is quietly wrong. And here's the move that kills both at once. You don't fix it with a smarter model. You fix it with structure. You build a small, deliberate set of folders, and [music] at the root, you put one short file whose entire job is to point the AI at the right context for the right task in front of it. For each kind of work, it loads just the right files, the exact context that job needs. Your structure is deterministic. The AI just walks it. It's another layer riding on top. So, let's build it, the way I actually run it. And the first [music] piece is the most important one in the whole system. At the root of your project sits one file. In Claude code, it's literally called claude.md. And it is the agent's front door. The first file it reads every session. And here's the rule almost everyone gets wrong. That file routes, it does not contain. >> [music] >> Its job is to point, not to hold. The heart of it is a little table. The kind of work on the left, the file to read first on the right. Doing UI work, read the build rules file. Touching the database, verify the schema first, then read the data layer doc. The router doesn't try to know everything. It knows where everything lives and sends the AI to the right shelf. It's the front desk of a big building. The person at the [music] desk doesn't answer every question. They just know exactly which floor to send you to. And I cannot oversell how much this one decision matters. Because the opposite is the most common way these setups collapse. People make that root file a knowledge dump. Every rule, every fact, every convention crammed into the front door until it's a wall of text a mile high. And the AI can't use it. It's the drowning problem all over again. >> [music] >> Built into the one file the AI reads first. The router points, the detail lives in the file it points to. Keep the front door thin and I mean it. No more than 200 lines. Okay. So, the router sends the AI somewhere. Where? Three more layers, each with one clear job. First, [music] a rules layer. In Claude code, that's a folder called .claude. This is where the conventions live. Your build rules, your design system rules, the catalog of components you reuse so the AI stops reinventing a button that already exists. These are the standards the AI follows on every decision and they sit in their own files so the router can point at the right one for the job. Don't make the AI guess your conventions. Write them down once and let the router hand them over when they're needed. Second, a knowledge layer. One reference file, the technical truth about your project, the facts the AI would otherwise re-derive from scratch every session sitting in one place where it can just look them up. Decide a fact once, write it down, and it stops getting re-litigated every time you open a new chat. And third, my favorite and the one most people skip, a documentation layer. But here's the trick that makes it actually work and it's not obvious. You split your docs by lifespan, not by topic. By how long the document stays true. Four folders inside. One, active. Your living plans, >> [music] >> the work in flight, updated as you go. Two, decisions. I'll come back to this one. It's gold. And three, [music] reference. Run books, registries, integration guides, the references that don't expire. And four, archive. Finished work kept for history. Labeled in plain language, do not follow. Now, why lifespan and not topic? Because a finished plan is dangerous if the AI still treats it as current. You spent a week on a plan, you shipped it. It's done. [music] If it's still sitting in the active pile, your AI reads it next month and starts building toward a target you already hit and moved past. Confidently steering you wrong because you never told it the plan was over. Stale docs are worse than no docs. With no docs, the AI asks. With stale docs, it charges off the wrong way, certain that it's right. So, you move finished work to archive. You stamp it, do not follow, and you mean it. That one label saves you from your own history. Now, the decisions folder. The highest leverage habit in the whole structure. And it costs you about 90 seconds. Every time you choose between two approaches, you pick one database over another, add a library, reject a library, change the architecture, you write a short note. What you chose and why. People call them decision records. And here's what they buy [music] you. Code shows what you did, never the why. Six months from now, you or your AI looks at some choice and goes, "Hmm. Why is it built this way?" And without that note, you re-argue it from scratch. And half the time, you undo a decision you made for a really good reason, but have just simply forgotten. The note freezes the why. Write it down and you never fight that battle twice. So, that's the skeleton. A thin router that points, a rules layer it follows, a knowledge layer it looks facts up in, and docs split by lifespan [music] with decision records freezing the why. Four moving parts, not one of them exotic. They're folders and text files. And here's the part that sounds too good to be true. There is no special tool to install. This entire skeleton can be built right into Claude code. You open the Claude desktop app and that root file, those folders, it already knows how to read all of it. Which means it's also the cheapest path there is. You're using the Claude subscription you already pay for, not renting some middleman platform [music] at API rates to do what a folder and a text file do for free. The most effective setup I found is also the cheapest one. That's not a coincidence. It's the point. Don't vibe code your way around this by bolting on tools. Build the structure. It's free and it's better. Now, let me hand you the ways this goes wrong because knowing the trap is half of not falling in it. The first one's the silent killer and I already hammered it. The router wants to grow. Every new rule will feel like it belongs in the front door. It does not. Let me repeat that. It does not. The moment that file becomes a manual instead of a table of pointers, the AI stops loading it well and the whole system quietly and quickly degrades. So, make this a standing rule in the router itself. The number one rule at the top, the AI asks you before it edits the root Claude.md file. That one file is what everything else depends on. It's sacred. You don't let it drift silently. You approve every change on purpose with intention. Second trap. A structure nobody routes to is just a pile of folders. [music] You can build this whole beautiful skeleton and get zero out of it because the value is never in having the folders. It's in the router actually pointing the AI at the right one. If the AI isn't reading that router first, none of it fires. It's all dead weight. So, the first move every session is read the router, then read the file it sends you to. That's the habit that makes the rest of it real. And the third, don't over fragment. People hear split it into files and make 400 tiny files, and now the AI can't find anything in the mix. The drowning problem wearing a different hat. The goal The goal is a small number of clear, well-named files each with one obvious home. Enough structure that everything has a place, not so much that finding the place is its own job. Here's what this actually gets you and why I run it on real production software every day. Without it, every session starts from zero. You re-explain your conventions and decisions and watch the AI rebuild something it built last week because it had no memory you ever made the call. You become the bottle neck feeding the same background in by hand forever. With the skeleton in place, the AI reads the router, loads the right files, and works from your rules and decisions without you spoon-feeding any of it. The structure does the remembering, so you go back to deciding what to build. And go look at your own project right now. If your AI starts every session blind, if your context is one giant prompt or no prompt at all, you just found the most valuable afternoon of work you'll do all month. Drop a short router file at the root. Stand up those four [music] docs folders. Write one decision record for a call you've already made. You'll learn more in one real attempt than in 10 more videos like this one. So, here's where to go from here. And I mean, come hang out with us on school. I run a school community. And it is packed. Nearly 10 hours of free training including foundations. The free course that takes you from never having written a line of code to actually building real software step-by-step. A free library of starter templates and prompts and a brand new video every single week. All of it completely free. Come join us. The link, it's in the description. And let me spell out exactly what premium is because hardly anyone knows. Premium is the inner membership of that same community. It's where the done-for-you build packs live including the exact folder skeleton from this video. It's simple to describe and it [music] took me real reps to get right. The router thin enough to work, the docs split [music] so stale plans can't poison a session, the standing rule that guards the front door, the mirroring so you're not locked to one AI tool. So, I built it for you. You don't wire it by hand. You download the pack, point your AI at the start file, and it reads it and builds the whole skeleton into your own project. It asks your stack and the kinds of work you do most [music] and walks you through it one step at a time. That pack plus 15 more. Everyone a real piece of production stack I run every [music] day. It's another 10 hours of deeper courses. It's the full resource repository. Every template, prompt, and tool. [music] And it's weekly access to me to get your own build unstuck. >> [music] >> What's free teaches you the pattern. Premium hands you the working machine and puts you in the room with me. But you do not have to start there >> [music] >> and honestly, most people shouldn't. Everything you need to begin is completely [music] free. Grab the build kit and the free course. It's all at aicodethatworks.com. [music] Then, come find us in the community. Head on over there. We're excited to work with you. Again, the link it's in the description. So that's the folder as architecture skeleton. The reason Claude code is underneath all the noise, just a folder structure that already knows how to be effective. You stop trying to make the AI smarter and you build the folders it reads. Go set it up and hit subscribe. I put out a new video like this every week. See you on the next one.

---

## Timestamped Segments

**[0:00]** Quad code is not a magic AI brain. It's

**[0:04]** a folder structure. That's it. And the

**[0:07]** day that finally clicked for me is the

**[0:09]** day my whole stack stopped flaking out

**[0:12]** because I quit trying to make the AI

**[0:14]** smarter and started building the folders

**[0:16]** it reads instead.

**[0:18]** Here's the part nobody tells you. The

**[0:20]** single most powerful piece of

**[0:23]** infrastructure in the whole setup isn't

**[0:26]** a model.

**[0:27]** Isn't a plugin. Isn't some $40 a month

**[0:31]** tool. It's the shape of your project on

**[0:34]** disk. The folders, the files,

**[0:37]** what sits where.

**[0:39]** Get it right and regular AI does

**[0:41]** brilliant work session after session.

**[0:44]** Get it wrong and the smartest model on

**[0:47]** earth guesses, drifts, and quietly

**[0:50]** wrecks your project while swearing

**[0:52]** everything is fine. So, stick with me.

**[0:55]** I'm going to show you the exact skeleton

**[0:57]** I run. The one file at the root that

**[0:59]** does most of the work, the four folders

**[1:02]** around it, and the rules that keep it

**[1:04]** from rotting.

**[1:05]** By the end, you'll be able to start

**[1:07]** layering it into your own project

**[1:09]** tonight. [music]

**[1:10]** Hi, I'm Alex Brockway and a year ago, I

**[1:13]** couldn't write a single line of code.

**[1:14]** Today, real companies run on software

**[1:17]** that I built. And on this channel, I

**[1:19]** show you exactly how it's done.

**[1:21]** Start with the problem because if you've

**[1:23]** coded with AI for more than a week,

**[1:26]** you've already felt it. You just didn't

**[1:28]** have a name for it. An AI agent is only

**[1:31]** as good as the context it's holding

**[1:33]** right this second. That's the whole ball

**[1:35]** game. And there are [music] two opposite

**[1:38]** ways to get it wrong.

**[1:39]** Some dump everything into one enormous

**[1:42]** prompt, every rule, every fact, every

**[1:45]** preference. A wall of text a mile long.

**[1:48]** And the AI drowns in it. It can't tell

**[1:50]** what matters. So, it half reads it and

**[1:53]** guesses. The other camp gives it almost

**[1:56]** nothing. A one-line ask, and the AI

**[1:59]** fills the silence with whatever it

**[2:01]** invents.

**[2:02]** Too much, and it drowns. Too little, and

**[2:05]** it guesses. [music]

**[2:06]** Both end in the same place. Code that

**[2:09]** compiles, looks plausible, and is

**[2:11]** quietly wrong. And here's the move that

**[2:14]** kills both at once. You don't fix it

**[2:16]** with a smarter model. You fix it with

**[2:18]** structure. You build a small, deliberate

**[2:21]** set of folders, and [music] at the root,

**[2:23]** you put one short file whose entire job

**[2:26]** is to point the AI at the right context

**[2:29]** for the right task in front of it.

**[2:31]** For each kind of work, it loads just the

**[2:34]** right files, the exact context that job

**[2:37]** needs. Your structure is deterministic.

**[2:40]** The AI just walks it. It's another layer

**[2:43]** riding on top.

**[2:45]** So, let's build it, the way I actually

**[2:47]** run it. And the first [music] piece is

**[2:49]** the most important one in the whole

**[2:51]** system.

**[2:52]** At the root of your project sits one

**[2:55]** file. In Claude code, it's literally

**[2:57]** called claude.md.

**[3:00]** And it is the agent's front door. The

**[3:04]** first file it reads every session. And

**[3:07]** here's the rule almost everyone gets

**[3:09]** wrong. That file routes, it does not

**[3:11]** contain.

**[3:12]** >> [music]

**[3:13]** >> Its job is to point, not to hold. The

**[3:16]** heart of it is a little table. The kind

**[3:18]** of work on the left, the file to read

**[3:21]** first on the right. Doing UI work, read

**[3:24]** the build rules file. Touching the

**[3:26]** database, verify the schema first, then

**[3:28]** read the data layer doc. The router

**[3:30]** doesn't try to know everything. It knows

**[3:32]** where everything lives and sends the AI

**[3:35]** to the right shelf.

**[3:37]** It's the front desk of a big building.

**[3:39]** The person at the [music] desk doesn't

**[3:40]** answer every question. They just know

**[3:42]** exactly which floor to send you to. And

**[3:45]** I cannot oversell how much this one

**[3:47]** decision matters. Because the opposite

**[3:50]** is the most common way these setups

**[3:51]** collapse. People make that root file a

**[3:54]** knowledge dump. Every rule, every fact,

**[3:57]** every convention crammed into the front

**[4:00]** door until it's a wall of text a mile

**[4:02]** high.

**[4:03]** And the AI can't use it. It's the

**[4:05]** drowning problem all over again.

**[4:07]** >> [music]

**[4:07]** >> Built into the one file the AI reads

**[4:09]** first. The router points, the detail

**[4:12]** lives in the file it points to. Keep the

**[4:14]** front door thin and I mean it. No more

**[4:18]** than 200 lines. Okay. So, the router

**[4:21]** sends the AI somewhere. Where? Three

**[4:23]** more layers, each with one clear job.

**[4:27]** First, [music] a rules layer. In Claude

**[4:29]** code, that's a folder called .claude.

**[4:32]** This is where the conventions live. Your

**[4:34]** build rules, your design system rules,

**[4:37]** the catalog of components you reuse so

**[4:39]** the AI stops reinventing a button that

**[4:41]** already exists. These are the standards

**[4:44]** the AI follows on every decision and

**[4:47]** they sit in their own files so the

**[4:49]** router can point at the right one for

**[4:51]** the job. Don't make the AI guess your

**[4:53]** conventions. Write them down once and

**[4:56]** let the router hand them over when

**[4:58]** they're needed. Second, a knowledge

**[5:00]** layer. One reference file, the technical

**[5:03]** truth about your project, the facts the

**[5:06]** AI would otherwise re-derive from

**[5:08]** scratch every session sitting in one

**[5:11]** place where it can just look them up.

**[5:13]** Decide a fact once, write it down, and

**[5:16]** it stops getting re-litigated every time

**[5:18]** you open a new chat. And third, my

**[5:21]** favorite and the one most people skip, a

**[5:24]** documentation layer. But here's the

**[5:26]** trick that makes it actually work and

**[5:28]** it's not obvious. You split your docs by

**[5:31]** lifespan, not by topic. By how long the

**[5:34]** document stays true. Four folders

**[5:36]** inside. One, active. Your living plans,

**[5:40]** >> [music]

**[5:40]** >> the work in flight, updated as you go.

**[5:43]** Two, decisions. I'll come back to this

**[5:46]** one. It's gold. And three, [music]

**[5:48]** reference. Run books, registries,

**[5:52]** integration guides, the references that

**[5:54]** don't expire. And four,

**[5:57]** archive. Finished work kept for history.

**[6:00]** Labeled in plain language, do not

**[6:03]** follow.

**[6:04]** Now, why lifespan and not topic? Because

**[6:07]** a finished plan is dangerous if the AI

**[6:10]** still treats it as current. You spent a

**[6:12]** week on a plan, you shipped it. It's

**[6:14]** done. [music]

**[6:15]** If it's still sitting in the active

**[6:17]** pile, your AI reads it next month and

**[6:19]** starts building toward a target you

**[6:21]** already hit and moved past. Confidently

**[6:24]** steering you wrong because you never

**[6:26]** told it the plan was over. Stale docs

**[6:28]** are worse than no docs. With no docs,

**[6:31]** the AI asks. With stale docs, it charges

**[6:34]** off the wrong way, certain that it's

**[6:36]** right. So, you move finished work to

**[6:39]** archive. You stamp it, do not follow,

**[6:42]** and you mean it. That one label saves

**[6:44]** you from your own history.

**[6:46]** Now, the decisions folder. The highest

**[6:49]** leverage habit in the whole structure.

**[6:51]** And it costs you about 90 seconds.

**[6:54]** Every time you choose between two

**[6:56]** approaches, you pick one database over

**[6:58]** another, add a library, reject a

**[7:00]** library, change the architecture, you

**[7:03]** write a short note. What you chose and

**[7:06]** why. People call them decision records.

**[7:09]** And here's what they buy [music] you.

**[7:11]** Code shows what you did, never the why.

**[7:15]** Six months from now, you or your AI

**[7:18]** looks at some choice and goes, "Hmm.

**[7:22]** Why is it built this way?" And without

**[7:24]** that note, you re-argue it from scratch.

**[7:28]** And half the time, you undo a decision

**[7:30]** you made for a really good reason, but

**[7:31]** have just simply forgotten.

**[7:34]** The note freezes the why. Write it down

**[7:37]** and you never fight that battle twice.

**[7:40]** So, that's the skeleton. A thin router

**[7:42]** that points, a rules layer it follows, a

**[7:46]** knowledge layer it looks facts up in,

**[7:48]** and docs split by lifespan [music] with

**[7:50]** decision records freezing the why.

**[7:53]** Four moving parts, not one of them

**[7:55]** exotic. They're folders and text files.

**[7:59]** And here's the part that sounds too good

**[8:01]** to be true. There is no special tool to

**[8:04]** install. This entire skeleton can be

**[8:07]** built right into Claude code. You open

**[8:10]** the Claude desktop app and that root

**[8:12]** file, those folders, it already knows

**[8:14]** how to read all of it. Which means it's

**[8:16]** also the cheapest path there is. You're

**[8:18]** using the Claude subscription you

**[8:20]** already pay for, not renting some

**[8:22]** middleman platform [music] at API rates

**[8:25]** to do what a folder and a text file do

**[8:27]** for free.

**[8:29]** The most effective setup I found is also

**[8:32]** the cheapest one. That's not a

**[8:33]** coincidence. It's the point. Don't vibe

**[8:36]** code your way around this by bolting on

**[8:38]** tools. Build the structure. It's free

**[8:42]** and it's better.

**[8:44]** Now, let me hand you the ways this goes

**[8:46]** wrong because knowing the trap is half

**[8:48]** of not falling in it. The first one's

**[8:51]** the silent killer and I already hammered

**[8:53]** it. The router wants to grow. Every new

**[8:56]** rule will feel like it belongs in the

**[8:58]** front door. It does not. Let me repeat

**[9:00]** that. It does not. The moment that file

**[9:04]** becomes a manual instead of a table of

**[9:06]** pointers, the AI stops loading it well

**[9:09]** and the whole system quietly and quickly

**[9:12]** degrades. So, make this a standing rule

**[9:14]** in the router itself. The number one

**[9:17]** rule at the top, the AI asks you before

**[9:20]** it edits the root Claude.md file. That

**[9:23]** one file is what everything else depends

**[9:26]** on. It's sacred. You don't let it drift

**[9:29]** silently. You approve every change on

**[9:32]** purpose with intention.

**[9:35]** Second trap. A structure nobody routes

**[9:38]** to is just a pile of folders. [music]

**[9:40]** You can build this whole beautiful

**[9:42]** skeleton and get zero out of it because

**[9:44]** the value is never in having the

**[9:46]** folders. It's in the router actually

**[9:48]** pointing the AI at the right one. If the

**[9:51]** AI isn't reading that router first, none

**[9:53]** of it fires. It's all dead weight. So,

**[9:56]** the first move every session is read the

**[9:59]** router, then read the file it sends you

**[10:02]** to. That's the habit that makes the rest

**[10:04]** of it real.

**[10:05]** And the third, don't over fragment.

**[10:08]** People hear split it into files and make

**[10:11]** 400 tiny files, and now the AI can't

**[10:14]** find anything in the mix.

**[10:16]** The drowning problem wearing a different

**[10:19]** hat.

**[10:20]** The goal

**[10:21]** The goal is a small number of clear,

**[10:23]** well-named files each with one obvious

**[10:26]** home. Enough structure that everything

**[10:28]** has a place, not so much that finding

**[10:31]** the place is its own job.

**[10:33]** Here's what this actually gets you and

**[10:36]** why I run it on real production software

**[10:39]** every day.

**[10:40]** Without it, every session starts from

**[10:42]** zero.

**[10:43]** You re-explain your conventions and

**[10:45]** decisions and watch the AI rebuild

**[10:48]** something it built last week because it

**[10:50]** had no memory you ever made the call.

**[10:53]** You become the bottle neck feeding the

**[10:55]** same background in by hand forever.

**[10:58]** With the skeleton in place, the AI reads

**[11:00]** the router, loads the right files, and

**[11:03]** works from your rules and decisions

**[11:06]** without you spoon-feeding any of it. The

**[11:09]** structure does the remembering, so you

**[11:11]** go back to deciding what to build.

**[11:15]** And go look at your own project right

**[11:16]** now. If your AI starts every session

**[11:19]** blind, if your context is one giant

**[11:22]** prompt or no prompt at all, you just

**[11:25]** found the most valuable afternoon of

**[11:27]** work you'll do all month.

**[11:29]** Drop a short router file at the root.

**[11:32]** Stand up those four [music] docs

**[11:34]** folders. Write one decision record for a

**[11:37]** call you've already made. You'll learn

**[11:39]** more in one real attempt than in 10 more

**[11:42]** videos like this one.

**[11:45]** So, here's where to go from here. And I

**[11:47]** mean, come hang out with us on school. I

**[11:50]** run a school community.

**[11:52]** And it is packed. Nearly 10 hours of

**[11:55]** free training including foundations. The

**[11:57]** free course that takes you from never

**[11:59]** having written a line of code to

**[12:01]** actually building real software

**[12:03]** step-by-step.

**[12:05]** A free library of starter templates and

**[12:07]** prompts and a brand new video every

**[12:10]** single week. All of it completely free.

**[12:13]** Come join us. The link, it's in the

**[12:16]** description.

**[12:17]** And let me spell out exactly what

**[12:20]** premium is because hardly anyone knows.

**[12:23]** Premium is the inner membership of that

**[12:25]** same community. It's where the

**[12:27]** done-for-you build packs live including

**[12:30]** the exact folder skeleton from this

**[12:32]** video.

**[12:33]** It's simple to describe and it [music]

**[12:35]** took me real reps to get right. The

**[12:37]** router thin enough to work, the docs

**[12:39]** split [music] so stale plans can't

**[12:41]** poison a session, the standing rule that

**[12:44]** guards the front door, the mirroring so

**[12:46]** you're not locked to one AI tool.

**[12:49]** So, I built it for you.

**[12:51]** You don't wire it by hand. You download

**[12:53]** the pack, point your AI at the start

**[12:55]** file, and it reads it and builds the

**[12:57]** whole skeleton into your own project. It

**[13:00]** asks your stack and the kinds of work

**[13:03]** you do most [music]

**[13:03]** and walks you through it one step at a

**[13:06]** time.

**[13:07]** That pack plus 15 more. Everyone a real

**[13:11]** piece of production stack I run every

**[13:13]** [music] day.

**[13:14]** It's another 10 hours of deeper courses.

**[13:16]** It's the full resource repository. Every

**[13:19]** template, prompt, and tool. [music] And

**[13:22]** it's weekly access to me to get your own

**[13:25]** build unstuck.

**[13:26]** >> [music]

**[13:26]** >> What's free teaches you the pattern.

**[13:29]** Premium hands you the working machine

**[13:31]** and puts you in the room with me.

**[13:33]** But you do not have to start there

**[13:35]** >> [music]

**[13:35]** >> and honestly, most people shouldn't.

**[13:38]** Everything you need to begin is

**[13:39]** completely [music]

**[13:40]** free.

**[13:41]** Grab the build kit and the free course.

**[13:44]** It's all at aicodethatworks.com. [music]

**[13:47]** Then, come find us in the community.

**[13:50]** Head on over there. We're excited to

**[13:52]** work with you. Again, the link it's in

**[13:55]** the description.

**[13:56]** So that's the folder as architecture

**[13:58]** skeleton. The reason Claude code is

**[14:01]** underneath all the noise, just a folder

**[14:04]** structure that already knows how to be

**[14:06]** effective. You stop trying to make the

**[14:08]** AI smarter and you build the folders it

**[14:11]** reads.

**[14:12]** Go set it up and hit subscribe. I put

**[14:14]** out a new video like this every week.

**[14:17]** See you on the next one.
