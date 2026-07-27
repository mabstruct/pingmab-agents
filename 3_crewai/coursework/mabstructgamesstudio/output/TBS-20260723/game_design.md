# The Big Swallow
## Game Design Document

---

## Game Title

**The Big Swallow** — *Glutton: The Organism*

---

## Short Idea Description

A strange, translucent alien organism awakens deep inside a derelict cosmic generation ship and discovers it is *very* hungry. Starting as a microscopic swallow-sac feeding on dust and bacteria, you eat, grow, and mutate your way up the food chain — until you're large enough to swallow the crew, the engines, and eventually the ship itself. Your final meal is the fusion core, and your final act is to ignite into a living star.

---

## Core Idea

*The Big Swallow* is a single-player, browser-based growth game — **Katamari meets cellular consumption** — wrapped in a surreal, melancholic sci-fi shell. The entire experience is a single escalating ~25–45 minute arc, fully resumable, from microscopic mote to living star. It is built on three design pillars:

1. **The Joy of Escalation.** The central dopamine loop is the recurring *"You can now eat X"* moment. Every system funnels toward, celebrates, and re-triggers that beat as the player crosses growth thresholds.
2. **You Are What You Eat.** Consumption isn't just growth — it's transformation. Keystone prey grant **mutations** that visibly reshape your silhouette and change how you play, making identity fluid and expressive.
3. **The Empty Ship.** As you grow, the world quiets. Cute gluttony curdles into something reflective and mournful. Every meaningful thing you swallow leaves an **echo** — a voice or memory fragment — so that by the end you are a collage of everything (and everyone) you've consumed, and you feel *slightly complicit*.

There is **no combat and no permadeath.** Hazards strip mass rather than kill, keeping the tone contemplative rather than stressful.

---

## Game Mechanics & Features

### Size Value (SV) & Growth

- Every entity, including the player, has a numeric **Size Value (SV)**. You can swallow anything with `SV < player.SV × 0.85` — you can eat things *nearly* your size but never quite equal, keeping the "just out of reach" tension alive.
- Growth is **logarithmic within a tier, exponential across tiers**: dust gives diminishing returns, pushing the player to keep hunting bigger prey rather than grinding.
- **Threshold anticipation:** when the player is within ~10% SV of being able to eat a new object, that object shudders faintly and slightly desaturates — an "almost" cue that pulls the player forward.
- **The "one bite too big" tease:** occasionally an object sits at SV just above the threshold near edible prey. Attempting to eat it produces a small negative-feedback thunk and bounce — making the eventual swallow, once grown, cathartic.

**Growth Tiers:**

| Tier | Name | Prey Examples | Environment Unlocked |
|------|------|---------------|----------------------|
| 0 | Motes | Dust, spores, bacteria | Ventilation microspaces |
| 1 | Vermin | Ship-rats, roaches, nanites | Crawlspaces, ducts |
| 2 | Flora & Machines | Fungal blooms, plants, drones | Botany bay, corridors |
| 3 | Crew | Colonists, engineers, the Captain | Habitation decks, bridge |
| 4 | Structure | Furniture, pods, deck plating | Engineering, hull sections |
| 5 | The Ship | Entire decks, reactor housing | The full vessel |
| 6 | The Core | The fusion core | **Endgame — stellar ignition** |

### The Swallow — Signature Verb Feel

The swallow fires thousands of times per session, so it is broken into three physical micro-phases for maximum satisfaction:

- **PULL (0–120ms):** The target is yanked toward the maw on an ease-out curve; the maw dilates open (~1.3x). A moment of dominion before the payoff.
- **INGEST (120–200ms):** The target shrinks as it crosses the maw and pops out of existence; the organism's body visibly *bulges* at the nearest silhouette vertices, then springs back with overshoot. The swallowed object briefly appears as a **shadow travelling through the translucent body** before dissolving — the "You Are What You Eat" fantasy made literal on every bite.
- **DIGEST (200ms–2s):** A slow mass tick-up, an internal glow pulse travelling toward the core, and an SV counter that animates upward with an overshoot-and-settle.

**Escalating Gulp SFX:** three crossfaded sound layers (wet micro-slurp → mid gulp → cavernous swallow), blended by size, with base pitch mapped continuously to `log(player.SV)` so the organism *smoothly* deepens across the whole run — not just at tier jumps. Per-swallow pitch and start-offset are randomized ±3% so rapid mote-eating reads as a satisfying rhythm, never a machine gun.

**Flow rewards:**
- **Maw magnetism** (late game): far-below-threshold objects gently drift toward you, making apex-tier eating feel effortless and powerful. Early game has no magnetism, so eating feels earned.
- **Dash-swallow combos:** Shift-dashing through a cluster of edible objects auto-swallows them in a chain with a rising pitch-ladder arpeggio, giving skilled players a flow-state expression.

### The Mutation System ("You Are What You Eat") — *signature mechanic*

- The player has **3 active mutation slots**; new keystone prey prompt a manual swap (Q/E) for full player agency.
- Mutations create *situational build decisions* rather than rigid classes — light, expressive replayability without heavy RPG systems.
- Each mutation changes the organism's **base idle animation and silhouette**, so the player recognizes their build at a glance. Swaps play a gelatinous "reconfigure" animation with a wet, organic SFX.

| Swallowed | Mutation | Effect | Silhouette Change |
|-----------|----------|--------|-------------------|
| Security Drone | **Plating** | Tanky; reduces hazard damage, slower | Chitinous metal scales |
| Fungal Bloom | **Corrosive** | Dissolves barriers/armor; toxic trail | Sickly green, dripping |
| Cleaner-Bot / Nanites | **Stealth** | Semi-translucent; shorter enemy detection | Shimmering, refractive |
| Crew Member | **Echo-Key** | Grants access codes + memory; swallow-speed buff | Humanoid ghost flickers within |
| Coolant Slug | **Fireproof** | Immune to heat/fire zones | Frosted, crystalline blue |
| Gravity Plating | **Anchor** | Immune to zero-G push zones | Dense, magnetized underside |
| Bio-Luminescent Algae | **Glow** | Lights dark areas, reveals prey (increases detection) | Pulsing internal light |

### The Echo System (Narrative Layer)

- Keystone entities — especially crew — leave collectible **Echoes** (short voice/text memory fragments), reviewable in the **"Innards"** menu.
- Swallowing a crew member ducks the ambient audio, plays a single soft glass/piano note, and releases a slowly-rising echo-mote that **lingers for a beat before you can collect it** — a built-in half-second of hesitation as you consume a person.
- As the ship empties, ambient chatter and comms fade while the echo-counter grows — a deliberate **inverse relationship** the player *feels and hears*. A global "life density" value drives audio layers down to near-silence by the core.
- Late-game echoes begin to **blur and overlap**, mechanically reinforcing the theme of consumed identity.
- Optional **Echo Threads** reward curiosity: swallowing related crew members completes their stories from inside you.

### Hazards & Light Threat (no combat, no permadeath)

- Bigger-than-you entities and environmental hazards (fire, vacuum breaches, UV sterilizers, crushing bulkheads, zero-G currents) **strip mass** rather than kill — you may shrink a tier, then eat your way back up.
- Each hazard is neutralized by a specific mutation, turning obstacles into **puzzles solved by eating the right thing.** Tone is contemplative, not stressful.

### Environmental Reactivity

- Prey flees as you grow; crew react to the emptying ship (huddling, barricading, whispering over comms).
- At Structural tier, walls, furniture, and whole rooms become edible, dramatically opening the space.

### Controls

- **WASD / Arrows** move; **mouse** aims the maw; **Left Click / Space** swallows; **Shift** pulse-dashes; **Q/E** cycle/toggle mutations; **Tab** opens the Innards menu.
- Full accessibility fallback: click-to-move with auto-swallow, remappable keys, colorblind-safe prey indicators, reduced-motion mode, adjustable game speed. Trackpad-friendly.

### UI / HUD

- **Growth Ring:** circular progress-to-next-threshold that pulses with a quickening heartbeat.
- **"Now Edible" Tier Indicator:** flashes the diegetic *"YOU CAN NOW SWALLOW: [X]"* escalation card, always showing a greyed silhouette of the next thing just out of reach.
- **Mutation Bar:** three glyph slots showing active/toggleable mutations.
- Minimal, diegetic, and breathing with the organism itself.

### Feedback & "Juice" Techniques

- **Squash-and-stretch** on the whole organism per swallow (~1.05x, spring-based).
- **Camera micro-punch** scaled to prey-to-player SV ratio — tiny meals give a 1px kick, big meals give a 6–8px kick plus a brief zoom-out-and-back.
- **Hitstop** (~60–90ms freeze) reserved *only* for milestone / new-tier swallows so those "you can now eat X" moments carry real weight.
- **Chromatic-aberration flash** (2px RGB split, decaying over 200ms) on the biggest swallows.
- A **digest sub-bass hum** whose volume tracks undigested mass, giving the "full stomach" a body.

### Session Structure

- A single escalating ~25–45 minute arc from microscopic mote to living star, with a defined climax: **The Big Swallow** — consuming the fusion core and igniting into a star.
- Fully **resumable** and browser-friendly.

---

## Game Art & Design

### Core Art Philosophy: "Light, not Detail"

Objects are not drawn in detail — they are **glowing silhouettes in the dark.** The generation ship's darkness is free to render and inherently moody. Every object reads as a flat vector shape defined by its own light or its rim against black:

- **Object recipe:** flat vector shape + soft radial glow + rim highlight. This scales identically from dust mote to fusion core.
- **Tight per-tier palette:** a hard-limited palette reads as "art directed" even with simple shapes, keeping asset weight minimal.

### The Organism — the one hero asset

- A translucent, pulsing, gel-like **swallow-sac**, rendered *procedurally* rather than as a sprite: a radial vertex ring (~16–24 points) with per-vertex sine offsets for the idle pulse, filled with a bright-center-to-transparent gradient plus an additive inner glow (~30 lines of code, infinitely scalable, no sprite sheets).
- **Translucency:** rendered at ~0.5–0.7 alpha with an additive core-glow layer and a normal-alpha membrane layer on top; swallowed-object silhouettes travel *between* the two layers.
- **Body-horror-cute:** gross but endearing — the game's central visual anchor and living HUD.
- **Mutations are additive vector over