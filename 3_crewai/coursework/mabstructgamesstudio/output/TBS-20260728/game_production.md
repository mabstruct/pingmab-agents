# Production Report — *The Big Swallow*
### *An Appetite at the End of Everything*

**Report type:** Final Production Sign-off
**Producer:** Game Producer
**Pipeline covered:** Ideation → Design → Development → Testing → Deployment

---

## 1. Ship Status

**✅ SHIPPED — Live (Temporary Build)**

The game has cleared the automated test gate (`overall=pass`) and has been deployed to a live, publicly reachable URL. This report reflects the **reconciled, current ground truth** after a discrepancy between an earlier tester report and the deployment record was investigated and resolved directly with the Browser Game Tester (see Section 4, *Gate Reconciliation*).

**Live URL:** https://brisk-ritual-mqm6.here.now/
**Hosting status:** *Temporary anonymous playtest build — expires in 24 hours*
**Claim URL (to make permanent):** https://here.now/claim?slug=brisk-ritual-mqm6&token=44ea1538cb3444e7aaa80938cade5f241ef288ba4ff2b5e5f58b66177d0a4501
**Notification:** Telegram alert sent to studio lead with the live testing URL — confirmed sent.

---

## 2. Project Summary

**The Big Swallow** is a single-player, single-file (`index.html`, ~29.8 KB / 865 lines) browser game with zero external dependencies, zero image/audio assets, and zero network calls. Everything — visuals and sound — is procedurally generated at runtime (vector shapes, offscreen-rendered glow sprites, synthesised WebAudio).

**Elevator pitch:** *Osmos with a digestive tract and a guilty conscience.* You are the Maw, a hungry hole in space. You inhale objects smaller than yourself through a suction cone, but swallowing is instant while digestion is not — everything you eat sits in a visible Gut Queue as a physics-relevant payload, and the *only* way to move is to belch some of that payload back out. Fuel and score are the same resource. Grow enough mass and the camera "Folds," zooming out hard into a new, larger tier of prey — from dust motes to full moons — while a rival entity, The Other Mouth, competes with you for the same food and grows if you dawdle.

The design deliberately inverts the "eat-and-grow" genre's usual power fantasy (*Osmos*, *Tasty Planet*, *hole.io*): here, **bigger is a liability**, not an automatic win, and every dodge is paid for with food already caught.

---

## 3. Feature Scope: Implemented vs. Deferred

### 3.1 Implemented — MVP (Shipped)

| Area | Status |
|---|---|
| Core inhale mechanic | ✅ Cone suction (`GAPE_ANGLE 34°`), Newton's-third-law recoil scaled by mass ratio, size-gated swallow (`GAPE_RATIO 0.62`), lip-jam shove for oversized bodies |
| The Gut (digestion queue) | ✅ Visible orbiting lump ring, per-lump digest timers, mass/essence yield, fullness-driven Indigestion (hitbox bloat, mushy steering, wobble), full-gut rejection, Rupture on damage |
| Belch propulsion | ✅ Momentum-conserving ejection of oldest lump, re-eatable ejected debris, Panic Eject (up to 4 lumps) |
| Void Charge | ✅ 100-pool drain/regen system, empty-charge lockout, open-maw double-damage exposure |
| Scale Jumps / Folds | ✅ Three tiers (Motes → Rubble → Worlds), two mid-run Folds + one terminal "Full Stop" win-state Fold, eased zoom, desaturation flash, audio sweep |
| Object archetypes | ✅ All six: dust, ice grain, asteroid, probe, comet, moon |
| Antagonist — The Other Mouth | ✅ Full WANDER/STALK/LUNGE/FLEE state machine, grows by eating, edible when outmassed |
| The Palate (mutations) | ✅ 1-of-3 seeded draw from a pool of 6, all six effects wired |
| Gravity wells | ✅ Tier 3, capped at 12 attractors, recomputed on spawn |
| Damage / death / recovery | ✅ Mass-loss-as-damage, death floor, invulnerability window, guaranteed "recovery crumb" spawn so players are never stranded |
| Art direction | ✅ Wobbling spline outline scaled by gut fullness, pre-rendered `'lighter'`-blend glow sprites (no per-frame `shadowBlur`), 3-layer/240-point parallax, reserved arterial-red danger colour |
| Audio | ✅ Fully synthesised WebAudio (inhale noise, swallow thud, digest blip, belch burst, fold sweep), created only on first user gesture, game fully playable muted |
| Persistence | ✅ `localStorage` best-run tracking |
| Run summary | ✅ Mass consumed, largest swallow, time, tier reached, generated epitaph line |

### 3.2 Deferred — Explicitly Out of Scope for v1

These were cut consciously and are **not bugs**:

- **Tiers 4–6** (Furnaces, Spiral, The Last Course) and the **self-swallow ending** — the game currently ends at Tier 3 with a narrative tease of what's beyond, not the full "swallow yourself" finale from the original concept.
- **Heat/quench mechanic** for stars (Tier 4 feature, never reached in v1).
- **Boss: The Long Throat** (stretch scope, not started).
- **NG+ mutation carryover** — referenced narratively on the win screen but not functionally implemented.
- **Chromatic ring wipe** on Fold — simplified to a white desaturation flash.
- **Spatial hash grid** for The Other Mouth's target-seeking — currently uses a sampled centroid every 4th body; adequate at MVP object counts but not the originally spec'd optimisation.
- **Reverb/delay tail** on the Fold audio sweep — dry sweep only.
- **Gravity well tuning** (softened `minD²`, inter-well collision exclusion) — basic implementation; wells don't yet visibly make belching "cheaper" beyond raw attraction.
- **Comet tail dynamics** — static velocity-aligned segments rather than true trailing history.
- **Daily seeded run, shareable result strings, ghost replay** — stretch features, not attempted.

---

## 4. Gate Evidence & Reconciliation (Testing)

### 4.1 Why this section is unusually detailed

During compilation of this report, I identified a **direct contradiction** between two coworker deliverables:

- The **Browser Game Tester's** original report stated: `overall=FAIL`, `tier0=pass`, `tier1=fail` with a runtime error (`addEventListener is not defined`), and explicitly concluded the game "must not be considered playable" and must not ship.
- The **Browser Game Deployment Specialist's** report stated `game_testing.json overall=pass`, gate = `DEPLOY ALLOWED`, and had already shipped the build live.

I do not consider it acceptable to publish a production report with self-contradicting gate evidence, so I escalated directly:

1. I first asked the Deployment Specialist to re-verify the artifact. They confirmed the gate they acted on showed `overall=pass` at deploy time but could not independently re-inspect raw JSON fields (`tier0`/`tier1`/error text) from their vantage point.
2. I then went to the **source of truth** — the Browser Game Tester — and requested a fresh, current-state check of `output/The Big Swallow/game_testing.json`.

### 4.2 Reconciled ground truth (current, authoritative)

The Browser Game Tester re-ran the automated test suite and confirmed the **current** state of `game_testing.json`:

```text
overall = pass
artifact = output/The Big Swallow/game_testing.json
tier0 = pass
tier1 = pass
```

**Tier 0 — Parse / Structure:** ✅ **PASS**
Evidence: single inline `<script>` block, valid JS parse, matched `body`/`html` closing tags. (`script_blocks=1`, `js_parse_ok=True`, `body_closes=1`, `html_closes=1`.)

**Tier 1 — Boot Smoke:** ✅ **PASS** (previously FAIL, now fixed and re-verified)
The earlier blocking defect — a runtime load error, `addEventListener is not defined`, which prevented the game from booting during the automated smoke test — is **no longer present** in the current artifact. The Tester confirmed the current re-run shows Tier 1 passing with no boot failure. The Tester could not attest to *who* fixed the underlying code from the artifact alone, but confirmed the fix is reflected in the current passing state and that this is the version subsequently deployed.

**Conclusion of reconciliation:** The game was **not** shipped despite a failing test. The originally reported `tier1=fail` was a real, blocking defect at the time it was found; it was resolved prior to the deploy gate evaluating `overall=pass`, and deployment proceeded correctly under a passing gate. The earlier BLOCKED status is now superseded and should not be read as the current state of the shipped build.

### 4.3 What Tier 0 / Tier 1 automated checks DO verify

- The file parses as valid HTML/JS with correct structural closure (Tier 0).
- The game loads in the automated test harness without throwing a runtime error during initial boot (Tier 1).

### 4.4 What was explicitly **NOT verified** (known gap — carried forward openly)

The automated Tier 0/Tier 1 checks are a **boot-smoke and static-parse gate only**. The following were **not** verified by any test artifact, tester, or deployment step, and should not be assumed to work simply because the gate is green:

- **Visual "feel" / actual rendered output** — no verification that the procedural rendering (Maw wobble spline, glow sprites, parallax, Fold zoom transition, HUD-as-body gut ring) actually *looks* correct, readable, or performant on screen. Tier 1 confirms the game boots without throwing errors; it does not confirm pixels are correct or aesthetically functional.
- **Touch input** — the design explicitly targets mouse-only control with keyboard fallback; no touch/mobile input path was implemented or tested. This game should be assumed **desktop-only** until stated otherwise.
- **Real browser testing** — no evidence of manual or automated verification in an actual browser environment (Chrome/Firefox/Safari/Edge) was reported. The Tier 0/1 checks appear to run in an automated harness, not a live browser session with a human or scripted UI driver clicking, holding mouse buttons, or observing frame rate.
- **Gameplay interaction verification** — the Tester explicitly noted that the passing Tier 1 result confirms boot-without-crash only, and does **not** provide evidence that core interactions (holding LMB to inhale, RMB/Space belch, Fold transitions triggering correctly, The Other Mouth's FSM behaving as designed, mutation selection UI, win/loss screens) were exercised and observed to work.
- **Performance under load** — no confirmation of frame rate/stability at the design