# THE BIG SWALLOW

*Devourer's Appetite Edition — Game Design Document*

---

## 1. Game Title

**THE BIG SWALLOW**

*(Marketing subtitle: "Feed the God That Ate a Galaxy")*

---

## 2. Short Idea Description

You don't control the monster — you control the menu. A colossal cosmic mouth called **the Devourer** drifts through a living galaxy with its jaws open and its patience thinning, and you reach into spacetime to slingshot stars, planets, and moons into its throat — or fling them to safety — to satisfy its ever-shifting cravings before it loses patience and swallows *everything*. It's *Angry Birds* meets orbital mechanics meets cosmic horror-comedy: bite-sized, endlessly replayable, and dripping with surreal flavor text about a god who is, frankly, a very picky eater.

---

## 3. Core Idea

**The Big Swallow** deliberately flips the predator/prey perspective of the studio's earlier singularity game (*Event Horizon*): instead of *being* the void, you play **fate itself** — the unseen hand of gravity deciding what falls into the abyss and what escapes it.

Each level presents a living starfield and a drifting Devourer mouth accompanied by a **Craving Card**: a short, absurd, specific order such as *"3 Blue Giants, 0 Inhabited Worlds"* or *"1 Gas Giant, No Rogue Moons."* Using **click-drag-release slingshot aiming**, you fling celestial bodies through a field of pre-existing gravity wells, curving and bouncing them either **into the Devourer's mouth** (to feed it exactly what it wants) or **out of the play field** (to protect worlds it must never eat). A **Patience Meter** constantly drains — let it empty and the Devourer **rage-swallows the whole level** (instant fail, delivered with dark comic flair).

Precision and restraint are rewarded far more than brute force: the best players clear a level with a single perfect throw and a fat *"NO COLLATERAL"* bonus. The tone sits at the intersection of **cosmic dread and dry cosmic comedy** — the Devourer speaks only through grunts, belches, and one-line surreal after-dinner memories (*"it tasted like a marriage that never happened"*). The galaxy is gorgeous and procedurally alive, but you are, gently, feeding a god. That's a little horrifying — and that's the hook.

---

## 4. Game Mechanics & Features

### 4.1 Core Loop

```
LOOK at Craving Card  →  AIM (drag from a body)  →  RELEASE (slingshot launch)
   →  WATCH physics resolve (gravity wells bend the arc)
   →  BODY enters Mouth (fed) / exits field (protected) / collides (wasted)
   →  Craving checklist updates  →  repeat until Craving fulfilled OR Patience = 0
   →  RESOLVE (win: score + star rating; lose: rage-swallow cutscene)
   →  INSTANT RETRY or advance to next level
```

Target level length: **20–45 seconds.** Failure must always feel like "one more try" — instant restart, zero load time.

### 4.2 Controls (single input, mouse/touch parity)

- **Click + hold** on any eligible body → enters **Aim Mode**.
- **Drag** → a live **dotted predictive arc** (a "gravity ghost trail") simulates the slingshot; pull-back distance = stored force, launched opposite the drag vector (Angry-Birds inverse).
- **Release** → body launches, immediately affected by every gravity well and the Devourer's own mass-pull.
- **Right-click / two-finger tap** → cancel aim without launching.
- **Spacebar / on-screen button** → activate **Slow-Swallow** (bullet time) when charged.
- No other inputs — one-mechanic purity is intentional; depth comes from level layout, not input complexity.

### 4.3 Celestial Body Types (The "Menu")

| Body | Flight Behavior | Feeding Value | Notes |
|---|---|---|---|
| **Blue Giant / Star** | Standard mass & drag | High — most Cravings want these | Slight self-gravity tugs nearby small bodies |
| **Red Dwarf** | Light, drifts easily | Low filler | Cheap "practice" body, tutorial-friendly |
| **Gas Giant** | **Bouncy** — ricochets off wells & edges | Medium, situational | Ideal for trick-shots and multi-body chains |
| **Rogue Moon** | Inert **blocker** | Zero (do not feed) | Can be flung at other bodies for billiard redirects |
| **Inhabited World** | **Fragile — NEVER feed** | Negative / instant Craving fail if eaten | The moral center: protection matters as much as predation |
| **Anomaly / Comet** (Sector 3+) | Erratic wobble, trajectory modifier | Wildcard | Splits/alters Craving requirements |

### 4.4 Gravity Wells & Physics

- **N-body-lite:** each level defines **0–4 fixed gravity wells** (dead stars, dense nebulae) using clamped inverse-square falloff (`F = G * mass / distance²`). Full N-body is intentionally avoided — puzzles must be solvable, not chaotic.
- **The Devourer is itself a gravity well** — near-misses often still get swallowed, creating tense "oh no—actually, yes!" moments.
- **Predictive arc** recalculated each frame via lightweight forward-Euler integration (8–12 sample steps) for honest, fair previews.
- **Collisions:** bodies can strike each other (billiard redirection), bounce off the soft boundary, or exit the frame (removed = "protected" if intended, "wasted" if needed).

### 4.5 The Craving Card System

- Level opens with the Devourer *inhaling* and a **Craving Card** (tarot-style ornate border) listing 1–3 conditions, e.g. `EAT: 2× Blue Giant` / `PROTECT: 1× Inhabited World` / `AVOID: 0× Rogue Moon`.
- **Live checklist HUD** ticks conditions off as fulfilled.
- **Overfeeding:** lowers star rating in early sectors; **hard-fails** from Sector 3 onward (*"The Devourer wanted exactly three. It is offended."*).
- Late Cravings get compound/logic-based (*"Eat 3 Stars, but never two in a row"* / *"Protect both worlds AND feed 2 Giants within 15s"*).

### 4.6 Patience Meter & Slow-Swallow

- A pulsing throat-styled bar drains from level start; **accelerates on hesitation**, **pauses briefly on every correct feed** — rewarding decisive play.
- **Empty = Rage-Swallow:** full-screen event where the mouth's rings expand and consume the entire field (protected worlds included), with a deadpan comic "burp caption."
- **Slow-Swallow (bullet time):** each clean, waste-free correct feed banks +1 charge (max 3). Spending one triggers **3 seconds of 30%-speed time** for threading gravity gauntlets or lining up bank shots — the game's core skill-expression currency (clean feeds → bullet time → harder shots → more clean feeds).

### 4.7 Scoring & Star Rating (0–3 Stars)

| Criterion | Weight | Detail |
|---|---|---|
| **Efficiency** | 40% | Fewer throws vs. the level's par count |
| **Speed** | 25% | Patience remaining at completion |
| **No-Collateral** | 25% | Zero worlds harmed, zero forbidden feeds |
| **Style** | 10% | Billiard redirects, gravity trick-shots, Slow-Swallow saves |

- A meta-currency **Cosmic Appetite Score** accumulates across levels, unlocking cosmetic mouth skins, nebula backdrops, and no-fail **"Digestif" bonus levels** (relaxed trick-shot practice).
- Post-level, the Devourer delivers a **surreal belch of memory** tied to what it ate (*"Ahh. Tastes like the first thing that ever burned."*) — pure tone/lore texture with strong replay charm.

### 4.8 Level Structure & Difficulty Curve

**Sectors** of **12 levels each**, themed by galactic region:

1. **The Nursery** — tutorial: single-condition Cravings, no gravity wells; teaches aim/release/feed.
2. **The Drift** — introduces gravity wells and Gas Giant bounce.
3. **The Grove of Living Worlds** — introduces Inhabited World protection and hard-fail overfeeding.
4. **The Boneyard** — Rogue Moon billiard puzzles, dense obstacle fields.
5. **The Deep Craving** — compound logic Cravings, multiple gravity wells, comets, and tight Patience windows.

Difficulty scales along four independent axes: **more bodies**, **tighter Cravings**, **more/stronger gravity wells**, and **shorter Patience** — mixed and matched so no two sectors feel like linear number-tuning.

### 4.9 Win / Lose Conditions

- **Win:** Craving Card fully satisfied (all EAT/PROTECT/AVOID conditions met) before Patience empties → results screen with star rating and memory belch.
- **Lose:** Patience hits zero (Rage-Swallow), an Inhabited World is destroyed/eaten, or a hard-fail Craving violation occurs → comic fail caption → instant retry.

---

## 5. Game Art & Design

### 5.1 Visual Identity

Painterly cosmic minimalism — **gorgeous but readable.** Every element is procedurally drawn on Canvas (no image assets). The galaxy feels alive and beautiful, which makes the act of feeding it to a mouth quietly unsettling: *beauty as bait.*

### 5.2 Color Palette

- **Deep space backdrop:** near-black indigo `#0a0a1e` → violet `#1a1040` gradient, with layered parallax nebula clouds in **teal, magenta, and amber** (soft additive-blended radial gradients + Perlin-noise wisps).
- **The Devourer:** a void-black mouth ringed by pulsing concentric rings shifting from **deep crimson `#6b0f1a`** at the rim to a searing hot **white-orange throat** in the center; a jagged, procedurally generated **toothy rim** silhouetted in black.
- **Bodies:** each type has a distinct hue for instant readability — Blue Giants (`#5ec8ff` cores), Red Dwarfs (dim ember `#c0392b`), Gas Giants (banded amber/ochre), Rogue Moons (desaturated grey), Inhabited Worlds (blue-green marbles with warm glowing city-light specks).
- **UI accents:** warm parchment/gold for Craving Cards; a wet, organic red-pink for the Patience/throat meter.

### 5.3 Procedural Visual Techniques

- **Stars & bodies:** radial gradients for glow; layered core + corona + flicker particles; Gas Giant bands via stacked clipped arcs with sine-offset colors.
- **Nebulae:** multiple large, slow-drifting semi-transparent radial gradients + noise for depth and parallax.
- **The Mouth:** animated concentric rings modulated by a sine wave (breathing), with the toothy rim generated once per level from a jagged polar function.
- **Predictive arc:** dotted trajectory line with fading opacity along its length.
- **Particles:** launch sparks, absorption swirls sucked into the mouth on a feed, and a full-screen ring-shockwave on Rage-Swallow.

### 5.4 Animation & Juice

- **Sling