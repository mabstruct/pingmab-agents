# The Big Swallow: Event Horizon
## Game Production Document

---

## Game Title & Subtitle

**Title:** The Big Swallow
**Subtitle:** *Event Horizon — Eat the Universe, One Star at a Time*

---

## Short Idea Description

You are a newborn singularity — a hungry, sentient black hole drifting through a cartoon-surreal cosmos. Swallow asteroids, moons, rogue planets and entire star systems to grow your gravity well, until you're consuming whole galaxies and bending spacetime itself. But gorge on something too massive too soon and you destabilize, violently spitting matter back out and shrinking — so every gulp is a delicious gamble.

---

## Core Idea

*The Big Swallow: Event Horizon* is a refined, single-player evolution of the beloved "eat-and-grow" loop (à la agar.io / Katamari), reframed as an act of cosmic gluttony. The player steers a heavy, inertia-driven gravity well with the mouse or a finger drag, pulling smaller objects into the void and absorbing them to grow ever larger.

The signature twist is the **Stability Meter** — a risk/reward heartbeat that forces the player to balance *appetite against digestion*. Overeat and you overload and purge; hold back and you starve on time and score. This transforms a simple "get bigger" loop into a strategic rhythm of **gorge → strain → digest → grow**, wrapped in the studio's surreal, wondrous cosmic identity.

---

## Game Mechanics & Features

### Controls
- **Steering (Mouse / Touch):** The black hole always drifts. The player sets a "pull point" with the cursor or finger; the singularity accelerates toward it with heavy, floaty inertia — weighty, never twitchy.
- **CLENCH (hold click):** Temporarily tightens and widens the gravity well to snag fleeing objects or clusters, draining a small focus reserve.
- **PURGE (Spacebar / double-click):** Voluntarily ejects mass — shrinks you but instantly restores stability. A strategic panic button.
- **Accessibility:** Keyboard fallback (WASD/arrows), single-hand playable, no precision-timing demands.

### Core Stats
- **MASS** — total matter consumed; drives visual size and score.
- **PULL RADIUS** — reach of your gravity well; scales with mass (shown as a shimmering ring).
- **SWALLOW THRESHOLD** — max safe object size (~60% of current mass). Objects glow **green** if safe, **red** if a gamble.

### The Stability Meter (the heart of the loop)
- Every swallow adds **Stability Load**; large objects add big spikes and take longer to digest.
- **Green (0–60%):** full control. **Amber (60–90%):** movement slows, edges vibrate. **Red (90–100%):** the hole shudders.
- Hit 100% → **DESTABILIZATION**: a violent matter purge, screen shake, and loss of mass (a setback, not a game over).
- Load naturally drains over time as matter digests into permanent MASS — creating the **gorge → strain → digest → grow** rhythm.

### Object Hierarchy (what you eat)
Space dust → asteroids → comets (fast, need CLENCH) → moons → rogue planets → stars (flare and push debris) → full star systems → nebulae (slurped over time) → galaxies (endgame cores).

### Progression
- **In-run:** constant, satisfying visual growth unlocking bigger object classes.
- **Meta (Gravity Lab hub):** spend **Singularity Essence** on permanent upgrades — bigger starting mass, faster digestion, wider pull radius, longer CLENCH, "Iron Stomach" (higher stability ceiling), and cosmetic skins.

### Zone / Level Structure (five escalating zones)
1. **The Nursery** — tutorial asteroid fields → reach target mass.
2. **The Rogue Belt** — comets & rogue planets → swallow the "Wandering Giant."
3. **Solar Court** — flaring star systems → consume 3 complete systems.
4. **The Nebula Deep** — nebulae & dying stars → drink the Great Nebula dry.
5. **Galactic Heart** — spiral arms & the Core → swallow the Galactic Core to win.
Zones transition via a **wormhole warp** (disguising loading).

### Scoring
- Primary score = **Solar Masses consumed**.
- **DEVOUR COMBO** multipliers (x2/x3/x5) for chain-swallowing; reset on pause or destabilization.
- Bonuses: **Perfect Systems**, **Brinkmanship** (surviving in the red), and **Surreal Snacks** (hidden objects).
- End-of-run summary: total mass, biggest single swallow, best combo, Essence earned.

### Win / Lose Conditions
- **Win:** meet each zone goal; the final win (Galactic Core) triggers the **"Event Horizon" ending** — spacetime collapses to a point, then blooms into a new Big Bang, implying you become a new universe. Unlocks Endless Mode.
- **Lose (soft):** no hard death. Repeated destabilizing costs mass/time; optional per-zone "collapsing void" timers add tension. **Failure still banks Essence** and feeds progression.

### Special Surreal Twists (studio signature)
- **The Space Whale** — a serene, singing giant; a huge late-game reward with a mournful song sting.
- **Cosmic Vending Machine** — dispenses temporary power-ups ("Insatiable," "Tiny Gulp," "Sugar Rush").
- **The Reverse Zone** — gravity briefly inverts; you must chase fleeing objects.
- **Talking Objects** — googly-eyed planets blurt one-liners as they're swallowed ("Tell my moons I love them").
- **The Fourth Wall Nibble** — at galactic scale, the UI itself drifts toward your gravity well.
- **Hidden Ouroboros** — in Endless Mode, grow enough to swallow a tiny black hole… a mini-you.

### Replayability Hooks
Meta-upgrades, **Endless Mode**, a **Daily Cosmos** (seeded shared layout), **Cosmic Feats** achievements, cosmetic skins, and localStorage high scores.

---

## Key Art & Design Elements

- **Visual style:** Clean cartoon-surreal vector art — bold outlines, flat-with-gradient shading; *Kurzgesagt*-style cosmic charm meets playful indie surrealism. Vector-first (SVG/Canvas) for tiny file sizes and crisp scaling.
- **The black hole:** A living, expressive singularity with a glowing, warping accretion disk and a subtly gravitational-lensed core; grows visibly across the run.
- **Objects:** Distinct, readable silhouettes per class (asteroids, comets with tails, moons, googly-eyed planets, flaring suns, diffuse nebulae, spiraling galaxies) plus quirky surreal props (space whale, vending machine, astronaut).
- **Color palette:** Deep cosmic blues/violets and inky blacks as a base, punctuated by vivid neon accents — cyan pull-rings, warm star oranges/golds, magenta/teal nebula clouds; escalating saturation as zones deepen.
- **Effects:** Gravitational-lens warping, spacetime distortion around the hole, absorption "slurp" bursts, screen shake on destabilization, wormhole warp transitions, and the "New Big Bang" endgame bloom.
- **UI:** Minimal, cosmic-elegant HUD — central pulsing Stability Meter, faint pull-radius ring, floating mass counter, green/red swallow indicators; UI drifts and wobbles during the endgame "Fourth Wall Nibble."
- **Environment:** Parallax starfields, drifting nebula backdrops, orbiting star systems, and the collapsing void boundary for timed tension.

---

## Key Music & Sound Elements

- **Music style:** Ambient, evolving synth-driven cosmic score — meditative and awe-inspiring in calm moments, swelling with tension as the Stability Meter climbs. Layered, adaptive tracks that intensify per zone and during gorging streaks.
- **Ambient soundscape:** Low cosmic drones, distant stellar hums, gentle nebula shimmer, and the ethereal, mournful song of the Space Whale.
- **Feedback SFX:**
  - **Swallowing:** satisfying "slurp"/whoosh that deepens in pitch as objects grow larger.
  - **Growing:** a warm, resonant "bloom" tone on size thresholds.
  - **Combo:** rising musical stingers stacking with each chained swallow.
  - **Strain (Amber/Red):** a tense, rumbling heartbeat that quickens as stability nears critical.
  - **Destabilization:** a violent bass-heavy rupture and debris scatter.
  - **Purge:** a controlled release "exhale."
  - **Surreal flourishes:** googly-eyed planet one-liner voice-blips, vending-machine jingle, whale song, and a serene "New Big Bang" chord for the ending.

---

## Why This Works as a Browser Game for the Studio

- **Proven, instantly readable loop:** The eat-and-grow mechanic is universally understood and endlessly addictive — but here it's reimagined as a *single-player, meditative-yet-tense* experience rather than frantic PvP, perfectly matching the studio's inventive, single-player focus.
- **Technically lightweight:** Vector art and simple physics on HTML5 Canvas keep load times near-instant, run smoothly on any device, and stream fast — essential for browser play. Warp animations elegantly disguise any loading.
- **Pick-up-and-play with depth:** One-input controls make it welcoming in seconds, while the Stability Meter, combos, and meta-upgrades give the "just one more run" depth that drives retention in short browser sessions.
- **On-brand cosmic surrealism:** A hungry, sentient black hole with googly-eyed talking planets, a singing space whale, and a fourth-wall-eating finale is exactly the studio's slightly-surreal, sci-fi/cosmic, creative-and-innovative identity — with a title whose double meaning ("The Big Swallow") is a wink the audience will love.
- **Strong replay & shareability:** Endless Mode, the seeded Daily Cosmos, achievements, and local leaderboards create low-cost, high-engagement replay hooks ideal for a browser audience, without heavy server infrastructure.