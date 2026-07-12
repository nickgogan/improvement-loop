# Transcript: The Skill vs Prompt Problem Everyone Gets Wrong

**URL:** https://www.youtube.com/watch?v=9PUaEj0pMYE
**Segments:** 532
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 17:45
**Uploaded:** 2026-06-19

---

## Full Text

A lot of us have an AI agent with a brain now. It still probably doesn't know how to work as well as it should. So, a few weeks ago I made a video called Open Brain. The argument was simple. Agents are becoming real, and if they're going to do useful work for you, they need access to your context in a way that works for you. They need to know what you're working on. They need to know what you decided last week. They need to know who the important people are. They need to know what you already tried, and they need memory that's not trapped inside one app, one SaaS product, one model provider, one brain for every AI. And that video has struck a chord because it named a bottleneck that we were all feeling, right? Every serious AI workflow still started with the same miserable ritual. Let me re-explain my life to this machine again. But, there is a second problem that shows up as soon as you solve the memory problem. And I've seen it enough that I want to talk about it here and talk about how I'm solving it. Even if the agent knows what you know, it may still not know how you work. It may know the project, it may know the people, it may know the decision history thanks to Open Brain. And then you still have to explain the procedure from scratch, and you still have to say when you research this, don't trust Dale model memory. You still have to say when you write for me, don't sound like a generic AI newsletter. You still have to say when you test this page, actually open the browser and check mobile and capture evidence, and don't just tell me it looks good. You still have to say, when you publish something, verify the live result. All of these things you have to re-explain, and that is not a memory problem. You can have a perfect Open Brain setup, and it still works that way. So, procedure problem. And people using agents seriously are starting to feel it as a procedural debt. And you can see this in at least four different places across serious workers' workflows. First, in prompt blow. People keep stuffing more rules into giant system prompts or markdown files, and then wondering why the agent gets worse. And it's because every preference and edge case and repo note and safety reminder and formatting instruction fights the others for attention. At some point, that stops being clarity and it just adds weight. Second, the re-explanation tax. Every new chat, every fresh agent session, every switch from cursor to Claude code to Codex means you have to explain your voice and your testing standard and your project patterns and your safe commands and your definition of done all over again. That's not work. That's setup work pretending to be work. Third, instruction fragmentation. You end up with one set of rules in one tool, another set in another tool, repo specific notes somewhere else, and custom instructions that slowly drift away from each other. Fourth, weak verification turns automation into a pile of review debt for you and me. Cuz the agent will say done, but the source is stale and the link is broken and the mobile view is bad or the change was never tested, so the human still has to inspect so much. The agent didn't remove the work in some cases, it just moved the work into the review stage. This is the problem space Open Skills is built for, and I'm launching it today. It's not that prompts are annoying, it's that agent work is developing procedural debt at exactly the moment agents are becoming capable of persistent action. Take a small product team at a startup that ships with both cursor and Claude code on the same codebase. Let's say they spent weeks tuning a solid set of cursor rules, security boundaries, when to write tests, get workflow expectations, how to handle large refactors, and the project's architectural patterns. And it works really well inside cursor. Then they started using Claude code for bigger multi-file changes. And the rules didn't travel very cleanly. So one engineer ended up maintaining two versions of the same guidance, one in cursor rules and another in a Claude.md file. Over time, those files tended to drift. One got updated with a new testing rule after a painful incident, the other still said the old thing. And then a contractor joined the project and got handed a long onboarding prompt that tried to summarize both files. And it sounded comprehensive, but it was vague on the details that actually prevented bad devs. The team is not short on intelligence in this situation, and they're not short on contacts. They're short on a portable way to carry the procedure itself. That is the gap Open Skills is designed to close. It's a gap in a multimodal world. That's what this video is about. It's not a prompt trick, it's not a list of clever AI hacks, it's not another folder of reusable wording. Open Skills is a public library of reusable agent procedures. The current version has 31 skills and seven categories and seven runbooks. Each skill comes with a copy-paste setup prompt, and the pattern is designed to work across Codex, Claude Code, and any other agent harness that can load a skill.markdown style convention. And I want to be precise about differentiation here, because this is not happening in a vacuum. A lot of the agent world is moving toward modular instructions. Individual tools have their own rule systems. Coding agents have their own markdown files. People are sharing tool-specific skills and cursor rules and agent instructions and those sync scripts that keep those files from drifting. That is all the right direction, but Open Skills is making a more specific bet. The differentiated piece here is not skills exist. You can find skills. The differentiated piece is portable procedures as an operating layer. One markdown source of truth, narrow skills as primitives, runbooks as compositions, and verification as part of the contract. Personal scope when the procedure belongs to you, and project scope when the procedure belongs to the repo. And a flywheel that turns repeated work into reusable skill candidates instead of letting the pattern disappear into old chat history. So, if Open Skills becomes just another list of useful prompts, I failed. It blends into everything else. That's not what this is. But, if it stays focused on portability and composition and verification and scope and compounding, it's a different layer. It's a needed layer. So, what is a skill, right? A skill is usually a small folder with a skill.markdown file inside it. That's the simple version. The file tells the agent when to use the skill, when not to use the skill, what job the skill owns, what tools or files it should use, what boundaries apply, what output should look like, and how to verify the results. That's the unit. Not a clever paragraph, not a vibe, not a one-time chat, not a prompt. A reusable procedure an agent can load when the situation calls for it. A prompt is something you say once, and a skill is something your agent knows how to do from now on. If I give an agent a prompt that says fact-check this article, that's a request. If I give an agent a current information search skill, that's a procedure. It can say use live search when the claim is recent, when pricing might have changed, when the software version matters, or when training data might be stale. It can say compare sources and show the date and separate consumed facts from inference. If I give an agent a current information search skill, that's a procedure. It can say use live search when the claim is recent, when pricing might have changed, when the software version matters, or when training data might be stale. It can say compare sources and show the date and separate confirmed facts from inference and let uncertainty block publishing if needed. Same thing with voice. If I say write this in my voice, the model has to guess. If I have a personal voice skill, it can tell the agent which real samples to read, which phrases to avoid, how long the sentences are, what argument structure works, and what fake AI language ought to be stripped out. Same thing with testing. If I say test the page, the agent may tell me it looks fine. If I have a browser QA skill, it can say open the actual route, check the console, check mobile, verify the changed workflow, capture screenshots, and report the evidence. The procedure is the valuable part. That's the thing to take away from these three. The words are not enough. This is the same structural mismatch I talked about in the open brain video, but one level higher. Open brain said most second brain tools were built for human readers. That was true. They were useful, but they were not designed as agent-readable memory infrastructure. Open skills says most SOPs and prompts and checklists and docs and preferences have the same problem. They may be readable by a person, but they're not packaged as agent-operable procedures. They don't have trigger rules. They don't say when not to run. They don't identify required tools. They don't define the output. They don't define the verification, and they don't travel cleanly from one agent harness to another. This is why the current world feels so painfully repetitive, so copy and paste. You have five AI tools and five separate piles of procedural sticky notes. One tool knows a little about how you write another as a project instruction, another as repo rules, another as a custom instruction box, and another one as a chat history where you explained everything perfectly, and you can never find it again. That is not a working system. That is just procedural sprawl. The answer is not a giant magical instruction block that says, "Be my perfect employee." That doesn't work. It's too broad. It's too vague. It can't be tested. It just isn't practical. The better path, the practical path, is a library of small, inspectable procedures that can be called from anywhere when needed. That's the answer to prompt bloat. Don't put every rule in the agent's head all the time. Give it a clean way to load the right procedure when the work calls for it. And once you have skills that are transferable, the next step is runbooks. Skills are primitives. Runbooks are composition. Both are part of open skills. A skill answers, "What can this agent do?" A runbook answers, "What can the system reliably produce?" Take the creator workflow. A voice memo becomes a published page. That sounds like one task, but it's really a chain. Media transcription turns the audio into a transcript. Brain dump processing separates the real ideas from the rambling. Personal voice turns the best idea into a draft that sounds like the person. HTML artifact builder turns the draft into a usable page. Personal site publisher ships it with the right route and the right metadata and the link preview and verification. That is a runbook. Or take release day. Something important ships, and you want to publish a useful, accurate briefing while the facts still matter. Current information search gathers the facts. New release briefing turns those facts into a publishable package. Image prompting and generation create the visuals. Site publisher ships the page, and stakeholder update closes the loop when something is actually live. That is speed with a quality bar. The point is not that one giant agent or giant skill knows everything. The point is that each skill owns a piece, and those skills are LEGO blocks, and they're composable. So, in that world, the transcription skill doesn't need to know how to publish, right? The voice skill doesn't need to know how to test a browser. The publisher doesn't need to know how to generate visuals. Each skill owns a specific contract. The runbook owns the flow. That's how real work gets done. And this is where the word open matters a lot. Open does not mean every skill is public by default. Open doesn't mean you paste secrets into a shared file. Open doesn't even mean every agent should be able to do everything. The skill becomes the source of truth. Cursor rules and Claude files and Codex instructions or whatever comes next can read from it or be generated from it instead of becoming separate drifting copies. Some procedures are personal. My voice is personal. My publishing habits are personal. My standards for a stakeholder update are personal. Other procedures are project local. The way you test a specific app should live with that app. The safe commands for one repo should not become universal rules for every repo. The known selectors and seed data and cleanup steps and deployment quirks should live where the project lives. That is another reason skills are not just prompts. They can be placed in the right scope. Global when the procedure belongs to you. Local when the procedure belongs to the project, and that is how you keep the system clean instead of turning it into a giant pile of preferences that are a mixture of yours and the team's. The other big thing skills give you is verification. This is where the agent conversation needs to get much more serious. As long as AI was mostly writing text, a lot of people tolerated vague confidence. Just being honest here. But with agents, vague confidence is not enough. If the agent edited code, what test passed? If I built a page, what browser did it open? If I published something, what URL did it check? If it summarized a source, what source did it actually read? If it used current facts, what date did it verify? A good skill can define that proof ahead of time. It can say, "Do not call this done unless this evidence exists." That one sentence changes a lot because agents are very good at producing plausible completion language and they're less reliable when the definition of done is vague. So, don't make it a vibe. Put it in the skill. That's how you turn automation from review debt into leverage. And there's one more piece that matters, the flywheel. One skill in the library I'm launching today is called session to skill extractor. The idea is simple, but it's very powerful. At the end of a substantial agent session, ask, "Did we learn a recurring non-obvious procedure worth preserving?" Most of the time the answer should be no, and that's part of the quality bar. You don't want to turn every little preference into a skill, but sometimes the answer is yes. Sometimes you discover a testing pattern or or a publishing checklist or a way to process transcripts or a repeatable source gathering process. And when that happens, the procedure should not disappear with that chat into the compost pile. It should become a skill candidate. That is the same compounding logic as Open Brain, but applied to procedures that help you work. Open Brain compounds because every thought you capture makes future retrieval better. That's how it works. Open Skills compounds because every good procedure you preserve makes future work more reliable. And that's where the leverage is now. And the real power is when the two systems come together. Open Brain gives the agent the context, the project, the audience, the decisions, the prior work, the constraints. Open Skills gives the agent the procedure, how to research, how to write, how to build, how to test, how to publish, and how to report what changed in a multimodal world where you can't be sure what model's going to be best next. And look at how this changes things for us. Right now, we humans are not spending the whole session saying, "Here's the background. Here's how I like this done." We humans can do the real work. And that gap, the ability to focus on real work, that compounds every week with open skills. It compounds every time a new model ships and you don't have to switch and cost yourself so much time. It compounds every time you try a new agent tool and you can bring open skills over because you are less locked into the memory and workflow assumptions of any one vendor. They don't deserve to have that. You do. You can move your context. You can move your procedures. You can plug better tools into the same operating layer. That is what open is supposed to mean here. Not vagueness, practical portability. Your thoughts, every AI, free for you to use. Your workflows, every agent. That is the callback to open bring here. It's the same spirit and that's why open skills is not a prompt library. A prompt library is way too small for this problem. It just doesn't work in 2026 in the same way. Open skills is more like a public operating manual for agent work. The value of open skills is not really in the 31 markdown files. Although they're really good. The value is that every single file has a job, a scope, a trigger, a boundary, and a proof standard. That's what separates open skills from the broader wave of skills and rules. We need to have and we deserve to have skills that are transferable with clear runbooks associated. Because this is bigger than skills. You can build with these skills once and you can recombine them forever in any AI you want. That is the heart of what open skills is about. Skills don't make agents perfect. Runbooks still require human judgment. AI skills are not magical autonomy people, but the real promise of open skills is still incredibly powerful. Because open skills means you don't have to explain the same procedure forever. It means you don't have to keep your working style in your head. You don't have to accept that every agent tool has its own separate pile of instructions. You can write the procedure down in a way an agent can load. That's open skills. You can inspect it. You can improve it. You can put it in the right scope and you can compose it into larger workflows. And you can carry it forward as the tools change. That matters. So, the decision rule is simple. If you do something with an agent once, a prompt is fine. If you are comfortable living in a world where you have to reacquire skills all the time and manually remember to set up loops to add to your skills as you go, and then you have skill draft as you have Codex and Claude Code and Cursor in the mix, great, more power to you. If you want a solution that you can control, that's Open Skills. And that's what I'm launching today. If you want more information, you can check out the URL I'm showing right on the screen right now, and you'll get all set up to go from there. I can't wait to see you there. Open Brain has been just an incredible opportunity for the community to collaborate around building a memory system that is ours to control and not some SaaS companies. I want Open Skills to be the same thing. It's a chance for all of us to contribute to a building set of skills that help us to be in charge of our work even as tools evolve and change. So, we can stay flexible, so we can grow, so our skills come with us. You know, a few weeks ago, I shared the reflection that one of the big challenges of the AI era is how a skilled knowledge worker moves from job to job and what they do with their skills that they acquire with AI along the way. Open Skills is that answer. Bring your Open Skills to work and then take them with you when you go. Open Skills help you be more effective across any AI tool that your work is going to throw at you and across your personal tools as well. If you're a company, Open Skills is a way for you and your teams to be more productive. Because we anticipate the team level. That's an important part of how we build meaningful things in the AI age. I do not believe the future is just a one-person billion-dollar company. As much as that's fun, there will be some of them. I think a lot of the future is humans building cool things together, and Open Skills is a powerful way to do that as well. So, check out Open Skills. I'm so excited for it. I think it solves one of the most persistent and painful issues I've seen in the skills ecosystem. It should not be hard to move your skills between different AIs. It should not be hard to evolve your skills over time, and it should not be hard to compose your skills into runbooks. Open Skills solves for all of that. Check it out, have fun with it, and contribute to the build. Let's make it great together. Cheers.

---

## Timestamped Segments

**[0:00]** A lot of us have an AI agent with a

**[0:02]** brain now. It still probably doesn't

**[0:04]** know how to work as well as it should.

**[0:05]** So, a few weeks ago I made a video

**[0:07]** called Open Brain. The argument was

**[0:09]** simple. Agents are becoming real, and if

**[0:11]** they're going to do useful work for you,

**[0:12]** they need access to your context in a

**[0:14]** way that works for you. They need to

**[0:16]** know what you're working on. They need

**[0:17]** to know what you decided last week. They

**[0:19]** need to know who the important people

**[0:21]** are. They need to know what you already

**[0:23]** tried, and they need memory that's not

**[0:25]** trapped inside one app, one SaaS

**[0:27]** product, one model provider, one brain

**[0:30]** for every AI. And that video has struck

**[0:32]** a chord because it named a bottleneck

**[0:34]** that we were all feeling, right? Every

**[0:36]** serious AI workflow still started with

**[0:38]** the same miserable ritual. Let me

**[0:40]** re-explain my life to this machine

**[0:43]** again. But, there is a second problem

**[0:45]** that shows up as soon as you solve the

**[0:47]** memory problem. And I've seen it enough

**[0:49]** that I want to talk about it here and

**[0:50]** talk about how I'm solving it. Even if

**[0:52]** the agent knows what you know, it may

**[0:54]** still not know how you work. It may know

**[0:57]** the project, it may know the people, it

**[0:59]** may know the decision history thanks to

**[1:01]** Open Brain. And then you still have to

**[1:03]** explain the procedure from scratch, and

**[1:05]** you still have to say when you research

**[1:06]** this, don't trust Dale model memory. You

**[1:08]** still have to say when you write for me,

**[1:10]** don't sound like a generic AI

**[1:12]** newsletter. You still have to say when

**[1:14]** you test this page, actually open the

**[1:16]** browser and check mobile and capture

**[1:17]** evidence, and don't just tell me it

**[1:19]** looks good. You still have to say, when

**[1:22]** you publish something, verify the live

**[1:24]** result. All of these things you have to

**[1:26]** re-explain, and that is not a memory

**[1:28]** problem. You can have a perfect Open

**[1:30]** Brain setup, and it still works that

**[1:31]** way. So, procedure problem. And people

**[1:34]** using agents seriously are starting to

**[1:36]** feel it as a procedural debt. And you

**[1:38]** can see this in at least four different

**[1:40]** places across serious workers'

**[1:42]** workflows. First, in prompt blow. People

**[1:45]** keep stuffing more rules into giant

**[1:47]** system prompts or markdown files, and

**[1:49]** then wondering why the agent gets worse.

**[1:52]** And it's because every preference and

**[1:53]** edge case and repo note and safety

**[1:55]** reminder and formatting instruction

**[1:57]** fights the others for attention. At some

**[1:59]** point, that stops being clarity and it

**[2:01]** just adds weight. Second, the

**[2:04]** re-explanation tax. Every new chat,

**[2:06]** every fresh agent session, every switch

**[2:08]** from cursor to Claude code to Codex

**[2:11]** means you have to explain your voice and

**[2:12]** your testing standard and your project

**[2:14]** patterns and your safe commands and your

**[2:15]** definition of done all over again.

**[2:17]** That's not work. That's setup work

**[2:20]** pretending to be work. Third,

**[2:21]** instruction fragmentation. You end up

**[2:23]** with one set of rules in one tool,

**[2:25]** another set in another tool, repo

**[2:27]** specific notes somewhere else, and

**[2:28]** custom instructions that slowly drift

**[2:30]** away from each other. Fourth, weak

**[2:32]** verification turns automation into a

**[2:35]** pile of review debt for you and me. Cuz

**[2:37]** the agent will say done, but the source

**[2:39]** is stale and the link is broken and the

**[2:40]** mobile view is bad or the change was

**[2:42]** never tested, so the human still has to

**[2:44]** inspect so much. The agent didn't remove

**[2:47]** the work in some cases, it just moved

**[2:48]** the work into the review stage. This is

**[2:50]** the problem space Open Skills is built

**[2:52]** for, and I'm launching it today. It's

**[2:54]** not that prompts are annoying, it's that

**[2:56]** agent work is developing procedural debt

**[2:59]** at exactly the moment agents are

**[3:01]** becoming capable of persistent action.

**[3:03]** Take a small product team at a startup

**[3:05]** that ships with both cursor and Claude

**[3:07]** code on the same codebase. Let's say

**[3:08]** they spent weeks tuning a solid set of

**[3:10]** cursor rules, security boundaries, when

**[3:12]** to write tests, get workflow

**[3:13]** expectations, how to handle large

**[3:15]** refactors, and the project's

**[3:17]** architectural patterns. And it works

**[3:18]** really well inside cursor. Then they

**[3:20]** started using Claude code for bigger

**[3:22]** multi-file changes. And the rules didn't

**[3:25]** travel very cleanly. So one engineer

**[3:27]** ended up maintaining two versions of the

**[3:28]** same guidance, one in cursor rules and

**[3:30]** another in a Claude.md file. Over time,

**[3:33]** those files tended to drift. One got

**[3:35]** updated with a new testing rule after a

**[3:37]** painful incident, the other still said

**[3:39]** the old thing. And then a contractor

**[3:41]** joined the project and got handed a long

**[3:43]** onboarding prompt that tried to

**[3:44]** summarize both files. And it sounded

**[3:46]** comprehensive, but it was vague on the

**[3:48]** details that actually prevented bad

**[3:50]** devs. The team is not short on

**[3:52]** intelligence in this situation, and

**[3:53]** they're not short on contacts. They're

**[3:55]** short on a portable way to carry the

**[3:57]** procedure itself. That is the gap Open

**[4:00]** Skills is designed to close. It's a gap

**[4:02]** in a multimodal world. That's what this

**[4:04]** video is about. It's not a prompt trick,

**[4:06]** it's not a list of clever AI hacks, it's

**[4:08]** not another folder of reusable wording.

**[4:11]** Open Skills is a public library of

**[4:13]** reusable agent procedures. The current

**[4:15]** version has 31 skills and seven

**[4:17]** categories and seven runbooks. Each

**[4:19]** skill comes with a copy-paste setup

**[4:21]** prompt, and the pattern is designed to

**[4:22]** work across Codex, Claude Code, and any

**[4:25]** other agent harness that can load a

**[4:26]** skill.markdown style convention. And I

**[4:29]** want to be precise about differentiation

**[4:31]** here, because this is not happening in a

**[4:32]** vacuum. A lot of the agent world is

**[4:34]** moving toward modular instructions.

**[4:36]** Individual tools have their own rule

**[4:37]** systems. Coding agents have their own

**[4:39]** markdown files. People are sharing

**[4:40]** tool-specific skills and cursor rules

**[4:43]** and agent instructions and those sync

**[4:45]** scripts that keep those files from

**[4:46]** drifting. That is all the right

**[4:48]** direction, but Open Skills is making a

**[4:50]** more specific bet. The differentiated

**[4:52]** piece here is not skills exist. You can

**[4:54]** find skills. The differentiated piece is

**[4:57]** portable procedures as an operating

**[4:59]** layer. One markdown source of truth,

**[5:02]** narrow skills as primitives, runbooks as

**[5:04]** compositions, and verification as part

**[5:07]** of the contract. Personal scope when the

**[5:09]** procedure belongs to you, and project

**[5:11]** scope when the procedure belongs to the

**[5:12]** repo. And a flywheel that turns repeated

**[5:15]** work into reusable skill candidates

**[5:17]** instead of letting the pattern disappear

**[5:19]** into old chat history.

**[5:20]** So, if Open Skills becomes just another

**[5:22]** list of useful prompts, I failed. It

**[5:24]** blends into everything else. That's not

**[5:26]** what this is. But, if it stays focused

**[5:28]** on portability and composition and

**[5:30]** verification and scope and compounding,

**[5:33]** it's a different layer. It's a needed

**[5:35]** layer. So, what is a skill, right? A

**[5:36]** skill is usually a small folder with a

**[5:39]** skill.markdown file inside it. That's

**[5:40]** the simple version. The file tells the

**[5:42]** agent when to use the skill, when not to

**[5:44]** use the skill, what job the skill owns,

**[5:45]** what tools or files it should use, what

**[5:48]** boundaries apply, what output should

**[5:49]** look like, and how to verify the

**[5:50]** results. That's the unit. Not a clever

**[5:53]** paragraph, not a vibe, not a one-time

**[5:54]** chat, not a prompt. A reusable procedure

**[5:56]** an agent can load when the situation

**[5:59]** calls for it. A prompt is something you

**[6:01]** say once, and a skill is something your

**[6:02]** agent knows how to do from now on. If I

**[6:04]** give an agent a prompt that says

**[6:06]** fact-check this article, that's a

**[6:07]** request. If I give an agent a current

**[6:09]** information search skill, that's a

**[6:11]** procedure. It can say use live search

**[6:12]** when the claim is recent, when pricing

**[6:14]** might have changed, when the software

**[6:15]** version matters, or when training data

**[6:16]** might be stale. It can say compare

**[6:18]** sources and show the date and separate

**[6:20]** consumed facts from inference. If I give

**[6:22]** an agent a current information search

**[6:23]** skill, that's a procedure. It can say

**[6:25]** use live search when the claim is

**[6:26]** recent, when pricing might have changed,

**[6:28]** when the software version matters, or

**[6:30]** when training data might be stale. It

**[6:32]** can say compare sources and show the

**[6:33]** date and separate confirmed facts from

**[6:35]** inference and let uncertainty block

**[6:37]** publishing if needed. Same thing with

**[6:39]** voice. If I say write this in my voice,

**[6:41]** the model has to guess. If I have a

**[6:43]** personal voice skill, it can tell the

**[6:45]** agent which real samples to read, which

**[6:47]** phrases to avoid, how long the sentences

**[6:49]** are, what argument structure works, and

**[6:51]** what fake AI language ought to be

**[6:52]** stripped out. Same thing with testing.

**[6:54]** If I say test the page, the agent may

**[6:56]** tell me it looks fine. If I have a

**[6:57]** browser QA skill, it can say open the

**[7:00]** actual route, check the console, check

**[7:01]** mobile, verify the changed workflow,

**[7:03]** capture screenshots, and report the

**[7:05]** evidence. The procedure is the valuable

**[7:07]** part. That's the thing to take away from

**[7:08]** these three. The words are not enough.

**[7:11]** This is the same structural mismatch I

**[7:13]** talked about in the open brain video,

**[7:16]** but one level higher. Open brain said

**[7:18]** most second brain tools were built for

**[7:20]** human readers. That was true. They were

**[7:22]** useful, but they were not designed as

**[7:23]** agent-readable memory infrastructure.

**[7:25]** Open skills says most SOPs and prompts

**[7:28]** and checklists and docs and preferences

**[7:30]** have the same problem. They may be

**[7:33]** readable by a person, but they're not

**[7:34]** packaged as agent-operable procedures.

**[7:37]** They don't have trigger rules. They

**[7:39]** don't say when not to run. They don't

**[7:40]** identify required tools. They don't

**[7:42]** define the output. They don't define the

**[7:44]** verification, and they don't travel

**[7:46]** cleanly from one agent harness to

**[7:48]** another.

**[7:49]** This is why the current world feels so

**[7:51]** painfully repetitive, so copy and paste.

**[7:55]** You have five AI tools and five separate

**[7:58]** piles of procedural sticky notes. One

**[8:00]** tool knows a little about how you write

**[8:01]** another as a project instruction,

**[8:03]** another as repo rules, another as a

**[8:05]** custom instruction box, and another one

**[8:06]** as a chat history where you explained

**[8:08]** everything perfectly, and you can never

**[8:10]** find it again. That is not a working

**[8:12]** system. That is just procedural sprawl.

**[8:15]** The answer is not a giant magical

**[8:17]** instruction block that says, "Be my

**[8:19]** perfect employee." That doesn't work.

**[8:21]** It's too broad. It's too vague. It can't

**[8:23]** be tested. It just isn't practical. The

**[8:25]** better path, the practical path, is a

**[8:27]** library of small, inspectable procedures

**[8:30]** that can be called from anywhere when

**[8:32]** needed. That's the answer to prompt

**[8:34]** bloat. Don't put every rule in the

**[8:36]** agent's head all the time. Give it a

**[8:38]** clean way to load the right procedure

**[8:40]** when the work calls for it. And once you

**[8:41]** have skills that are transferable, the

**[8:44]** next step is runbooks. Skills are

**[8:46]** primitives. Runbooks are composition.

**[8:49]** Both are part of open skills. A skill

**[8:51]** answers, "What can this agent do?" A

**[8:52]** runbook answers, "What can the system

**[8:54]** reliably produce?" Take the creator

**[8:56]** workflow. A voice memo becomes a

**[8:58]** published page. That sounds like one

**[9:00]** task, but it's really a chain. Media

**[9:02]** transcription turns the audio into a

**[9:04]** transcript. Brain dump processing

**[9:06]** separates the real ideas from the

**[9:07]** rambling. Personal voice turns the best

**[9:10]** idea into a draft that sounds like the

**[9:11]** person. HTML artifact builder turns the

**[9:14]** draft into a usable page. Personal site

**[9:16]** publisher ships it with the right route

**[9:18]** and the right metadata and the link

**[9:19]** preview and verification. That is a

**[9:21]** runbook. Or take release day. Something

**[9:23]** important ships, and you want to publish

**[9:25]** a useful, accurate briefing while the

**[9:27]** facts still matter. Current information

**[9:29]** search gathers the facts. New release

**[9:31]** briefing turns those facts into a

**[9:32]** publishable package. Image prompting and

**[9:34]** generation create the visuals. Site

**[9:36]** publisher ships the page, and

**[9:38]** stakeholder update closes the loop when

**[9:40]** something is actually live. That is

**[9:42]** speed with a quality bar. The point is

**[9:44]** not that one giant agent or giant skill

**[9:46]** knows everything. The point is that each

**[9:48]** skill owns a piece, and those skills are

**[9:51]** LEGO blocks, and they're composable. So,

**[9:53]** in that world, the transcription skill

**[9:55]** doesn't need to know how to publish,

**[9:56]** right? The voice skill doesn't need to

**[9:58]** know how to test a browser. The

**[9:59]** publisher doesn't need to know how to

**[10:01]** generate visuals. Each skill owns a

**[10:03]** specific contract. The runbook owns the

**[10:05]** flow. That's how real work gets done.

**[10:08]** And this is where the word open matters

**[10:10]** a lot. Open does not mean every skill is

**[10:12]** public by default. Open doesn't mean you

**[10:14]** paste secrets into a shared file. Open

**[10:17]** doesn't even mean every agent should be

**[10:18]** able to do everything. The skill becomes

**[10:21]** the source of truth. Cursor rules and

**[10:23]** Claude files and Codex instructions or

**[10:25]** whatever comes next can read from it or

**[10:27]** be generated from it instead of becoming

**[10:29]** separate drifting copies. Some

**[10:31]** procedures are personal. My voice is

**[10:33]** personal. My publishing habits are

**[10:34]** personal. My standards for a stakeholder

**[10:36]** update are personal. Other procedures

**[10:39]** are project local. The way you test a

**[10:41]** specific app should live with that app.

**[10:43]** The safe commands for one repo should

**[10:45]** not become universal rules for every

**[10:46]** repo. The known selectors and seed data

**[10:49]** and cleanup steps and deployment quirks

**[10:51]** should live where the project lives.

**[10:53]** That is another reason skills are not

**[10:55]** just prompts. They can be placed in the

**[10:57]** right scope. Global when the procedure

**[10:59]** belongs to you. Local when the procedure

**[11:00]** belongs to the project, and that is how

**[11:02]** you keep the system clean instead of

**[11:05]** turning it into a giant pile of

**[11:06]** preferences that are a mixture of yours

**[11:08]** and the team's. The other big thing

**[11:09]** skills give you is verification. This is

**[11:11]** where the agent conversation needs to

**[11:13]** get much more serious. As long as AI was

**[11:15]** mostly writing text, a lot of people

**[11:17]** tolerated vague confidence. Just being

**[11:20]** honest here. But with agents, vague

**[11:22]** confidence is not enough. If the agent

**[11:24]** edited code, what test passed? If I

**[11:26]** built a page, what browser did it open?

**[11:28]** If I published something, what URL did

**[11:30]** it check? If it summarized a source,

**[11:32]** what source did it actually read? If it

**[11:34]** used current facts, what date did it

**[11:36]** verify? A good skill can define that

**[11:38]** proof ahead of time. It can say, "Do not

**[11:41]** call this done unless this evidence

**[11:42]** exists." That one sentence changes a lot

**[11:45]** because agents are very good at

**[11:46]** producing plausible completion language

**[11:48]** and they're less reliable when the

**[11:50]** definition of done is vague. So, don't

**[11:52]** make it a vibe. Put it in the skill.

**[11:54]** That's how you turn automation from

**[11:56]** review debt into leverage. And there's

**[11:58]** one more piece that matters, the

**[11:59]** flywheel. One skill in the library I'm

**[12:01]** launching today is called session to

**[12:03]** skill extractor. The idea is simple, but

**[12:06]** it's very powerful. At the end of a

**[12:07]** substantial agent session, ask, "Did we

**[12:10]** learn a recurring non-obvious procedure

**[12:12]** worth preserving?" Most of the time the

**[12:13]** answer should be no, and that's part of

**[12:15]** the quality bar. You don't want to turn

**[12:17]** every little preference into a skill,

**[12:19]** but sometimes the answer is yes.

**[12:20]** Sometimes you discover a testing pattern

**[12:22]** or or a publishing checklist or a way to

**[12:24]** process transcripts or a repeatable

**[12:26]** source gathering process. And when that

**[12:28]** happens, the procedure should not

**[12:30]** disappear with that chat into the

**[12:31]** compost pile. It should become a skill

**[12:33]** candidate. That is the same compounding

**[12:35]** logic as Open Brain, but applied to

**[12:37]** procedures that help you work. Open

**[12:39]** Brain compounds because every thought

**[12:41]** you capture makes future retrieval

**[12:43]** better. That's how it works. Open Skills

**[12:45]** compounds because every good procedure

**[12:47]** you preserve makes future work more

**[12:51]** reliable. And that's where the leverage

**[12:53]** is now. And the real power is when the

**[12:55]** two systems come together. Open Brain

**[12:57]** gives the agent the context, the

**[12:58]** project, the audience, the decisions,

**[13:00]** the prior work, the constraints. Open

**[13:02]** Skills gives the agent the procedure,

**[13:04]** how to research, how to write, how to

**[13:05]** build, how to test, how to publish, and

**[13:07]** how to report what changed in a

**[13:09]** multimodal world where you can't be sure

**[13:12]** what model's going to be best next. And

**[13:14]** look at how this changes things for us.

**[13:16]** Right now, we humans are not spending

**[13:18]** the whole session saying, "Here's the

**[13:19]** background. Here's how I like this

**[13:21]** done." We humans can do the real work.

**[13:24]** And that gap, the ability to focus on

**[13:27]** real work, that compounds every week

**[13:29]** with open skills. It compounds every

**[13:30]** time a new model ships and you don't

**[13:32]** have to switch and cost yourself so much

**[13:34]** time. It compounds every time you try a

**[13:36]** new agent tool and you can bring open

**[13:37]** skills over because you are less locked

**[13:39]** into the memory and workflow assumptions

**[13:41]** of any one vendor. They don't deserve to

**[13:43]** have that. You do. You can move your

**[13:45]** context. You can move your procedures.

**[13:47]** You can plug better tools into the same

**[13:50]** operating layer. That is what open is

**[13:52]** supposed to mean here. Not vagueness,

**[13:55]** practical portability. Your thoughts,

**[13:57]** every AI, free for you to use. Your

**[14:00]** workflows, every agent. That is the

**[14:01]** callback to open bring here. It's the

**[14:03]** same spirit and that's why open skills

**[14:05]** is not a prompt library. A prompt

**[14:07]** library is way too small for this

**[14:09]** problem. It just doesn't work in 2026 in

**[14:11]** the same way. Open skills is more like a

**[14:13]** public operating manual for agent work.

**[14:16]** The value of open skills is not really

**[14:18]** in the 31 markdown files. Although

**[14:21]** they're really good. The value is that

**[14:23]** every single file has a job, a scope, a

**[14:26]** trigger, a boundary, and a proof

**[14:28]** standard. That's what separates open

**[14:30]** skills from the broader wave of skills

**[14:32]** and rules. We need to have and we

**[14:34]** deserve to have skills that are

**[14:36]** transferable with clear runbooks

**[14:39]** associated. Because this is bigger than

**[14:41]** skills. You can build with these skills

**[14:44]** once and you can recombine them forever

**[14:46]** in any AI you want. That is the heart of

**[14:49]** what open skills is about. Skills don't

**[14:52]** make agents perfect. Runbooks still

**[14:54]** require human judgment. AI skills are

**[14:57]** not magical autonomy people, but the

**[14:59]** real promise of open skills is still

**[15:01]** incredibly powerful. Because open skills

**[15:03]** means you don't have to explain the same

**[15:05]** procedure forever. It means you don't

**[15:07]** have to keep your working style in your

**[15:08]** head. You don't have to accept that

**[15:09]** every agent tool has its own separate

**[15:11]** pile of instructions. You can write the

**[15:14]** procedure down in a way an agent can

**[15:15]** load. That's open skills. You can

**[15:17]** inspect it. You can improve it. You can

**[15:18]** put it in the right scope and you can

**[15:20]** compose it into larger workflows. And

**[15:22]** you can carry it forward as the tools

**[15:24]** change. That matters. So, the decision

**[15:26]** rule is simple. If you do something with

**[15:29]** an agent once, a prompt is fine. If you

**[15:31]** are comfortable living in a world where

**[15:33]** you have to reacquire skills all the

**[15:35]** time and manually remember to set up

**[15:37]** loops to add to your skills as you go,

**[15:40]** and then you have skill draft as you

**[15:41]** have Codex and Claude Code and Cursor in

**[15:43]** the mix, great, more power to you. If

**[15:45]** you want a solution that you can

**[15:48]** control, that's Open Skills. And that's

**[15:51]** what I'm launching today. If you want

**[15:52]** more information, you can check out the

**[15:54]** URL I'm showing right on the screen

**[15:56]** right now, and you'll get all set up to

**[15:58]** go from there. I can't wait to see you

**[16:00]** there. Open Brain has been just an

**[16:02]** incredible opportunity for the community

**[16:05]** to collaborate around building a memory

**[16:07]** system that is ours to control and not

**[16:09]** some SaaS companies. I want Open Skills

**[16:11]** to be the same thing. It's a chance for

**[16:14]** all of us to contribute to a building

**[16:17]** set of skills that help us to be in

**[16:20]** charge of our work even as tools evolve

**[16:23]** and change. So, we can stay flexible, so

**[16:25]** we can grow, so our skills come with us.

**[16:28]** You know, a few weeks ago, I shared the

**[16:30]** reflection that one of the big

**[16:32]** challenges of the AI era is how a

**[16:35]** skilled knowledge worker moves from job

**[16:38]** to job and what they do with their

**[16:40]** skills that they acquire with AI along

**[16:42]** the way. Open Skills is that answer.

**[16:45]** Bring your Open Skills to work and then

**[16:47]** take them with you when you go. Open

**[16:49]** Skills help you be more effective across

**[16:52]** any AI tool that your work is going to

**[16:54]** throw at you and across your personal

**[16:55]** tools as well. If you're a company, Open

**[16:58]** Skills is a way for you and your teams

**[17:00]** to be more productive. Because we

**[17:02]** anticipate the team level. That's an

**[17:03]** important part of how we build

**[17:05]** meaningful things in the AI age. I do

**[17:07]** not believe the future is just a

**[17:08]** one-person billion-dollar company. As

**[17:10]** much as that's fun, there will be some

**[17:11]** of them. I think a lot of the future is

**[17:14]** humans building cool things together,

**[17:16]** and Open Skills is a powerful way to do

**[17:17]** that as well. So, check out Open Skills.

**[17:19]** I'm so excited for it. I think it solves

**[17:21]** one of the most persistent and painful

**[17:23]** issues I've seen in the skills

**[17:24]** ecosystem. It should not be hard to move

**[17:27]** your skills between different AIs. It

**[17:30]** should not be hard to evolve your skills

**[17:33]** over time, and it should not be hard to

**[17:35]** compose your skills into runbooks. Open

**[17:38]** Skills solves for all of that. Check it

**[17:40]** out, have fun with it, and contribute to

**[17:42]** the build. Let's make it great together.

**[17:44]** Cheers.
