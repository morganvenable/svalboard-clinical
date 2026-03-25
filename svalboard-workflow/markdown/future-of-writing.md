---
title: The Future of Writing in an AI World
hero_title: The Future of Writing in an AI World
hero_subtitle: Why the way you interact with your tools matters more than ever, and how to think about your own workflow.
hero_buttons: none
---

<div class="section mechanism" markdown="1">

## Writing and Talking Are Different Things

My first attempts at writing by voice were incredibly painful. What I do when I talk just feels ... different? than what I do when I write.

Talking is more of a performance. I do it with an awareness of the audience continuously observing me.

Writing, whether by hand or by typing, looks inward in a different way.

I've experimented with speech input quite a bit over the years. Indeed speech is now my default mode of text entry when using mobile devices, because phone grip and touchscreens absolutely destroy my hands. Over the years I've become marginally more competent at crafting prose with my voice, but it's never quite the same. It's like I have to actively turn something on in my brain, which REALLY doesn't want to be on when I'm talking, and which actively interferes with thought synthesis.

It turns out there is a substantive body of research on this exact topic. When you speak, you commit to your words in real time, with an audience, and you move on. When you write, the words sit there on the screen and you can argue with them. You read back a sentence and realize it's not what you meant, and the effort of fixing it changes what you think. Bereiter and Scardamalia (1987) called this **knowledge transformation**, and the research since then has consistently found that it's real: the act of writing generates understanding that wasn't there before you started (Emig, 1977; Galbraith, 1999).

The brain uses different pathways to compose speech and written prose.

</div>

---

<div class="section clinical" markdown="1">

## The Physical Part Matters

When you've typed long enough that you're no longer conscious of the keystrokes, your fingers and your thinking stop competing for the same mental resources.

Logan and Crump (2011) showed that expert typists literally can't tell you which fingers they use for which keys. The motor execution has dropped completely out of awareness, leaving everything available for the actual composing. Chenoweth and Hayes (2001) found that faster typists produce longer uninterrupted bursts of composition, which is the measurable version of what most writers would just call being in flow.

I have personal experience with this. If you ask me which finger I move in which direction in order to strike a specific key on the keyboard, I can't tell you. I have to literally mock up the movement in my head in order to find the mapping. I feel the muscles in my hands awaken satisfyingly with the sensation of that spatial-symbolic memory.

This is why RSI is so devastating to people who think through their fingers. It's not just that your hands hurt and you type slower. Pain grabs your attention (Eccleston & Crombez, 1999), and when attention is going to your hands it's not going to your thinking. The automaticity breaks, and with it the cognitive benefit of typing. One in five computer users develops hand or arm symptoms in a given year (Marcus et al., 2002), and once it starts, people report not just physical problems but difficulty concentrating, loss of creative momentum, and anxiety about whether the pain will come back (Moore et al., 2019).

I lived with this for over a decade before I found DataHand. Afterward, my typing pain went away completely. That experience is what eventually led me to build Svalboard, and it's why I think about the relationship between physical input and cognitive work as much as I do.

</div>

---

<div class="section problem" markdown="1">

## AI Complicates the Picture

How does AI fit into this?

It depends on who you ask and what they expect of the world over the next ten years. As somebody who is using these tools continuously on a day-to-day basis, I'm still of the opinion that human judgment and taste are relevant to productivity and will continue to matter. At the same time there really are big shifts happening in how much the generation of text depends on humans and their bodies, particularly in more technical domains. There's no question that software engineering is being remade before our eyes here in 2026, nor will many other disciplines remain untouched.

AI is genuinely, dramatically useful for producing text. I used it extensively in assembling the research behind this page. The solo developer who supports Svalboard with open source firmware is using agentic AI to do work that would have required a whole department a few years ago. These are BIG productivity gains.

But there's something worth paying attention to in the tradeoff. When AI writes for you, you get the output without going through the process that would have changed your understanding: you get a real artifact, but you haven't undergone the thinking that writing it yourself would have produced. If you engage deeply with LLMs, you can even get some of this benefit in thinking through problems if they have access to sufficient domain expertise and the frame is right.

Sometimes that's fine, sometimes the output is all you need. Other times, particularly when you're trying to learn something deeply or work through a genuinely hard problem, the process is the whole point.

There's some evidence this matters at scale. Dell'Acqua et al. (2023) ran a study with BCG consultants and found that AI assistance improved their performance by 40% on tasks the AI was good at, but on tasks outside the AI's strengths, performance dropped 19%. The consultants had started leaning on the AI for the thinking. Kellogg (2008) estimates that the capacity for knowledge-transforming writing takes a decade of deliberate practice to develop. You can't let it go and expect to get it back easily.

None of this is an argument against using AI. I use it constantly. It's more of an observation that the choice of when to write yourself and when to let AI write for you is a choice about what kind of thinking you're doing, and it's worth making that choice deliberately.

Humans have very sophisticated pathways between thought and motor control, and exploiting those pathways with well-designed input mechanisms is an essential part of building experiences that will keep our most valuable intellectual functions, taste and judgment, at the center of our work.

</div>

---

<div class="section mechanism" markdown="1">

## Productivity Means Increased Stakes

I don't know anybody who is working less now that they have agentic coding tools. Everyone I know is dramatically more productive and overwhelmed by how much they can accomplish in a short period of time.

Senior and principal engineers have never been more valuable. The trajectory from school to junior to senior roles has become murkier, but ultimately there will have to be some equilibrium where people still gain experience and still become more productive over the course of their careers.

But when AI multiplies what a single person can accomplish, the person's capacity to sustain focused work becomes the constraint on a much larger output. If a developer gets sidelined by RSI now, they're not losing one person's productivity. They're losing a whole team's worth.

A $1,000 keyboard is already a rounding error in the productivity value of a software engineer to an employer in the developed world. In this new world it might be ten times that if the stakes are "no pain vs too much pain to work".

That makes the physical interface a higher-stakes problem than it used to be. It also makes the whole question of workflow design more interesting. The tools available now are dramatically richer than they were even a couple of years ago: local speech recognition that actually works, gaze tracking that can complement other inputs, AI that can interpret loose intent across modalities. The integration between these things is still rough, but the pieces are coming together quickly.

These combine quite practically for me day to day:

- **Voice** for when I want speed, thinking out loud, or when I want iterative refinement with a patient and responsive partner (even if they're a weird alien with superhuman knowledge, yet huge gaps in taste or common sense)
- **Typing** for when I need the recursive, inward-looking quality of written composition
- **Gaze** for cursor warping/pointing without lifting my hands

Soon, I expect we'll have much more sophisticated systems tying it all together, interpreting what I mean from the combination of what I say, where I look and what I type. We're not there yet, but things are moving FAST.

</div>

---

<div class="section clinical" markdown="1">

## Going Deeper

Each of these areas has more to it than I can cover here. I've written separate pages on the ones I find most interesting:

**[Speech](speech.html)** gets into local recognition tools like Handy, structural voice editing with Cursorless, and what changes when an LLM sits between your voice and the output.

**[Gaze](gaze.html)** covers Tobii hardware, the current state of open-source webcam alternatives, and the possibility that LLM screen context could make approximate gaze tracking genuinely useful without expensive hardware.

**[Motor input](motor-input.html)** is a place where I have a lot to say, for obvious reasons. The DataHand research, how Svalboard builds on it, why fitting a keyboard to a hand at the millimeter level matters, and what happens when the physical interface fails.

**[Memory and attention](memory.html)** addresses something I spent a lot of time thinking about at Google and still find exciting: the problem of capturing insights when you're away from your desk, and the tension between wanting frictionless capture and needing protected focus.

</div>

---

<div class="section provider" markdown="1">

## The Question

AI is changing how all of this works, fast. The human role in knowledge work is shifting toward direction and judgment and the kind of understanding that comes from composing your own thoughts. The tools for doing that are better and more varied than they've ever been.

Svalboard exists because typing is how a lot of people, myself included, think best, and because most keyboards can eventually cause pain that breaks us. If that resonates with you, the [clinical pages](../index.html) go into the evidence in detail, and the [discord community](https://discord.gg/svalboard) can give you plenty of anecdotal support, along with specific answers to your questions.

But the question underneath all of this is bigger than any particular product:

**How do you want to work, and what does your body need to keep doing it for the next thirty-plus years?**

</div>
