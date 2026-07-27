# The Big Swallow — Game Concept Briefs

*Prepared by the Game Producer for handoff to the Game Designer. Six distinct, browser-ready concepts, each interpreting "swallowing" through a genuinely different mechanical lens. All are designed as lightweight, single-player, HTML5 Canvas builds fitting the studio's inventive, surreal, cosmic/sci-fi voice.*

---

# 1. The Big Swallow — *Event Horizon Diet*

**Short Idea**
You are a fussy black hole with an eating disorder: you can only swallow matter of the color you're *currently craving*, and that craving flips on a rhythmic beat. It's a color-matching rhythm game dressed in a cosmic-consumption costume, where growth rewards restraint and pattern-reading instead of mindless hoovering.

## Core Idea
Drift a gravity well across a starfield of colored debris. A "craving" halo tints your event horizon and changes every few seconds. Vacuum matching-colored matter to grow and build combos; slurp the wrong color and you get "cosmic indigestion" — belching it back out, shedding mass and warping the screen. Mastery is the greedy art of clearing a whole cluster in the split-second before your craving flips.

## Key Features & Mechanics
- **Rhythmic craving system** — a beat-synced color you must match.
- **Selective gravitational swallow** — only matching debris grows you.
- **Combo scoring** — chained correct swallows multiply score.
- **Indigestion penalty** — mismatches cost mass + trigger screen distortion.
- **Ramping tempo** — craving-swap speed accelerates for a natural difficulty curve.

## Mechanics & Features Breakdown
- **Growth loop:** match color → grow event horizon → larger gravity radius → clear clusters faster.
- **Risk/reward:** hoovering everything nearby is punished; timing greed against the craving flip is the skill ceiling.
- **Readable feedback:** halo tint = current craving; chromatic aberration on mistakes signals failure instantly.
- **Session cap:** difficulty ramp naturally ends runs at ~4–8 minutes.

## Why It Works as a Browser Game
Pure Canvas 2D — radial gradients, additive-blend particles, no external assets. Game state is tiny (position, mass, craving color, combo). Instant-load, single-file, mobile-friendly.

## Key Music & Sound Elements
- A pulsing synth heartbeat that **is** the craving-swap timer.
- Each correct match layers in a harmonic — a great run literally composes its own track.
- A detuned "gulp-gone-wrong" SFX for mistakes.

## Why It Works for the Studio
Deeply "Mabstruct": surreal, cosmic, screenshot-worthy (swallowing a galaxy at the perfect beat), and mechanically inventive rather than a Hole.io reskin.

---

# 2. The Big Swallow — *A Whale Who Ate the Sky*

**Short Idea**
A colossal sky-whale is slowly swallowing the heavens — clouds, birds, the sun, even the color blue itself. You are not the whale; you are the small caretaker below, deciding what to protect and what to let it eat. It's a surreal, melancholy sorting game about curated loss.

## Core Idea
Objects rise from the horizon toward the whale's open mouth. Flick precious things (a kite, a paper plane, a balloon) safely aside and let junk (storm clouds, static, dread) be swallowed. Every wrong choice permanently dims the world's palette, making stakes visible at a glance.

## Key Features & Mechanics
- **Inverted power fantasy** — you curate the swallow, you don't perform it.
- **Drag/flick physics** — divert objects away from the mouth.
- **Permanent desaturation** — the world loses color as beauty is eaten.
- **A shareable "final sky"** — a unique frozen painting of what you saved.

## Mechanics & Features Breakdown
- **Judgment loop:** identify → flick-to-save or ignore-to-swallow → world palette responds.
- **Ambient tension:** the swallow is inevitable and slow; the player manages *what*, not *whether*.
- **Readability:** color drain is a persistent, always-visible scoreboard of your choices.
- **Natural end:** the sky "empties" in a few minutes.

## Why It Works as a Browser Game
Vertical drag input (excellent on mobile web), layered parallax sky, simple flick physics. Lightweight and single-file. Short-session by design.

## Key Music & Sound Elements
- Ambient wind + a slow, distant whale-song that lowers in pitch as the sky empties.
- Each swallow: a soft, cavernous "whoomf."
- Minimal UI sound — mood carries the experience.

## Why It Works for the Studio
Ghibli-meets-cosmic-dread emotional resonance; low-friction pitch; unmistakably surreal and shareable. Shows the studio can do mood, not just adrenaline.

---

# 3. The Big Swallow — *Sound Eater*

**Short Idea**
You pilot a mouth that can only see the world when it makes noise. The screen is near-black; every sound emits visible ripples, and you can only swallow what you can *hear*. Silence is invisible danger — a synesthetic stealth-eat game.

## Core Idea
Navigate a dark space where objects ping outward as expanding sound-rings, briefly revealing their shape and position. Move toward and swallow noisy prey to score — but each swallow silences that source, shrinking your vision. Every meal makes you blinder, weaponizing the core tension between eating and staying safe.

## Key Features & Mechanics
- **Sound-as-sight** — objects are only visible while emitting ripples.
- **Consumption-reduces-perception** — eating removes your own eyesight.
- **Silent hazards** — dangers give no ping until they're on top of you.
- **Radar-poetry aesthetic** — luminous ripples on black.

## Mechanics & Features Breakdown
- **Core loop:** listen/watch for pings → navigate → swallow → world goes darker.
- **Baked-in risk/reward:** points vs. perception are directly traded on every bite.
- **Escalating dread:** the more successful you are, the harder navigation becomes.

## Why It Works as a Browser Game
The Web Audio API + Canvas is a perfect marriage. Ripples are just expanding stroked circles synced to sound triggers. Minimal visuals = tiny footprint. Genuinely novel and clip-worthy.

## Key Music & Sound Elements
- **The core mechanic itself** — spatialized pings drive perception.
- A low drone for the void.
- A wet click-swallow that abruptly cuts a sound off mid-note (unsettling + satisfying).

## Why It Works for the Studio
The boldest, most inventive "Mabstruct" swing — pure innovation, deeply surreal, and a showcase of technical/creative daring.

---

# 4. The Big Swallow — *Ouroboros.exe*

**Short Idea**
You are a cosmic serpent forced to eat your own tail to survive — but every segment you swallow *reprograms* your body. Eat a fire-segment and your whole snake becomes flammable; eat a phase-segment and you pass through walls. A self-cannibalizing puzzle-arcade where you sculpt yourself by consuming yourself.

## Core Idea
Snake-like movement across a cosmic grid. You must periodically bite your own tail to shorten and stay fast enough to catch drifting star-fruit that lengthens you. Each tail segment carries a property, and swallowing it applies that property to the whole snake for a short window — which you exploit to reach otherwise-blocked fruit and exits.

## Key Features & Mechanics
- **Self-swallow as transformation** — eating yourself grants powers.
- **Segment-property system** — fire, phase, magnet, etc., data-driven and expandable.
- **Length management** — balance speed (short) vs. reach/power (long).
- **Inverted Snake rule** — eating yourself is the whole strategy.

## Mechanics & Features Breakdown
- **Loop:** grow via fruit → choose which segment to sacrifice → apply its power → solve/reach the goal.
- **Strategic depth:** the ordering of your own segments becomes a puzzle you manage.
- **Readability:** each segment is a distinct emissive hue for instant planning.

## Why It Works as a Browser Game
Grid-based snake logic is famously lightweight and single-file. The property system is trivially expandable. Instantly readable and shareable ("I turned to glass and phased through the boss").

## Key Music & Sound Elements
- Arcade bleeps that pitch-bend as the snake changes state.
- A squelchy "self-swallow" chomp.
- A droning synth bassline that shifts key per active property.

## Why It Works for the Studio
Retro-cosmic vaporwave; the most immediately fun and easiest-to-prototype arcade hook, with a genuinely fresh twist on a beloved classic.

---

# 5. The Big Swallow — *The Compressor*

**Short Idea**
Reality is running out of memory, so a program called SWALLOW is compressing the universe — literally eating detail to save space. You are the compression cursor: draw boxes around chunks of a beautiful hand-drawn cosmos and swallow them into low-res blocks to hit your storage quota before the level crashes. A darkly funny game about deleting beauty to survive.

## Core Idea
Each level is a lush scene (a nebula garden, a mechanical sun). A shrinking storage bar demands you compress X% of the scene fast. Drag-select regions to swallow them into pixelated, JPEG-artifacted blocks that free up space — but some regions are load-bearing (compress them and the scene glitches and collapses early), and others yield bonus space. You must "read" an image for meaning to survive.

## Key Features & Mechanics
- **Destructive optimization puzzle** — you vandalize art to hit a quota.
- **Region-selection swallow** — drag-boxes downsample in real time.
- **Load-bearing vs. expendable detail** — reading structure is the skill.
- **Unique corrupted artwork per run** — extremely shareable output.

## Mechanics & Features Breakdown
- **Loop:** assess scene → drag-select regions → swallow to free space → race the crashing storage bar.
- **Tension:** wrong (structural) compressions cause early collapse; smart ones bank bonus space.
- **Native tech fit:** Canvas is a pixel buffer, so "compression" = live downsampling of regions.

## Why It Works as a Browser Game
Canvas is literally a pixel buffer — real-time downsampling is native and cheap. Each finished level is a half-destroyed artwork, making every screenshot unique and share-driven.

## Key Music & Sound Elements
- Clean ambient pads that get bit-crushed and downsampled in real time as you compress — the soundtrack degrades with the visuals.
- Each swallow: a data-crunch "zip" sound.

## Why It Works for the Studio
Nobody is doing "eat the resolution." Glitch-art-meets-tech-dystopia is surreal, satirical, and maximally novel — a defensible, screenshot-driven identity.

---

# 6. The Big Swallow — *Chrono Gullet*

**Short Idea**
You are an entity that swallows *time itself*. Each level is a single frozen moment; you gulp seconds from stable objects to fast-forward others, threading them into a chain reaction. A physics puzzle where the thing you consume is duration.

## Core Idea
Every puzzle is a static tableau (a comet mid-fall, a door mid-open). With a limited "time appetite," you swallow time from stable objects (freezing them) to spend it advancing others — engineering a Rube-Goldberg sequence that delivers a star