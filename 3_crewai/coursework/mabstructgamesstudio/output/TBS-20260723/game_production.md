# THE BIG SWALLOW
## Game Production Document

---

## Game Title
**The Big Swallow**

## Game Subtitle
*Glutton: The Organism*

---

## Short Idea Description

A strange, translucent alien organism awakens deep inside a derelict cosmic generation ship and discovers it is *very* hungry. Starting as a microscopic swallow-sac feeding on dust and bacteria, you eat, grow, and mutate your way up the food chain — until you're large enough to swallow the crew, the engines, and eventually the ship itself. Your final meal is the fusion core, and your final act is to ignite into a living star.

---

## Core Idea

*The Big Swallow* is a single-player, browser-based growth game — think *Katamari* meets cellular consumption — wrapped in a slightly surreal, melancholic sci-fi shell. The game is built on three design pillars:

1. **The Joy of Escalation.** The central dopamine loop is the recurring *"You can now eat X"* moment. Everything funnels toward, celebrates, and re-triggers that beat as you cross growth thresholds.
2. **You Are What You Eat.** Consumption isn't just growth — it's transformation. Keystone prey grant **mutations** that visibly reshape your silhouette and change how you play, making identity fluid and expressive.
3. **The Empty Ship.** As you grow, the world quiets. Cute gluttony curdles into something reflective and mournful. Every meaningful thing you swallow leaves an **echo** — a voice or memory fragment — so that by the end you are a collage of everything (and everyone) you've consumed, and you feel just slightly complicit.

---

## Game Mechanics & Features

### Size Value (SV) & Growth
- Every entity, including the player, has a numeric **Size Value (SV)**. You can swallow anything with `SV < player.swallowThreshold`, where `swallowThreshold = player.SV × 0.85` — you can eat things *nearly* your size but never quite equal, keeping the "just out of reach" tension alive.
- Growth is **logarithmic within a tier, exponential across tiers**: dust gives diminishing returns, pushing the player to keep hunting bigger prey rather than grinding.

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

### The Mutation System ("You Are What You Eat") — *signature mechanic*
- The player has **3 active mutation slots**; new keystone prey prompt a manual swap for full player agency.
- Mutations create *situational build decisions* rather than rigid classes, keeping the game replayable and expressive without heavy RPG systems.

| Swallowed | Mutation | Effect | Silhouette Change |
|-----------|----------|--------|-------------------|
| Security Drone | **Plating** | Tanky; reduces hazard damage, slower | Chitinous metal scales |
| Fungal Bloom | **Corrosive** | Dissolves barriers/armor; toxic trail | Sickly green, dripping |
| Cleaner-Bot / Nanites | **Stealth** | Semi-translucent; shorter enemy detection | Shimmering, refractive |
| Crew Member | **Echo-Key** | Grants access codes + memory; swallow-speed buff | Humanoid ghost flickers within |
| Coolant Slug | **Fireproof** | Immune to heat/fire zones | Frosted, crystalline blue |
| Gravity Plating | **Anchor** | Immune to zero-G push zones | Dense, magnetized underside |
| Bio-Luminescent Algae | **Glow** | Lights dark areas, reveals prey (but increases detection) | Pulsing internal light |

### The Echo System (Narrative Layer)
- Keystone entities — especially crew — leave collectible **Echoes** (short voice/text memory fragments), reviewable in the "Innards" menu.
- As the ship empties, ambient chatter fades and comms go silent while the echo-counter grows — a deliberate **inverse relationship** the player feels.
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
- **"Now Edible" Tier Indicator:** flashes the *"YOU CAN NOW EAT: [X]"* escalation card.
- **Mutation Bar:** three glyph slots showing active/toggleable mutations.
- Minimal, diegetic, and breathing with the organism itself.

### Session Structure
- A single escalating ~25–45 minute arc from microscopic mote to living star, with a defined climax: **The Big Swallow** — consuming the fusion core.
- Fully **resumable** and browser-friendly.

---

## Key Art & Design Elements

- **The Organism:** a translucent, pulsing, gel-like "swallow-sac" whose silhouette visibly evolves as mutations stack — the game's central visual anchor and living HUD. Body-horror-cute: gross but endearing.
- **Perspective:** clean top-down 2D with soft depth and layered parallax; vector-friendly forms for lightweight rendering.
- **The Ship:** a decaying retro-futuristic generation ship — organic-industrial interiors, flickering emergency lighting, overgrown hydroponics, frosted coolant chambers, and warm human habitation decks that grow eerily still.
- **Visual escalation:** the world literally opens up as you grow — cramped ducts give way to vast decks and finally the cavernous reactor chamber.
- **Color journey:** cool bioluminescent micro-world → warm, lived-in human decks → fiery reactor climax → blinding stellar white-gold ignition finale.
- **Juicy feedback:** maw stretch animations, screen pulses, particle bursts on swallow, ghostly echo-shapes drifting inside the translucent body.

---

## Key Music & Sound Elements

- **Adaptive soundtrack** that layers up with each growth tier: sparse ambient drones and wet micro-textures at Tier 0, building warmth and rhythm through the crewed decks, swelling to an orchestral-electronic climax at stellar ignition.
- **Signature swallow SFX:** a satisfying, escalating "gulp" that deepens in pitch and body as the organism grows — the game's most-repeated and most rewarding sound.
- **Echo audio:** whispered, intimate voice fragments (crew memories) that gradually overlap and blur into a haunting choral wash by the end.
- **Diegetic emptiness:** ship comms, ambient chatter, and machinery hum that progressively fade to silence — the audio directly expressing "The Empty Ship" pillar.
- **Escalation stings:** a bright, triumphant musical cue for every *"You can now eat X"* threshold moment.
- **Finale:** a resonant, awe-tinged crescendo as the fusion core is swallowed and the organism ignites into a star.

---

## Why This Works as a Browser Game for the Studio

- **Proven, lightweight loop.** The grow-to-eat mechanic is a browser-native staple that is instantly satisfying, requires no tutorial, and runs beautifully with simple 2D vector art and particle systems — no heavy assets, fast load, single-player, resumable.
- **Elevated to fit our identity.** Where most grow-games are hollow, we layer on the surreal, cosmic, slightly melancholic tone the studio is known for. The mutation system and echo narrative make it unmistakably *us* — inventive and emotionally weird — without inflating scope.
- **Expressive without complexity.** Three-slot mutations deliver light "build variety" and replayability while staying trivial to implement and teach in a browser context.
- **Emotional payoff rare in the genre.** The inverse relationship between growth and loneliness, plus the star-birth finale, gives players a reason to *feel* something and to share — turning a snackable browser game into a memorable one.
- **Contained, shippable scope.** A single ~30-minute arc, no combat, no permadeath, and no online infrastructure means we can produce a polished, complete experience efficiently — exactly the sweet spot for a single-player browser title.