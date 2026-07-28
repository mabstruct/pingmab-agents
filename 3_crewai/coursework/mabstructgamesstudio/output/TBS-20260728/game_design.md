# The Big Swallow
### *An Appetite at the End of Everything*

**Build target:** one `index.html`, one inline `<script>`, no external assets, no dependencies, no network calls.
**Design intent:** a 10–14 minute single-player run. Eat-and-grow, but *size is a liability* and *your fuel is your score*.

---

## 1. Game Title and Short Description

**The Big Swallow**

You are **the Maw** — a newborn absence in space that woke up hungry.

Hold the mouse to open a cone of suction and inhale anything smaller than your gape. Swallowing is instant; **digesting is not**. Everything you eat sits churning in your **Gut** as a physics-relevant payload, and the only way to move is to **belch some of it back out**. Every dodge spends food you already caught. Grow enough and the camera *Folds* — a hard zoom-out that turns your entire conquered playground into background dust and streams in a new, larger class of prey.

Something else out there is eating the same things you are, and it is also growing.

**Elevator line:** *Osmos with a digestive tract and a guilty conscience.*

---

## 2. Core Mechanics

### 2.1 The Maw (inhale)
- **Hold LMB** (or `Z` / `K`): a suction cone opens from the Maw's centre toward the cursor.
  - Cone half-angle `GAPE_ANGLE = 34°`, length `gapeRange = 5.5 * playerRadius`.
  - Force on a body inside the cone: `F = SUCK_K * (1 - d/range) * cos(offAngle)`, applied toward the Maw.
  - Newton's third law: the Maw receives `-F * (bodyMass / playerMass)`. **Big bodies are anchors** — inhale a moon to slingshot yourself toward it.
- **Swallow gate:** a body is swallowed when `dist < playerRadius * 0.85` **and** `body.radius <= playerRadius * GAPE_RATIO` (`GAPE_RATIO = 0.62`). Otherwise it jams at the lip, wobbles, and shoves you.
- **Void Charge:** inhaling drains `18/s` from a 100 pool. Regen `9/s` while inhaling-off, `22/s` while fully idle (no inhale, no belch, for 0.6s). At 0 charge the maw snaps shut with a wet clack and a 0.8s lockout.
- **Open maw = open wound:** while inhaling, incoming damage is **×2**. Eating is a commitment.

### 2.2 Belch Propulsion (movement)
- **RMB / Space / `X`**: eject the *oldest* undigested gut lump directly away from the cursor.
  - Impulse: `dv = EJECT_K * lumpMass / playerMass`, capped at `MAX_BELCH_DV`.
  - The lump becomes a real body in the world at `-dv * playerMass / lumpMass` velocity — it is **re-eatable**, and it can slam into and knock around bodies too big to swallow.
  - There is **no thrust key.** Zero gut = zero mobility. Running dry in front of The Other Mouth is the game's signature death.
- **Panic Eject** (double-tap belch, or `Shift`): dumps up to 4 lumps in one cone-shaped spray. Big burst, big loss.

### 2.3 The Gut (digestion queue)
- A visible ring of `gutSlots` lumps around the core (`base 6`, mutatable).
- Each lump carries `digestTime`, `massYield`, `essenceYield`, `hardness`. On completion: `mass += massYield`, `essence += essenceYield`, lump pops with a satisfying gulp-thud.
- **Fullness** `f = lumps / gutSlots`:
  - `f > 0.75` → **Indigestion**: hitbox inflates by up to `+22%`, steering damping drops (mushy), outline wobble frequency scales with `f`.
  - `f >= 1.0` → swallow attempts *fail* with a rejection burp. You cannot eat what you cannot fit.
  - Taking damage while `f > 0.75` → **Rupture**: lose 50% of gut contents as fast-moving debris, lose 12% mass, 1.2s stun.
- **Design payoff:** carrying a nearly-full gut is *optimal fuel management* and *maximum fragility* at the same time. The risk dial lives in the player's hands every second.

### 2.4 Scale Jumps (the Fold)
When `mass` crosses a tier threshold, the world **Folds**: 1.5s eased camera zoom-out, world radius grows, old bodies are demoted to parallax dust, a new archetype set streams in, audio swells and drops an octave.

| Tier | You Are | New Food | New Rule |
|---|---|---|---|
| **1. Motes** | a speck | dust, ice grains | inhale + belch basics |
| **2. Rubble** | a pebble-hole | asteroids, derelict probes, comets | debris physics, The Other Mouth appears |
| **3. Worlds** | a moon-hole | moons, ringed bodies | **gravity wells** bend everything |

Tier 3 ends the v1 run: reaching `TIER3_MASS_GOAL` triggers **The Full Stop** — a win-state Fold that zooms out one final time to reveal a single unswallowed mote (the Tier 4+ tease), then the run summary. NG+ carries one mutation.

### 2.5 Gravity Wells (Tier 3)
- Any body with `mass > WELL_MASS` becomes an attractor. **Hard cap 12 attractors**, recomputed on spawn/despawn, never per-frame discovered.
- `F = G * m / max(d², minD²)`, softened, no collisions between attractors.
- Wells make belching *cheaper* (fall in) and *escaping* expensive. They are also where The Other Mouth ambushes you.

### 2.6 The Other Mouth (antagonist)
A mirror entity: same rules, dumber brain, no gut-management skill. FSM:

- **WANDER** → drifts toward densest food cluster (spatial-hash bucket count).
- **STALK** → if `player.mass < self.mass * 1.15` and within 900u, closes with lead-prediction.
- **LUNGE** → 1.4s telegraph (jaw flare + rising tone) then a committed dash-inhale.
- **FLEE** → if `player.mass > self.mass * 1.25`, belches away in panic. **You can eat it** — largest single swallow in the game, worth 25% of its mass and 40 essence.
- It eats the same food you do and grows off it. Dawdling is punished by an arms race, not a timer.

### 2.7 The Palate (mutations)
On each Fold: pick **1 of 3** drawn from a pool of 6 (seeded draw, no repeats of owned).

| Mutation | Effect |
|---|---|
**Second Stomach** | `+3` gut slots
**Barbed Throat** | digest ×1.4 speed, belch thrust ×0.75
**Prehensile Lip** | cone angle ×1.3, range ×0.8
**Iron Lining** | rupture threshold 0.75 → 0.92, `-10%` void regen
**Retch Reflex** | one free Panic Eject per tier with `×2.2` thrust and no mass loss
**Sympathetic Ache** | bodies inside your cone pre-digest 30% before swallowing (shorter timers)

Pure data. Trivial to implement. Enormous perceived depth.

### 2.8 Health / Damage / Death
- No hit points bar. Damage = **mass loss + gut loss**. Sources: rupture, Other Mouth lunge (`-15%` mass), high-speed collision with an unswallowable body (`-6%` mass).
- **Death** = `mass < TIER_FLOOR[currentTier] * 0.5` → you collapse below your own tier and are **unmade**. Run summary, restart.
- **Recovery**: after any damage, 1.5s invulnerability, gut visually bruised, and 3 free "crumbs" spawn nearby so you are never mathematically stranded with an empty gut. *A stranded player must always be able to earn one belch.*

---

## 3. Art Direction

**Concept:** *bioluminescent negative space.* You are a hole that glows at the edges. Everything is drawn with code.

- **Palette:** near-black field `#05060b`; the Maw is a true-black disc ringed in hot violet `#b06cff` bleeding to cyan `#54e6ff` when inhaling. Food is warm — bone-white dust, pale blue ice, ochre asteroids, rust-green probes, comet white-blue tails, moons in dim clay tones. Danger is a single reserved colour: **arterial red `#ff3a54`**, used *only* for The Other Mouth's telegraph and rupture. Nothing else in the game is red.
- **Bodies:** seeded irregular polygons (`8–14` verts, radius jitter ±18%), one flat fill, one 1.5px lighter rim. Comets get a 6-segment tapered tail. Moons get a rim-light arc facing world-centre.
- **The Maw's body:** black core + wobbling outline. Outline is a closed spline whose radial offset is `sum of 3 sine terms` with amplitude and frequency driven by **gut fullness**. At `f=1` it visibly *pulsates like something about to be sick*. This single effect carries most of the game's character.
- **Gut ring:** lumps orbit the core at `1.35 * radius`, each a mini-copy of the thing you ate, shrinking and desaturating toward digestion. **The HUD is the body.**
- **Glow:** three pre-rendered radial-gradient sprites (small/med/large) on offscreen canvases, blitted with `globalAlpha` and `'lighter'`. **Never per-frame `shadowBlur`.**
- **Fold moment:** 1.5s `easeInOutQuart` zoom; a chromatic ring wipes outward; existing bodies get alpha-decayed into the parallax layer; the frame briefly desaturates to white-on-black and back. Budget real polish here — it is the game's single "wow" beat.
- **Parallax dust:** 3 layers, 240 points total, drawn as 1–2px rects at `0.15/0.35/0.6` scroll factors. Cheap and it sells scale.
- **Audio:** WebAudio only. Inhale = filtered brown noise whose lowpass cutoff tracks suction force. Swallow = short pitched sine thud, pitch inversely proportional to swallowed radius. Digest complete = soft marimba-ish blip. Belch = noise burst through a descending bandpass. Fold = 1.5s sine sweep down two octaves + reverb-ish delay tail. All synthesised; **AudioContext created only on first user gesture**, and the game is fully playable muted.

---

## 4. MVP Scope (shipping in v1)

1. **Full core loop**: cone inhale with third-law recoil, size-gated swallow, gut queue with per-lump digest timers, belch propulsion with momentum conservation, ejected lumps persisting as re-eatable world bodies.
2. **Three tiers** (Motes → Rubble → Worlds) with **two Folds** and a **third terminal Fold** (The Full Stop win state).
3. **Six object archetypes**: `dust, iceGrain, asteroid, probe, comet