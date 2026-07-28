# The Big Swallow
### *Event Horizon Appetite* — "A Beautiful Monster Racing Its Own Death."

**Game Design Document — v1.0 (Production-Facing)**
**Platform:** Single self-contained `index.html` (HTML5 Canvas + vanilla JS + WebAudio). No build step, no server, no dependencies. Desktop + touch. One-input control scheme.

---

## 1. Game Title

**The Big Swallow**
Subtitle / tagline options (interchangeable in marketing and title screen):
- *Event Horizon Appetite*
- *A Beautiful Monster Racing Its Own Death.*

---

## 2. Short Idea Description

You **are** a newborn black hole adrift in an infinite procedural cosmos. Devour everything smaller than you — dust, asteroids, moons, planets, stars — to grow, while a relentless Hawking-radiation decay shrinks you every second. Keep eating or dissipate into nothing; grow large enough to swallow the Galactic Core and win.

---

## 3. Core Idea

The Big Swallow takes the beloved eat-and-grow arcade loop (Agar.io, Hole.io) and injects a single transformative twist: **self-destruction pressure.** You are *always shrinking*. Growth is never safe. This turns a casual snack-and-grow genre into a desperate, elegant race against entropy.

The emotional fantasy is contradiction: you are an **unstoppable devourer that is nonetheless doomed.** Every gulp is a stay of execution. The player is a beautiful monster — vast, gravitational, terrifying — and yet fragile, leaking itself into the void with each passing second. Winning is not "surviving forever"; it is **reaching escape velocity from your own mortality** by growing large enough to consume the Galactic Core before decay claims you.

**Design pillars:**

1. **Haunting, not stressful.** Tension comes from a slow, readable decay clock, not from twitch reflexes.
2. **Weighty, readable growth.** Every size increase must *feel* massive and be *instantly legible* at a glance.
3. **Positioning over aim.** Softened gravity rewards smart movement and setup, not pixel-perfect cursor work.
4. **Elegant minimalism.** One input, a clean HUD, and a cosmic art language that carries the mood.
5. **Cosmic melancholy.** The audiovisual identity is beautiful, vast, and slightly mournful.

---

## 4. Game Mechanics & Features

### 4.1 Control Scheme (One Input)

- **Desktop:** The black hole continuously **drifts toward the mouse cursor.** No clicking required for movement.
- **Touch:** The black hole drifts toward the last touch/finger position.
- **No other inputs during play.** Pause is handled via a UI button or `Esc` / tap-out.
- Movement is **acceleration-based**, not instant snapping:
  - Player applies an acceleration vector toward the cursor.
  - `accel = clamp(cursorDir * ACCEL_BASE, maxAccel)`.
  - Velocity is damped each frame: `vel *= DRAG` (DRAG ≈ 0.92 per frame at 60fps).
  - **Larger holes accelerate more slowly** (inertia scales with mass): `ACCEL_BASE = k / (radius^0.5)`. This makes big holes feel majestic and ponderous, small holes feel nimble.

**Tuning targets:**

| Size class | Approx. max drift speed | Turn feel |
|---|---|---|
| Newborn (dust-eater) | Fast, darty | Snappy |
| Planet-eater | Medium | Smooth, slight glide |
| Star-eater | Slow, glacial | Long momentum tails |

### 4.2 Core Loop

1. **Locate** edible objects (green ring).
2. **Position** so softened gravity funnels them into you.
3. **Swallow** — object spirals in, mass added, audio whoomp, decay clock buys back time.
4. **Grow** — radius increases, new tiers become edible, new threats become relevant.
5. **Manage decay** — never stop eating; the Event Horizon Stability bar is always draining.
6. **Escalate** toward the Galactic Core win condition, avoiding rival black holes.

The loop is a **treadmill of entropy**: standing still = death.

### 4.3 Mass, Radius & Scaling

- **Mass is the true stat.** Everything derives from it.
- **Radius uses cube-root scaling** to mimic real volume→radius and to keep growth readable and weighty:
  `radius = R_MIN + K_RADIUS * (mass)^(1/3)`
- Early growth *looks* dramatic (small numbers, big visible jumps) while late growth *feels* earned (huge mass, gently increasing radius). It prevents the screen-filling blob problem of pure linear scaling.
- **Camera zoom** dynamically pulls out as radius grows so the player always occupies a comfortable fraction (~12–18%) of the viewport. Zoom is eased (`lerp`, ~0.06/frame) to avoid nausea.

**Mass units:** displayed in **solar masses (M☉)**, starting well below 1 (e.g. `0.000003 M☉` at birth). Internally store a raw float; display with adaptive units:
- `< 0.001` → scientific / micro notation
- `0.001 – 1` → 3 decimals
- `1 – 1000` → 1 decimal
- `> 1000` → thousands with suffix toward 100,000

### 4.4 Object Tiers

Everything in the cosmos has a mass and a tier. **You can eat anything whose mass ≤ your mass** (EAT_RATIO ≈ 1.0). Anything *larger* is a threat or inert-until-you-grow.

| Tier | Object | Relative mass (M☉, illustrative) | Behavior | Visual |
|---|---|---|---|---|
| 0 | **Cosmic dust / debris** | 1e-9 – 1e-6 | Drifts, plentiful | Tiny specks, faint |
| 1 | **Asteroid** | 1e-6 – 1e-4 | Slow drift, clustered fields | Irregular gray rocks |
| 2 | **Comet** | 1e-4 – 1e-3 | Fast trajectories, ion tail | Bright head + streaming tail |
| 3 | **Moon** | 1e-3 – 1e-2 | Orbits planets | Cratered spheres |
| 4 | **Planet (rocky)** | 1e-2 – 1 | Slow orbit | Textured colored spheres |
| 5 | **Gas giant** | 1 – 30 | Slow, large | Banded, stormy, rings |
| 6 | **Star (main sequence)** | 30 – 3,000 | Radiates light | Bright, bloom, corona |
| 7 | **Neutron star / pulsar** | 3,000 – 20,000 | Fast spin, sweeping beam | Tiny, blinding, beam |
| 8 | **Rival black hole** | Dynamic (AI) | Hunts/flees, grows too | Dark lens + accretion glow |
| 9 | **Galactic Core** | 100,000 (win target) | Static, guarded, radiant | Colossal luminous maelstrom |

**Object spawning:** Procedural, density-based around the player using a chunked/hashed grid so the world feels infinite. Spawn distribution shifts with player mass:
- Small player → dust/asteroid/comet dense; occasional distant giant as "aspiration."
- Growing player → moons/planets increase, dust culled to reduce clutter and CPU.
- Large player → stars/neutron stars/rivals become staple; small debris fades to background parallax.

**Object budget (perf):** Cap active gravitationally-simulated objects at ~250–400 (desktop) / ~150–200 (mobile). Distant objects are background parallax sprites only (no physics).

### 4.5 Targeting Feedback — The Green/Red Ring

The single most important readability feature.

- Every nearby object within a "consideration radius" gets a **thin outline ring**:
  - **Green ring** = *edible* (object mass ≤ your mass). Subtle inward-pulse invites you.
  - **Red ring** = *danger / inedible* (object mass > your mass). If it's a rival black hole large enough to eat YOU, ring is **bold, pulsing red** with a faint warning vignette on approach.
- Rings fade with distance; only render near the player and cursor path to avoid clutter.
- **Threshold objects** (mass within ±5% of yours) get a **flickering green↔yellow** ring: "risky but doable."

Color = instant intent; the player never needs to read numbers to decide.

### 4.6 Softened Gravity (Positioning over Twitch)

The player exerts a gentle gravitational pull on nearby smaller objects.

- Only objects within `gravityReach = radius * GRAV_REACH_MULT` (≈ 6–9× your radius) are pulled.
- Force uses a **softened (Plummer) kernel** to avoid singularities and jitter:
  `F = G_soft * playerMass * objMass / (dist² + softening²)` with `softening ≈ radius * 0.5`.
- Only **edible** objects are pulled meaningfully; larger objects are unaffected.
- Effect: you learn to **swing wide and let clusters funnel in**, combing asteroid fields gracefully.
- **Absorption trigger:** an object is swallowed when its center crosses your event-horizon radius (`dist < radius`), then does a fast **spiral-in animation** (~0.25–0.4s) before mass is credited.

### 4.7 Hawking-Radiation Decay — The Survival Clock

The signature mechanic. You are **always losing mass.**

- Decay is **sublinear** (smaller holes decay proportionally faster — mirroring real physics and giving great game feel):
  `decayPerSecond = DECAY_K / (mass^DECAY_EXP)` with `DECAY_EXP ≈ 0.5`.
- At low mass, decay is a real hourglass; at high mass, a slow ominous bleed that only bites if you stop eating.
- **A single decent meal always outpaces several seconds of decay** — eating is always progress, idling is always death.

**Event Horizon Stability bar (the decay clock as UI):**
- Shows "time until dissipation at current decay rate if you eat nothing": `stabilitySeconds = mass / decayPerSecond`.
- Bar fills (greens/blues) after a meal, drains toward empty (fragile whites/reds) as you starve.
- **Death threshold:** if `mass < MASS_MIN` (e.g. 1e-9 M☉), you dissipate — a quiet "puff into radiation" animation, game over.

**Decay grace / early-safe window (onboarding):**
- First **12 seconds:** decay disabled (grace).
- 12–30s: decay ramps 0% → 100% via smoothstep.
- After 30s: full decay.

### 4.8 Rival Black Holes (Moving Threat)

- AI-controlled black holes that also eat and grow.
- They can eat **you** if larger; you can eat **them** if larger — high-value meals.
- **Decision hysteresis** prevents jitter: rivals commit cleanly to HUNT (you're smaller) or FLEE (you're bigger) states, with a dead-band buffer so near-equal masses don't cause them to flicker between behaviors.
- Behaviors: HUNT (pursue player), FLEE (evade), FEED (chase easy clusters when player is far), WANDER.
- Rivals also decay, and can dissipate on their own — the cosmos is dog-eat-dog.

### 4.9 Difficulty Curve

- **Early (0–30s):** grace window, dust/asteroid abundance, gentle onboarding.
- **Mid:** decay