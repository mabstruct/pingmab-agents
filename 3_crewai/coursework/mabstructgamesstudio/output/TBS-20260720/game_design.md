# The Big Swallow — Game Design Document

---

## Game Title
**The Big Swallow**

---

## Short Idea Description
*The Big Swallow* is a fast-paced, physics-driven browser game where you control a tiny, insatiable blob that grows by swallowing everything in its path — from crumbs and coins to cars, buildings, and eventually entire planets. The twist: everything you eat stays *inside* you, forming a chaotic living inventory that reshapes your abilities, weight, and playstyle. Eat smart, digest strategically, and grow big enough to swallow the world itself.

---

## Core Idea

*The Big Swallow* fuses the addictive **"eat-to-grow"** loop of *Agar.io*, *Hole.io*, and *Katamari* with an original **"living stomach" inventory system** inspired by roguelike deck-builders. Traditional grow-em-up games treat swallowed objects as mere score. Here, everything you consume becomes a **living, active part of your character** — jiggling visibly inside your translucent body and altering how you play.

**Examples of the living stomach in action:**

- Swallow a **magnet** → nearby metal objects drift toward your mouth.
- Swallow a **beehive** → angry bees swarm you, stunning small prey but slowly stinging your insides.
- Swallow a **balloon vendor** → you float higher and move faster, but are easier to knock around.

Players climb escalating **scale tiers** — *Sidewalk → Street → City → Continent → Planet → Cosmos* — each unlocked by hitting a size threshold. Between tiers, a **Digestion Phase** lets players decide which stomach contents to *digest* (permanent stat upgrades) and which to *keep* (active abilities). This creates meaningful, replayable build decisions.

The tone is **comedic, cartoonish, and gloriously absurd** — a googly-eyed blob with a grin too big for its body, wobbling down a street while a fire-truck siren wails from inside its belly.

**The design pillars:**

- **Instantly Understandable** — everyone gets "eat everything to grow bigger."
- **Surprisingly Deep** — the stomach system gives mid-core players strategic build-crafting.
- **Inherently Shareable** — absurd swallow moments beg to be posted.

---

## Game Mechanics & Features

### Core Mechanics

- **Swallow-to-Grow Loop** — A mouse/touch-controlled blob that can only swallow objects *smaller than itself*. Size gates create natural progression and "forbidden fruit" tension — that bus you can't eat *yet* is a goal, not a wall.

- **Living Stomach Inventory** — Every swallowed object appears jiggling inside your translucent body and grants a passive or active effect. **Your stomach *is* your build.** Slot capacity is limited, forcing players to choose what to hold.

- **Digestion Phase (Strategic Layer)** — Between scale tiers, players pause in a mini-round to decide, per item:
  - *Digest* → convert to a permanent upgrade (speed, jaw size, stomach capacity, defense).
  - *Keep* → retain as an active or passive ability for synergy combos.
  - **Deck-building meets snack-building.**

- **Physics-Based Weight System** — Diet affects movement:
  - **Heavy items** → slow you down but grant knockback immunity.
  - **Light items** → nimble and fast but fragile and easily bounced.
  - Balancing your "diet weight" is a core strategic tension.

- **Indigestion & Hazards** — Some objects fight back from inside (angry dogs, dynamite, chili peppers). Players can **burp them out** as projectiles — turning internal hazards into offensive weapons against rivals and bosses.

### Ability & Synergy System

- **Passive Effects** — always-on modifiers (magnet pull, floatation, armor).
- **Active Powers** — triggered via click-hold (burp dash, projectile expel, shockwave belch).
- **Synergy Combos** — stacking related items unlocks emergent bonuses (e.g., *magnet + metal car + dynamite* = a homing explosive burp).

### Progression Feature: Combo Chains

- **Flavor Combos** — swallowing similar items in sequence (all vehicles, all animals, all food) builds a multiplier for score and growth speed, rewarding themed feeding frenzies.

### Game Modes

- **Solo Campaign — "From Crumb to Cosmos"**
  - 6 escalating scale tiers, each with a themed environment and boss.
  - Bosses include a **rival swallower**, a **vacuum-cleaner mech**, and a **hungry black hole** finale.
  - Runs of **8–12 minutes**.

- **Battle Royale — "Swallow or Be Swallowed"**
  - 20-player `.io`-style arena where players eat each other.
  - Swallowed players briefly **fight from inside** the enemy's stomach for a chance to burst free.
  - Matches of **~5 minutes**.

- **Daily Buffet Challenge**
  - Daily seeded run with themed item pools (e.g., *"Junk Food Friday"*).
  - Global leaderboards for competitive replay.

### Engagement & Retention Features

- **Belly Trophy Room** — a persistent meta-gallery of rare **Legendary Swallows** (the Eiffel Tower, a whale, the Moon) to collect and display.
- **Cosmetic Progression** — unlockable skins, mouth styles, burp sound packs, and stomach patterns. **Strictly no pay-to-win** — monetized via cosmetics and optional rewarded ads.
- **One-Click Shareable Moments** — auto-generated GIF clips of your most absurd swallows *("You just swallowed a wedding. Share it?")* for viral social spread.

### Technical & Accessibility

- **Instant Play** — no login required for first session; HTML5/WebGL; loads in under 5 seconds; runs on desktop and mobile browsers.
- **One-Input Control Scheme** — fully playable with mouse or single touch; burp/dash mapped to `click-hold` for depth without complexity.
- **Session Design** — snackable sessions with a strong "one more run" hook.

---

## Game Art & Design

### Visual Style

- **Overall Aesthetic** — bright, bold, cartoonish 2D vector art with juicy squash-and-stretch animation. Think *Rayman* meets *Katamari Damacy* meets a mobile-friendly comic strip.
- **The Blob (Player)** — a translucent, jelly-like creature with an oversized googly-eyed grin. Its **see-through body is the star**: players watch swallowed objects tumble, jiggle, and interact inside in real time. As it grows, its wobble physics exaggerate for comedic weight.
- **Living Stomach Visualization** — swallowed items float and collide inside the body with soft physics. A subtle glow highlights *active* items so players can read their build at a glance.

### Color & Mood

- **Palette** — saturated, candy-bright primaries against clean backgrounds for high readability at small mobile sizes.
- **Tier Color Themes:**
  - *Sidewalk* — warm pavement grays and pastel crumbs.
  - *Street* — vibrant urban reds, yellows, and neon.
  - *City* — cool glass-and-steel blues.
  - *Continent* — earthy greens and ocean teals.
  - *Planet* — atmospheric gradients and cloud whites.
  - *Cosmos* — deep purples, starfields, and cosmic neon.

### Environment Design

- Each scale tier is a **distinct diorama** that recontextualizes scale — objects that were giant obstacles one tier ago become tiny snacks the next. This "zoom-out" payoff is a key emotional beat.
- Backgrounds are layered with **parallax depth** for a sense of speed and scale without cluttering gameplay readability.

### UI & UX Design

- **Minimalist HUD** — size meter, growth progress toward next tier, active-item icons, and combo multiplier. Everything designed to be glanceable during fast play.
- **Digestion Phase Screen** — a clean, card-based interface where each stomach item is a "snack card" with clear *Digest* vs *Keep* choices and readable effect descriptions.
- **Feedback & Juice** — every swallow triggers satisfying gulp sounds, screen-space particles, squash animation, and a growth "pop." Big milestone swallows trigger a brief slow-mo celebration.

### Audio Design

- **Music** — playful, escalating orchestral-comedic score that grows fuller and more epic with each tier — culminating in a grand cosmic theme.
- **Sound Effects** — exaggerated, comedic gulps, burps, and squelches. Swallowed objects retain **audible echoes** from inside the belly (a muffled car horn, a wailing siren, a barking dog) — a signature comedic touch.
- **Customizable Burp Sound Packs** — a lighthearted cosmetic hook and a driver of shareable moments.

### Character & Item Design Language

- **Readability First** — every swallowable object has a distinct silhouette and size so players instantly judge "can I eat this?"
- **Personality in Everything** — even background props have googly eyes or comedic reactions when nearly eaten, reinforcing the absurd, charming tone.
- **Legendary Swallows** get bespoke art and exaggerated "trophy" presentation in the Belly Trophy Room.

---

## Why It Will Work

The eat-and-grow genre has proven mass appeal (*Agar.io*, *Hole.io*, *Katamari*), but no browser title has combined it with **build-crafting depth**. *The Big Swallow* offers casual players an instantly understandable fantasy — *eat everything* — while giving mid-core players roguelike strategy through the living-stomach system. The comedic tone and auto-shareable absurd moments make it inherently viral, and the low-friction browser format ensures maximum reach.

*Bon appétit. The world looks delicious.*