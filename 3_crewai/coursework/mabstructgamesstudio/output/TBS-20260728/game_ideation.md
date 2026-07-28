# The Big Swallow
### *An Appetite at the End of Everything*

---

## Short Idea Description

You are **the Maw** — a newborn absence in space that woke up hungry. Inhale everything smaller than you, digest it into mass, and belch out the leftovers to propel yourself through a universe that keeps zooming out as you grow, from dust motes to galactic superclusters. The twist: *swallowing is instant, but digesting is not* — your gut is a physics-affecting payload of half-eaten matter, and the only way to move is to spit some of it back out.

---

## Core Idea & Key Mechanics

The genre baseline is the "eat-and-grow" lineage (*Osmos*, *Tasty Planet*, *hole.io*), but those games are frictionless power fantasies: bigger is always strictly better. **The Big Swallow** makes size a *liability you have to manage* and turns eating into a resource-economy puzzle wrapped in a cosmic body-horror comedy.

### 1. The Maw (inhale, not collide)
You don't ram into food. You **hold the mouse button to open your maw**, creating a cone-shaped suction field aimed at the cursor. Objects inside the cone are pulled toward you and swallowed if their radius is below your **gape threshold**. Bigger objects get tugged, wobble, and *pull you back* (Newton's third law) — you can use them as anchors.

- Inhaling drains **Void Charge** (regenerates slowly, faster while idle).
- Open maw = **open wound**: while inhaling you take double damage from grazing hazards. Eating is a commitment.

### 2. Belch Propulsion (movement costs digestion)
There is no thrust key. You move by **ejecting swallowed matter out the back** (right-click / spacebar, direction = away from cursor). Every dodge, every course correction, spends food you already caught. This is the game's central tension: *the fuel and the score are the same substance.*

- Ejected chunks remain in the world as physical debris — they can be re-eaten, or used as projectiles to knock bigger bodies around.

### 3. The Gut (digestion queue)
Swallowed objects don't become mass instantly. They enter a visible **Gut Queue** — a churning ring around your body core showing 6–10 lumps.

- Each lump digests on a timer → converts to permanent **Mass** (size) + **Essence** (mutation currency).
- Hard things (rock, metal, frozen cores) digest slowly. Soft things (gas, plasma, organics) digest fast but yield less.
- **Overfull gut** → *Indigestion*: your hitbox visibly bloats and destabilises, steering becomes mushy and laggy, and you take **rupture damage** if hit, spraying half your gut into space.
- Deliberately staying slightly full is optimal (fuel on hand), staying stuffed is a death sentence. Risk dial in the player's hands at all times.

### 4. Scale Jumps
When Mass crosses a tier threshold, the camera performs a **Fold** — a hard, gorgeous zoom-out where everything you spent five minutes conquering shrinks into background dust, and a new class of objects streams in. Each tier reskins physics and threat model:

| Tier | You Are | Food | New Rule Introduced |
|---|---|---|---|
| 1. **Motes** | A speck | dust, ice grains, micro-debris | inhale + belch basics |
| 2. **Rubble** | A pebble-hole | asteroids, wrecked probes, comets | debris physics, first hazard |
| 3. **Worlds** | A moon-hole | moons, planets, rings | **gravity wells** bend your path |
| 4. **Furnaces** | A star-hole | stars, pulsars, nebulae | **heat** — stars must be quenched with comets before swallowing, or they burn your gut |
| 5. **Spiral** | A galaxy-hole | star clusters, galactic arms | **the Rival** hunts you seriously |
| 6. **The Last Course** | Everything | the void itself | there is nothing left but you |

### 5. The Palate (light roguelite)
After each Fold, spend Essence to pick **1 of 3 mutations**. Surreal, organ-themed, stackable:

- **Second Stomach** — +3 gut slots.
- **Barbed Throat** — swallowed objects digest 40% faster but ejection loses 25% thrust.
- **Prehensile Lip** — suction cone is 30% wider but 20% shorter.
- **Cold Palate** — stars can be swallowed lukewarm.
- **Retch Reflex** — one free full-gut panic-eject per tier, huge thrust burst.
- **Sympathetic Ache** — you slowly digest nearby objects you *haven't* eaten yet, pre-softening them.

### 6. The Ending (the actual hook)
At Tier 6 there is no food left in the universe. The only object with mass still on screen is **you**. The suction cone will lock onto your own body. The final action of the game is to **swallow yourself** — the screen inverts, the gut queue empties one last time, and a single mote appears in the black, hungry, and the run count ticks to 2. *NG+ carries one mutation forward.*

---

## MVP Features (must ship in v1)

Single `index.html`, zero dependencies, zero assets, everything procedurally drawn and procedurally sounded.

1. **Core loop, fully playable**: inhale cone, size-gated swallowing, gut queue with per-object digest timers, belch propulsion with real momentum conservation.
2. **Three tiers** (Motes → Rubble → Worlds) with two Fold transitions. Three tiers is enough to prove the escalation fantasy.
3. **Six object archetypes** — dust, ice grain, asteroid, derelict probe, comet, moon — differing in radius, hardness, digest time, and Essence yield.
4. **Indigestion + rupture system** with clear visual bloat feedback (the body deforms, the outline wobbles at a frequency tied to fullness).
5. **Gravity wells** from any body above a mass threshold — a small, capped set (≤12 attractors) so the math stays cheap.
6. **One antagonist: The Other Mouth** — a mirror-entity with simple state-machine AI (wander → stalk → lunge → flee-when-outmassed). It eats the same food you do, so it grows if you dawdle. One enemy type, executed well, is worth more than five shallow ones.
7. **Palate mutation screen** — 3 offered from a pool of 6, chosen at each Fold. Pure data, trivial to implement, massive perceived depth.
8. **Fold transition**: 1.5s eased camera zoom + world respawn + a hard audio swell. This is the single most important "wow" beat — budget real polish time here.
9. **Run summary**: mass consumed, largest single swallow, time, tier reached, one-line generated epitaph ("*You ate 4,102 things and were still hungry.*").
10. **Mouse-only control** with keyboard fallback. Pause on blur/tab-out.
11. **Procedural vector rendering**: no image files. Bodies are polygons/circles with seeded irregularity; glow via **pre-rendered radial-gradient sprites on offscreen canvases** (never per-frame `shadowBlur` — that's the classic canvas framerate killer).
12. **Performance discipline**: fixed-timestep accumulator with `requestAnimationFrame`, object pooling (zero allocation in the hot loop), a spatial hash grid for suction/collision queries, hard cap ~600 active bodies with distance-culled "background dust" rendered as a cheap parallax layer.
13. **localStorage**: best run + NG+ mutation carryover.

---

## Stretch Features (defer without guilt)

- **Tiers 4–6** (stars, galaxies, the self-swallow ending). *The ending is the best idea in the doc and should be the very first stretch item promoted if there's time.*
- **Heat/quench mechanic** for stars.
- **Boss: The Long Throat** — a segmented tube-entity you must eat from the tail forward.
- **Daily seeded run** + shareable result string (no server: encode the seed and score into the URL hash).
- **Ghost replay** of your best run drifting in the background.
- **Generative ad