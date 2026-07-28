# The Big Swallow — Build Complete

**File written:** `output/The Big Swallow/index.html`
**Size:** 29,825 bytes (865 lines)
**Tier-0 validation:** ✅ **PASS** — `script_blocks=1`, `js_parse_ok=True`, `body_closes=1`, `html_closes=1`

Single inline `<script>`, inline CSS, zero external assets/network calls. Physics is `dt`-scaled and `update(dt)` is separated from `render()`.

---

## ✅ Implemented (MVP)

- **Core loop** — cone inhale (`GAPE_ANGLE 34°`, force `SUCK_K·(1−d/range)·cos(off)`) with **Newton's-third-law recoil** scaled by mass ratio; size-gated swallow (`GAPE_RATIO 0.62`, `dist < r·0.85`); lip-jam shove on too-big bodies.
- **The Gut** — visible orbiting lump ring, per-lump `digestTime`/`massYield`/`essenceYield`, fullness `f=lumps/slots` driving **Indigestion** (+22% hitbox, mushy damping, wobble frequency), full-gut swallow rejection, and **Rupture** on damage above threshold.
- **Belch propulsion** — ejects oldest lump away from cursor with momentum conservation; lump respawns as a real **re-eatable body**; **Panic Eject** (double-tap / Shift) sprays up to 4.
- **Void Charge** — 100 pool, `−18/s` inhale drain, tiered regen (9/22 idle), 0.8s lockout at empty; open-maw damage exposure.
- **Three tiers + two Folds + terminal Fold** — `easeInOutQuart` zoom, white desaturation flash, old bodies decayed into parallax dust, audio sweep, **The Full Stop** win state.
- **Six archetypes** — dust, iceGrain, asteroid, probe, comet (tapered tail), moon (rim-light arc).
- **The Other Mouth** — WANDER/STALK/LUNGE(1.4s telegraph)/FLEE FSM; eats & grows; edible when you outmass it (25% mass + 40 essence).
- **The Palate** — 1-of-3 seeded mutation draw from 6, all effects wired (slots, digest/thrust, cone, rupture/regen, retch, pre-digest).
- **Gravity wells** (Tier 3, 12-cap, recomputed on spawn), damage-as-mass-loss, death floor, invuln + **recovery crumbs** so you're never stranded.
- **Art/Audio** — wobbling spline Maw outline scaled by fullness, pre-rendered `'lighter'` glow sprites (no per-frame `shadowBlur`), 3-layer 240-point parallax, reserved arterial-red danger colour, and fully synthesised WebAudio (inhale noise, swallow thud, digest blip, belch burst, fold sweep) created only on first gesture.

## ⏳ Deferred (honest list)

- **Chromatic ring wipe** during Folds (simplified to the white desaturation flash).
- **Spatial hash** for Other Mouth cluster-seeking (currently a sampled centroid every 4th body — adequate at MVP density).
- **NG+ carry-one-mutation** and Tier 4+ "single unswallowed mote" reveal (win screen references it narratively only).
- **Reverb/delay tail** on the Fold sweep (dry sweep only).
- **Softened gravity `minD²` tuning & inter-well collision exclusion** are basic; wells don't yet make belching visibly "cheaper" beyond raw attraction.
- **Comet tail dynamics** are velocity-aligned static segments rather than trailing history.

The game is fully playable start-to-win/lose, muted or with audio.