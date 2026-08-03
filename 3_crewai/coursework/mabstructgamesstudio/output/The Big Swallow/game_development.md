# The Big Swallow — Build Complete

**Status:** `index.html` written successfully and **Tier-0 validation PASSED**.

- **Path:** `output/The Big Swallow/index.html`
- **Byte size:** `17,543 bytes` (574 lines)
- **Tier-0:** `PASS` — `script_blocks=1`, `js_parse_ok=True`, `body_closes=1`, `html_closes=1`
- **Architecture:** Exactly one inline `<script>`, vanilla JS, inline CSS, zero dependencies, `update(dt, state)` cleanly separated from `render(state)`, all physics multiplied by `dt` with a frame-gap clamp for frame-rate independence.

## Implemented (MVP)

- **The fixed Maw** — locked dead-centre at `(480,300)`, pulsing lip ring, flickering teeth, throat glow. Never translates (camera shake excepted).
- **Inhale Cone (hold LMB)** — cursor-aimed wedge with the spec's exact force model: `F = PULL_K * strength * (1/d) * falloff`, cosine falloff to zero at cone edge, plus tangential term so entities **spiral** rather than beeline.
- **Width ↔ Strength inverse link** — scroll wheel sets `coneWidth [18°,70°]`, `strength = 28/widthDeg` clamped `[0.4,1.6]`, live HUD readout. The game's single stat.
- **Breath economy** — `breathMax 100`, drain `26/s × strength`, `18/s` regen after `0.35s` grace, **GASP** punish at zero (1.4s locked maw, doubled judder, red overlay).
- **Exhale (RMB or LMB-release with loaded queue)** — 6-pellet shotgun at `900 px/s` with spread, costs 8 breath, shatters *big* multi-HP objects. Gullet is never reduced by exhaling.
- **Gullet + Swallow transition** — fill the gullet to trigger a white-flash zoom, the **"STILL HUNGRY"** intertitle, and fade into the next of **4 courses** (Bedroom → Seaside Town → Orbit → The Observer).
- **The finale** — completing the Observer course triggers a white-out and **THE END** title card ("You ate everything. Even this."), instant click-restart.
- **Silent-film presentation** — procedural sepia silhouettes, per-frame film grain, random scratch lines, vignette rings, letterbox bars, camera shake.
- **Arena management** — entities beyond `radius 760` are culled and respawned at the rim; the world never empties.

## Deferred (honest list)

- **Literally-edible UI in the finale** — the design's thesis (eating the score counter, breath bar, frame, and lens as physical entities) is represented narratively via the win card rather than as interactive edible HUD objects.
- **Distinct per-course entity behaviours & bespoke silhouettes** — kinds currently share a shared shape-set switch; no unique AI per course.
- **Mass-tier gating** ("what is food vs. not" via `playerMass`) — big objects require shattering, but full mass-comparison edibility rules are simplified.
- **Barbed Palate / upgrade modifiers** — debris fixed at 1 shatter damage.
- **Audio** — build is silent (matches the surreal silent-film tone, but no SFX layer).
- **Right-drag-vertical cone control** — only scroll-wheel width control is wired.