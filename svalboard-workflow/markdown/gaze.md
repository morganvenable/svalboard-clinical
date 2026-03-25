---
title: Gaze Tracking
hero_title: Gaze
hero_subtitle: Hardware trackers, webcam alternatives, and what happens when you add AI to approximate gaze.
hero_buttons: none
---

<div class="section mechanism" markdown="1">

## Gaze as Complement, Not Replacement

Eye tracking is most powerful not as a standalone input method but as a complement that makes every other modality more efficient.

The core idea is simple: your eyes already look at what you want to interact with. If the computer can approximate where you're looking, it can warp the cursor to that region before you even begin a pointing gesture. This eliminates the ballistic phase of mouse movement (the long-distance travel) and leaves only the fine adjustment, which can be handled by a trackpoint, trackball, head movement, or even a brief voice command.

For Svalboard users, this is particularly interesting because fingers never leave their wells. Gaze-to-approximate-position + Trackpoint/trackball fine adjustment could eliminate even the small pointing movements currently needed, creating a nearly motionless pointing workflow.

</div>

---

<div class="section clinical" markdown="1">

## Tobii Eye Trackers {#tobii}

Tobii's hardware eye trackers (particularly the Tobii Eye Tracker 5 and its successors) provide the gold standard in consumer eye tracking. They use dedicated infrared illuminators and sensors to track gaze with precision significantly better than webcam-based solutions.

### Integration with Talon

Talon Voice integrates directly with Tobii hardware using a lightweight custom driver that replaces Tobii's heavier software stack. The integration provides:

- Gaze-based cursor positioning (warping to approximate gaze location)
- Head tracking for fine cursor adjustment
- Combined gaze + head tracking that achieves usable pointing precision

For users who already use Talon for voice control, adding a Tobii tracker creates a complete hands-free pointing system.

### Limitations

- Dedicated hardware required (~$230 for the Eye Tracker 5)
- Requires mounting on or near the monitor
- Calibration needed per user and session
- Accuracy degrades with glasses, certain lighting conditions, and off-angle head positions
- Not portable between workstations without remounting

</div>

---

<div class="section mechanism" markdown="1">

## Open-Source Webcam Alternatives

The open-source webcam gaze tracking landscape is honest: it is fragmented, less precise than Tobii, and most projects are either research demos or in early stages. But several are worth watching.

### Actively Maintained

**Project Gameface** (Google, open-source, 2023-present) is the strongest entry. It uses MediaPipe's 478 face landmarks and 52 blendshape scores via a standard webcam to provide head-movement cursor control and facial-gesture clicking. Open-source on GitHub (`google/project-gameface`), expanded to Android in 2024. Backed by Google with real accessibility motivation. Technically this is face/head tracking rather than pure gaze estimation, but the MediaPipe foundation could be extended with gaze estimation layers.

**EyeTrax** (MIT license, v0.2.2, April 2025) is a Python library providing webcam-based gaze estimation with 9-point calibration, Kalman and EMA smoothing, and gaze prediction. More of a library than an end-user product, but actively maintained and architecturally sound.

**OptiKey** (open-source, C#/.NET) is a mature on-screen keyboard and mouse emulation system designed for ALS/MND patients. It supports Tobii hardware directly and can also work with webcam-based head tracking. Long-running project with genuine accessibility commitment.

**GazePointer** uses the GazeFlow engine to estimate gaze direction from a standard webcam and control cursor position. Available on SourceForge; the underlying GazeFlow engine is proprietary but the tool is free.

### Honest Assessment

Webcam gaze tracking today does not match Tobii precision. The hardware gap is real: Tobii uses dedicated infrared illumination that webcams lack. But for the "warping" use case (jumping the cursor to the right quadrant of the screen, then refining with another input), webcam accuracy may be sufficient. You don't need pixel-perfect gaze to know the user is looking at the top-right monitor.

</div>

---

<div class="section problem" markdown="1">

## The LLM Opportunity {#the-llm-opportunity}

This is where the picture gets genuinely interesting.

Combine a webcam gaze tracker (imprecise, but gives approximate screen region) with an LLM that has screen context (understanding what's on screen, what the application state is, what the user has been working on), and you may get a large fraction of the way to Tobii-level utility without dedicated hardware.

### How It Would Work

1. Webcam estimates you're looking at roughly the upper-right quadrant of the screen
2. LLM knows there's a code editor open, and the upper-right area contains the function `handle_sensor_timeout()`
3. You say "that function" or even just "there"
4. The system resolves the ambiguity: imprecise gaze + screen context + voice = precise target

GazePointAR (Lee et al., CHI 2024) demonstrated exactly this principle in an AR context: gaze + pointing gestures + conversation history + LLM understanding resolved ambiguous spoken references like "what's over there?" into precise targets.

### SpeakFaster: Proof of Concept

Google Research and Team Gleason published SpeakFaster in *Nature Communications* (2024), showing that LLMs can dramatically amplify reduced-bandwidth input channels. ALS patients using eye-gaze typing entered only word initials, and the LLM expanded to full phrases using conversational context. The result: 57% fewer motor actions and 29-60% faster entry rates.

If LLMs can do this for gaze typing (arguably the lowest-bandwidth input method in use), the potential for LLM-augmented webcam gaze tracking is substantial.

### Timeline

This is not production-ready today. But the trajectory suggests that the combination of cheap webcam input, LLM context understanding, and multimodal fusion could democratize gaze-assisted workflows within a few years. The pieces exist; the integration does not, yet.

</div>

---

<div class="section provider" markdown="1">

## Gaze + Other Modalities

The real value of gaze tracking emerges in combination:

| Combination | What It Enables |
|-------------|----------------|
| Gaze + Trackpoint (Svalboard) | Near-motionless pointing: gaze warps, trackpoint refines |
| Gaze + Voice (Talon) | Hands-free pointing: gaze positions, voice commands act |
| Gaze + LLM context | Disambiguation without precision: "that function" resolves correctly |
| Gaze + Head tracking | Dual-bandwidth pointing: gaze for speed, head for precision |

The goal is not to make gaze tracking work alone. It is to make every other input modality work better by adding approximate spatial context that the eyes provide naturally.

</div>
