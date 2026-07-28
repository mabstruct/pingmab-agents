# The Big Swallow
### *A Silent Film About the End of Everything*

---

## Short Idea Description

*The Big Swallow* is a single-player, one-screen cosmic arcade game in which **you are the mouth**. You don't run around eating things — you sit motionless at the centre of the void, aim an inhale-cone with your cursor, and drag the universe down your throat one order of magnitude at a time. Styled as a flickering 1901 trick film that has somehow kept running for thirteen billion years, it ends the only way it can: with you swallowing the camera, the interface, and the person watching.

---

## Core Idea & Key Mechanics

### The Central Twist: The Player Never Moves

Every "eat and grow" game (Agar.io, Tasty Planet, Hole.io) is a chase game — you steer a blob at prey. *The Big Swallow* inverts it. **The maw is fixed dead-centre and fills the screen edge.** Objects orbit, drift, and flee around you in a radial arena. You are a hungry singularity with a mouth, and the entire game is about *pulling* rather than *pursuing*. This makes it instantly readable, mouse-only, and mechanically distinct from the entire genre.

### 1. The Inhale Cone (hold LMB)

Cursor sets direction. Holding the left mouse button opens a **suction cone** — a widening wedge of pull force radiating from your maw. Objects inside it are dragged inward on curved, spiralling paths (pull force scales with `1/distance`, plus a tangential component so things swirl rather than beeline — vastly more satisfying and readable).

- Cone **width** and **strength** are inversely linked: a narrow cone is a laser-precise straw; a wide cone is a weak, greedy hoover. Scroll wheel or right-drag adjusts the tradeoff live.
- Inhaling drains **Breath**, a stamina bar. Run dry and your maw hangs open, gasping and defenceless, for ~1.5s.

### 2. The Exhale (release / RMB)

The anti-degenerate mechanic. If inhaling were free, the game would be "hold button, win." So:

- **Exhale** fires everything currently in your gullet-queue back out as a shotgun blast of debris.
- This is the *only* way to deal with **Unswallowables** — objects above your current mass tier that will crack your teeth (damage) if you try to force them down. You shatter them with spat debris, then eat the fragments.
- Creates the core combat rhythm: **inhale small → spit at big → eat the pieces.** Suction and expulsion, in and out. The whole game breathes.

### 3. Indigestion (the risk layer)

Not everything is food. Swallowing hazards — **Ice** (freezes your Breath regen), **Splinters** (bleed damage over time), **Mirrors** (invert your cursor for 5s), **Something That Screams** (temporarily reveals it was alive) — punishes indiscriminate hoovering. Late tiers mix hazards *inside* clusters of good food, forcing cone-narrowing precision.

### 4. The Swallow (scale jump — the money moment)

Fill the Gullet meter and the **SWALLOW** prompt appears. Trigger it and the game performs a hard cinematic beat:

> The screen convulses. The camera rips *backwards* through an order of magnitude. Everything you just spent 90 seconds eating collapses into a single speck. A silent-film intertitle card slams down: **"STILL HUNGRY."**

Then the new tier's objects fade in around your — now proportionally tiny — mouth. Because the camera is just a canvas transform, this "wow" moment is nearly free to implement and is the single most shareable thing in the game.

**The Seven Courses:**

| Tier | Arena | Diet |
|---|---|---|
| I | A Bedroom | Dust, moths, buttons, a wedding ring |
| II | A Seaside Town | Bicycles, gulls, lampposts, a brass band |
| III | The Weather | Clouds, aeroplanes, weather balloons, lightning |
| IV | Orbit | Satellites, moons, the ISS, a whale (unexplained) |
| V | The Local Star | Solar flares, comets, the Oort cloud |
| VI | The Galactic Arm | Nebulae, pulsars, dead civilisations' radio signals |
| VII | **The Observer** | The starfield, the HUD, the frame, the lens |

### 5. Gut Traits (light roguelite spine)

After each Swallow, pick **1 of 3** mutations drawn from what you ate most of:

- *Tidal Lung* — cone pull strength +30%, width −20%
- *Second Stomach* — hazards are neutralised but cost double Gullet space
- *Barbed Palate* — spat debris does 2× shatter damage
- *Slow Peristalsis* — Breath regen doubled, Gullet fills 25% slower
- *The Taste For It* — eating a live thing restores Breath fully (and dims the screen a little, permanently)

This turns a 10-minute run into a build, gives replay value, and is ~60 lines of data.

### 6. The Finale: Swallowing the Camera

Tier VII is the payload of the entire concept and a direct homage to Williamson's 1901 original, where a man walks up to the lens and eats the cameraman. Here, once the starfield is gone, the only remaining objects on screen are:

1. Your score counter
2. Your Breath bar
3. The vignette
4. The film grain
5. The black frame border itself

You inhale each one. They physically detach, tumble, spiral in, and vanish. The canvas goes to white. An intertitle: **"THE BIG SWALLOW."** Then the title card is eaten too, and the game returns to a menu that is now, subtly, missing something.

---

## MVP Features (must ship in v1)

Everything below is comfortably achievable in one self-contained HTML file, vanilla JS, 2D Canvas, zero dependencies.

- ✅ **Fixed-centre maw + mouse-aimed inhale cone** with radial pull physics (spiral tangential force)
- ✅ **Breath stamina** meter with drain/regen and gasp-punish state
- ✅ **Exhale/spit** debris shotgun
- ✅ **Mass tiers** — objects tagged edible / shatterable / hazardous relative to current tier
- ✅ **Gullet meter → Swallow scale-jump** with canvas zoom-out transition and intertitle card
- ✅ **4 tiers minimum** (Bedroom, Town, Orbit, The Observer) — ship the first, the middle, and *definitely* the finale; the finale is the whole pitch
- ✅ **Gut Traits** — 8–10 traits, pick 1 of 3 between tiers
- ✅ **Health** (teeth cracks) + fail state + restart in <1s
- ✅ **Full camera-swallowing finale** including HUD elements as physical eatable entities
- ✅ **Silent-film visual layer** — grain, vignette, frame judder, sepia/monochrome grade, intertitle cards
- ✅ **Score + "best run" via `localStorage`**, shareable end-card text
- ✅ **Mouse-only controls, no tutorial text** — a single intertitle reading *"OPEN WIDE"*

**Realistic scope:** ~1,800–2,500 lines of JS, all art drawn procedurally with canvas paths (silhouettes only — see visual direction). No sprite sheets, no asset loading, no build step.

---

## Stretch Features (defer without guilt)

- 🔶 **All 7 tiers** — each additional tier is just a data table of shapes + a palette, but they cost polish time. Ship 4, add 3.
- 🔶 **Procedural WebAudio** — see audio note below.
- 🔶 **"Living" prey AI** — objects that flee the cone, hide behind larger objects, or clump defensively. Big feel-upgrade, moderate cost.
- 🔶 **Boss courses** — one large multi-part entity per tier that must be dismantled limb by limb (e.g. the brass band conductor, a whale, a dying star that spits back).
- 🔶 **Endless "After" mode** unlocked post-finale, with escalating abstract geometry and a score chase.
- 🔶 ⚠️ **AMBITIOUS FOR ONE FILE:** true fluid/particulate suction (thousands of soft-body particles). Fake it — 300–500 cheap point particles with additive blending reads as fluid at 60fps. Do *not* attempt real SPH.
- 🔶 ⚠️ **AMBITIOUS:** breaking out of the canvas to eat the actual DOM/page. Gorgeous, very on-theme, but fragile across browsers. **MVP fakes it** by rendering a convincing browser-chrome frame *inside* the canvas and eating that instead. Nobody will