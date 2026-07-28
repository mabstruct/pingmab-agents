# The Big Swallow — Game Design Document

## Game Title
**The Big Swallow**

## Short Idea
You are a newborn black hole adrift in a living cosmos, and everything around you is food. Steer your singularity to swallow dust, planets, and entire stars — growing from a pinpoint into a galaxy-eater — until you perform the ultimate act: *The Big Swallow*. A surreal, one-input cosmic power fantasy that runs entirely in the browser.

---

## Core Idea

*You are the black hole.* The player controls a growing singularity whose only verb is **swallow**. Everything in the surreal starfield is potential prey, and the joy of the game is the constantly renegotiated question: *"What is now edible?"*

Using real (softened) gravity, matter is pulled into your event horizon, spirals inward, and is devoured with a physical, greedy *pop*. Each swallow grows your mass, which widens your gravity well, which unlocks the next tier of ever-larger prey. The central tension is that **mass is momentum** — the bigger and hungrier you become, the slower and more ponderous you are to steer, demanding anticipation and orbital finesse. The arc escalates from swallowing cosmic dust to swallowing the galactic core itself, at which point the camera pulls back to reveal you were only ever a speck — the game's surreal, awe-inducing payoff.

The flagship black-hole growth build ships first and serves as the foundation engine (softened gravity, `G=60000`) that later expansions — *Event Horizon*, *Devourer of Time*, *Symbiont*, and *The Last Star* — will fork and reinvent.

---

## Game Mechanics & Features

### Core Gameplay Loop (the 8-second loop)
1. **Steer** your black hole toward smaller objects.
2. **Pull** — matter within your gravity well accelerates, spirals inward, and is captured.
3. **Swallow** — matter crosses the horizon with a satisfying distortion-pinch, flash, and audio pluck; the mass counter ticks up.
4. **Grow** — your horizon radius visibly expands and your gravity reach widens, unlocking bigger prey.
5. **Repeat at higher stakes** — bigger objects, faster hazards, denser fields, rival holes.

> **The one thing to nail:** the *moment of the swallow* — the spiral-in, the visual pinch, the audio pluck, the mass tick, the escalating unit label. Repeated hundreds of times per run, this micro-feedback loop *is* the game.

### Growth Mechanics — Mass as the Single Currency
Everything derives from one number: `mass`.

- `radius = k * cbrt(mass)` — cube-root scaling so early growth feels dramatic and late growth feels slow and majestic.
- `gravityReach = radius * 4.0` — the pull zone widens as you grow (passive harvesting of small debris late-game).
- Softened gravity: `F = G * m / (r² + ε)` with `G = 60000`, softening `ε = radius * 0.5` to prevent singularity blowups.

**The eat rule (the key tuning knob):**
- **Swallow** anything with mass ≤ `yourMass * 0.9`.
- Objects between `0.9x` and `1.5x` your mass are **rivals** — they contest food, exert pull on you, and can swallow you if they outgrow you.
- Objects `> 1.5x` are **hazardous/immovable** (dense stars, neutron cores) until you grow into them.

**Swallow reward:** `mass += eatenMass * 0.85` — the 0.85 "radiation leakage" prevents runaway snowballing and forces continued active play.

**Skill bonus — Spiral / Spaghettification:** objects caught in a fast angular infall grant a small mass multiplier, rewarding players who slingshot and funnel prey rather than gobbling head-on.

### Difficulty Escalation — Five Procedural Tiers
No hard screen loads; the field is procedurally reskinned and new prey/threats are introduced as mass crosses thresholds. The camera zooms out per tier, reframing what was "big" as now small.

| Tier | Fantasy | Prey Introduced | New Threat |
|------|---------|-----------------|------------|
| **1. Dust** | Just born | Cosmic dust, ice, debris | None (safe ~15s onboarding) |
| **2. Rocks** | Micro-hole | Asteroids, fleeing comets | Pulsars (radiation beam — sheds mass); first rival holes |
| **3. Worlds** | Planet-eater | Moons, planets, ring systems | Neutron stars (too dense — tidal recoil + knockback) |
| **4. Stars** | Star-eater | Stars, novae (explode when eaten → AoE shockwave swallow) | Aggressive rival holes |
| **5. Galactic** | The Big Swallow | Star clusters, nebulae, galaxies | The **Elder Hole** — the win-condition rival |

**Escalation levers (introduced one at a time):**
- Edible mass density drops as you grow → you must roam more → pace naturally rises.
- **Rival holes** grow in parallel under the same rules, creating an arms race; if one crosses `1.5x` your mass, it hunts you.
- **Hazards** (pulsars, neutron stars, novae, cosmic-string gravity currents) add positioning skill without adding controls.

**Pacing philosophy:** never punish growth with a wall — punish *carelessness*. Target run length: **4–7 minutes** to full galactic. First swallow within 3 seconds; first tier-up within ~30 seconds; Tier 1 has zero threats so a new player cannot lose immediately.

### Controls — One-Verb, Mouse/Touch
- **Point-to-move:** the black hole eases toward the cursor/finger. Distance from the hole controls speed (capped); hovering close = drift/brake.
- **Speed is inversely proportional to mass:** `speed = base / sqrt(mass)` — small holes dart, huge holes are ponderous and inevitable. Momentum management is the entire skill ceiling from one input.
- **Optional secondary — "Cinch"** (hold click / two-finger tap, cooldown-gated ~4s): briefly tightens the horizon for a shorter but much stronger pull — snag a fleeing rival, dodge a pulsar, or avoid accidentally grabbing something too big.
- Fully playable one-input. WASD offered as an accessibility alternative. No mid-game menus: Load → title flash → tap to begin.

### Scoring
- **Primary — Mass**, displayed via an *escalating unit label* (grams → tonnes → Earths → Suns → Solar Systems → Galaxies). Watching the *unit* change is more satisfying than a climbing number.
- **Swallow Chain / Style score** — a combo "heat" meter for rapid consecutive swallows and eating rivals; the leaderboard number and skill expression. Cools if you idle.
- **Bonuses:** spiral captures, no-graze tier completion.
- **Post-run screen:** final mass, biggest object swallowed, longest combo, time-to-finale, and a procedural title ("You became a Type-II Devourer"). Personal best persisted to `localStorage` — no server, stays single-file.

### Win / Lose Conditions
- **Win — "The Big Swallow":** consume the Elder Hole / galactic nucleus in Tier 5. The horizon fills the screen, the field spirals to a singularity, then a soft white bloom — you swallowed the level itself. The camera pulls back to reveal you were a speck. Offers **"Devour Again"** (New Game+, faster/denser) and a teaser line for the *Event Horizon* expansion.
- **Lose:** swallowed by a larger rival, or mass driven to zero by hazards. Presented on-theme: your view is torn apart by tidal forces, redshifts, and winks out — *"Now you're the swallowed."* (seeding the sequel). Death is quick, fair, teaching, and instantly re-runnable ("Again" — no reload).

---

## Game Art & Design

### Visual Direction
Cold, elegant, surreal cosmic sci-fi — a lonely, greedy singularity in an endless starfield. Fully **procedural, zero external assets**, rendered on **Canvas 2D**.

- **The Black Hole:** a dark central disk ringed by a distortion halo built from radial gradients and additive glow, with a rotating **accretion swirl** (rotating gradient arcs). A cheap **faked gravitational lens** — sampling/offsetting the starfield radially near the horizon — sells the surreal "bending space" effect at low cost.
- **Infalling matter:** additive-blend particle streams that accelerate and spiral inward; a luminous trail behind the player.
- **Prey:** radial gradients + simple polygons — glowing ice/dust motes, rocky asteroids, banded planets with ring systems, blazing stars, shimmering nebulae.
- **Starfield background:** parallax twinkling points and soft gradient nebula washes; each tier applies a **color shift** to reinforce progression.
- **Camera:** mass-locked zoom — the black hole stays a consistent fraction of the screen, so zooming out *is* the visual language of growth.
- **UI:** minimal, single-glance — an escalating mass/unit readout, a combo-heat bar, and the cinch cooldown. No clutter; the cosmos is the interface.

### Color Palette
- **Voids & horizon:** deep indigo-to-black.
- **Accretion & energy:** hot cyan, violet, and amber gradients bleeding into white at capture.
- **Prey:** cool blues (ice/comets), warm ochres (rock/planets), fierce whites and golds (stars), iridescent teal-magenta (nebulae).
- **Tier progression:** palette warms and intensifies as you grow, culminating in a blinding white bloom at *The Big Swallow*.

### Audio & Sound Design (Procedural WebAudio)
Fully synthesized — no audio files — for instant load and offline play.

- **Ambient bed:** a low sub-bass drone that *drops in pitch and opens its filter as you grow* — you literally sound heavier and deeper the bigger you become. A new ambient layer is added at each tier-up.
- **Swallow cue:** a short, wet filtered-noise "whoomph"/pluck, pitch-scaled to the swallowed object's size, and pitch-shifted upward on combos.
- **Combo heat:** a rhythmic pulse layer that intensifies with the style meter.
- **Tension:** a rising pad when a rival closes in; silence-into-swell arcs for danger; crystalline chimes on tier thresholds.
- **Finale:** a resonant, collapsing "swallow" bloom on victory; a redshifted, receding tidal-stretch tone on death.

### Technical Design Notes
- One `<canvas>`, one `requestAnimationFrame` loop, **fixed-timestep physics with an accumulator** for deterministic gravity across framerates.
- **Uniform-grid spatial partitioning** and object pooling so the field can hold hundreds of bodies without frame drops (only screen-relative objects influence the hole).
- Target footprint: **under 50KB, single file, zero dependencies, no external requests, playable offline.**

---

## Roadmap Context
The flagship ships first and becomes the shared engine for the expansion suite:
**Flagship → Event Horizon (inverted survival) → Devourer of Time / Symbiont → The Last Star (emotional capstone).**