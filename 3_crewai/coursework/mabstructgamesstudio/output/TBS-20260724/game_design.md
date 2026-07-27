# The Big Swallow — *Sound Eater*
### Game Design Document

---

## Game Title

**The Big Swallow — *Sound Eater***

---

## Short Idea

You pilot a hungry cosmic Mouth adrift in a near-black void, and you can only swallow what you can *see* — but you can only see what makes *noise*. Every sound source blooms into an expanding ripple of light, and every meal you swallow silences that source forever, growing your mass while stealing your sight. It's a synesthetic stealth-eat game where the more you consume, the blinder you become.

---

## Core Idea

You are a Mouth drifting through a dark cosmic sea. The screen is near-black; the only way to perceive the world is through **sound**. Every object pulses, emitting expanding ripples that briefly illuminate the geometry around them — and **you can only swallow what is currently lit** by an active ripple.

Every swallow silences its source *permanently*: you gain mass, but that light is gone forever and your world grows darker. This weaponizes the central tension of the game — **eating and seeing are directly opposed resources.** Mastery is the greedy art of feasting while keeping just enough of the lights on to survive.

The signature refinement is the **Heartbeat Pulse**: your Mouth involuntarily emits a faint, slow ripple of its own, dimly revealing your immediate surroundings for free. As you grow, your heartbeat becomes *brighter but slower* — bigger reveals separated by longer blind gaps — so difficulty escalates organically from the growth mechanic itself.

---

## Game Mechanics & Features

### Core Loop
1. **You are a Mouth** drifting in a dark cosmic void.
2. **Sound sources pulse**, emitting expanding ripples that briefly light up the space around them.
3. **You can only swallow what is currently illuminated** — no blind fishing. Eating is tied directly to the light economy.
4. **Swallowing a source silences it forever** — you gain mass, but that light vanishes and the world dims.
5. **Goal:** reach the mass quota for the level before you go fully blind or before "the Hush" closes in.

### The Light Economy — Three Source Types
This triangle is the strategic heart of the game:

- **Prey** *(dim, near-silent)* — small, plentiful food. Eating them barely dims the world. Your bread-and-butter mass.
- **Beacons** *(bright, loud, rhythmic)* — large illuminators offering big mass, but swallowing one plunges a whole region into darkness. High risk / high reward.
- **Chimes** *(moving, evasive)* — dart across the screen trailing bright ripples. They can't be eaten (or grant a bonus if caught) — their true value is as **mobile lamps** that light your path.

Together these create the game's core decision engine: **eat for mass / preserve light / chase moving light.**

### The Heartbeat Pulse
- Your Mouth emits a slow, involuntary ripple that dimly reveals your surroundings for free — eliminating a total "stuck in the dark" fail state.
- As mass grows, the heartbeat gets **brighter but slower** — an automatic, escalating difficulty curve baked into the growth mechanic.

### Difficulty Curve (single 4–8 minute run)
- **0:00–1:00 — Onboarding (bright):** World mostly lit. Teach "eat what's lit; eating silences." Beacons plentiful, no fail pressure. Player feels powerful.
- **1:00–3:00 — The Squeeze:** Prey thins out; quota rises. Player must start eating Beacons and living with the dark. Chimes introduced as relief.
- **3:00–6:00 — Blind Mastery:** World mostly dark. Play becomes routing between Chimes and timing heartbeat pulses. Peak skill expression.
- **6:00–8:00 — The Hush:** A slow wall of total silence encroaches from the screen edges, forcing a final greedy sprint — a natural climax that caps session length.

### Scoring & Meta
- **Score = accumulated mass + a "Kept the Lights On" bonus** measuring how much of the map remains illuminated at the end. This *rewards restraint*, separating strategists from button-mashers.
- **Echo Chain combo:** swallow multiple sources within a single ripple's lifetime for a score multiplier — rewards reading the ambient rhythm of the soundscape.

### Controls
- **One verb.** Move the Mouth (mouse/touch drag or point-to-move). Swallowing is automatic on contact-while-lit. Frictionless, fully mobile-friendly.

### Audio-Optional by Design
- The game is **fully playable with sound off.** Ripples are Canvas-driven and gameplay-complete without audio; Web Audio is a sensory *enhancement layer*, not a dependency. Sound sources emit visible ripples whether or not you can hear them — the visuals are truth, the audio is flavor.

---

## Game Art & Design

### Visual Aesthetic
- **Radar-poetry on black.** A near-black cosmic void pierced by luminous, expanding ripples of sound. Surreal, synesthetic, unmistakably the studio's cosmic/sci-fi voice.
- **Ripples** rendered as expanding radial gradients / additive circle strokes composited onto an offscreen "light buffer" over the dark scene — cheap, no per-pixel shaders, smooth on mobile Canvas 2D.
- **Source identity by light signature:** Prey = small, dim, cool-toned pulses; Beacons = large, warm, rhythmic blooms; Chimes = fast, bright, trailing streaks.
- **The Mouth** is a soft, dark silhouette defined mostly by its own faint heartbeat halo — you feel your size more than you see it.
- Subtle **CRT/void shimmer** for texture and a dreamlike, slightly unsettling atmosphere.

### Sound Design
- **The mechanic IS the presentation** — spatialized pings drive perception; every gameplay object is an instrument.
- A **low, sustained drone** for the void; the ambient bed of the cosmos.
- **Beacons** pulse on rhythm, forming an emergent, generative soundtrack unique to each playthrough.
- **The swallow:** a wet, satisfying click that abruptly cuts a sound off mid-note — simultaneously gratifying and unsettling, reinforcing the theme of consumption-as-silencing.
- As "the Hush" advances, the soundscape thins toward oppressive silence.

### Shareability Artifact — The "Silence Map"
- At run's end, the game freezes into a **Silence Map**: dark craters where you devoured sources, glowing points where you spared them — a **procedurally personal constellation** unique to every run. This is the screenshot/share hook, and because it's generated from the player's choices, it can never be duplicated.
- The **dark-screen-blooming-with-sound reveal** is video-native and clip-worthy — the "wait, you can *only* see what you *hear*?" moment is a perfect 10-second share.

---

## Why This Is *The Big Swallow*

*Sound Eater* is the concept only this studio would make: a genuinely irreducible mechanic where eating, seeing, theme, and aesthetic are the same idea. It delivers the highest fun-per-minute of the concept set through constant meaningful micro-decisions, ships as a tiny, instant-load, single-file HTML5 Canvas build, and markets itself through both its viral reveal and its one-of-a-kind Silence Map. It is surreal, cosmic, inventive, and defensibly novel — the boldest and most *Mabstruct* swing on the table.