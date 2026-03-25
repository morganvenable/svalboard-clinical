---
title: Speech Input
hero_title: Speech
hero_subtitle: Voice is not a replacement for typing. It is a complementary channel optimized for different cognitive modes.
hero_buttons: none
---

<div class="section mechanism" markdown="1">

## The State of Voice Input

Voice input has come a long way from rigid command grammars. Modern local speech recognition, combined with LLM understanding of context, is making voice a genuinely powerful input modality for knowledge work.

The fundamental advantage of speech is speed: humans speak at 150+ words per minute versus 40-80 WPM for most typists. The fundamental limitation is precision: editing, formatting, and navigating spatial layouts by voice remains slower and more error-prone than by keyboard (Karat et al., 1999; Shneiderman, 2000). The interesting question is how to combine both modalities so each handles what it does best.

Speech excels at ideation, high-level direction, rapid rough-drafting, and conversational exploration of ideas. Typing excels at precise editing, structured composition, and the physical-cognitive feedback loop that many people experience as essential to deep thinking. The emerging pattern is not voice *or* keyboard but voice *and* keyboard, with AI as the bridge.

</div>

---

<div class="section clinical" markdown="1">

## Handy: Local Speech Recognition Done Right {#handy}

[Handy](https://github.com/cjpais/Handy) is a free, open-source speech-to-text application that runs entirely offline. Built with Tauri (Rust + React/TypeScript), it performs all recognition locally without sending audio to cloud servers.

### Model Switching

Handy supports multiple recognition backends, including OpenAI's Whisper models (GPU-accelerated) and Parakeet V3 (efficient CPU-only with automatic language detection). Users can seamlessly switch between models to find what works best for their voice, accent, and use case.

This matters because no single speech model is best for everyone. Accents, speaking styles, microphone quality, and domain vocabulary all affect recognition accuracy. The ability to try different models and compare results without changing tools or workflows is a significant practical advantage.

### Vocabulary Customization

The ability to tune recognition for domain-specific terminology matters enormously for technical users. Medical, legal, and engineering vocabularies are poorly served by generic models. A cardiologist dictating notes needs "atrioventricular" recognized on the first try. A firmware developer needs "QMK" and "TMAG3001" handled correctly. Vocabulary customization turns speech from a frustrating approximation into a reliable input channel.

### Press-to-Record Workflow

A configurable keyboard shortcut starts recording; releasing transcribes and pastes into whatever text field is active. This tight integration with typing workflows means voice and keyboard complement each other rather than competing. You type when you want precision. You speak when you want speed. The transition between them is a single keypress.

For Svalboard users specifically, this means voice input can be triggered without removing fingers from the wells, keeping the multimodal workflow completely fluid.

### Privacy

All processing stays on your machine. For professionals working with confidential content (legal, medical, financial), this is not a preference. It is a requirement. Cloud-based speech services require sending audio to external servers, which may be prohibited by HIPAA, attorney-client privilege, or corporate security policies.

</div>

---

<div class="section mechanism" markdown="1">

## Voice and LLMs: Beyond Transcription {#voice-and-llms}

Raw transcription is the starting point, not the destination. When a local speech model feeds into an LLM that understands your project context, the voice channel becomes dramatically more powerful.

### Speaking Intent, Not Dictation

Traditional dictation requires you to speak exactly the words you want written. LLM-mediated voice input lets you speak *intent*: describe what you want, explain the goal, talk through the problem loosely. The AI interprets your meaning, resolves ambiguities, and produces structured output. You can say "add error handling to the sensor read function for I2C timeouts" instead of dictating code character by character.

This is the workflow that produced much of the content on this site: voice direction to an AI assistant that understands the project deeply enough to act on imprecise instructions.

### Vibe Coding with Voice

The "vibe coding" pattern (coined by Andrej Karpathy, 2025) describes using natural-language voice input with AI code editors like Cursor and Windsurf. Users speak naturally to describe desired functionality; the LLM generates code. When the LLM understands your intent, voice input shifts the bottleneck from mechanical production to conceptual thinking.

Tools like Wispr Flow facilitate this by providing low-latency speech-to-text that integrates directly with AI editors. The voice-to-intent-to-code pipeline is still rough, but the trajectory is clear.

### The Voice + Keyboard + AI Triangle

The most productive workflows emerging in 2025-2026 use all three:

- **Voice** to express intent quickly and explore ideas
- **AI** to interpret intent and generate structured output
- **Keyboard** to review, edit, refine, and do the precise knowledge-transforming work of composition

Each channel handles what it does best. None replaces the others.

</div>

---

<div class="section problem" markdown="1">

## Talon Voice: Full Computer Control

[Talon Voice](https://talonvoice.com/), created by Ryan Hileman after developing severe hand pain in 2017, provides comprehensive computer control by voice, scriptable in Python. It is the foundation that several other voice-control tools build on.

### How It Works

Talon consists of several integrated subsystems:

- **Speech recognition**: Ships with a free Conformer-based engine (low latency). Also supports Dragon NaturallySpeaking via NatLink integration.
- **Noise recognition**: Detects non-speech sounds (pop, hiss) with very low latency. Pop typically triggers a click; hiss triggers click-and-drag. This bypasses the speech recognition pipeline entirely, enabling near-instant interaction.
- **Eye tracking**: Integrates with Tobii eye trackers using a lightweight custom driver. Gaze positions the cursor roughly; head tracking refines it.
- **Scripting**: `.talon` files define voice commands with intuitive syntax. Complex logic uses Python. The community-maintained `talonhub/community` repository provides a standard command grammar covering most desktop operations.

### Who Uses Talon

Primarily developers and power users with RSI or physical impairments, but increasingly anyone interested in voice-driven workflows. The Talon Slack community is active, with Hileman himself participating regularly. Pricing: free public version; beta access at $25/month for latest features.

</div>

---

<div class="section clinical" markdown="1">

## Cursorless: Structural Voice Editing

[Cursorless](https://www.cursorless.org/), created by Pokey Rule (also after developing RSI), is a spoken language for structural code editing in VS Code, built on top of Talon Voice.

### The Hat System

Cursorless places small colored and shaped decorations ("hats") above every token on screen. Users speak commands that reference these hats to identify targets, then apply actions. The language is built on four abstractions:

- **Marks**: Which token (identified by hat color/shape + letter)
- **Actions**: What to do (move, delete, copy, wrap, etc.)
- **Modifiers**: Expand or refine the selection (containing function, matching pair, etc.)
- **Scopes**: Structural units (argument, statement, function body, class)

Commands chain together. A single utterance like "move argument air to after drum" replaces what would be multiple keyboard operations: select the argument, cut, navigate to the target, paste.

### Why It Matters

Cursorless operates at the abstract syntax tree level, not the character level. This means voice commands express *structural intent* rather than cursor movements. You say "delete the if statement containing blue cap" rather than "select from line 47 to line 53, then delete." This is a fundamentally different relationship between voice and code than traditional dictation.

Roughly 7,000 VS Code installs, 5.0 rating, actively maintained as of 2026. The learning curve is steep but structured, with community-maintained tutorials and cheatsheets. Experienced users report meeting or exceeding keyboard editing speeds.

</div>

---

<div class="section provider" markdown="1">

## Choosing a Voice Workflow

There is no single right answer. The tools serve different needs and can be combined:

| Need | Tool | Notes |
|------|------|-------|
| Quick dictation into any app | Handy | Local, private, model-switchable |
| Voice-directed AI coding | Wispr Flow + Cursor/Windsurf | LLM interprets intent |
| Full hands-free computer control | Talon Voice | Steep learning curve, maximum capability |
| Structural code editing by voice | Cursorless (on Talon) | AST-level, not character-level |
| Voice as complement to typing | Handy + Svalboard | Press-to-record from the keyboard |

The key question is not "voice or keyboard?" but "what balance serves your body and your thinking over the long term?"

</div>
