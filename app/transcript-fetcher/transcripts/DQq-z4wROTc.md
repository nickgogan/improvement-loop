# Transcript: Loop Engineering Explained by Claude Code Creators | Self Improving Agentic Loop

**URL:** https://www.youtube.com/watch?v=DQq-z4wROTc
**Segments:** 205
**Channel:** Cloud Codes
**Duration:** 8:31
**Uploaded:** 2026-06-26

---

## Full Text

Here is a story that sounds made up. An engineer types one sentence into Claude code and goes to make coffee. He comes back and 40 agents have spun up, written code, checked each other, and left him three pull requests to review. He did not write 40 prompts. He wrote one loop. And that one sentence, I wrote one loop, is quietly rewriting how the best engineers work with AI. It started with a single line. You should not be prompting your coding agents anymore. You should be designing the loops that prompt them for you. Then the head of Claude code at Anthropic said it out loud. I do not prompt Claude anymore. I have loops running that prompt Claude and figure out what to do. My job is to write loops. In a single week of June 2026, it got a name, loop engineering, and a 12-page field guide that spread everywhere. For 2 years, the deal was simple. You write a prompt, you read what comes back, you write the next one. You are the tool, and your hand is on it the whole time. You were the loop, the thing standing between every step, reading the output, catching the mistake, deciding what happens next, telling it to try again. Loop engineering is stepping out of that inner cycle and up a level to designing the track the agent runs on. You build it once and let it poke the agents instead of you. Because strip away the jargon, and a loop is just four moves on repeat. Discover the work, plan it, execute it, verify it, then repeat until a condition you set is actually true. And here is the part nobody tells you. A loop is a generator wired to a verifier. The generator was never the bottleneck. The verifier is. Hold that thought. Step back and look at the line this sits on. 2024, you wrote prompts. You were an operator. 2025, you ran several agents at once, a manager. 2026, you design the system that runs them, a system designer. Think of it as a stack. First, the prompt, then the context, then the harness. Everything a single agent run gets. Loop engineering sits one floor above the harness. It is the outer system that runs the harness on a timer. At its simplest, a loop is almost dumb. Goal, get the test suite passing. Loop, run the tests, read the failures, fix the likely cause, run again, stop when everything is green or after six rounds. That is a real loop and it works. A loop that actually holds together needs five pieces and one place to remember things. The five pieces are what the agent uses. The memory is what keeps the whole thing from forgetting itself. First, automations, the heartbeat. Something fires on a schedule, does discovery and triage by itself, and drops what it finds into an inbox. This is what makes it a loop and not just one run you did once. Second, work trees. The moment you run two agents, their files start colliding. A Git work tree gives each one its own checkout on its own branch, so one agent literally cannot touch the other one's work. Third, skills. A skill is your project knowledge written down once. The conventions, the build steps, the thing you only do this way because of that one incident. Without it, the loop rederives your whole project from zero every single cycle. Fourth, connectors. Built on MCP, they let the loop reach your real tools, the issue tracker, the database, Slack, Stripe. This is the difference between an agent that says, "Here is the fix." and a loop that opens the pull request itself. Fifth, sub agents. The single most useful move in a loop is splitting the one who writes from the one who checks. The model that wrote the code is far too kind grading its own homework. A second agent with different instructions catches what the first one talked itself into. And then the sixth thing, the memory. A markdown file, a linear board, anything that lives outside the single conversation and holds what is done and what is next. The agent forgets everything between runs. The repo does not. The memory is the spine. Now back to that thought. Every loop has two halves. A generator that produces work, that is the model, and models are now extremely good. And a verifier that judges whether the work is any good. For two years we obsessed over the generator, but in a loop the generator runs over and over for almost nothing. So watch what a weak verifier does. Make this landing page better. Keep going. No definition of better. It rewrites the hero eight times, each one different, none clearly better, and reports success. You just paid real money for motion without progress. That is the slop machine. Here is the mental flip. Writing a verifier is writing a reward function. You are not training the model, you are defining what good means. Your taste, your judgment, your sense of what correct looks like in your problem, that is the moat. The model is a commodity, which is why you never let an agent grade its own work. It always gives itself an A. So Claude Code's goal command hands the stop decision to a separate faster model. The one that wrote the code is not the one that says it is done. That makes the real engineering decision clear. A closed-loop pins success up front, checks every step, and stops on command. Predictable, cheap, safe to leave alone. An open loop gets a goal and room to explore. That is where novel solutions live, but it burns tokens and slides into slop fast. And the trick that rescues the open loop, keep your hard checks as the floor, then add one open instruction, surprise me with the headline. Now you get exploration that simply cannot drop below your standard. The verifier is what makes either kind ship. You do not build the machinery from scratch. There is a clear ladder from rigid to autonomous, a bare shell loop where you are the stop button, the goal command where a small model judges done, goal tracking setups, and always-on agents that never sleep. The rule, pick the least autonomous tool that does the job. Then it compounds. One loop answers support tickets every 30 minutes and logs what it learns into a shared folder. Another writes content. Another prioritizes the roadmap. They all read and write the same files, so what one loop learns every other loop picks up. One builder runs this and ships 20 to 40 pages a day without watching. For any of it to work, the code base has to be ready for agents, legible so it can find what to change, executable so the dev server is already up, and verifiable, give it away to prove the work like a browser test that records a clip you can actually watch. But the loop does not delete you from the work, and three problems get sharper, not easier. Verification is still on you. Done is a claim, not a proof. Your understanding rots if you stop reading what the loop made, and the comfortable move, just taking whatever it hands back, is the dangerous one. Is it just a buzzword? Honestly, partly. The term was coined to ride attention, and some of it repackages what agent builders already knew. So ignore the word and check the shift. Are you designing systems that run agents now instead of prompting them? Yes. Is defining them the scarce skill? Yes. The label is optional. The shift is not. And this is the part that matters most. Two people build the exact same loop and get opposite results. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. The loop does not know the difference. You do. So, that is loop engineering. Stop prompting the agent. Design the loop that prompts it. Five pieces and a memory. A generator wired to a verifier, where the verifier is the whole game. Build it once and stay the engineer. If that finally made loop engineering click, subscribe. Cloud Code takes apart one system like this every single week. Build, solve, deploy. And I will see you in the next one.

---

## Timestamped Segments

**[0:00]** Here is a story that sounds made up. An

**[0:02]** engineer types one sentence into Claude

**[0:05]** code and goes to make coffee. He comes

**[0:07]** back and 40 agents have spun up, written

**[0:10]** code, checked each other, and left him

**[0:12]** three pull requests to review. He did

**[0:15]** not write 40 prompts. He wrote one loop.

**[0:18]** And that one sentence, I wrote one loop,

**[0:21]** is quietly rewriting how the best

**[0:23]** engineers work with AI. It started with

**[0:26]** a single line. You should not be

**[0:28]** prompting your coding agents anymore.

**[0:30]** You should be designing the loops that

**[0:32]** prompt them for you. Then the head of

**[0:34]** Claude code at Anthropic said it out

**[0:36]** loud. I do not prompt Claude anymore. I

**[0:39]** have loops running that prompt Claude

**[0:41]** and figure out what to do. My job is to

**[0:43]** write loops. In a single week of June

**[0:46]** 2026, it got a name, loop engineering,

**[0:50]** and a 12-page field guide that spread

**[0:52]** everywhere. For 2 years, the deal was

**[0:54]** simple. You write a prompt, you read

**[0:57]** what comes back, you write the next one.

**[0:59]** You are the tool, and your hand is on it

**[1:01]** the whole time. You were the loop, the

**[1:04]** thing standing between every step,

**[1:06]** reading the output, catching the

**[1:08]** mistake, deciding what happens next,

**[1:10]** telling it to try again. Loop

**[1:12]** engineering is stepping out of that

**[1:14]** inner cycle and up a level to designing

**[1:17]** the track the agent runs on. You build

**[1:20]** it once and let it poke the agents

**[1:22]** instead of you. Because strip away the

**[1:24]** jargon, and a loop is just four moves on

**[1:26]** repeat. Discover the work, plan it,

**[1:29]** execute it, verify it, then repeat until

**[1:32]** a condition you set is actually true.

**[1:35]** And here is the part nobody tells you. A

**[1:37]** loop is a generator wired to a verifier.

**[1:40]** The generator was never the bottleneck.

**[1:43]** The verifier is. Hold that thought. Step

**[1:45]** back and look at the line this sits on.

**[1:48]** 2024, you wrote prompts. You were an

**[1:50]** operator. 2025, you ran several agents

**[1:54]** at once, a manager. 2026, you design the

**[1:57]** system that runs them, a system

**[1:59]** designer. Think of it as a stack. First,

**[2:02]** the prompt, then the context, then the

**[2:04]** harness. Everything a single agent run

**[2:07]** gets. Loop engineering sits one floor

**[2:10]** above the harness. It is the outer

**[2:12]** system that runs the harness on a timer.

**[2:15]** At its simplest, a loop is almost dumb.

**[2:18]** Goal, get the test suite passing. Loop,

**[2:21]** run the tests, read the failures, fix

**[2:24]** the likely cause, run again, stop when

**[2:27]** everything is green or after six rounds.

**[2:29]** That is a real loop and it works. A loop

**[2:32]** that actually holds together needs five

**[2:34]** pieces and one place to remember things.

**[2:37]** The five pieces are what the agent uses.

**[2:40]** The memory is what keeps the whole thing

**[2:42]** from forgetting itself. First,

**[2:44]** automations, the heartbeat. Something

**[2:47]** fires on a schedule, does discovery and

**[2:49]** triage by itself, and drops what it

**[2:52]** finds into an inbox. This is what makes

**[2:55]** it a loop and not just one run you did

**[2:57]** once. Second, work trees. The moment you

**[3:00]** run two agents, their files start

**[3:02]** colliding. A Git work tree gives each

**[3:05]** one its own checkout on its own branch,

**[3:07]** so one agent literally cannot touch the

**[3:10]** other one's work. Third, skills. A skill

**[3:13]** is your project knowledge written down

**[3:15]** once. The conventions, the build steps,

**[3:18]** the thing you only do this way because

**[3:19]** of that one incident. Without it, the

**[3:22]** loop rederives your whole project from

**[3:24]** zero every single cycle.

**[3:27]** Fourth, connectors. Built on MCP, they

**[3:30]** let the loop reach your real tools, the

**[3:32]** issue tracker, the database, Slack,

**[3:35]** Stripe. This is the difference between

**[3:37]** an agent that says, "Here is the fix."

**[3:39]** and a loop that opens the pull request

**[3:41]** itself.

**[3:43]** Fifth, sub agents. The single most

**[3:45]** useful move in a loop is splitting the

**[3:47]** one who writes from the one who checks.

**[3:50]** The model that wrote the code is far too

**[3:52]** kind grading its own homework. A second

**[3:55]** agent with different instructions

**[3:57]** catches what the first one talked itself

**[3:59]** into. And then the sixth thing, the

**[4:01]** memory. A markdown file, a linear board,

**[4:05]** anything that lives outside the single

**[4:07]** conversation and holds what is done and

**[4:09]** what is next. The agent forgets

**[4:11]** everything between runs. The repo does

**[4:14]** not. The memory is the spine. Now back

**[4:17]** to that thought. Every loop has two

**[4:20]** halves. A generator that produces work,

**[4:23]** that is the model, and models are now

**[4:25]** extremely good. And a verifier that

**[4:27]** judges whether the work is any good. For

**[4:30]** two years we obsessed over the

**[4:32]** generator, but in a loop the generator

**[4:34]** runs over and over for almost nothing.

**[4:37]** So watch what a weak verifier does. Make

**[4:40]** this landing page better. Keep going. No

**[4:43]** definition of better. It rewrites the

**[4:45]** hero eight times, each one different,

**[4:48]** none clearly better, and reports

**[4:50]** success. You just paid real money for

**[4:53]** motion without progress. That is the

**[4:55]** slop machine. Here is the mental flip.

**[4:58]** Writing a verifier is writing a reward

**[5:01]** function. You are not training the

**[5:03]** model, you are defining what good means.

**[5:06]** Your taste, your judgment, your sense of

**[5:09]** what correct looks like in your problem,

**[5:11]** that is the moat. The model is a

**[5:13]** commodity, which is why you never let an

**[5:16]** agent grade its own work. It always

**[5:18]** gives itself an A. So Claude Code's goal

**[5:21]** command hands the stop decision to a

**[5:23]** separate faster model. The one that

**[5:26]** wrote the code is not the one that says

**[5:28]** it is done. That makes the real

**[5:30]** engineering decision clear. A

**[5:32]** closed-loop pins success up front,

**[5:34]** checks every step, and stops on command.

**[5:37]** Predictable, cheap, safe to leave alone.

**[5:40]** An open loop gets a goal and room to

**[5:42]** explore. That is where novel solutions

**[5:45]** live, but it burns tokens and slides

**[5:48]** into slop fast. And the trick that

**[5:50]** rescues the open loop, keep your hard

**[5:52]** checks as the floor, then add one open

**[5:55]** instruction, surprise me with the

**[5:57]** headline. Now you get exploration that

**[5:59]** simply cannot drop below your standard.

**[6:02]** The verifier is what makes either kind

**[6:04]** ship. You do not build the machinery

**[6:07]** from scratch. There is a clear ladder

**[6:09]** from rigid to autonomous, a bare shell

**[6:12]** loop where you are the stop button, the

**[6:14]** goal command where a small model judges

**[6:17]** done, goal tracking setups, and

**[6:20]** always-on agents that never sleep. The

**[6:22]** rule, pick the least autonomous tool

**[6:25]** that does the job. Then it compounds.

**[6:28]** One loop answers support tickets every

**[6:30]** 30 minutes and logs what it learns into

**[6:32]** a shared folder. Another writes content.

**[6:36]** Another prioritizes the roadmap. They

**[6:38]** all read and write the same files, so

**[6:41]** what one loop learns every other loop

**[6:43]** picks up.

**[6:45]** One builder runs this and ships 20 to 40

**[6:47]** pages a day without watching. For any of

**[6:50]** it to work, the code base has to be

**[6:52]** ready for agents, legible so it can find

**[6:55]** what to change, executable so the dev

**[6:58]** server is already up, and verifiable,

**[7:01]** give it away to prove the work like a

**[7:03]** browser test that records a clip you can

**[7:05]** actually watch. But the loop does not

**[7:07]** delete you from the work, and three

**[7:09]** problems get sharper, not easier.

**[7:12]** Verification is still on you. Done is a

**[7:15]** claim, not a proof. Your understanding

**[7:17]** rots if you stop reading what the loop

**[7:19]** made, and the comfortable move, just

**[7:22]** taking whatever it hands back, is the

**[7:24]** dangerous one.

**[7:25]** Is it just a buzzword? Honestly, partly.

**[7:28]** The term was coined to ride attention,

**[7:31]** and some of it repackages what agent

**[7:33]** builders already knew. So ignore the

**[7:35]** word and check the shift. Are you

**[7:37]** designing systems that run agents now

**[7:40]** instead of prompting them? Yes. Is

**[7:42]** defining them the scarce skill? Yes. The

**[7:45]** label is optional. The shift is not. And

**[7:48]** this is the part that matters most. Two

**[7:50]** people build the exact same loop and get

**[7:53]** opposite results. One uses it to move

**[7:55]** faster on work they understand deeply.

**[7:58]** The other uses it to avoid understanding

**[8:00]** the work at all. The loop does not know

**[8:02]** the difference. You do. So, that is loop

**[8:05]** engineering. Stop prompting the agent.

**[8:08]** Design the loop that prompts it. Five

**[8:10]** pieces and a memory. A generator wired

**[8:13]** to a verifier, where the verifier is the

**[8:15]** whole game. Build it once and stay the

**[8:17]** engineer. If that finally made loop

**[8:20]** engineering click, subscribe. Cloud Code

**[8:23]** takes apart one system like this every

**[8:25]** single week. Build, solve, deploy. And I

**[8:29]** will see you in the next one.
