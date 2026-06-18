# Transcript: E1idsrv79tI

**URL:** https://www.youtube.com/watch?v=E1idsrv79tI
**Segments:** 1112

---

## Full Text

Nobody understands their own code anymore. There is code running in production now at companies we use every day that nobody can really explain. Not the engineer who shipped it, not the team that owns the service, not the CTO. The code works. It passes tests. And no human on the payroll fully understands what it does, why it does it, or what would happen if it stopped doing it. The industry is starting to call this dark code behavior in production that nobody can really trace end to end. It's not buggy code. It's not spaghetti code and it's not technical debt. Dark code is code that was never understood by anyone at any point because it was made by AI. It was generated. It passed automated checks and it shipped. The comprehension step didn't happen. Not because someone was careless, but because the process no longer requires it to ship. Now, this is often portrayed as a security issue. It's often portrayed as an engineering quality issue. I think we need to look past both of those. It's partly those things, but it's really an organizational capability problem. It's got regulatory exposure elements. It's got business liability elements. If you are building software right now, there is a fundamental shift in what it means to be good at your job. And at the heart of that shift is grappling with dark code, which is only going to 10x from here. You think it's a problem now, it's going to be 10x more next year. So, in this video, I'm going to lay out what's actually happening, why the obvious responses aren't as effective as they seem, and what actually works. So, first, let's dig into the problem. Anyone who's used AI tools, this is going to feel very intuitive. We're not going to spend very long on it. We have two reasons why dark code is multiplying and they interplay to make things worse. The first reason is structural. AI generating code means that it is harder for you to understand the code because the AI wrote it in the first place and you didn't bang it out with your fingers. That is just a structural reason why it is harder to understand the code unless you're really really disciplined with your nonfunctional requirements. Hint hint, you should be. The other reason why dark code is tough is because we are moving so fast. AI enables us to move fast. The pressure is to move fast. That is part of the reason we're making these trillion dollar bets on AI as an industry is because we want to move fast. When you combine velocity with a structural reason not to understand code, comprehension starts to decouple from authorship unless you take really, really clear measures to prevent that. So that's the problem. We've all lived it. Even if all we've done is type in please make this in lovable and it makes something fast, that is dark code. Why do the obvious responses to dark code not work very well? Fundamentally, the obvious responses to dark code are rooted in the idea that this is a tooling problem and it's not a tooling problem. Let me give you some examples. Number one, there's often a response to dark code that says we should make dark code observable. If we instrument every service in the stack, we're going to understand what's happening and that's going to give us the ability to respond rapidly and effectively. I would respond and say, you know what, you should be observable. I love telemetry, but that doesn't mean the same thing as comprehension, right? That doesn't solve your dark code problem. It just means you can measure what dark code is breaking for you in production, which is great. You should do that. It's still dark code. It doesn't solve the problem. The second way people solve this that I think is also incorrect is people have an instinct and and here I'm especially going to call out my colleagues in engineering there's an instinct to say we can harness the agents so the dark code by definition is fine that is partly true it is certainly good to have guard rails right it is certainly good to have excellent orchestration platforms I've made videos about it it's super important having an excellent pipeline reduces your risk in enterprise production systems 100% it's really important important if you're building with an agent in 2026. But if you're adding layers to your agent pipeline, that is also not actually solving your dark code problem. That is just adding a layer. And when you try and figure out what went wrong with the dark code in production, now you have to troubleshoot multiple things. So that doesn't solve it either. It's still important. You still have to do it just like the telemetry, but it doesn't solve the problem. Answer number three is to say it's okay to have dark code and we're fine with it. Factory.ai is a famous example of this. We're going to see this thesis tested. I think it is unlikely that we will survive for very long with code in production if nobody understands it at all. I think there will be problems if you don't understand the code thoroughly. And I want to give factory.ai credit here because I don't think it's that they don't understand the code. I think is that they're extending their understanding with a hypothesis that extraordinary testing and extraordinary discipline at the eval layer proxies for that understanding in a way that is useful and allows them to learn from their code. That is a genuine hypothesis that not a lot of people are trying and most of the people who are yoloing their code into production aren't as disciplined as factory.ai. So regardless of how you do it, maybe you're super disciplined, maybe you're good at your non-functional emails and that's how you're extending this. Or maybe like most orgs that I've seen, you just yolo the dark code and the PM puts stuff out there and the engineering team puts stuff out there and the marketing team puts stuff out there and you gain it a little bit, right? You know, the marketing team has to manage the website and the PM can only vibe code up to a certain stage and then engineering has to take it. But the problem with all of this yoloing is that nobody owns the sustained total package of code in production. You have problems with ownership because you have distributed authorship. And distributed authorship is a strength we want to encourage. So it's not as intuitive as saying you got to shut it off. And I know IT departments who are like, you know what, we're shutting it all off. Nobody can vibe code. Only engineers can write code. They're in trouble too. They're in trouble because they can't ship fast. So the answer is not as simple as don't do it. You have to let people code and start to build. That's actually super important. But you have to think through what accountability looks like when everybody is now able to code. And that is a hard problem. I think AI's strengths really mask its weaknesses here. So we've talked about some of these different responses that organizations make, right? Some of them are like observation matters, telemetry matters, that's how we solve it. Some of them are like agentic pipelines matter, that's how we solve it. And those are both important things. And some of them are like, you know, yolo, like for one way or another, we're going to accept that there's dark code and we'll deal with it. The issue here is that it looks more okay to yolo stuff. It looks more okay to say we'll just observe it in production. As AI gets stronger. And so, in a sense, AI's strengths really mask its weaknesses because the stronger an AI model becomes, the easier it becomes to say, you know what, it's okay. We're not going to go there. The AI will know what its code is and does, and the AI will be the one that fixes the code and we're just going to let it be. Right? I think the challenge with that is that it is hard to know when the AI is overconfident and when it is not. And so this is a situation where if you're like well how do AI native orgs solve this problem? How does anthropic solve this problem? How does open AAI solve this problem? It is sort of like an amalgam of multiple approaches that I've described here without an assumption that AI is magical. Yes, the AI native companies do not have an assumption that AI is magical. So they're going to invest heavily in eval sort of like factory.ai does. They're going to invest a lot in understanding their agentic pipelines. We saw that with a claude code leak. They're going to invest a ton in telemetry and understanding how their systems work in production. And all of those don't mask the fact that they are also having individual engineers still commit PRs and still have reviews of those code and still understand the code that's going out. And in that sense, as much as AI is doing a lot of the codew writing, they are still demanding a degree of legibility and comprehension from engineering teams that reflects the sophistication of the work that they're doing. Ironically, right now, the moves that the industry is making are compounding this problem for the worse. Dark code gets worse when we lay off people and expect the others to do even more and they don't have time to understand the code. We are in a sense creating more of a dark code problem for ourselves, the more we lay off engineers across the industry. And if you think this is just an engineering team problem, this is a company entity board level problem, right? questions about sock 2, questions about encryption at risk, things that companies become liable for are things that dark code touches. And if we don't have good answers for those answers we are held accountable to, we are going to be in trouble. So you get the idea. We have tried different things. We've tried observability. We've tried telemetry. We've seen hints of how this works as the labs have opened up the kimono and showed us a little bit of how they work internally through interviews and newspaper pieces and and comments on X. But what we really need is a comprehensive approach to dark code that treats it as what it really is, an organizational capability problem. And that's what I want to lay out here in the second part of this video. So what actually helps? If dark code is an organizational problem, what do we need to do to fix it as a team? I think there are three layers to this solution and I want to talk about each of them separately. Layer one is simple. Force understanding before the code exists. There are two ways people fail at this. Number one, there are a lot of teams in 2026 that persist in 2010's era of product development where they overdocument before they go and they do it for the sake of human process. I've argued against this strenuously. I've said agents are becoming more and more and more the heart of the development process so we can speed up. I'm going to say it again. As long as you understand what you want to build and can write it out clearly, go. But for people increasingly in 2026 who just want to go and who don't want to take time to understand this principle is also a break. Stop understand what you want to build then go make the code exist. Do you see what I mean? I'm not giving you a blank check to just go vibe code. I'm also not telling you slow down for lots of process. I'm saying do just enough to understand what you want to build in a degree of detail you can write down. That's it. That is such an organizational discipline because so many people want to fall off on one side or the other. They want to jump into process and say, "Give me a linear process. I want to have like 16 artifacts I have to make." Not because I want them, but because that gives me an assurance that I've thought about it and I don't have to get in trouble if something goes wrong. No, no, no. It's your code. You own it. You're liable. You're accountable. Make sure you understand what you want to build. That's all you have to do. That's it. That's the principle. force understanding as a cultural primary artifact before the code exists. I call this specd driven development. You basically write the spec out and that makes it really clear. And here's a detail worth noting. After the December outage, Amazon actually rebuilt their coding tool Kira with exactly this concept. The tool now leads with specdriven development, turning prompts into requirements, tasks, and task lists before the code gets generated. They learned very expensively that AI coding tools need to force comprehension before generation. When the company that learned this lesson the hardest bakes it into the product, maybe we should all learn that lesson. And by the way, if you're wondering how do specs relate to evals, I'll give you a hint. The spec becomes the eval. It's actually not that hard. If you can write out a clear spec, that is how you get an eval that you can then set the agent again. Because really all you're doing with an eval is you're saying, "Here is the test. The test is the spec. the agent is going to keep trying to pass the test until it does. So writing a clear spec helps you to get good code and also code you can understand. Layer two, right? Make your systems inherently selfdescribing. So I'm not talking about an agent self-reporting. That's not what I mean here. I dismissed that earlier in this video. I'm talking about something more structural. Context engineering is the practice of restructuring your codebase so comprehension is embedded in the code itself. That's part of what we do with context engineering. Some people think it's just getting the docs together. It's also the code. You don't want the code understanding locked in the heads of people. You want it easily and immediately legible to humans and agents alike. So think about this in three layers. I know this is a three layer and a three layer. Stick with me. We're not going to go too far down the rabbit hole. If you're making a system self-describing, part one is make sure you have structural context that answers the question where. Every module should have a manifest that describes what it does, what it depends on, and what depends on it. Where does this code go to? Right? Part two, have semantic context. Semantic context needs to answer the question, what? In other words, when an AI reads an interface, it needs to read semantic context that gives it the rules of engagement, not just the shape of the data. What I mean by rules of engagement are things like performance expectations, failure modes, retry semantics, behavioral contracts. Basically, how the interface is expected to behave. This is a cousin to the idea that we should have API contracts. Right? In this case, what I'm saying is all interfaces need a degree of semantic context, not just API interfaces. Layer three, you're trying to catch what the first two layers miss. What I'm suggesting is we talk about eval driven development as having a test and then once you pass functional and non-functional tests, the code is reviewed by a senior engineer and it ships. Now, we're running into a situation where there's so much code generation where engineers have trouble making that legible. My goal is to put a comprehension gate in front of the code as a senior engineer is trying to read it and keep an eye on the PRs that are coming across his or her desk. And I want that comprehension gate to make key questions that a senior engineer would ask immediately and obviously legible. And yes, if you're wondering, can AI do this and help? It can. Can AI discover things through that comprehension check that we pass back to the evals for better code? 100%. This is a flywheel. Ask questions that a good senior engineer is going to ask. A good senior engineer is going to ask you, why did you call that dependency here? Why did you structure the code so that it caches in a location unreadable by other services? How are you thinking about separation of concerns? If you're making this monolithic, you want to think through the kinds of questions your leading engineers ask and use them to create a comprehension filter that acts as a way of making the code legible. And again, it does two things. One, it helps to make the code readable and therefore accountable by people in the organization. And two, it becomes something that feeds your flywheel and makes your emails better and improves the quality of your code over time. Can you imagine improving speed and quality of code at the same time? It's the dream. We can do it. We just have to set ourselves up so we don't have dark code. If you've got this far, I hope you realize this is not a security team's problem. This is not an observability problem. This is not an agent pipeline problem. This is an all of us problem. This is a problem for everybody who's building in the software space. And if you think you're not, when was the last time you vibe coded? If you are leading an engineering org right now, the question you should ask yourself is not how's our observability, how's our agentic pipelines. Those are table stakes questions. The question you need to ask yourself is, do I have mechanisms that enable me to make the dark code that I'm producing legible so that I know where I'm driving? Because otherwise, you really are driving with a headlights off and you are liable to run into the ditch and generate problems that you are not aware you're causing from a risk perspective. And that should make you stay up at night. If you're a founder, this is both a competitive mode and also a risk. If you're like most founders, and I'll be honest, I've seen a lot of them, they vibe code so fast and get to market so fast, and they listen to only the speed part of YC teachings, they try and sell you on something that is really a thesis and a trench code. And maybe the code isn't there, and maybe it's not high quality, and maybe it's not what you need to depend on. Honestly, that's a liability for the founder. That's a liability for the company. You can stand out so easily as a founder if you just know the code in this day and age. Just get to know it. Make sure you don't have dark code. Make it legible. explain your trade-offs, be transparent, you're going to stand out, and like be so easy to do business with and build so much trust. And by the way, if you're a vendor, ask for that, right? Ask for transparent code. Ask about dark code. Ask how much if they're shipping a lot, they understand what they're shipping. That is a question vendors should be asking. And if you're just getting started in this field, if you are just getting out of college, if you are just getting into vibe coding and then kind of leaning into the technical track, take this as an opportunity. This whole idea of a comprehension gate, you can set up and I've given one and set one up for you. You can set up a skill that allows you to look at a piece of code and start to understand those questions that senior engineers ask, the principal engineers ask. And that accelerates your comprehension. That makes the code less dark. And then one last note, if you are a senior engineer, if you're a principal and you're used to reviewing by hand, I know this is a massive adjustment. I know trusting AI to give you a comprehension gate is a big step. You absolutely should feel comfortable adjusting and embroidering the prompts and the skills, the stuff I've packaged together with this video so that it feels good to you. It's a tool that needs to feel good in your hand. But I don't think you can avoid using AI to help you understand code because the expectation for volume is not going away. And so you need to figure out how you can remain accountable for the code while putting your eyes across more stuff. And I think that you need essentially lenses on the code that help you to see more farther clearer so that the code is not dark to you because the alternative is just looking at those emailed PR reviews and autofixes from Codeex or Claude Code and saying, "Ah, it's probably fine." You don't want to be that person. That's too risky. Look, nobody's gonna slow down. shipping before you fully understand what you've built is a problem we can fix, but it's not a problem we can fix organizationally by just choosing to go back to the way things work. This is a river we've crossed. AI is helping us speed up. No one wants to slow down. No one should slow down. And I'm not arguing that that is a good idea. I think we need to speed up. I think on average, most orgs still go way too slow. But we have to be honest that going fast imposes new kinds of requirements for understanding the code that we are shipping at speed and that is a different class of problem than the old way of understanding code because the old way of understanding code was human mediated right and one of the larger thesis I've been exploring in 2026 through this video series has really been saying a lot of our human mediated touch points are breaking under the speed that AI is imposing on the business. How do we start to think differently about those mechanisms? And dark code takes that kind of thinking because otherwise it is going to balloon and become an absolute security nightmare. Don't tolerate dark code. It is an organizational choice and you can fight it. Choose to do so. Nobody understands their own code anymore. There is code running in production now at companies we use every day that nobody can really explain. Not the engineer who shipped it, not the team that owns the service, not the CTO. The code works. It passes tests. And no human on the payroll fully understands what it does, why it does it, or what would happen if it stopped doing it. The industry is starting to call this dark code behavior in production that nobody can really trace end to end. It's not buggy code. It's not spaghetti code and it's not technical debt. Dark code is code that was never understood by anyone at any point because it was made by AI. It was generated. It passed automated checks and it shipped. The comprehension step didn't happen. Not because someone was careless, but because the process no longer requires it to ship. Now, this is often portrayed as a security issue. It's often portrayed as an engineering quality issue. I think we need to look past both of those. It's partly those things, but it's really an organizational capability problem. It's got regulatory exposure elements. It's got business liability elements. If you are building software right now, there is a fundamental shift in what it means to be good at your job. And at the heart of that shift is grappling with dark code, which is only going to 10x from here. You think it's a problem now, it's going to be 10x more next year. So, in this video, I'm going to lay out what's actually happening, why the obvious responses aren't as effective as they seem, and what actually works. So, first, let's dig into the problem. Anyone who's used AI tools, this is going to feel very intuitive. We're not going to spend very long on it. We have two reasons why dark code is multiplying and they interplay to make things worse. The first reason is structural. AI generating code means that it is harder for you to understand the code because the AI wrote it in the first place and you didn't bang it out with your fingers. That is just a structural reason why it is harder to understand the code unless you're really really disciplined with your nonfunctional requirements. Hint hint, you should be. The other reason why dark code is tough is because we are moving so fast. AI enables us to move fast. The pressure is to move fast. That is part of the reason we're making these trillion dollar bets on AI as an industry is because we want to move fast. When you combine velocity with a structural reason not to understand code, comprehension starts to decouple from authorship unless you take really, really clear measures to prevent that. So that's the problem. We've all lived it. Even if all we've done is type in please make this in lovable and it makes something fast, that is dark code. Why do the obvious responses to dark code not work very well? Fundamentally, the obvious responses to dark code are rooted in the idea that this is a tooling problem and it's not a tooling problem. Let me give you some examples. Number one, there's often a response to dark code that says we should make dark code observable. If we instrument every service in the stack, we're going to understand what's happening and that's going to give us the ability to respond rapidly and effectively. I would respond and say, you know what, you should be observable. I love telemetry, but that doesn't mean the same thing as comprehension, right? That doesn't solve your dark code problem. It just means you can measure what dark code is breaking for you in production, which is great. You should do that. It's still dark code. It doesn't solve the problem. The second way people solve this that I think is also incorrect is people have an instinct and and here I'm especially going to call out my colleagues in engineering there's an instinct to say we can harness the agents so the dark code by definition is fine that is partly true it is certainly good to have guard rails right it is certainly good to have excellent orchestration platforms I've made videos about it it's super important having an excellent pipeline reduces your risk in enterprise production systems 100% it's really important important if you're building with an agent in 2026. But if you're adding layers to your agent pipeline, that is also not actually solving your dark code problem. That is just adding a layer. And when you try and figure out what went wrong with the dark code in production, now you have to troubleshoot multiple things. So that doesn't solve it either. It's still important. You still have to do it just like the telemetry, but it doesn't solve the problem. Answer number three is to say it's okay to have dark code and we're fine with it. Factory.ai is a famous example of this. We're going to see this thesis tested. I think it is unlikely that we will survive for very long with code in production if nobody understands it at all. I think there will be problems if you don't understand the code thoroughly. And I want to give factory.ai credit here because I don't think it's that they don't understand the code. I think is that they're extending their understanding with a hypothesis that extraordinary testing and extraordinary discipline at the eval layer proxies for that understanding in a way that is useful and allows them to learn from their code. That is a genuine hypothesis that not a lot of people are trying and most of the people who are yoloing their code into production aren't as disciplined as factory.ai. So regardless of how you do it, maybe you're super disciplined, maybe you're good at your non-functional emails and that's how you're extending this. Or maybe like most orgs that I've seen, you just yolo the dark code and the PM puts stuff out there and the engineering team puts stuff out there and the marketing team puts stuff out there and you gain it a little bit, right? You know, the marketing team has to manage the website and the PM can only vibe code up to a certain stage and then engineering has to take it. But the problem with all of this yoloing is that nobody owns the sustained total package of code in production. You have problems with ownership because you have distributed authorship. And distributed authorship is a strength we want to encourage. So it's not as intuitive as saying you got to shut it off. And I know IT departments who are like, you know what, we're shutting it all off. Nobody can vibe code. Only engineers can write code. They're in trouble too. They're in trouble because they can't ship fast. So the answer is not as simple as don't do it. You have to let people code and start to build. That's actually super important. But you have to think through what accountability looks like when everybody is now able to code. And that is a hard problem. I think AI's strengths really mask its weaknesses here. So we've talked about some of these different responses that organizations make, right? Some of them are like observation matters, telemetry matters, that's how we solve it. Some of them are like agentic pipelines matter, that's how we solve it. And those are both important things. And some of them are like, you know, yolo, like for one way or another, we're going to accept that there's dark code and we'll deal with it. The issue here is that it looks more okay to yolo stuff. It looks more okay to say we'll just observe it in production. As AI gets stronger. And so, in a sense, AI's strengths really mask its weaknesses because the stronger an AI model becomes, the easier it becomes to say, you know what, it's okay. We're not going to go there. The AI will know what its code is and does, and the AI will be the one that fixes the code and we're just going to let it be. Right? I think the challenge with that is that it is hard to know when the AI is overconfident and when it is not. And so this is a situation where if you're like well how do AI native orgs solve this problem? How does anthropic solve this problem? How does open AAI solve this problem? It is sort of like an amalgam of multiple approaches that I've described here without an assumption that AI is magical. Yes, the AI native companies do not have an assumption that AI is magical. So they're going to invest heavily in eval sort of like factory.ai does. They're going to invest a lot in understanding their agentic pipelines. We saw that with a claude code leak. They're going to invest a ton in telemetry and understanding how their systems work in production. And all of those don't mask the fact that they are also having individual engineers still commit PRs and still have reviews of those code and still understand the code that's going out. And in that sense, as much as AI is doing a lot of the codew writing, they are still demanding a degree of legibility and comprehension from engineering teams that reflects the sophistication of the work that they're doing. Ironically, right now, the moves that the industry is making are compounding this problem for the worse. Dark code gets worse when we lay off people and expect the others to do even more and they don't have time to understand the code. We are in a sense creating more of a dark code problem for ourselves, the more we lay off engineers across the industry. And if you think this is just an engineering team problem, this is a company entity board level problem, right? questions about sock 2, questions about encryption at risk, things that companies become liable for are things that dark code touches. And if we don't have good answers for those answers we are held accountable to, we are going to be in trouble. So you get the idea. We have tried different things. We've tried observability. We've tried telemetry. We've seen hints of how this works as the labs have opened up the kimono and showed us a little bit of how they work internally through interviews and newspaper pieces and and comments on X. But what we really need is a comprehensive approach to dark code that treats it as what it really is, an organizational capability problem. And that's what I want to lay out here in the second part of this video. So what actually helps? If dark code is an organizational problem, what do we need to do to fix it as a team? I think there are three layers to this solution and I want to talk about each of them separately. Layer one is simple. Force understanding before the code exists. There are two ways people fail at this. Number one, there are a lot of teams in 2026 that persist in 2010's era of product development where they overdocument before they go and they do it for the sake of human process. I've argued against this strenuously. I've said agents are becoming more and more and more the heart of the development process so we can speed up. I'm going to say it again. As long as you understand what you want to build and can write it out clearly, go. But for people increasingly in 2026 who just want to go and who don't want to take time to understand this principle is also a break. Stop understand what you want to build then go make the code exist. Do you see what I mean? I'm not giving you a blank check to just go vibe code. I'm also not telling you slow down for lots of process. I'm saying do just enough to understand what you want to build in a degree of detail you can write down. That's it. That is such an organizational discipline because so many people want to fall off on one side or the other. They want to jump into process and say, "Give me a linear process. I want to have like 16 artifacts I have to make." Not because I want them, but because that gives me an assurance that I've thought about it and I don't have to get in trouble if something goes wrong. No, no, no. It's your code. You own it. You're liable. You're accountable. Make sure you understand what you want to build. That's all you have to do. That's it. That's the principle. force understanding as a cultural primary artifact before the code exists. I call this specd driven development. You basically write the spec out and that makes it really clear. And here's a detail worth noting. After the December outage, Amazon actually rebuilt their coding tool Kira with exactly this concept. The tool now leads with specdriven development, turning prompts into requirements, tasks, and task lists before the code gets generated. They learned very expensively that AI coding tools need to force comprehension before generation. When the company that learned this lesson the hardest bakes it into the product, maybe we should all learn that lesson. And by the way, if you're wondering how do specs relate to evals, I'll give you a hint. The spec becomes the eval. It's actually not that hard. If you can write out a clear spec, that is how you get an eval that you can then set the agent again. Because really all you're doing with an eval is you're saying, "Here is the test. The test is the spec. the agent is going to keep trying to pass the test until it does. So writing a clear spec helps you to get good code and also code you can understand. Layer two, right? Make your systems inherently selfdescribing. So I'm not talking about an agent self-reporting. That's not what I mean here. I dismissed that earlier in this video. I'm talking about something more structural. Context engineering is the practice of restructuring your codebase so comprehension is embedded in the code itself. That's part of what we do with context engineering. Some people think it's just getting the docs together. It's also the code. You don't want the code understanding locked in the heads of people. You want it easily and immediately legible to humans and agents alike. So think about this in three layers. I know this is a three layer and a three layer. Stick with me. We're not going to go too far down the rabbit hole. If you're making a system self-describing, part one is make sure you have structural context that answers the question where. Every module should have a manifest that describes what it does, what it depends on, and what depends on it. Where does this code go to? Right? Part two, have semantic context. Semantic context needs to answer the question, what? In other words, when an AI reads an interface, it needs to read semantic context that gives it the rules of engagement, not just the shape of the data. What I mean by rules of engagement are things like performance expectations, failure modes, retry semantics, behavioral contracts. Basically, how the interface is expected to behave. This is a cousin to the idea that we should have API contracts. Right? In this case, what I'm saying is all interfaces need a degree of semantic context, not just API interfaces. Layer three, you're trying to catch what the first two layers miss. What I'm suggesting is we talk about eval driven development as having a test and then once you pass functional and non-functional tests, the code is reviewed by a senior engineer and it ships. Now, we're running into a situation where there's so much code generation where engineers have trouble making that legible. My goal is to put a comprehension gate in front of the code as a senior engineer is trying to read it and keep an eye on the PRs that are coming across his or her desk. And I want that comprehension gate to make key questions that a senior engineer would ask immediately and obviously legible. And yes, if you're wondering, can AI do this and help? It can. Can AI discover things through that comprehension check that we pass back to the evals for better code? 100%. This is a flywheel. Ask questions that a good senior engineer is going to ask. A good senior engineer is going to ask you, why did you call that dependency here? Why did you structure the code so that it caches in a location unreadable by other services? How are you thinking about separation of concerns? If you're making this monolithic, you want to think through the kinds of questions your leading engineers ask and use them to create a comprehension filter that acts as a way of making the code legible. And again, it does two things. One, it helps to make the code readable and therefore accountable by people in the organization. And two, it becomes something that feeds your flywheel and makes your emails better and improves the quality of your code over time. Can you imagine improving speed and quality of code at the same time? It's the dream. We can do it. We just have to set ourselves up so we don't have dark code. If you've got this far, I hope you realize this is not a security team's problem. This is not an observability problem. This is not an agent pipeline problem. This is an all of us problem. This is a problem for everybody who's building in the software space. And if you think you're not, when was the last time you vibe coded? If you are leading an engineering org right now, the question you should ask yourself is not how's our observability, how's our agentic pipelines. Those are table stakes questions. The question you need to ask yourself is, do I have mechanisms that enable me to make the dark code that I'm producing legible so that I know where I'm driving? Because otherwise, you really are driving with a headlights off and you are liable to run into the ditch and generate problems that you are not aware you're causing from a risk perspective. And that should make you stay up at night. If you're a founder, this is both a competitive mode and also a risk. If you're like most founders, and I'll be honest, I've seen a lot of them, they vibe code so fast and get to market so fast, and they listen to only the speed part of YC teachings, they try and sell you on something that is really a thesis and a trench code. And maybe the code isn't there, and maybe it's not high quality, and maybe it's not what you need to depend on. Honestly, that's a liability for the founder. That's a liability for the company. You can stand out so easily as a founder if you just know the code in this day and age. Just get to know it. Make sure you don't have dark code. Make it legible. explain your trade-offs, be transparent, you're going to stand out, and like be so easy to do business with and build so much trust. And by the way, if you're a vendor, ask for that, right? Ask for transparent code. Ask about dark code. Ask how much if they're shipping a lot, they understand what they're shipping. That is a question vendors should be asking. And if you're just getting started in this field, if you are just getting out of college, if you are just getting into vibe coding and then kind of leaning into the technical track, take this as an opportunity. This whole idea of a comprehension gate, you can set up and I've given one and set one up for you. You can set up a skill that allows you to look at a piece of code and start to understand those questions that senior engineers ask, the principal engineers ask. And that accelerates your comprehension. That makes the code less dark. And then one last note, if you are a senior engineer, if you're a principal and you're used to reviewing by hand, I know this is a massive adjustment. I know trusting AI to give you a comprehension gate is a big step. You absolutely should feel comfortable adjusting and embroidering the prompts and the skills, the stuff I've packaged together with this video so that it feels good to you. It's a tool that needs to feel good in your hand. But I don't think you can avoid using AI to help you understand code because the expectation for volume is not going away. And so you need to figure out how you can remain accountable for the code while putting your eyes across more stuff. And I think that you need essentially lenses on the code that help you to see more farther clearer so that the code is not dark to you because the alternative is just looking at those emailed PR reviews and autofixes from Codeex or Claude Code and saying, "Ah, it's probably fine." You don't want to be that person. That's too risky. Look, nobody's gonna slow down. shipping before you fully understand what you've built is a problem we can fix, but it's not a problem we can fix organizationally by just choosing to go back to the way things work. This is a river we've crossed. AI is helping us speed up. No one wants to slow down. No one should slow down. And I'm not arguing that that is a good idea. I think we need to speed up. I think on average, most orgs still go way too slow. But we have to be honest that going fast imposes new kinds of requirements for understanding the code that we are shipping at speed and that is a different class of problem than the old way of understanding code because the old way of understanding code was human mediated right and one of the larger thesis I've been exploring in 2026 through this video series has really been saying a lot of our human mediated touch points are breaking under the speed that AI is imposing on the business. How do we start to think differently about those mechanisms? And dark code takes that kind of thinking because otherwise it is going to balloon and become an absolute security nightmare. Don't tolerate dark code. It is an organizational choice and you can fight it. Choose to do so.

---

## Timestamped Segments

**[0:00]** Nobody understands their own code

**[0:01]** anymore. There is code running in

**[0:03]** production now at companies we use every

**[0:05]** day that nobody can really explain. Not

**[0:08]** the engineer who shipped it, not the

**[0:10]** team that owns the service, not the CTO.

**[0:12]** The code works. It passes tests. And no

**[0:15]** human on the payroll fully understands

**[0:17]** what it does, why it does it, or what

**[0:19]** would happen if it stopped doing it. The

**[0:21]** industry is starting to call this dark

**[0:23]** code behavior in production that nobody

**[0:25]** can really trace end to end. It's not

**[0:28]** buggy code. It's not spaghetti code and

**[0:30]** it's not technical debt. Dark code is

**[0:32]** code that was never understood by anyone

**[0:34]** at any point because it was made by AI.

**[0:37]** It was generated. It passed automated

**[0:39]** checks and it shipped. The comprehension

**[0:41]** step didn't happen. Not because someone

**[0:43]** was careless, but because the process no

**[0:45]** longer requires it to ship. Now, this is

**[0:47]** often portrayed as a security issue.

**[0:49]** It's often portrayed as an engineering

**[0:50]** quality issue. I think we need to look

**[0:52]** past both of those. It's partly those

**[0:54]** things, but it's really an

**[0:56]** organizational capability problem. It's

**[0:58]** got regulatory exposure elements. It's

**[1:00]** got business liability elements. If you

**[1:02]** are building software right now, there

**[1:04]** is a fundamental shift in what it means

**[1:07]** to be good at your job. And at the heart

**[1:09]** of that shift is grappling with dark

**[1:11]** code, which is only going to 10x from

**[1:13]** here. You think it's a problem now, it's

**[1:15]** going to be 10x more next year. So, in

**[1:17]** this video, I'm going to lay out what's

**[1:18]** actually happening, why the obvious

**[1:20]** responses aren't as effective as they

**[1:22]** seem, and what actually works. So,

**[1:24]** first, let's dig into the problem.

**[1:26]** Anyone who's used AI tools, this is

**[1:28]** going to feel very intuitive. We're not

**[1:29]** going to spend very long on it. We have

**[1:31]** two reasons why dark code is multiplying

**[1:33]** and they interplay to make things worse.

**[1:35]** The first reason is structural. AI

**[1:38]** generating code means that it is harder

**[1:41]** for you to understand the code because

**[1:43]** the AI wrote it in the first place and

**[1:44]** you didn't bang it out with your

**[1:45]** fingers. That is just a structural

**[1:47]** reason why it is harder to understand

**[1:49]** the code unless you're really really

**[1:50]** disciplined with your nonfunctional

**[1:52]** requirements. Hint hint, you should be.

**[1:54]** The other reason why dark code is tough

**[1:57]** is because we are moving so fast. AI

**[2:00]** enables us to move fast. The pressure is

**[2:02]** to move fast. That is part of the reason

**[2:04]** we're making these trillion dollar bets

**[2:05]** on AI as an industry is because we want

**[2:08]** to move fast. When you combine velocity

**[2:11]** with a structural reason not to

**[2:13]** understand code, comprehension starts to

**[2:16]** decouple from authorship unless you take

**[2:18]** really, really clear measures to prevent

**[2:20]** that. So that's the problem. We've all

**[2:22]** lived it. Even if all we've done is type

**[2:24]** in please make this in lovable and it

**[2:26]** makes something fast, that is dark code.

**[2:28]** Why do the obvious responses to dark

**[2:30]** code not work very well? Fundamentally,

**[2:33]** the obvious responses to dark code are

**[2:35]** rooted in the idea that this is a

**[2:37]** tooling problem and it's not a tooling

**[2:39]** problem. Let me give you some examples.

**[2:41]** Number one, there's often a response to

**[2:43]** dark code that says we should make dark

**[2:45]** code observable. If we instrument every

**[2:48]** service in the stack, we're going to

**[2:49]** understand what's happening and that's

**[2:51]** going to give us the ability to respond

**[2:53]** rapidly and effectively. I would respond

**[2:55]** and say, you know what, you should be

**[2:56]** observable. I love telemetry, but that

**[2:59]** doesn't mean the same thing as

**[3:00]** comprehension, right? That doesn't solve

**[3:02]** your dark code problem. It just means

**[3:04]** you can measure what dark code is

**[3:06]** breaking for you in production, which is

**[3:08]** great. You should do that. It's still

**[3:10]** dark code. It doesn't solve the problem.

**[3:12]** The second way people solve this that I

**[3:14]** think is also incorrect is people have

**[3:15]** an instinct and and here I'm especially

**[3:17]** going to call out my colleagues in

**[3:18]** engineering there's an instinct to say

**[3:21]** we can harness the agents so the dark

**[3:24]** code by definition is fine that is

**[3:27]** partly true it is certainly good to have

**[3:29]** guard rails right it is certainly good

**[3:31]** to have excellent orchestration

**[3:32]** platforms I've made videos about it it's

**[3:35]** super important having an excellent

**[3:37]** pipeline reduces your risk in enterprise

**[3:39]** production systems 100% it's really

**[3:41]** important important if you're building

**[3:42]** with an agent in 2026. But if you're

**[3:44]** adding layers to your agent pipeline,

**[3:47]** that is also not actually solving your

**[3:48]** dark code problem. That is just adding a

**[3:51]** layer. And when you try and figure out

**[3:52]** what went wrong with the dark code in

**[3:53]** production, now you have to troubleshoot

**[3:55]** multiple things. So that doesn't solve

**[3:56]** it either. It's still important. You

**[3:58]** still have to do it just like the

**[3:59]** telemetry, but it doesn't solve the

**[4:01]** problem. Answer number three is to say

**[4:03]** it's okay to have dark code and we're

**[4:04]** fine with it. Factory.ai is a famous

**[4:06]** example of this. We're going to see this

**[4:08]** thesis tested. I think it is unlikely

**[4:11]** that we will survive for very long with

**[4:14]** code in production if nobody understands

**[4:16]** it at all. I think there will be

**[4:18]** problems if you don't understand the

**[4:20]** code thoroughly. And I want to give

**[4:22]** factory.ai credit here because I don't

**[4:24]** think it's that they don't understand

**[4:25]** the code. I think is that they're

**[4:27]** extending their understanding with a

**[4:29]** hypothesis that extraordinary testing

**[4:32]** and extraordinary discipline at the eval

**[4:35]** layer proxies for that understanding in

**[4:37]** a way that is useful and allows them to

**[4:39]** learn from their code. That is a genuine

**[4:42]** hypothesis that not a lot of people are

**[4:43]** trying and most of the people who are

**[4:45]** yoloing their code into production

**[4:47]** aren't as disciplined as factory.ai. So

**[4:49]** regardless of how you do it, maybe

**[4:50]** you're super disciplined, maybe you're

**[4:52]** good at your non-functional emails and

**[4:54]** that's how you're extending this. Or

**[4:55]** maybe like most orgs that I've seen, you

**[4:57]** just yolo the dark code and the PM puts

**[4:59]** stuff out there and the engineering team

**[5:01]** puts stuff out there and the marketing

**[5:02]** team puts stuff out there and you gain

**[5:04]** it a little bit, right? You know, the

**[5:05]** marketing team has to manage the website

**[5:07]** and the PM can only vibe code up to a

**[5:09]** certain stage and then engineering has

**[5:10]** to take it. But the problem with all of

**[5:13]** this yoloing is that nobody owns the

**[5:16]** sustained total package of code in

**[5:18]** production. You have problems with

**[5:20]** ownership because you have distributed

**[5:23]** authorship. And distributed authorship

**[5:25]** is a strength we want to encourage. So

**[5:27]** it's not as intuitive as saying you got

**[5:28]** to shut it off. And I know IT

**[5:30]** departments who are like, you know what,

**[5:31]** we're shutting it all off. Nobody can

**[5:33]** vibe code. Only engineers can write

**[5:34]** code. They're in trouble too. They're in

**[5:36]** trouble because they can't ship fast. So

**[5:38]** the answer is not as simple as don't do

**[5:40]** it. You have to let people code and

**[5:42]** start to build. That's actually super

**[5:44]** important. But you have to think through

**[5:46]** what accountability looks like when

**[5:48]** everybody is now able to code. And that

**[5:49]** is a hard problem. I think AI's

**[5:51]** strengths really mask its weaknesses

**[5:53]** here. So we've talked about some of

**[5:54]** these different responses that

**[5:56]** organizations make, right? Some of them

**[5:57]** are like observation matters, telemetry

**[5:59]** matters, that's how we solve it. Some of

**[6:00]** them are like agentic pipelines matter,

**[6:02]** that's how we solve it. And those are

**[6:03]** both important things. And some of them

**[6:04]** are like, you know, yolo, like for one

**[6:06]** way or another, we're going to accept

**[6:07]** that there's dark code and we'll deal

**[6:08]** with it. The issue here is that it looks

**[6:11]** more okay to yolo stuff. It looks more

**[6:13]** okay to say we'll just observe it in

**[6:15]** production. As AI gets stronger. And so,

**[6:17]** in a sense, AI's strengths really mask

**[6:20]** its weaknesses because the stronger an

**[6:21]** AI model becomes, the easier it becomes

**[6:24]** to say, you know what, it's okay. We're

**[6:26]** not going to go there. The AI will know

**[6:28]** what its code is and does, and the AI

**[6:30]** will be the one that fixes the code and

**[6:31]** we're just going to let it be. Right? I

**[6:32]** think the challenge with that is that it

**[6:34]** is hard to know when the AI is

**[6:36]** overconfident and when it is not. And so

**[6:38]** this is a situation where if you're like

**[6:40]** well how do AI native orgs solve this

**[6:41]** problem? How does anthropic solve this

**[6:43]** problem? How does open AAI solve this

**[6:44]** problem? It is sort of like an amalgam

**[6:48]** of multiple approaches that I've

**[6:49]** described here without an assumption

**[6:52]** that AI is magical. Yes, the AI native

**[6:54]** companies do not have an assumption that

**[6:56]** AI is magical. So they're going to

**[6:57]** invest heavily in eval sort of like

**[6:59]** factory.ai does. They're going to invest

**[7:02]** a lot in understanding their agentic

**[7:05]** pipelines. We saw that with a claude

**[7:06]** code leak. They're going to invest a ton

**[7:09]** in telemetry and understanding how their

**[7:11]** systems work in production. And all of

**[7:13]** those don't mask the fact that they are

**[7:15]** also having individual engineers still

**[7:18]** commit PRs and still have reviews of

**[7:20]** those code and still understand the code

**[7:22]** that's going out. And in that sense, as

**[7:24]** much as AI is doing a lot of the codew

**[7:26]** writing, they are still demanding a

**[7:28]** degree of legibility and comprehension

**[7:29]** from engineering teams that reflects the

**[7:32]** sophistication of the work that they're

**[7:34]** doing. Ironically, right now, the moves

**[7:35]** that the industry is making are

**[7:37]** compounding this problem for the worse.

**[7:39]** Dark code gets worse when we lay off

**[7:42]** people and expect the others to do even

**[7:44]** more and they don't have time to

**[7:45]** understand the code. We are in a sense

**[7:48]** creating more of a dark code problem for

**[7:50]** ourselves, the more we lay off engineers

**[7:53]** across the industry. And if you think

**[7:54]** this is just an engineering team

**[7:55]** problem, this is a company entity board

**[7:58]** level problem, right? questions about

**[8:00]** sock 2, questions about encryption at

**[8:02]** risk, things that companies become

**[8:04]** liable for are things that dark code

**[8:07]** touches. And if we don't have good

**[8:09]** answers for those answers we are held

**[8:11]** accountable to, we are going to be in

**[8:13]** trouble. So you get the idea. We have

**[8:15]** tried different things. We've tried

**[8:16]** observability. We've tried telemetry.

**[8:18]** We've seen hints of how this works as

**[8:19]** the labs have opened up the kimono and

**[8:21]** showed us a little bit of how they work

**[8:22]** internally through interviews and

**[8:23]** newspaper pieces and and comments on X.

**[8:26]** But what we really need is a

**[8:28]** comprehensive approach to dark code that

**[8:31]** treats it as what it really is, an

**[8:33]** organizational capability problem. And

**[8:35]** that's what I want to lay out here in

**[8:37]** the second part of this video. So what

**[8:38]** actually helps? If dark code is an

**[8:40]** organizational problem, what do we need

**[8:43]** to do to fix it as a team? I think there

**[8:46]** are three layers to this solution and I

**[8:48]** want to talk about each of them

**[8:49]** separately. Layer one is simple. Force

**[8:51]** understanding before the code exists.

**[8:54]** There are two ways people fail at this.

**[8:57]** Number one, there are a lot of teams in

**[8:59]** 2026 that persist in 2010's era of

**[9:02]** product development where they

**[9:03]** overdocument before they go and they do

**[9:05]** it for the sake of human process. I've

**[9:07]** argued against this strenuously. I've

**[9:09]** said agents are becoming more and more

**[9:11]** and more the heart of the development

**[9:13]** process so we can speed up. I'm going to

**[9:16]** say it again. As long as you understand

**[9:18]** what you want to build and can write it

**[9:20]** out clearly, go. But for people

**[9:23]** increasingly in 2026 who just want to go

**[9:26]** and who don't want to take time to

**[9:27]** understand this principle is also a

**[9:30]** break. Stop understand what you want to

**[9:33]** build then go make the code exist. Do

**[9:35]** you see what I mean? I'm not giving you

**[9:36]** a blank check to just go vibe code. I'm

**[9:39]** also not telling you slow down for lots

**[9:40]** of process. I'm saying do just enough to

**[9:44]** understand what you want to build in a

**[9:46]** degree of detail you can write down.

**[9:48]** That's it. That is such an

**[9:51]** organizational discipline because so

**[9:52]** many people want to fall off on one side

**[9:54]** or the other. They want to jump into

**[9:55]** process and say, "Give me a linear

**[9:57]** process. I want to have like 16

**[9:59]** artifacts I have to make." Not because I

**[10:01]** want them, but because that gives me an

**[10:03]** assurance that I've thought about it and

**[10:04]** I don't have to get in trouble if

**[10:05]** something goes wrong. No, no, no. It's

**[10:08]** your code. You own it. You're liable.

**[10:10]** You're accountable. Make sure you

**[10:12]** understand what you want to build.

**[10:13]** That's all you have to do. That's it.

**[10:15]** That's the principle. force

**[10:16]** understanding as a cultural primary

**[10:20]** artifact before the code exists. I call

**[10:22]** this specd driven development. You

**[10:23]** basically write the spec out and that

**[10:25]** makes it really clear. And here's a

**[10:27]** detail worth noting. After the December

**[10:29]** outage, Amazon actually rebuilt their

**[10:31]** coding tool Kira with exactly this

**[10:33]** concept. The tool now leads with

**[10:35]** specdriven development, turning prompts

**[10:37]** into requirements, tasks, and task lists

**[10:40]** before the code gets generated. They

**[10:42]** learned very expensively that AI coding

**[10:44]** tools need to force comprehension before

**[10:47]** generation. When the company that

**[10:48]** learned this lesson the hardest bakes it

**[10:50]** into the product, maybe we should all

**[10:51]** learn that lesson. And by the way, if

**[10:52]** you're wondering how do specs relate to

**[10:54]** evals, I'll give you a hint. The spec

**[10:57]** becomes the eval. It's actually not that

**[10:59]** hard. If you can write out a clear spec,

**[11:01]** that is how you get an eval that you can

**[11:04]** then set the agent again. Because really

**[11:06]** all you're doing with an eval is you're

**[11:07]** saying, "Here is the test. The test is

**[11:09]** the spec. the agent is going to keep

**[11:11]** trying to pass the test until it does.

**[11:13]** So writing a clear spec helps you to get

**[11:15]** good code and also code you can

**[11:17]** understand. Layer two, right? Make your

**[11:20]** systems inherently selfdescribing. So

**[11:23]** I'm not talking about an agent

**[11:25]** self-reporting. That's not what I mean

**[11:26]** here. I dismissed that earlier in this

**[11:28]** video. I'm talking about something more

**[11:29]** structural. Context engineering is the

**[11:32]** practice of restructuring your codebase

**[11:34]** so comprehension is embedded in the code

**[11:36]** itself. That's part of what we do with

**[11:38]** context engineering. Some people think

**[11:40]** it's just getting the docs together.

**[11:41]** It's also the code. You don't want the

**[11:43]** code understanding locked in the heads

**[11:45]** of people. You want it easily and

**[11:47]** immediately legible to humans and agents

**[11:49]** alike. So think about this in three

**[11:51]** layers. I know this is a three layer and

**[11:52]** a three layer. Stick with me. We're not

**[11:54]** going to go too far down the rabbit

**[11:55]** hole. If you're making a system

**[11:56]** self-describing, part one is make sure

**[11:58]** you have structural context that answers

**[12:01]** the question where. Every module should

**[12:04]** have a manifest that describes what it

**[12:07]** does, what it depends on, and what

**[12:09]** depends on it. Where does this code go

**[12:11]** to? Right? Part two, have semantic

**[12:14]** context. Semantic context needs to

**[12:17]** answer the question, what? In other

**[12:19]** words, when an AI reads an interface, it

**[12:22]** needs to read semantic context that

**[12:25]** gives it the rules of engagement, not

**[12:27]** just the shape of the data. What I mean

**[12:28]** by rules of engagement are things like

**[12:30]** performance expectations, failure modes,

**[12:33]** retry semantics, behavioral contracts.

**[12:36]** Basically, how the interface is expected

**[12:38]** to behave. This is a cousin to the idea

**[12:40]** that we should have API contracts.

**[12:42]** Right? In this case, what I'm saying is

**[12:44]** all interfaces need a degree of semantic

**[12:46]** context, not just API interfaces. Layer

**[12:50]** three, you're trying to catch what the

**[12:51]** first two layers miss. What I'm

**[12:53]** suggesting is we talk about eval driven

**[12:56]** development as having a test and then

**[12:57]** once you pass functional and

**[12:59]** non-functional tests, the code is

**[13:01]** reviewed by a senior engineer and it

**[13:03]** ships. Now, we're running into a

**[13:04]** situation where there's so much code

**[13:06]** generation where engineers have trouble

**[13:08]** making that legible. My goal is to put a

**[13:11]** comprehension gate in front of the code

**[13:15]** as a senior engineer is trying to read

**[13:16]** it and keep an eye on the PRs that are

**[13:18]** coming across his or her desk. And I

**[13:20]** want that comprehension gate to make key

**[13:22]** questions that a senior engineer would

**[13:24]** ask immediately and obviously legible.

**[13:27]** And yes, if you're wondering, can AI do

**[13:29]** this and help? It can. Can AI discover

**[13:32]** things through that comprehension check

**[13:34]** that we pass back to the evals for

**[13:36]** better code? 100%. This is a flywheel.

**[13:39]** Ask questions that a good senior

**[13:41]** engineer is going to ask. A good senior

**[13:43]** engineer is going to ask you, why did

**[13:45]** you call that dependency here? Why did

**[13:47]** you structure the code so that it caches

**[13:49]** in a location unreadable by other

**[13:51]** services? How are you thinking about

**[13:53]** separation of concerns? If you're making

**[13:55]** this monolithic, you want to think

**[13:57]** through the kinds of questions your

**[14:00]** leading engineers ask and use them to

**[14:03]** create a comprehension filter that acts

**[14:06]** as a way of making the code legible. And

**[14:10]** again, it does two things. One, it helps

**[14:12]** to make the code readable and therefore

**[14:13]** accountable by people in the

**[14:15]** organization. And two, it becomes

**[14:17]** something that feeds your flywheel and

**[14:19]** makes your emails better and improves

**[14:21]** the quality of your code over time. Can

**[14:23]** you imagine improving speed and quality

**[14:24]** of code at the same time? It's the

**[14:26]** dream. We can do it. We just have to set

**[14:28]** ourselves up so we don't have dark code.

**[14:29]** If you've got this far, I hope you

**[14:31]** realize this is not a security team's

**[14:33]** problem. This is not an observability

**[14:34]** problem. This is not an agent pipeline

**[14:36]** problem. This is an all of us problem.

**[14:39]** This is a problem for everybody who's

**[14:40]** building in the software space. And if

**[14:42]** you think you're not, when was the last

**[14:44]** time you vibe coded? If you are leading

**[14:46]** an engineering org right now, the

**[14:47]** question you should ask yourself is not

**[14:49]** how's our observability, how's our

**[14:51]** agentic pipelines. Those are table

**[14:52]** stakes questions. The question you need

**[14:54]** to ask yourself is, do I have mechanisms

**[14:56]** that enable me to make the dark code

**[14:58]** that I'm producing legible so that I

**[15:00]** know where I'm driving? Because

**[15:01]** otherwise, you really are driving with a

**[15:03]** headlights off and you are liable to run

**[15:04]** into the ditch and generate problems

**[15:06]** that you are not aware you're causing

**[15:07]** from a risk perspective. And that should

**[15:09]** make you stay up at night. If you're a

**[15:11]** founder, this is both a competitive mode

**[15:13]** and also a risk. If you're like most

**[15:15]** founders, and I'll be honest, I've seen

**[15:16]** a lot of them, they vibe code so fast

**[15:18]** and get to market so fast, and they

**[15:20]** listen to only the speed part of YC

**[15:22]** teachings, they try and sell you on

**[15:24]** something that is really a thesis and a

**[15:25]** trench code. And maybe the code isn't

**[15:27]** there, and maybe it's not high quality,

**[15:28]** and maybe it's not what you need to

**[15:29]** depend on. Honestly, that's a liability

**[15:32]** for the founder. That's a liability for

**[15:34]** the company. You can stand out so easily

**[15:37]** as a founder if you just know the code

**[15:39]** in this day and age. Just get to know

**[15:41]** it. Make sure you don't have dark code.

**[15:42]** Make it legible. explain your

**[15:44]** trade-offs, be transparent, you're going

**[15:46]** to stand out, and like be so easy to do

**[15:48]** business with and build so much trust.

**[15:50]** And by the way, if you're a vendor, ask

**[15:52]** for that, right? Ask for transparent

**[15:54]** code. Ask about dark code. Ask how much

**[15:57]** if they're shipping a lot, they

**[15:59]** understand what they're shipping. That

**[16:00]** is a question vendors should be asking.

**[16:03]** And if you're just getting started in

**[16:04]** this field, if you are just getting out

**[16:06]** of college, if you are just getting into

**[16:09]** vibe coding and then kind of leaning

**[16:10]** into the technical track, take this as

**[16:12]** an opportunity. This whole idea of a

**[16:14]** comprehension gate, you can set up and

**[16:16]** I've given one and set one up for you.

**[16:19]** You can set up a skill that allows you

**[16:22]** to look at a piece of code and start to

**[16:23]** understand those questions that senior

**[16:25]** engineers ask, the principal engineers

**[16:27]** ask. And that accelerates your

**[16:29]** comprehension. That makes the code less

**[16:31]** dark. And then one last note, if you are

**[16:35]** a senior engineer, if you're a principal

**[16:37]** and you're used to reviewing by hand, I

**[16:39]** know this is a massive adjustment. I

**[16:40]** know trusting AI to give you a

**[16:42]** comprehension gate is a big step. You

**[16:45]** absolutely should feel comfortable

**[16:47]** adjusting and embroidering the prompts

**[16:48]** and the skills, the stuff I've packaged

**[16:50]** together with this video so that it

**[16:52]** feels good to you. It's a tool that

**[16:54]** needs to feel good in your hand. But I

**[16:56]** don't think you can avoid using AI to

**[16:59]** help you understand code because the

**[17:01]** expectation for volume is not going

**[17:03]** away. And so you need to figure out how

**[17:05]** you can remain accountable for the code

**[17:07]** while putting your eyes across more

**[17:09]** stuff. And I think that you need

**[17:11]** essentially lenses on the code that help

**[17:13]** you to see more farther clearer so that

**[17:16]** the code is not dark to you because the

**[17:18]** alternative is just looking at those

**[17:20]** emailed PR reviews and autofixes from

**[17:23]** Codeex or Claude Code and saying, "Ah,

**[17:25]** it's probably fine." You don't want to

**[17:27]** be that person. That's too risky. Look,

**[17:31]** nobody's gonna slow down. shipping

**[17:33]** before you fully understand what you've

**[17:35]** built is a problem we can fix, but it's

**[17:37]** not a problem we can fix

**[17:38]** organizationally by just choosing to go

**[17:41]** back to the way things work. This is a

**[17:42]** river we've crossed. AI is helping us

**[17:44]** speed up. No one wants to slow down. No

**[17:47]** one should slow down. And I'm not

**[17:48]** arguing that that is a good idea. I

**[17:50]** think we need to speed up. I think on

**[17:52]** average, most orgs still go way too

**[17:54]** slow. But we have to be honest that

**[17:58]** going fast imposes new kinds of

**[18:02]** requirements for understanding the code

**[18:04]** that we are shipping at speed and that

**[18:06]** is a different class of problem than the

**[18:09]** old way of understanding code because

**[18:10]** the old way of understanding code was

**[18:11]** human mediated right and one of the

**[18:13]** larger thesis I've been exploring in

**[18:15]** 2026 through this video series has

**[18:16]** really been saying a lot of our human

**[18:18]** mediated touch points are breaking under

**[18:20]** the speed that AI is imposing on the

**[18:22]** business. How do we start to think

**[18:25]** differently about those mechanisms? And

**[18:27]** dark code takes that kind of thinking

**[18:29]** because otherwise it is going to balloon

**[18:31]** and become an absolute security

**[18:32]** nightmare. Don't tolerate dark code. It

**[18:35]** is an organizational choice and you can

**[18:37]** fight it. Choose to do so.

**[0:00]** Nobody understands their own code

**[0:01]** anymore. There is code running in

**[0:03]** production now at companies we use every

**[0:05]** day that nobody can really explain. Not

**[0:08]** the engineer who shipped it, not the

**[0:10]** team that owns the service, not the CTO.

**[0:12]** The code works. It passes tests. And no

**[0:15]** human on the payroll fully understands

**[0:17]** what it does, why it does it, or what

**[0:19]** would happen if it stopped doing it. The

**[0:21]** industry is starting to call this dark

**[0:23]** code behavior in production that nobody

**[0:25]** can really trace end to end. It's not

**[0:28]** buggy code. It's not spaghetti code and

**[0:30]** it's not technical debt. Dark code is

**[0:32]** code that was never understood by anyone

**[0:34]** at any point because it was made by AI.

**[0:37]** It was generated. It passed automated

**[0:39]** checks and it shipped. The comprehension

**[0:41]** step didn't happen. Not because someone

**[0:43]** was careless, but because the process no

**[0:45]** longer requires it to ship. Now, this is

**[0:47]** often portrayed as a security issue.

**[0:49]** It's often portrayed as an engineering

**[0:50]** quality issue. I think we need to look

**[0:52]** past both of those. It's partly those

**[0:54]** things, but it's really an

**[0:56]** organizational capability problem. It's

**[0:58]** got regulatory exposure elements. It's

**[1:00]** got business liability elements. If you

**[1:02]** are building software right now, there

**[1:04]** is a fundamental shift in what it means

**[1:07]** to be good at your job. And at the heart

**[1:09]** of that shift is grappling with dark

**[1:11]** code, which is only going to 10x from

**[1:13]** here. You think it's a problem now, it's

**[1:15]** going to be 10x more next year. So, in

**[1:17]** this video, I'm going to lay out what's

**[1:18]** actually happening, why the obvious

**[1:20]** responses aren't as effective as they

**[1:22]** seem, and what actually works. So,

**[1:24]** first, let's dig into the problem.

**[1:26]** Anyone who's used AI tools, this is

**[1:28]** going to feel very intuitive. We're not

**[1:29]** going to spend very long on it. We have

**[1:31]** two reasons why dark code is multiplying

**[1:33]** and they interplay to make things worse.

**[1:35]** The first reason is structural. AI

**[1:38]** generating code means that it is harder

**[1:41]** for you to understand the code because

**[1:43]** the AI wrote it in the first place and

**[1:44]** you didn't bang it out with your

**[1:45]** fingers. That is just a structural

**[1:47]** reason why it is harder to understand

**[1:49]** the code unless you're really really

**[1:50]** disciplined with your nonfunctional

**[1:52]** requirements. Hint hint, you should be.

**[1:54]** The other reason why dark code is tough

**[1:57]** is because we are moving so fast. AI

**[2:00]** enables us to move fast. The pressure is

**[2:02]** to move fast. That is part of the reason

**[2:04]** we're making these trillion dollar bets

**[2:05]** on AI as an industry is because we want

**[2:08]** to move fast. When you combine velocity

**[2:11]** with a structural reason not to

**[2:13]** understand code, comprehension starts to

**[2:16]** decouple from authorship unless you take

**[2:18]** really, really clear measures to prevent

**[2:20]** that. So that's the problem. We've all

**[2:22]** lived it. Even if all we've done is type

**[2:24]** in please make this in lovable and it

**[2:26]** makes something fast, that is dark code.

**[2:28]** Why do the obvious responses to dark

**[2:30]** code not work very well? Fundamentally,

**[2:33]** the obvious responses to dark code are

**[2:35]** rooted in the idea that this is a

**[2:37]** tooling problem and it's not a tooling

**[2:39]** problem. Let me give you some examples.

**[2:41]** Number one, there's often a response to

**[2:43]** dark code that says we should make dark

**[2:45]** code observable. If we instrument every

**[2:48]** service in the stack, we're going to

**[2:49]** understand what's happening and that's

**[2:51]** going to give us the ability to respond

**[2:53]** rapidly and effectively. I would respond

**[2:55]** and say, you know what, you should be

**[2:56]** observable. I love telemetry, but that

**[2:59]** doesn't mean the same thing as

**[3:00]** comprehension, right? That doesn't solve

**[3:02]** your dark code problem. It just means

**[3:04]** you can measure what dark code is

**[3:06]** breaking for you in production, which is

**[3:08]** great. You should do that. It's still

**[3:10]** dark code. It doesn't solve the problem.

**[3:12]** The second way people solve this that I

**[3:14]** think is also incorrect is people have

**[3:15]** an instinct and and here I'm especially

**[3:17]** going to call out my colleagues in

**[3:18]** engineering there's an instinct to say

**[3:21]** we can harness the agents so the dark

**[3:24]** code by definition is fine that is

**[3:27]** partly true it is certainly good to have

**[3:29]** guard rails right it is certainly good

**[3:31]** to have excellent orchestration

**[3:32]** platforms I've made videos about it it's

**[3:35]** super important having an excellent

**[3:37]** pipeline reduces your risk in enterprise

**[3:39]** production systems 100% it's really

**[3:41]** important important if you're building

**[3:42]** with an agent in 2026. But if you're

**[3:44]** adding layers to your agent pipeline,

**[3:47]** that is also not actually solving your

**[3:48]** dark code problem. That is just adding a

**[3:51]** layer. And when you try and figure out

**[3:52]** what went wrong with the dark code in

**[3:53]** production, now you have to troubleshoot

**[3:55]** multiple things. So that doesn't solve

**[3:56]** it either. It's still important. You

**[3:58]** still have to do it just like the

**[3:59]** telemetry, but it doesn't solve the

**[4:01]** problem. Answer number three is to say

**[4:03]** it's okay to have dark code and we're

**[4:04]** fine with it. Factory.ai is a famous

**[4:06]** example of this. We're going to see this

**[4:08]** thesis tested. I think it is unlikely

**[4:11]** that we will survive for very long with

**[4:14]** code in production if nobody understands

**[4:16]** it at all. I think there will be

**[4:18]** problems if you don't understand the

**[4:20]** code thoroughly. And I want to give

**[4:22]** factory.ai credit here because I don't

**[4:24]** think it's that they don't understand

**[4:25]** the code. I think is that they're

**[4:27]** extending their understanding with a

**[4:29]** hypothesis that extraordinary testing

**[4:32]** and extraordinary discipline at the eval

**[4:35]** layer proxies for that understanding in

**[4:37]** a way that is useful and allows them to

**[4:39]** learn from their code. That is a genuine

**[4:42]** hypothesis that not a lot of people are

**[4:43]** trying and most of the people who are

**[4:45]** yoloing their code into production

**[4:47]** aren't as disciplined as factory.ai. So

**[4:49]** regardless of how you do it, maybe

**[4:50]** you're super disciplined, maybe you're

**[4:52]** good at your non-functional emails and

**[4:54]** that's how you're extending this. Or

**[4:55]** maybe like most orgs that I've seen, you

**[4:57]** just yolo the dark code and the PM puts

**[4:59]** stuff out there and the engineering team

**[5:01]** puts stuff out there and the marketing

**[5:02]** team puts stuff out there and you gain

**[5:04]** it a little bit, right? You know, the

**[5:05]** marketing team has to manage the website

**[5:07]** and the PM can only vibe code up to a

**[5:09]** certain stage and then engineering has

**[5:10]** to take it. But the problem with all of

**[5:13]** this yoloing is that nobody owns the

**[5:16]** sustained total package of code in

**[5:18]** production. You have problems with

**[5:20]** ownership because you have distributed

**[5:23]** authorship. And distributed authorship

**[5:25]** is a strength we want to encourage. So

**[5:27]** it's not as intuitive as saying you got

**[5:28]** to shut it off. And I know IT

**[5:30]** departments who are like, you know what,

**[5:31]** we're shutting it all off. Nobody can

**[5:33]** vibe code. Only engineers can write

**[5:34]** code. They're in trouble too. They're in

**[5:36]** trouble because they can't ship fast. So

**[5:38]** the answer is not as simple as don't do

**[5:40]** it. You have to let people code and

**[5:42]** start to build. That's actually super

**[5:44]** important. But you have to think through

**[5:46]** what accountability looks like when

**[5:48]** everybody is now able to code. And that

**[5:49]** is a hard problem. I think AI's

**[5:51]** strengths really mask its weaknesses

**[5:53]** here. So we've talked about some of

**[5:54]** these different responses that

**[5:56]** organizations make, right? Some of them

**[5:57]** are like observation matters, telemetry

**[5:59]** matters, that's how we solve it. Some of

**[6:00]** them are like agentic pipelines matter,

**[6:02]** that's how we solve it. And those are

**[6:03]** both important things. And some of them

**[6:04]** are like, you know, yolo, like for one

**[6:06]** way or another, we're going to accept

**[6:07]** that there's dark code and we'll deal

**[6:08]** with it. The issue here is that it looks

**[6:11]** more okay to yolo stuff. It looks more

**[6:13]** okay to say we'll just observe it in

**[6:15]** production. As AI gets stronger. And so,

**[6:17]** in a sense, AI's strengths really mask

**[6:20]** its weaknesses because the stronger an

**[6:21]** AI model becomes, the easier it becomes

**[6:24]** to say, you know what, it's okay. We're

**[6:26]** not going to go there. The AI will know

**[6:28]** what its code is and does, and the AI

**[6:30]** will be the one that fixes the code and

**[6:31]** we're just going to let it be. Right? I

**[6:32]** think the challenge with that is that it

**[6:34]** is hard to know when the AI is

**[6:36]** overconfident and when it is not. And so

**[6:38]** this is a situation where if you're like

**[6:40]** well how do AI native orgs solve this

**[6:41]** problem? How does anthropic solve this

**[6:43]** problem? How does open AAI solve this

**[6:44]** problem? It is sort of like an amalgam

**[6:48]** of multiple approaches that I've

**[6:49]** described here without an assumption

**[6:52]** that AI is magical. Yes, the AI native

**[6:54]** companies do not have an assumption that

**[6:56]** AI is magical. So they're going to

**[6:57]** invest heavily in eval sort of like

**[6:59]** factory.ai does. They're going to invest

**[7:02]** a lot in understanding their agentic

**[7:05]** pipelines. We saw that with a claude

**[7:06]** code leak. They're going to invest a ton

**[7:09]** in telemetry and understanding how their

**[7:11]** systems work in production. And all of

**[7:13]** those don't mask the fact that they are

**[7:15]** also having individual engineers still

**[7:18]** commit PRs and still have reviews of

**[7:20]** those code and still understand the code

**[7:22]** that's going out. And in that sense, as

**[7:24]** much as AI is doing a lot of the codew

**[7:26]** writing, they are still demanding a

**[7:28]** degree of legibility and comprehension

**[7:29]** from engineering teams that reflects the

**[7:32]** sophistication of the work that they're

**[7:34]** doing. Ironically, right now, the moves

**[7:35]** that the industry is making are

**[7:37]** compounding this problem for the worse.

**[7:39]** Dark code gets worse when we lay off

**[7:42]** people and expect the others to do even

**[7:44]** more and they don't have time to

**[7:45]** understand the code. We are in a sense

**[7:48]** creating more of a dark code problem for

**[7:50]** ourselves, the more we lay off engineers

**[7:53]** across the industry. And if you think

**[7:54]** this is just an engineering team

**[7:55]** problem, this is a company entity board

**[7:58]** level problem, right? questions about

**[8:00]** sock 2, questions about encryption at

**[8:02]** risk, things that companies become

**[8:04]** liable for are things that dark code

**[8:07]** touches. And if we don't have good

**[8:09]** answers for those answers we are held

**[8:11]** accountable to, we are going to be in

**[8:13]** trouble. So you get the idea. We have

**[8:15]** tried different things. We've tried

**[8:16]** observability. We've tried telemetry.

**[8:18]** We've seen hints of how this works as

**[8:19]** the labs have opened up the kimono and

**[8:21]** showed us a little bit of how they work

**[8:22]** internally through interviews and

**[8:23]** newspaper pieces and and comments on X.

**[8:26]** But what we really need is a

**[8:28]** comprehensive approach to dark code that

**[8:31]** treats it as what it really is, an

**[8:33]** organizational capability problem. And

**[8:35]** that's what I want to lay out here in

**[8:37]** the second part of this video. So what

**[8:38]** actually helps? If dark code is an

**[8:40]** organizational problem, what do we need

**[8:43]** to do to fix it as a team? I think there

**[8:46]** are three layers to this solution and I

**[8:48]** want to talk about each of them

**[8:49]** separately. Layer one is simple. Force

**[8:51]** understanding before the code exists.

**[8:54]** There are two ways people fail at this.

**[8:57]** Number one, there are a lot of teams in

**[8:59]** 2026 that persist in 2010's era of

**[9:02]** product development where they

**[9:03]** overdocument before they go and they do

**[9:05]** it for the sake of human process. I've

**[9:07]** argued against this strenuously. I've

**[9:09]** said agents are becoming more and more

**[9:11]** and more the heart of the development

**[9:13]** process so we can speed up. I'm going to

**[9:16]** say it again. As long as you understand

**[9:18]** what you want to build and can write it

**[9:20]** out clearly, go. But for people

**[9:23]** increasingly in 2026 who just want to go

**[9:26]** and who don't want to take time to

**[9:27]** understand this principle is also a

**[9:30]** break. Stop understand what you want to

**[9:33]** build then go make the code exist. Do

**[9:35]** you see what I mean? I'm not giving you

**[9:36]** a blank check to just go vibe code. I'm

**[9:39]** also not telling you slow down for lots

**[9:40]** of process. I'm saying do just enough to

**[9:44]** understand what you want to build in a

**[9:46]** degree of detail you can write down.

**[9:48]** That's it. That is such an

**[9:51]** organizational discipline because so

**[9:52]** many people want to fall off on one side

**[9:54]** or the other. They want to jump into

**[9:55]** process and say, "Give me a linear

**[9:57]** process. I want to have like 16

**[9:59]** artifacts I have to make." Not because I

**[10:01]** want them, but because that gives me an

**[10:03]** assurance that I've thought about it and

**[10:04]** I don't have to get in trouble if

**[10:05]** something goes wrong. No, no, no. It's

**[10:08]** your code. You own it. You're liable.

**[10:10]** You're accountable. Make sure you

**[10:12]** understand what you want to build.

**[10:13]** That's all you have to do. That's it.

**[10:15]** That's the principle. force

**[10:16]** understanding as a cultural primary

**[10:20]** artifact before the code exists. I call

**[10:22]** this specd driven development. You

**[10:23]** basically write the spec out and that

**[10:25]** makes it really clear. And here's a

**[10:27]** detail worth noting. After the December

**[10:29]** outage, Amazon actually rebuilt their

**[10:31]** coding tool Kira with exactly this

**[10:33]** concept. The tool now leads with

**[10:35]** specdriven development, turning prompts

**[10:37]** into requirements, tasks, and task lists

**[10:40]** before the code gets generated. They

**[10:42]** learned very expensively that AI coding

**[10:44]** tools need to force comprehension before

**[10:47]** generation. When the company that

**[10:48]** learned this lesson the hardest bakes it

**[10:50]** into the product, maybe we should all

**[10:51]** learn that lesson. And by the way, if

**[10:52]** you're wondering how do specs relate to

**[10:54]** evals, I'll give you a hint. The spec

**[10:57]** becomes the eval. It's actually not that

**[10:59]** hard. If you can write out a clear spec,

**[11:01]** that is how you get an eval that you can

**[11:04]** then set the agent again. Because really

**[11:06]** all you're doing with an eval is you're

**[11:07]** saying, "Here is the test. The test is

**[11:09]** the spec. the agent is going to keep

**[11:11]** trying to pass the test until it does.

**[11:13]** So writing a clear spec helps you to get

**[11:15]** good code and also code you can

**[11:17]** understand. Layer two, right? Make your

**[11:20]** systems inherently selfdescribing. So

**[11:23]** I'm not talking about an agent

**[11:25]** self-reporting. That's not what I mean

**[11:26]** here. I dismissed that earlier in this

**[11:28]** video. I'm talking about something more

**[11:29]** structural. Context engineering is the

**[11:32]** practice of restructuring your codebase

**[11:34]** so comprehension is embedded in the code

**[11:36]** itself. That's part of what we do with

**[11:38]** context engineering. Some people think

**[11:40]** it's just getting the docs together.

**[11:41]** It's also the code. You don't want the

**[11:43]** code understanding locked in the heads

**[11:45]** of people. You want it easily and

**[11:47]** immediately legible to humans and agents

**[11:49]** alike. So think about this in three

**[11:51]** layers. I know this is a three layer and

**[11:52]** a three layer. Stick with me. We're not

**[11:54]** going to go too far down the rabbit

**[11:55]** hole. If you're making a system

**[11:56]** self-describing, part one is make sure

**[11:58]** you have structural context that answers

**[12:01]** the question where. Every module should

**[12:04]** have a manifest that describes what it

**[12:07]** does, what it depends on, and what

**[12:09]** depends on it. Where does this code go

**[12:11]** to? Right? Part two, have semantic

**[12:14]** context. Semantic context needs to

**[12:17]** answer the question, what? In other

**[12:19]** words, when an AI reads an interface, it

**[12:22]** needs to read semantic context that

**[12:25]** gives it the rules of engagement, not

**[12:27]** just the shape of the data. What I mean

**[12:28]** by rules of engagement are things like

**[12:30]** performance expectations, failure modes,

**[12:33]** retry semantics, behavioral contracts.

**[12:36]** Basically, how the interface is expected

**[12:38]** to behave. This is a cousin to the idea

**[12:40]** that we should have API contracts.

**[12:42]** Right? In this case, what I'm saying is

**[12:44]** all interfaces need a degree of semantic

**[12:46]** context, not just API interfaces. Layer

**[12:50]** three, you're trying to catch what the

**[12:51]** first two layers miss. What I'm

**[12:53]** suggesting is we talk about eval driven

**[12:56]** development as having a test and then

**[12:57]** once you pass functional and

**[12:59]** non-functional tests, the code is

**[13:01]** reviewed by a senior engineer and it

**[13:03]** ships. Now, we're running into a

**[13:04]** situation where there's so much code

**[13:06]** generation where engineers have trouble

**[13:08]** making that legible. My goal is to put a

**[13:11]** comprehension gate in front of the code

**[13:15]** as a senior engineer is trying to read

**[13:16]** it and keep an eye on the PRs that are

**[13:18]** coming across his or her desk. And I

**[13:20]** want that comprehension gate to make key

**[13:22]** questions that a senior engineer would

**[13:24]** ask immediately and obviously legible.

**[13:27]** And yes, if you're wondering, can AI do

**[13:29]** this and help? It can. Can AI discover

**[13:32]** things through that comprehension check

**[13:34]** that we pass back to the evals for

**[13:36]** better code? 100%. This is a flywheel.

**[13:39]** Ask questions that a good senior

**[13:41]** engineer is going to ask. A good senior

**[13:43]** engineer is going to ask you, why did

**[13:45]** you call that dependency here? Why did

**[13:47]** you structure the code so that it caches

**[13:49]** in a location unreadable by other

**[13:51]** services? How are you thinking about

**[13:53]** separation of concerns? If you're making

**[13:55]** this monolithic, you want to think

**[13:57]** through the kinds of questions your

**[14:00]** leading engineers ask and use them to

**[14:03]** create a comprehension filter that acts

**[14:06]** as a way of making the code legible. And

**[14:10]** again, it does two things. One, it helps

**[14:12]** to make the code readable and therefore

**[14:13]** accountable by people in the

**[14:15]** organization. And two, it becomes

**[14:17]** something that feeds your flywheel and

**[14:19]** makes your emails better and improves

**[14:21]** the quality of your code over time. Can

**[14:23]** you imagine improving speed and quality

**[14:24]** of code at the same time? It's the

**[14:26]** dream. We can do it. We just have to set

**[14:28]** ourselves up so we don't have dark code.

**[14:29]** If you've got this far, I hope you

**[14:31]** realize this is not a security team's

**[14:33]** problem. This is not an observability

**[14:34]** problem. This is not an agent pipeline

**[14:36]** problem. This is an all of us problem.

**[14:39]** This is a problem for everybody who's

**[14:40]** building in the software space. And if

**[14:42]** you think you're not, when was the last

**[14:44]** time you vibe coded? If you are leading

**[14:46]** an engineering org right now, the

**[14:47]** question you should ask yourself is not

**[14:49]** how's our observability, how's our

**[14:51]** agentic pipelines. Those are table

**[14:52]** stakes questions. The question you need

**[14:54]** to ask yourself is, do I have mechanisms

**[14:56]** that enable me to make the dark code

**[14:58]** that I'm producing legible so that I

**[15:00]** know where I'm driving? Because

**[15:01]** otherwise, you really are driving with a

**[15:03]** headlights off and you are liable to run

**[15:04]** into the ditch and generate problems

**[15:06]** that you are not aware you're causing

**[15:07]** from a risk perspective. And that should

**[15:09]** make you stay up at night. If you're a

**[15:11]** founder, this is both a competitive mode

**[15:13]** and also a risk. If you're like most

**[15:15]** founders, and I'll be honest, I've seen

**[15:16]** a lot of them, they vibe code so fast

**[15:18]** and get to market so fast, and they

**[15:20]** listen to only the speed part of YC

**[15:22]** teachings, they try and sell you on

**[15:24]** something that is really a thesis and a

**[15:25]** trench code. And maybe the code isn't

**[15:27]** there, and maybe it's not high quality,

**[15:28]** and maybe it's not what you need to

**[15:29]** depend on. Honestly, that's a liability

**[15:32]** for the founder. That's a liability for

**[15:34]** the company. You can stand out so easily

**[15:37]** as a founder if you just know the code

**[15:39]** in this day and age. Just get to know

**[15:41]** it. Make sure you don't have dark code.

**[15:42]** Make it legible. explain your

**[15:44]** trade-offs, be transparent, you're going

**[15:46]** to stand out, and like be so easy to do

**[15:48]** business with and build so much trust.

**[15:50]** And by the way, if you're a vendor, ask

**[15:52]** for that, right? Ask for transparent

**[15:54]** code. Ask about dark code. Ask how much

**[15:57]** if they're shipping a lot, they

**[15:59]** understand what they're shipping. That

**[16:00]** is a question vendors should be asking.

**[16:03]** And if you're just getting started in

**[16:04]** this field, if you are just getting out

**[16:06]** of college, if you are just getting into

**[16:09]** vibe coding and then kind of leaning

**[16:10]** into the technical track, take this as

**[16:12]** an opportunity. This whole idea of a

**[16:14]** comprehension gate, you can set up and

**[16:16]** I've given one and set one up for you.

**[16:19]** You can set up a skill that allows you

**[16:22]** to look at a piece of code and start to

**[16:23]** understand those questions that senior

**[16:25]** engineers ask, the principal engineers

**[16:27]** ask. And that accelerates your

**[16:29]** comprehension. That makes the code less

**[16:31]** dark. And then one last note, if you are

**[16:35]** a senior engineer, if you're a principal

**[16:37]** and you're used to reviewing by hand, I

**[16:39]** know this is a massive adjustment. I

**[16:40]** know trusting AI to give you a

**[16:42]** comprehension gate is a big step. You

**[16:45]** absolutely should feel comfortable

**[16:47]** adjusting and embroidering the prompts

**[16:48]** and the skills, the stuff I've packaged

**[16:50]** together with this video so that it

**[16:52]** feels good to you. It's a tool that

**[16:54]** needs to feel good in your hand. But I

**[16:56]** don't think you can avoid using AI to

**[16:59]** help you understand code because the

**[17:01]** expectation for volume is not going

**[17:03]** away. And so you need to figure out how

**[17:05]** you can remain accountable for the code

**[17:07]** while putting your eyes across more

**[17:09]** stuff. And I think that you need

**[17:11]** essentially lenses on the code that help

**[17:13]** you to see more farther clearer so that

**[17:16]** the code is not dark to you because the

**[17:18]** alternative is just looking at those

**[17:20]** emailed PR reviews and autofixes from

**[17:23]** Codeex or Claude Code and saying, "Ah,

**[17:25]** it's probably fine." You don't want to

**[17:27]** be that person. That's too risky. Look,

**[17:31]** nobody's gonna slow down. shipping

**[17:33]** before you fully understand what you've

**[17:35]** built is a problem we can fix, but it's

**[17:37]** not a problem we can fix

**[17:38]** organizationally by just choosing to go

**[17:41]** back to the way things work. This is a

**[17:42]** river we've crossed. AI is helping us

**[17:44]** speed up. No one wants to slow down. No

**[17:47]** one should slow down. And I'm not

**[17:48]** arguing that that is a good idea. I

**[17:50]** think we need to speed up. I think on

**[17:52]** average, most orgs still go way too

**[17:54]** slow. But we have to be honest that

**[17:58]** going fast imposes new kinds of

**[18:02]** requirements for understanding the code

**[18:04]** that we are shipping at speed and that

**[18:06]** is a different class of problem than the

**[18:09]** old way of understanding code because

**[18:10]** the old way of understanding code was

**[18:11]** human mediated right and one of the

**[18:13]** larger thesis I've been exploring in

**[18:15]** 2026 through this video series has

**[18:16]** really been saying a lot of our human

**[18:18]** mediated touch points are breaking under

**[18:20]** the speed that AI is imposing on the

**[18:22]** business. How do we start to think

**[18:25]** differently about those mechanisms? And

**[18:27]** dark code takes that kind of thinking

**[18:29]** because otherwise it is going to balloon

**[18:31]** and become an absolute security

**[18:32]** nightmare. Don't tolerate dark code. It

**[18:35]** is an organizational choice and you can

**[18:37]** fight it. Choose to do so.
