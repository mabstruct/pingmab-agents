# The Big Swallow — Game Concept Briefs

*Four new, distinct concepts for the single-player browser game **The Big Swallow**, each interpreting the title in a fresh way. All are feasible as a single self-contained `index.html` (Canvas + inline JS, fully procedural visuals, Web Audio synthesized sound — no external assets), and all fit the studio's creative, inventive, slightly surreal, sci-fi/cosmic identity.*

> **Note:** These four concepts deliberately avoid the black-hole/singularity idea already shipped as *The Big Swallow: Event Horizon*. Each takes a genuinely different reading of the word "swallow" — a migrating bird, the literal act of ingestion, a devouring cosmic mouth (with a perspective flip), and a whimsical word-eating pun.

---

# Concept 1 — The Big Swallow: *Long Migration*

## Idea Description
You *are* the swallow — a lone migratory bird crossing a vast, surreal, ever-shifting cosmos to reach a home that keeps moving. Every autumn the flock scatters and you must "swallow the distance" across a procedurally generated dreamscape, riding thermals, dodging storms, and gathering the warm memories that keep your wings beating. It reframes "the big swallow" as the epic seasonal journey of one small bird against an enormous sky.

## Core Idea
A momentum-based, one-input endless flight game. The screen scrolls horizontally through stylized biomes (electric-storm oceans, crystalline deserts, aurora tundra). Holding input makes the swallow dive and gain speed; releasing lets it soar and climb on invisible thermal currents. The whole run is a single unbroken "migration" measured in nautical-league milestones — a nod to the sailor's swallow-tattoo lore (one swallow per 5,000 nautical miles).

## Key Features & Mechanics
- **Thermal riding** — rising warm-air columns you catch to gain altitude and stamina
- **Momentum flight** — dive to build speed, soar to conserve stamina; gravity vs. lift, no jump button
- **Warmth meter (stamina)** — depletes over cold stretches, refilled by "ember motes" and sun-warmed updrafts
- **Milestone tattoos** — every 5,000 leagues earns a glowing swallow-tattoo icon on a scrolling banner (score/progression)
- **Storm gauntlets** — procedural lightning walls and crosswinds that shove the bird
- **Homecoming beacon** — a distant flickering light that grows subtly closer, giving the endless run a felt destination

## Mechanics & Feature Breakdown
- **Input:** Single button. Press = pitch down (dive, +speed, −altitude). Release = pitch up (glide, −speed, +altitude on thermals).
- **Physics:** Vertical velocity integrator with a gravity constant, lift force scaled by thermal proximity, drag scaled by speed.
- **Procedural world:** Seeded biome segments; parallax layers drawn as filled bézier hills and gradient skies.
- **Difficulty curve:** Storm frequency and cold-stretch length scale with distance; thermals thin out late to raise tension.
- **Fail state:** Stamina hits zero → the bird slows, sinks, and the season "ends" — soft, poetic, restart-friendly.

## Key Music & Sound Elements
- Airy, breathy pad synths that swell when soaring, thin out when diving
- Procedural wind noise filtered by altitude and speed (Web Audio biquad filter sweeps)
- Soft chime "pluck" when catching an ember mote; low rumble on storm approach
- A single warm cello-like drone that grows in volume as the homecoming beacon nears

## Why This Works as a Browser Game for the Studio
Instant one-input pick-up-and-play suits short browser sessions, and the endless-migration structure means zero level loading. It's surreal and cosmic (a bird flying through a dreamlike, aurora-lit sky), single-player and contemplative, and leans into the poetic side of the studio's identity. Every element — gradients, particles, bézier terrain, synth audio — is trivially procedural in one self-contained HTML file.

---

# Concept 2 — The Big Swallow: *Hard to Swallow*

## Idea Description
A tiny sentient probe drifts through the throat-canal of a colossal sleeping space-god, and every capsule, memory, and secret it encounters is something the giant "swallowed" long ago. You dive down its endless gullet, swallowing (absorbing) glowing data-pills to stay awake, while deciding which memories are safe to keep down and which are "hard to swallow" and must be spat back out before they poison you. It turns "swallow" into the literal act of ingestion — pills, memories, truths — wrapped in body-horror-lite cosmic surrealism.

## Core Idea
A vertical descent / sorting game. You fall past objects and either swallow or reject each one. Good memories nourish; corrupted ones must be rejected in time. The twist: some memories *look* sweet but are corrupted, so you learn to read subtle visual tells — a "which pills to swallow" risk-reward loop.

## Key Features & Mechanics
- **Swallow / reject binary** — two-button sorting under time pressure
- **Digestion meter** — fills as you swallow good memories; a full meter = level clear ("fully awake")
- **Corruption tells** — bad memories flicker, pulse off-rhythm, or bleed a wrong-color aura (learnable procedural cues)
- **Bitter-aftertaste combo** — chain correct swallows for a multiplier; one wrong swallow resets it and shakes the screen
- **Throat-peristalsis waves** — the tunnel contracts rhythmically, briefly hiding objects and forcing timing reads
- **Memory reveal** — each swallowed memory prints a one-line surreal fragment of the god's past ("It remembers the taste of a dead star")

## Mechanics & Feature Breakdown
- **Input:** Two actions — swallow (keep) vs. reject (spit). Keyboard arrows or left/right mouse halves.
- **Object spawner:** Timed spawns each carrying a `corrupted` boolean and a visual-tell intensity that decreases as difficulty rises (harder to spot).
- **Scoring:** Correct sort +points ×combo; wrong sort −health and combo reset.
- **Rendering:** Peristaltic tunnel = animated concentric shapes with sine-wave radius modulation; memories = glowing procedural orbs with noise auras.
- **Progression:** Faster spawns, subtler tells, tighter peristalsis windows.

## Key Music & Sound Elements
- A wet, organic low heartbeat pulse (Web Audio sine + envelope) syncing with peristalsis
- A satisfying "gulp" swallow sound (pitch-shifted noise burst); a sour, dissonant "reject" tone
- Rising sub-bass drone as the digestion meter fills
- Glassy chime cascade on combo milestones

## Why This Works as a Browser Game for the Studio
Reaction-sorting is a proven, deeply browser-friendly loop — fast rounds, instant restart, one-handed play. The premise is unmistakably surreal and cosmic (spelunking inside a sleeping deity), and the flavor-text memory fragments give it the studio's inventive, slightly unsettling voice. All visuals are procedural sine-modulated shapes and particles; audio is fully synthesized. Purely single-player, meditative-yet-tense.

---

# Concept 3 — The Big Swallow: *Devourer's Appetite*

## Idea Description
A colossal cosmic mouth — the Devourer — drifts across a living galaxy, and *you steer the galaxy, not the mouth*. You must feed the insatiable maw exactly what it craves each cycle while protecting the worlds it should never eat, sculpting orbits and flinging planets like a slingshot chef appeasing a god. This reframes "the big swallow" as an eternal cosmic entity that eats stars — but flips the perspective so you're the caretaker managing its hunger, not the monster itself.

## Core Idea
A physics/aiming puzzle-arcade. Each level, the Devourer opens its mouth and displays a "craving" (e.g., *"3 blue giants, 0 inhabited worlds"*). You grab and fling celestial bodies with gravity-slingshot mechanics into — or away from — the mouth before its patience meter empties and it swallows *everything* indiscriminately.

## Key Features & Mechanics
- **Gravity slingshot** — drag-and-release to fling planets and stars along curved orbital trajectories
- **Craving cards** — per-level order tickets specifying what to feed and what to withhold
- **Patience meter** — a countdown; empty = the Devourer rage-swallows the whole board (fail)
- **Body types** — stars (fuel, high value), gas giants (bouncy), rogue moons (blockers), inhabited worlds (never feed — protect!)
- **Chain feeding** — bank a satisfied craving to unlock a temporary "slow-swallow" bullet-time for tricky trick-shots
- **Orbital hazards** — existing gravity wells bend your throws, turning each puzzle into a trajectory-reading challenge

## Mechanics & Feature Breakdown
- **Input:** Click-drag-release aiming with a predicted-arc dotted trajectory line.
- **Physics:** N-body-lite — a handful of fixed gravity wells plus the flung body; simple velocity + gravitational acceleration per frame.
- **Win condition:** Fulfill the craving exactly (correct bodies swallowed, forbidden bodies protected) before patience empties.
- **Scoring:** Efficiency (fewer throws), speed, and no-collateral bonuses.
- **Rendering:** Planets as radial-gradient circles; the mouth as an animated concentric-ring void with a toothy procedural rim; trajectory as a dotted arc.
- **Progression:** More bodies, tighter cravings, cross-cutting gravity wells, shorter patience.

## Key Music & Sound Elements
- Deep, slow, hungry breathing drone from the Devourer
- A rising anxious arpeggio as the patience meter drains
- Wet, resonant "swallow" boom on a successful feed; a jarring cosmic groan + screen shake on a wrong feed
- Sparkly launch "whoosh" (filtered noise sweep) on each fling; a warm resolve chord on level clear

## Why This Works as a Browser Game for the Studio
Slingshot/trajectory puzzles (the Angry-Birds lineage) are among the most successful browser genres — bite-sized levels, instant retry, snackable sessions. The perspective flip (you're the *feeder* of a cosmic god, sculpting a galaxy) is exactly the inventive, slightly surreal, sci-fi/cosmic tone the studio wants, and it's a completely different mechanic and role from *Event Horizon*'s black hole. Pure procedural circles, arcs, and synth audio in one file. Single-player puzzle progression.

---

# Concept 4 — The Big Swallow: *A Bird in the Word*

## Idea Description
A pun-loving swallow (the bird) has escaped from a dusty dictionary and is now literally eating language — you fly around swallowing letters and words to spell your way out of an absurd, floating cosmic library. But beware: swallow the wrong words and reality warps around you (swallow **GRAVITY** and everything floats; swallow **NIGHT** and the screen goes dark; swallow **SPEED** and time accelerates). This is the playful wordplay take — "the big swallow" as a bird that swallows words, with surreal cause-and-effect from whatever it eats.

## Core Idea
A collect-and-spell arcade-puzzle. You fly the swallow through a zero-gravity library-cosmos, g