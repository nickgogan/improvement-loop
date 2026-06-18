# Transcript: hGYfsvlQ5Ok

**URL:** https://www.youtube.com/watch?v=hGYfsvlQ5Ok
**Segments:** 89

---

## Full Text

Enthropic just released the advisor strategy which allows us to not only get better performance from our enthropic models but do it at a lower cost. And the way it works is pretty simple. It pairs opus as an adviser with sonnet or haik coup as an executive. So opus is coming up with a plan and the cheaper model does all the work. So this is very similar to when we're using cloud code and have opus run the plan mode but have the actual execution pass off the sonnet. The difference is with the advisor strategy, this is all done automatically via an API. So this is perfect if you're working on things outside of cloud code. So if you have any sort of web application that uses anthropic APIs under the hood, this is a no-brainer. You're going to get more effective outputs for cheaper. And it's actually a bit more sophisticated than what we do in clawed code with opus planning and then Sonic executing because this advisor exeutor relationship is constantly in flux and it isn't a one-time thing where opus advises one time and then Sonic executes. It actually goes back and forth like it states here when the executive so sonnet or haiku hits a decision it can't reasonably solve it consults opus for guidance as the adviser. Opus has full context of what Sonnet is doing. And so it isn't just like plan mode where it gives it one strategy and then it goes. It's as if you did that and Sonic goes and tries to execute. It hits a stumbling block, then it's going to go back to Opus. So there's a constant back and forth. Furthermore, to keep costs low, Opus isn't doing any tool calls at any point in time. The only tool calls are being done by that smaller LLM, in this case, Sonnet or Haiku. But Opus does retain that full shared context. And like I mentioned in the intro, this gives us better results for less. So right here, it's comparing Sonnet 4.6 High with Opus Advisor versus Sonnet 4.6 High on its own. Sonnet scored higher on Sweet Bench at 74.8 versus 72.1. And it came in cheaper. So it was just over 96 cents per Agentic Task versus almost $19, which is significant. And you see the same thing play out in other benchmarks like browse comp and terminal bench. So 60.4 versus 58.1 and it's cheaper. The cheaper thing is great because as we all know the anthropic APIs are awesome but they're so damn expensive and often times you feel like you want something in between sonnet and opus but that just doesn't exist. So this gives us a middle ground in terms of sonnet and opus performance but with a cost that is cheaper than normal sonnet. So what's not to love? Like I said before, this is an API thing, not necessarily a clawed code thing. So to use this, you're just going to have to adjust your code and how it's actually making those API calls. Specifically, you have to call out the type to be advisor as well as the max uses. Now, the max uses being the number of times it's going to go back to Opus to get advice on a particular issue. So to sum it up, this is an amazing upgrade if you're someone who uses Anthropics API in actual projects outside of the cloud code ecosystem. We're getting better results for cheaper because as you know often times opus is just overkill for the vast majority of things. Yet sometimes you want something a little better with sonet and here we go. This is the perfect middle ground.

---

## Timestamped Segments

**[0:00]** Enthropic just released the advisor

**[0:02]** strategy which allows us to not only get

**[0:04]** better performance from our enthropic

**[0:06]** models but do it at a lower cost. And

**[0:09]** the way it works is pretty simple. It

**[0:10]** pairs opus as an adviser with sonnet or

**[0:13]** haik coup as an executive. So opus is

**[0:16]** coming up with a plan and the cheaper

**[0:18]** model does all the work. So this is very

**[0:20]** similar to when we're using cloud code

**[0:22]** and have opus run the plan mode but have

**[0:24]** the actual execution pass off the

**[0:27]** sonnet. The difference is with the

**[0:29]** advisor strategy, this is all done

**[0:31]** automatically via an API. So this is

**[0:33]** perfect if you're working on things

**[0:34]** outside of cloud code. So if you have

**[0:36]** any sort of web application that uses

**[0:39]** anthropic APIs under the hood, this is a

**[0:41]** no-brainer. You're going to get more

**[0:44]** effective outputs for cheaper. And it's

**[0:46]** actually a bit more sophisticated than

**[0:48]** what we do in clawed code with opus

**[0:50]** planning and then Sonic executing

**[0:52]** because this advisor exeutor

**[0:54]** relationship is constantly in flux and

**[0:57]** it isn't a one-time thing where opus

**[0:59]** advises one time and then Sonic

**[1:01]** executes. It actually goes back and

**[1:02]** forth like it states here when the

**[1:04]** executive so sonnet or haiku hits a

**[1:06]** decision it can't reasonably solve it

**[1:08]** consults opus for guidance as the

**[1:10]** adviser. Opus has full context of what

**[1:14]** Sonnet is doing. And so it isn't just

**[1:16]** like plan mode where it gives it one

**[1:17]** strategy and then it goes. It's as if

**[1:19]** you did that and Sonic goes and tries to

**[1:21]** execute. It hits a stumbling block, then

**[1:23]** it's going to go back to Opus. So

**[1:24]** there's a constant back and forth.

**[1:26]** Furthermore, to keep costs low, Opus

**[1:28]** isn't doing any tool calls at any point

**[1:30]** in time. The only tool calls are being

**[1:32]** done by that smaller LLM, in this case,

**[1:34]** Sonnet or Haiku. But Opus does retain

**[1:37]** that full shared context. And like I

**[1:39]** mentioned in the intro, this gives us

**[1:41]** better results for less. So right here,

**[1:44]** it's comparing Sonnet 4.6 High with Opus

**[1:47]** Advisor versus Sonnet 4.6 High on its

**[1:50]** own. Sonnet scored higher on Sweet Bench

**[1:52]** at 74.8 versus 72.1. And it came in

**[1:56]** cheaper. So it was just over 96 cents

**[1:59]** per Agentic Task versus almost $19,

**[2:02]** which is significant. And you see the

**[2:04]** same thing play out in other benchmarks

**[2:06]** like browse comp and terminal bench. So

**[2:09]** 60.4 versus 58.1 and it's cheaper. The

**[2:12]** cheaper thing is great because as we all

**[2:14]** know the anthropic APIs are awesome but

**[2:16]** they're so damn expensive and often

**[2:19]** times you feel like you want something

**[2:21]** in between sonnet and opus but that just

**[2:23]** doesn't exist. So this gives us a middle

**[2:25]** ground in terms of sonnet and opus

**[2:27]** performance but with a cost that is

**[2:29]** cheaper than normal sonnet. So what's

**[2:31]** not to love? Like I said before, this is

**[2:33]** an API thing, not necessarily a clawed

**[2:35]** code thing. So to use this, you're just

**[2:37]** going to have to adjust your code and

**[2:39]** how it's actually making those API

**[2:40]** calls. Specifically, you have to call

**[2:42]** out the type to be advisor as well as

**[2:45]** the max uses. Now, the max uses being

**[2:48]** the number of times it's going to go

**[2:49]** back to Opus to get advice on a

**[2:51]** particular issue. So to sum it up, this

**[2:53]** is an amazing upgrade if you're someone

**[2:55]** who uses Anthropics API in actual

**[2:57]** projects outside of the cloud code

**[2:59]** ecosystem. We're getting better results

**[3:02]** for cheaper because as you know often

**[3:05]** times opus is just overkill for the vast

**[3:07]** majority of things. Yet sometimes you

**[3:08]** want something a little better with

**[3:09]** sonet and here we go. This is the

**[3:11]** perfect middle ground.
