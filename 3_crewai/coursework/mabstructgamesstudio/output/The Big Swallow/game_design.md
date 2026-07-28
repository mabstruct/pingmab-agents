# THE BIG SWALLOW
### *A Silent Film About the End of Everything*
**Design Document — v1.0 (build target: one `.html` file, one inline `<script>`, zero dependencies)**

---

## 1. Game Title & Short Description

**The Big Swallow** — a one-screen, mouse-only cosmic arcade game in which *you are the mouth*.

You never move. You sit dead-centre in a flickering 1901 trick film that has somehow kept running for thirteen billion years. Your cursor aims a **suction cone**; the universe spirals in and goes down your throat. When your gullet is full you **SWALLOW**, the camera tears backwards through an order of magnitude, an intertitle slams down reading **"STILL HUNGRY,"** and a bigger world fades in around your now-tiny mouth.

Four courses: **A Bedroom → A Seaside Town → Orbit → The Observer.** In the final course the only things left to eat are your own score counter, your own breath bar, the film grain, the frame, and the lens. You eat them. The screen goes white. Then you eat the title card.

Run length: **8–12 minutes.** Restart: **instant.** Controls: **left mouse, right mouse, scroll wheel.** Tutorial: **two words.**

---

## 2. Design Pillars

1. **You are the fixed point.** Every other eat-and-grow game is a chase. This one is a *pull*. The maw never leaves the centre of the screen. Readability is free; the genre-distinctness is free.
2. **The game breathes.** In and out are both verbs. Inhale is your economy, exhale is your weapon. A run should have an audible rhythm even in silence.
3. **Scale is the reward.** Not upgrades, not levels — **magnitude**. The Swallow transition is the money shot and must be the loudest thing in the build.
4. **The frame is edible.** The finale isn't an epilogue; it's the thesis. Everything the player has trusted as "UI" is revealed as food.
5. **Cheap and mean.** All art is procedural canvas paths. Silhouettes and two shades of sepia. If a feature needs an asset pipeline, it isn't in v1.

---

## 3. Core Mechanics

### 3.1 The Maw (fixed)
- Logical canvas: **960 × 600**, letterboxed and scaled to fit; all gameplay in logical units.
- Maw sits at `(480, 300)`. Base radius **46px**. It pulses open/closed with input state; it never translates (camera judder excepted).
- **Arena radius 640.** Entities that drift beyond `radius 760` are culled and respawned at the rim. The player can never "run out of world."

### 3.2 The Inhale Cone (hold LMB)
- Cursor angle = cone bearing. Holding LMB opens a wedge of pull force from the maw.
- Pull on an entity inside the cone:

```
d      = clamp(dist(maw, e), 60, 800)
F      = PULL_K * strength * (1 / d) * falloff(angleOffset)
radial     = -F                     // toward maw
tangential = +F * 0.35 * spinSign   // makes things spiral, not beeline
```
  `falloff()` is `cos(angleOffset / halfWidth * π/2)` — full force on axis, zero at the cone edge. This one line is what makes aiming feel like aiming.
- **Width ↔ Strength are inversely linked.** Scroll wheel (or right-drag vertically) sets `coneWidth` in `[18°, 70°]`; `strength = 28 / widthDeg`, clamped `[0.4, 1.6]`. A narrow cone is a precision straw. A wide cone is a weak, greedy hoover. **This is the game's only stat, and the player controls it live.**
- Entities that touch the maw disc are **consumed**: score += value, gullet += gulletValue, and one **pellet** is pushed to the gullet-queue.

### 3.3 Breath (stamina + the gasp punish)
- `breathMax = 100`. Inhaling drains `26/s × strength`. Idle regen `18/s` after a `0.35s` grace delay.
- Hit zero → **GASP**: maw hangs open, inhale locked, pull force 0, incoming damage ×1.5, for **1.4s**. Screen film-judder amplitude doubles. This is the only "you are vulnerable" window in the game and it is entirely self-inflicted.

### 3.4 The Exhale (RMB, or LMB-release with a loaded queue)
- Gullet-queue holds up to **6 pellets**. Exhale fires them as a shotgun: 6 debris projectiles, `900 px/s`, `±14°` spread, along the cursor bearing. Costs **8 Breath**.
- Debris deals **1 shatter damage** per hit (2 with *Barbed Palate*).
- Exhaling **does not** reduce the Gullet meter (progress is never punished) — it only empties the ammo queue. Pellets refill by eating.

### 3.5 Mass Tiers — what is food and what is not
Player has `playerMass`, starting at `1.0` for each tier and rising to **1