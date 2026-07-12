# Transcript: AI Gateway: The Layer Every AI Stack Eventually Needs

**URL:** https://www.youtube.com/watch?v=MYPLpkENs7A
**Segments:** 285
**Channel:** Devsplainers
**Duration:** 11:21
**Uploaded:** 2026-07-08

---

## Full Text

The most important piece of your AI stack might be one you never wrote a line off. It sits between your app and every model you call, and the day it goes down, every AI feature you have goes down with [music] it. Teams are all adding this when their AI stack grows mature. It's the AI gateway, and by the end of this video, you'll know exactly what it does, when [music] you actually need one, and the one trade-off that can make a cheaper setup cost you [music] more. You usually get a gateway by accident. On day one, your app just calls a single model with an API key. Then, it grows. You add a second provider because the first one is getting rate limited. A teammate wires the model into a second service. Someone hardcodes an API key into a repo, then copies it into three more. Retry logic gets written from scratch four separate times, slightly wrong each time. And when the invoice comes in, nobody can tell you which feature spent the money. About 3 months in, every team hits the same wall. Five different services all talking to the model directly without any shared logic. One provider gets its model pulled by the government, and half your product goes dark with it. Lucky thing for you, these are all plumbing problems that were there before AI. >> [music] >> Regular web APIs ran into this mess a decade ago, back when auth and rate limiting and logging got copied, pasted into every service until someone finally pulled them out into one shared layer. That layer was the API gateway. The AI gateway is the same idea, but pointed at models. What does this shared layer do? Strip away the marketing, and there are five jobs it's really there for. Most importantly, it's a single standard way to talk to every model. Normally, every provider has a different request format and its own quirks and failure modes. The gateway hides all of that behind one interface. Almost everyone copied the format OpenAI shipped first. So, in practice, you point your code at the gateway, change one line, and swap from one model to another by editing a string. Second, it [music] holds the keys. Instead of the real provider keys floating around your code base, they live in the gateway. Each app gets its own throwaway key that the gateway trades for the real [music] one. Lose one, revoke it, nobody else notices. Third, it retries [music] and fails over. When a provider throws an error or starts rate limiting, the gateway can retry on its own or reroute the request to a backup model before you bother your users with anything. Fourth, it keeps track of everything passing it. Every token in, every token out, tagged by team, by app, [music] by model. That's how you set a budget and enforce it instead of finding out at the end of the month. And fifth, because every request flows through it, it's the natural place to watch everything at once. Latency, errors, and spend on one dashboard. Think of it less like a smart assistant and more like the front desk of a building. Everything checks in there, gets logged, and gets pointed to the right room. Boring and load-bearing. Now for the confusing part, because this corner of the industry has a naming problem. You'll see AI gateway and LLM gateway used for the same thing. If you want to get specific, LLM gateway leans developer and routing, while AI gateway leans enterprise and governance, and now [music] stretches to cover images, audio, and agents. It's fine to interchange them in most cases. >> [music] >> Then, there's the plain API gateway, the decade-old ancestor I mentioned. An AI gateway is that pattern specialized for model traffic. Some products are literally an old API gateway with AI plugins bolted on. The difference is that the AI version reads the prompt. It understands tokens [music] and streaming and model names where the old one just saw web requests go by. Two more you'll bump into. An MCP gateway governs what an agent is allowed to do, meaning the tools it calls, not the model it talks to. And an inference gateway is a lower level thing that spreads traffic across your own GPUs. Are you still with me? Underneath all that, the term AI gateway is doing two jobs at once. Half the time it means a unified proxy that centralizes keys, cost, and logging. The other half it means something smarter, a router that picks the best model for each request. Those are two different products wearing one name, which is where most of the confusion comes from. That second job, routing, is where the real fight is. It comes [music] in two flavors. The first is dumb on purpose and what most production systems run. You write the rules, send cheap requests here, send this customer's traffic there, and if the main model is down, fall back to that one. It's predictable and easy to debug. The second flavor is smart routing, where the gateway tries to read each prompt, guess how hard it is, then send the easy questions to a cheap model, and save the expensive one for the tricky stuff. This routing is also increasingly happening in your favorite frontier coding harness. When it works, the savings are real. An open research project called Route LLM showed you could hold around 95% of a frontier's model's quality while sending only a quarter of the requests [music] its way. Everything else went to a model a fraction of the price, and most people couldn't tell the difference. And when the researchers later swapped in different models on both ends, the [music] routing still held up, which is a big part of why the idea gets taken seriously. You arrive at a catch-22. To reliably know a prompt is too hard for the cheap model, your little router has to understand that prompt about as well as the expensive model would. And if it could do that, you wouldn't [music] need the expensive model. The smarter the routing gets, the closer it creeps to being just another big model sitting in front of your big model. It's still useful to have since a lot of traffic is obviously easy, and a cheap check catches it. Just don't expect the free lunch the pitch decks imply. Which brings us to the trade-off I promised, the one that turns cheaper model into a bigger bill. Modern AI tools lean hard on a warm cache. When you're deep in a session with one model, a lot of your conversation is already sitting in fast memory on the provider's side, ready to reuse. So, you're not paying full freight to reprocess it every turn. There's another video for that if you want to know more. Now, let a smart router switch you to a different model mid-conversation to save a few cents, that new model has no warm cache for [music] you. It has to read the entire conversation again, cold. The one-time cost of that reload can swallow the savings from the cheaper model [music] and then some. You optimized the price per token and blew up the token count instead. [music] The fix is to make the router aware of the cache. Once a model is warm, raise the bar for switching away from it, so you only jump ship when the savings clearly beat the cost of going cold. It's a small idea that plenty of naive routers miss, and it's exactly why just route to whatever's cheapest is worse [music] advice than it sounds. Caching shows up one more place. It's called semantic caching. A normal cache only reuses an answer if the new question is character-for-character identical. Semantic caching goes further. It turns each prompt into a string of numbers that captures its meaning, then checks whether any past question means roughly the same thing. Ask, [music] "What's the capital of France?" and "France capital city, please." and it can serve the [music] same cached answer to both. When it hits, you skip the model entirely. Near zero cost, [music] instant reply. The danger hides in the word roughly. Set the similarity bar too loose and it starts matching questions that look alike but mean opposite things. Sort ascending and sort descending land almost on top of each other in that number space. Match them and the gateway hands someone the wrong answer. Pylon's stale data where a price changed [music] but the cache didn't, plus the fact that upgrading your embedding model can wipe out the whole cache without warning, and you've got a feature that dazzles in a demo and frays nerves in production. Useful, but a knob to turn carefully. Not a switch to leave on. For all that you get out of it, the layer costs you something, [music] too. It adds a hop. Every request now detours through the gateway before it reaches the model. In practice, that overhead is tiny next to the seconds the model itself takes, and a well-run gateway at the edge can even come back faster thanks [music] to better pipes to the providers. But on a truly latency-critical path, measure it yourself. The bigger issue is that you've built a single point of failure. Everything routes through this one layer, so if it all falls over, every AI feature you have falls over with it. The thing you added for reliability becomes the thing that can take you down. You plan for that with backups and ideally a code path that can skip the gateway and call the provider directly in a pinch. Talk about gateway-ception. There's a trust cost, too. This layer holds every one of your API keys in one place. Last year, the most popular open-source gateway, LightLLM, got hit by a supply chain [music] attack where compromised code went straight after those keys. A blunt reminder that the box holding every key is the box attackers most want to crack. So, when do you need an AI gateway? Plenty of teams really don't. If all you call is one provider from one app, call the model directly and skip all of this. A gateway's what you add when your situation turns plural. A second provider, a second service calling models, the first surprise invoice, or the first time someone asked which [music] team spent all the money. The demo everyone leads with, one key for many models, is the least interesting [music] reason this layer exists. Calling a model stopped being something one app does on its own and turned into shared infrastructure the whole company leans on. Once you've got multiple models, real money on the line, and rules about what's allowed, [music] those concerns stop belonging in every service and start belonging in one place. Whether we keep calling that place an AI gateway or it gets swallowed [music] into the tools you already run, nobody knows yet. It's all really young. The job it does isn't going anywhere because the mess it cleans up is what you get when AI grows up inside your code base.

---

## Timestamped Segments

**[0:00]** The most important piece of your AI

**[0:02]** stack might be one you never wrote a

**[0:04]** line off. It sits between your app and

**[0:07]** every model you call, and the day it

**[0:09]** goes down, every AI feature you have

**[0:12]** goes down with [music] it. Teams are all

**[0:14]** adding this when their AI stack grows

**[0:17]** mature. It's the AI gateway, and by the

**[0:20]** end of this video, you'll know exactly

**[0:22]** what it does, when [music] you actually

**[0:24]** need one, and the one trade-off that can

**[0:26]** make a cheaper setup cost you [music]

**[0:28]** more.

**[0:29]** You usually get a gateway by accident.

**[0:32]** On day one, your app just calls a single

**[0:34]** model with an API key. Then, it grows.

**[0:38]** You add a second provider because the

**[0:40]** first one is getting rate limited. A

**[0:42]** teammate wires the model into a second

**[0:44]** service. Someone hardcodes an API key

**[0:47]** into a repo, then copies it into three

**[0:50]** more. Retry logic gets written from

**[0:53]** scratch four separate times, slightly

**[0:55]** wrong each time. And when the invoice

**[0:58]** comes in, nobody can tell you which

**[1:00]** feature spent the money. About 3 months

**[1:03]** in, every team hits the same wall. Five

**[1:06]** different services all talking to the

**[1:08]** model directly without any shared logic.

**[1:11]** One provider gets its model pulled by

**[1:14]** the government, and half your product

**[1:16]** goes dark with it. Lucky thing for you,

**[1:18]** these are all plumbing problems that

**[1:20]** were there before AI.

**[1:22]** >> [music]

**[1:22]** >> Regular web APIs ran into this mess a

**[1:25]** decade ago, back when auth and rate

**[1:28]** limiting and logging got copied, pasted

**[1:30]** into every service until someone finally

**[1:32]** pulled them out into one shared layer.

**[1:35]** That layer was the API gateway. The AI

**[1:39]** gateway is the same idea, but pointed at

**[1:41]** models. What does this shared layer do?

**[1:44]** Strip away the marketing, and there are

**[1:46]** five jobs it's really there for. Most

**[1:48]** importantly, it's a single standard way

**[1:51]** to talk to every model. Normally, every

**[1:54]** provider has a different request format

**[1:57]** and its own quirks and failure modes.

**[1:59]** The gateway hides all of that behind one

**[2:02]** interface. Almost everyone copied the

**[2:04]** format OpenAI shipped first. So, in

**[2:07]** practice, you point your code at the

**[2:09]** gateway, change one line, and swap from

**[2:12]** one model to another by editing a

**[2:14]** string.

**[2:15]** Second, it [music] holds the keys.

**[2:17]** Instead of the real provider keys

**[2:19]** floating around your code base, they

**[2:21]** live in the gateway. Each app gets its

**[2:24]** own throwaway key that the gateway

**[2:26]** trades for the real [music] one. Lose

**[2:28]** one, revoke it, nobody else notices.

**[2:31]** Third, it retries [music] and fails

**[2:33]** over. When a provider throws an error or

**[2:36]** starts rate limiting, the gateway can

**[2:38]** retry on its own or reroute the request

**[2:41]** to a backup model before you bother your

**[2:43]** users with anything.

**[2:45]** Fourth, it keeps track of everything

**[2:47]** passing it. Every token in, every token

**[2:50]** out, tagged by team, by app, [music] by

**[2:52]** model. That's how you set a budget and

**[2:55]** enforce it instead of finding out at the

**[2:57]** end of the month. And fifth, because

**[2:59]** every request flows through it, it's the

**[3:02]** natural place to watch everything at

**[3:04]** once. Latency, errors, and spend on one

**[3:07]** dashboard.

**[3:09]** Think of it less like a smart assistant

**[3:11]** and more like the front desk of a

**[3:13]** building. Everything checks in there,

**[3:15]** gets logged, and gets pointed to the

**[3:17]** right room. Boring and load-bearing.

**[3:20]** Now for the confusing part, because this

**[3:23]** corner of the industry has a naming

**[3:24]** problem. You'll see AI gateway and LLM

**[3:28]** gateway used for the same thing. If you

**[3:31]** want to get specific, LLM gateway leans

**[3:34]** developer and routing, while AI gateway

**[3:37]** leans enterprise and governance, and now

**[3:40]** [music] stretches to cover images,

**[3:42]** audio, and agents. It's fine to

**[3:44]** interchange them in most cases.

**[3:46]** >> [music]

**[3:46]** >> Then, there's the plain API gateway, the

**[3:49]** decade-old ancestor I mentioned. An AI

**[3:52]** gateway is that pattern specialized for

**[3:54]** model traffic. Some products are

**[3:57]** literally an old API gateway with AI

**[4:00]** plugins bolted on. The difference is

**[4:02]** that the AI version reads the prompt. It

**[4:05]** understands tokens [music] and streaming

**[4:07]** and model names where the old one just

**[4:09]** saw web requests go by.

**[4:11]** Two more you'll bump into. An MCP

**[4:14]** gateway governs what an agent is allowed

**[4:16]** to do, meaning the tools it calls, not

**[4:19]** the model it talks to. And an inference

**[4:21]** gateway is a lower level thing that

**[4:23]** spreads traffic across your own GPUs.

**[4:27]** Are you still with me?

**[4:28]** Underneath all that, the term AI gateway

**[4:31]** is doing two jobs at once. Half the time

**[4:34]** it means a unified proxy that

**[4:36]** centralizes keys, cost, and logging. The

**[4:39]** other half it means something smarter, a

**[4:42]** router that picks the best model for

**[4:44]** each request. Those are two different

**[4:47]** products wearing one name, which is

**[4:49]** where most of the confusion comes from.

**[4:51]** That second job, routing, is where the

**[4:53]** real fight is. It comes [music] in two

**[4:55]** flavors. The first is dumb on purpose

**[4:58]** and what most production systems run.

**[5:01]** You write the rules, send cheap requests

**[5:04]** here, send this customer's traffic

**[5:06]** there, and if the main model is down,

**[5:08]** fall back to that one. It's predictable

**[5:10]** and easy to debug. The second flavor is

**[5:13]** smart routing, where the gateway tries

**[5:16]** to read each prompt, guess how hard it

**[5:18]** is, then send the easy questions to a

**[5:21]** cheap model, and save the expensive one

**[5:23]** for the tricky stuff. This routing is

**[5:26]** also increasingly happening in your

**[5:28]** favorite frontier coding harness. When

**[5:30]** it works, the savings are real. An open

**[5:34]** research project called Route LLM showed

**[5:37]** you could hold around 95% of a

**[5:40]** frontier's model's quality while sending

**[5:42]** only a quarter of the requests [music]

**[5:44]** its way. Everything else went to a model

**[5:47]** a fraction of the price, and most people

**[5:49]** couldn't tell the difference. And when

**[5:51]** the researchers later swapped in

**[5:53]** different models on both ends, the

**[5:55]** [music] routing still held up, which is

**[5:57]** a big part of why the idea gets taken

**[5:59]** seriously.

**[6:01]** You arrive at a catch-22. To reliably

**[6:04]** know a prompt is too hard for the cheap

**[6:06]** model, your little router has to

**[6:08]** understand that prompt about as well as

**[6:10]** the expensive model would. And if it

**[6:12]** could do that, you wouldn't [music] need

**[6:14]** the expensive model. The smarter the

**[6:16]** routing gets, the closer it creeps to

**[6:18]** being just another big model sitting in

**[6:20]** front of your big model. It's still

**[6:23]** useful to have since a lot of traffic is

**[6:25]** obviously easy, and a cheap check

**[6:27]** catches it. Just don't expect the free

**[6:30]** lunch the pitch decks imply.

**[6:32]** Which brings us to the trade-off I

**[6:33]** promised, the one that turns cheaper

**[6:35]** model into a bigger bill.

**[6:37]** Modern AI tools lean hard on a warm

**[6:40]** cache. When you're deep in a session

**[6:42]** with one model, a lot of your

**[6:44]** conversation is already sitting in fast

**[6:46]** memory on the provider's side, ready to

**[6:49]** reuse. So, you're not paying full

**[6:51]** freight to reprocess it every turn.

**[6:53]** There's another video for that if you

**[6:55]** want to know more. Now, let a smart

**[6:57]** router switch you to a different model

**[6:59]** mid-conversation to save a few cents,

**[7:01]** that new model has no warm cache for

**[7:03]** [music] you. It has to read the entire

**[7:05]** conversation again, cold. The one-time

**[7:08]** cost of that reload can swallow the

**[7:10]** savings from the cheaper model [music]

**[7:11]** and then some. You optimized the price

**[7:14]** per token and blew up the token count

**[7:16]** instead. [music]

**[7:17]** The fix is to make the router aware of

**[7:19]** the cache. Once a model is warm, raise

**[7:22]** the bar for switching away from it, so

**[7:24]** you only jump ship when the savings

**[7:26]** clearly beat the cost of going cold.

**[7:29]** It's a small idea that plenty of naive

**[7:31]** routers miss, and it's exactly why just

**[7:34]** route to whatever's cheapest is worse

**[7:36]** [music] advice than it sounds. Caching

**[7:38]** shows up one more place. It's called

**[7:41]** semantic caching. A normal cache only

**[7:43]** reuses an answer if the new question is

**[7:46]** character-for-character identical.

**[7:49]** Semantic caching goes further. It turns

**[7:52]** each prompt into a string of numbers

**[7:54]** that captures its meaning, then checks

**[7:56]** whether any past question means roughly

**[7:59]** the same thing. Ask, [music] "What's the

**[8:01]** capital of France?" and "France capital

**[8:04]** city, please." and it can serve the

**[8:06]** [music] same cached answer to both. When

**[8:08]** it hits, you skip the model entirely.

**[8:11]** Near zero cost, [music] instant reply.

**[8:14]** The danger hides in the word roughly.

**[8:16]** Set the similarity bar too loose and it

**[8:18]** starts matching questions that look

**[8:20]** alike but mean opposite things. Sort

**[8:23]** ascending and sort descending land

**[8:25]** almost on top of each other in that

**[8:27]** number space. Match them and the gateway

**[8:29]** hands someone the wrong answer. Pylon's

**[8:32]** stale data where a price changed [music]

**[8:34]** but the cache didn't, plus the fact that

**[8:37]** upgrading your embedding model can wipe

**[8:39]** out the whole cache without warning, and

**[8:41]** you've got a feature that dazzles in a

**[8:43]** demo and frays nerves in production.

**[8:45]** Useful, but a knob to turn carefully.

**[8:48]** Not a switch to leave on.

**[8:50]** For all that you get out of it, the

**[8:52]** layer costs you something, [music] too.

**[8:54]** It adds a hop. Every request now detours

**[8:57]** through the gateway before it reaches

**[8:59]** the model. In practice, that overhead is

**[9:02]** tiny next to the seconds the model

**[9:04]** itself takes, and a well-run gateway at

**[9:06]** the edge can even come back faster

**[9:08]** thanks [music] to better pipes to the

**[9:10]** providers. But on a truly

**[9:12]** latency-critical path, measure it

**[9:14]** yourself. The bigger issue is that

**[9:17]** you've built a single point of failure.

**[9:19]** Everything routes through this one

**[9:21]** layer, so if it all falls over, every AI

**[9:24]** feature you have falls over with it. The

**[9:26]** thing you added for reliability becomes

**[9:29]** the thing that can take you down. You

**[9:31]** plan for that with backups and ideally a

**[9:34]** code path that can skip the gateway and

**[9:36]** call the provider directly in a pinch.

**[9:39]** Talk about gateway-ception.

**[9:41]** There's a trust cost, too. This layer

**[9:43]** holds every one of your API keys in one

**[9:46]** place. Last year, the most popular

**[9:48]** open-source gateway, LightLLM, got hit

**[9:51]** by a supply chain [music] attack where

**[9:53]** compromised code went straight after

**[9:55]** those keys. A blunt reminder that the

**[9:58]** box holding every key is the box

**[10:00]** attackers most want to crack. So, when

**[10:03]** do you need an AI gateway? Plenty of

**[10:05]** teams really don't. If all you call is

**[10:08]** one provider from one app, call the

**[10:10]** model directly and skip all of this. A

**[10:12]** gateway's what you add when your

**[10:14]** situation turns plural. A second

**[10:17]** provider, a second service calling

**[10:19]** models, the first surprise invoice, or

**[10:21]** the first time someone asked which

**[10:23]** [music] team spent all the money. The

**[10:25]** demo everyone leads with, one key for

**[10:28]** many models, is the least interesting

**[10:30]** [music] reason this layer exists.

**[10:32]** Calling a model stopped being something

**[10:34]** one app does on its own and turned into

**[10:36]** shared infrastructure the whole company

**[10:38]** leans on. Once you've got multiple

**[10:41]** models, real money on the line, and

**[10:43]** rules about what's allowed, [music]

**[10:44]** those concerns stop belonging in every

**[10:46]** service and start belonging in one

**[10:49]** place. Whether we keep calling that

**[10:51]** place an AI gateway or it gets swallowed

**[10:53]** [music] into the tools you already run,

**[10:55]** nobody knows yet. It's all really young.

**[10:58]** The job it does isn't going anywhere

**[11:00]** because the mess it cleans up is what

**[11:02]** you get when AI grows up inside your

**[11:04]** code base.
