# Transcript: -iSLQe_imrE

**URL:** https://www.youtube.com/watch?v=-iSLQe_imrE
**Segments:** 249

---

## Full Text

Markdown is dying and the people killing it built Claude code. Derrick works on Claude code at Anthropic. Last week he dropped a thesis that broke the dev internet. 750,000 views, 2.7 thousand likes, 340 reposts and the replies are split. But again and again you see the same line. Wait. You stop too. He claims markdown is the wrong format for every spec, every plan, every PR write-up you hand to your agent. Almost all of it out and he has the receipts. This is the unreasonable effectiveness of HTML. By the end of this video you will know exactly why your code base is about to look very different. And whether that is a good thing. Here is what HTML can carry that markdown cannot. It one, information density. Markdown can carry headings, bold, a bullet list, a table if you squint at it. That is roughly it. HTML can carry eight things in one file. Tables, CSS driven design, SVG illustrations, code snippets inside script tags, live interactions wired with JavaScript and CSS, workflows drawn with SVG and HTML side by side, spatial data, anything you can place on a canvas with absolute positions, and actual images with image tags. Derrick's claim, and I think it holds, there is almost nothing Claude can read that you cannot represent in HTML. So what does the model do when the format fails it? It improvises, ASCII diagrams, or his favorite, estimating colors with Unicode characters. Boxes that pretend to be charts, hashes that pretend to be color swatches. That is the cost of forcing a powerful agent through a format built for a 1990s readme. When you give it HTML, the agent stops faking the chart and just draws the chart. So, compare. Same data, two formats. Markdown gives you this. A bar chart hand-drawn out of pipes and dashes. From a distance, it looks like a chart. Up close, the columns drift. The bars do not line up with the axis. And the second you paste it into a doc with a different font, every alignment breaks. HTML gives you this. Same five numbers. A real SVG bar chart, rendered crisply, picking its own colors from a palette. Sitting inside a single.html you can open in any browser. That is why Direct writes HTML documents are easier to read, easier to organize visually, easier to navigate with tabs and links and illustrations. He says the chance someone actually reads your spec, your report, your PR write-up, that chance gets much, much higher when it is HTML. A Markdown file is a thing your colleague will skim. An HTML file is a thing your colleague will open. That is the difference. And yes, there is a price. The honest one. HTML can take two to four times longer to generate than Markdown. Two to four X. That is real. But here is the piece that changes the math. Opus 4.7 ships with a 1 million token context window. 1 million, which means the extra tokens you spend rendering HTML, they barely register against the budget you already have. The cost is real. The cost is also absorbable. And in exchange, you get a document your team will actually read. Some of the replies under the post pushed back on this. They argued Markdown's lower token spend is itself the value. The honest answer is it depends what you are buying. Over a thousand builders. Daily hangouts, weekly workshops, and a community that actually ships together. Three full courses. The agentic coding course, 18 modules. Master the systems that make AI coding repeatable. The AI agent mastery course, build production agents with N8N and Python. And the second brain bootcamp, eight modules. Build your own personal AI system from scratch. Link in description, 10% off. Back to the video. Here is the part that turns this from a thesis into a workflow. Five places where switching to HTML changes everything. Use case one, specs, planning, and exploration. You ask Claude code to fan out six approaches to a problem in one HTML file. Side by side, each one labeled with the trade-off it is making. You pick. The pick becomes a plan with mockups and code snippets baked in. Use case two, code review. The PR diff rendered with margin annotations. Severity colors, jump links. Derek attaches an HTML code explainer to every PR he makes now. And he is on the team. He says it works better than the default GitHub diff view. Use case three, design and prototypes. Claude design is built on HTML for a reason. HTML is incredibly expressive for design. Even when your end surface is React or Swift or anything else. Claude sketches in HTML then translates. You can ship the prototype with sliders and knobs. Tune the animation, then copy the parameters back into a prompt. Use case four, reports, research, and learning. You point Claude code at your code base, your get history, your Slack, the internet. You get back a single readable explainer page. A diagram of flow, three or four key code snippets annotated, a gotcha section at the bottom. Use case five, custom editing interfaces. This one is the sleeper. Sometimes typing in a text box cannot describe what you want. So, Claude Code builds you a throwaway editor. A single HTML file purpose-built for your one piece of data. Drag 30 linear tickets into now, next, later, cut. Edit a feature dependency warnings. Tune a system prompt with live re-render of three sample inputs. And every one of them ends with one button. Copy it back out. As markdown, as a diff, as a prompt for the next session. So, why Claude Code specifically? Why not Claude AI or Claude Design? Because of what Claude Code can ingest, your file system. Every dot HTML file you have already generated, all visible at once. Your MCP surface, Slack, Linear, anything you have connected, your browser when you have Claude in Chrome. Your Git history, the why behind every line of code. That stack of context is what makes the HTML output actually informed. The agent is not synthesizing in the dark. It is synthesizing from your real work. Move the same prompt to a chat surface and you lose half of it. The artifact comes back generic. Pretty maybe, but generic. This is the part that does not transfer. Claude Code's reach into your environment is the input that makes the output worth having. Here is the part the article actually ends on. Derek says the real reason he switched is not density. It is not sharing. It is not even the joy of making things. It is that he stopped reading the markdown plans. He would offload work to Claude, get back a wall of text, and he just would not read it. Which meant he was leaving Claude to make every choice. Which is a slow way to lose the plot. The HTML versions, he reads them. He clicks around. He suggests changes. He is back in the loop. So, I will let Derek close it himself. I'm happy to say I feel more in the loop than ever before when using HTML. I hope you do, too. The replies under the post are full of people saying the same thing. I was already doing this. I just did not have the framing yet. This finally explains why Claude keeps printing HTML as artifacts. I'm moving my whole planning workflow today. You are going to see this format show up everywhere over the next few months. Specs, PR write-ups, status reports, internal explainers. Even editorial magazines, and judging by the replies, plenty of other places, too. Get ahead of it. Open one of the files in Derek's gallery. Look at how it reads compared to the markdown you would normally get. And if you want to learn more about AI, check out the dynamis.ai community.

---

## Timestamped Segments

**[0:00]** Markdown is dying and the people killing

**[0:02]** it built Claude code.

**[0:04]** Derrick works on Claude code at

**[0:06]** Anthropic.

**[0:07]** Last week he dropped a thesis that broke

**[0:09]** the dev internet.

**[0:11]** 750,000

**[0:12]** views, 2.7 thousand likes,

**[0:16]** 340 reposts and the replies are split.

**[0:19]** But again and again you see the same

**[0:21]** line.

**[0:22]** Wait. You stop too.

**[0:25]** He claims markdown is the wrong format

**[0:27]** for every spec, every plan, every PR

**[0:30]** write-up you hand to your agent.

**[0:32]** Almost all of it out and he has the

**[0:35]** receipts.

**[0:36]** This is the unreasonable effectiveness

**[0:38]** of HTML.

**[0:40]** By the end of this video you will know

**[0:42]** exactly why your code base is about to

**[0:45]** look very different.

**[0:47]** And whether that is a good thing. Here

**[0:48]** is what HTML can carry that markdown

**[0:50]** cannot.

**[0:52]** It one, information density. Markdown

**[0:54]** can carry headings,

**[0:56]** bold, a bullet list, a table if you

**[0:58]** squint at it.

**[1:00]** That is roughly it. HTML can carry eight

**[1:03]** things in one file.

**[1:05]** Tables, CSS driven design, SVG

**[1:08]** illustrations,

**[1:09]** code snippets inside script tags, live

**[1:12]** interactions wired with JavaScript and

**[1:14]** CSS,

**[1:16]** workflows drawn with SVG and HTML side

**[1:18]** by side,

**[1:20]** spatial data, anything you can place on

**[1:22]** a canvas with absolute positions,

**[1:25]** and actual images with image tags.

**[1:27]** Derrick's claim, and I think it holds,

**[1:30]** there is almost nothing Claude can read

**[1:32]** that you cannot represent in HTML.

**[1:36]** So what does the model do when the

**[1:37]** format fails it?

**[1:39]** It improvises, ASCII diagrams, or his

**[1:42]** favorite, estimating colors with Unicode

**[1:44]** characters.

**[1:46]** Boxes that pretend to be charts, hashes

**[1:48]** that pretend to be color swatches.

**[1:51]** That is the cost of forcing a powerful

**[1:53]** agent through a format built for a 1990s

**[1:55]** readme.

**[1:57]** When you give it HTML, the agent stops

**[1:59]** faking the chart and just draws the

**[2:01]** chart.

**[2:02]** So, compare. Same data, two formats.

**[2:04]** Markdown gives you this.

**[2:07]** A bar chart hand-drawn out of pipes and

**[2:09]** dashes.

**[2:10]** From a distance, it looks like a chart.

**[2:13]** Up close, the columns drift.

**[2:15]** The bars do not line up with the axis.

**[2:17]** And the second you paste it into a doc

**[2:19]** with a different font, every alignment

**[2:21]** breaks.

**[2:23]** HTML gives you this. Same five numbers.

**[2:26]** A real SVG bar chart, rendered crisply,

**[2:29]** picking its own colors from a palette.

**[2:32]** Sitting inside a single.html

**[2:35]** you can open in any browser.

**[2:37]** That is why Direct writes

**[2:40]** HTML documents are easier to read,

**[2:42]** easier to organize visually, easier to

**[2:44]** navigate with tabs and links and

**[2:46]** illustrations.

**[2:48]** He says the chance someone actually

**[2:50]** reads your spec, your report, your PR

**[2:53]** write-up, that chance gets much, much

**[2:55]** higher when it is HTML.

**[2:58]** A Markdown file is a thing your

**[3:00]** colleague will skim.

**[3:02]** An HTML file is a thing your colleague

**[3:04]** will open.

**[3:06]** That is the difference. And yes, there

**[3:08]** is a price.

**[3:10]** The honest one. HTML can take two to

**[3:12]** four times longer to generate than

**[3:14]** Markdown.

**[3:15]** Two to four X. That is real.

**[3:18]** But here is the piece that changes the

**[3:20]** math.

**[3:21]** Opus 4.7 ships with a 1 million token

**[3:23]** context window.

**[3:25]** 1 million, which means the extra tokens

**[3:27]** you spend rendering HTML,

**[3:30]** they barely register against the budget

**[3:32]** you already have.

**[3:33]** The cost is real. The cost is also

**[3:35]** absorbable.

**[3:37]** And in exchange, you get a document your

**[3:39]** team will actually read.

**[3:41]** Some of the replies under the post

**[3:43]** pushed back on this.

**[3:45]** They argued Markdown's lower token spend

**[3:46]** is itself the value.

**[3:49]** The honest answer is it depends what you

**[3:51]** are buying. Over a thousand builders.

**[3:54]** Daily hangouts, weekly workshops, and a

**[3:56]** community that actually ships together.

**[3:59]** Three full courses.

**[4:01]** The agentic coding course, 18 modules.

**[4:04]** Master the systems that make AI coding

**[4:06]** repeatable.

**[4:08]** The AI agent mastery course, build

**[4:10]** production agents with N8N and Python.

**[4:13]** And the second brain bootcamp, eight

**[4:15]** modules.

**[4:16]** Build your own personal AI system from

**[4:18]** scratch. Link in description, 10% off.

**[4:22]** Back to the video.

**[4:24]** Here is the part that turns this from a

**[4:26]** thesis into a workflow.

**[4:28]** Five places where switching to HTML

**[4:31]** changes everything.

**[4:33]** Use case one, specs, planning, and

**[4:35]** exploration.

**[4:36]** You ask Claude code to fan out six

**[4:38]** approaches to a problem in one HTML

**[4:41]** file.

**[4:42]** Side by side, each one labeled with the

**[4:44]** trade-off it is making.

**[4:47]** You pick.

**[4:48]** The pick becomes a plan with mockups and

**[4:50]** code snippets baked in.

**[4:52]** Use case two, code review. The PR diff

**[4:55]** rendered with margin annotations.

**[4:57]** Severity colors, jump links. Derek

**[5:00]** attaches an HTML code explainer to every

**[5:03]** PR he makes now.

**[5:05]** And he is on the team.

**[5:07]** He says it works better than the default

**[5:09]** GitHub diff view.

**[5:10]** Use case three, design and prototypes.

**[5:13]** Claude design is built on HTML for a

**[5:15]** reason.

**[5:16]** HTML is incredibly expressive for

**[5:19]** design. Even when your end surface is

**[5:21]** React or Swift or anything else.

**[5:24]** Claude sketches in HTML then translates.

**[5:28]** You can ship the prototype with sliders

**[5:30]** and knobs. Tune the animation, then copy

**[5:32]** the parameters back into a prompt.

**[5:35]** Use case four, reports, research, and

**[5:37]** learning.

**[5:38]** You point Claude code at your code base,

**[5:40]** your get history, your Slack, the

**[5:42]** internet.

**[5:44]** You get back a single readable explainer

**[5:45]** page.

**[5:47]** A diagram of flow, three or four key

**[5:49]** code snippets annotated, a gotcha

**[5:51]** section at the bottom.

**[5:53]** Use case five, custom editing

**[5:55]** interfaces.

**[5:57]** This one is the sleeper. Sometimes

**[5:59]** typing in a text box cannot describe

**[6:01]** what you want.

**[6:02]** So, Claude Code builds you a throwaway

**[6:04]** editor.

**[6:05]** A single HTML file purpose-built for

**[6:08]** your one piece of data.

**[6:10]** Drag 30 linear tickets into now, next,

**[6:12]** later, cut.

**[6:14]** Edit a feature

**[6:16]** dependency warnings.

**[6:18]** Tune a system prompt with live re-render

**[6:20]** of three sample inputs.

**[6:22]** And every one of them ends with one

**[6:24]** button. Copy it back out.

**[6:27]** As markdown, as a diff, as a prompt for

**[6:29]** the next session.

**[6:31]** So, why Claude Code specifically? Why

**[6:33]** not Claude AI or Claude Design?

**[6:36]** Because of what Claude Code can ingest,

**[6:38]** your file system.

**[6:40]** Every dot HTML file you have already

**[6:43]** generated, all visible at once.

**[6:46]** Your MCP surface, Slack, Linear,

**[6:48]** anything you have connected, your

**[6:50]** browser when you have Claude in Chrome.

**[6:53]** Your Git history, the why behind every

**[6:55]** line of code.

**[6:57]** That stack of context is what makes the

**[6:59]** HTML output actually informed. The agent

**[7:02]** is not synthesizing in the dark.

**[7:05]** It is synthesizing from your real work.

**[7:08]** Move the same prompt to a chat surface

**[7:10]** and you lose half of it.

**[7:12]** The artifact comes back generic. Pretty

**[7:14]** maybe,

**[7:15]** but generic.

**[7:17]** This is the part that does not transfer.

**[7:20]** Claude Code's reach into your

**[7:21]** environment is the input that makes the

**[7:23]** output worth having.

**[7:25]** Here is the part the article actually

**[7:27]** ends on.

**[7:29]** Derek says the real reason he switched

**[7:30]** is not density.

**[7:32]** It is not sharing. It is not even the

**[7:34]** joy of making things.

**[7:36]** It is that he stopped reading the

**[7:38]** markdown plans.

**[7:40]** He would offload work to Claude, get

**[7:41]** back a wall of text, and he just would

**[7:43]** not read it.

**[7:45]** Which meant he was leaving Claude to

**[7:47]** make every choice.

**[7:49]** Which is a slow way to lose the plot.

**[7:51]** The HTML versions, he reads them.

**[7:54]** He clicks around. He suggests changes.

**[7:56]** He is back in the loop.

**[7:58]** So, I will let Derek close it himself.

**[8:01]** I'm happy to say I feel more in the loop

**[8:03]** than ever before when using HTML.

**[8:06]** I hope you do, too. The replies under

**[8:08]** the post are full of people saying the

**[8:10]** same thing.

**[8:12]** I was already doing this. I just did not

**[8:14]** have the framing yet.

**[8:15]** This finally explains why Claude keeps

**[8:17]** printing HTML as artifacts.

**[8:20]** I'm moving my whole planning workflow

**[8:22]** today.

**[8:24]** You are going to see this format show up

**[8:26]** everywhere over the next few months.

**[8:29]** Specs, PR write-ups, status reports,

**[8:31]** internal explainers.

**[8:33]** Even editorial magazines, and judging by

**[8:35]** the replies, plenty of other places,

**[8:37]** too.

**[8:39]** Get ahead of it. Open one of the files

**[8:41]** in Derek's gallery.

**[8:42]** Look at how it reads compared to the

**[8:44]** markdown you would normally get.

**[8:47]** And if you want to learn more about AI,

**[8:49]** check out the dynamis.ai community.
