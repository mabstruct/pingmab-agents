# THE BIG SWALLOW: EVENT HORIZON — Production Complete 🌌

The new browser game **The Big Swallow** has been fully produced, tested, refined, and **deployed live**.

---

## 🚀 Deployment

- **Live URL:** https://serene-plume-3bmp.here.now/
- **Claim URL:** https://here.now/claim?slug=serene-plume-3bmp&token=869f7ac93321d1fdac1f7838ab97265f457f22d0b3d61113cb37556b2d75f136
- **Source file:** `output/The Big Swallow/index.html` *(single self-contained file — no external assets or libraries)*
- **Build type:** Temporary playtest build (expires in 24 hours)
- A Telegram notification was sent to the studio lead.

---

## 🎮 The Game

**The Big Swallow: Event Horizon** is a surreal, single-player cosmic arcade game. You are a *newborn singularity* adrift in a pocket universe. You swallow everything smaller than you and grow — while your ever-expanding gravity well visibly warps the space around you.

### Core Fantasy & Twist
The signature mechanic is the **Instability Meter** — feeding too greedily and too fast destabilizes your singularity, and at 100% you **collapse**. This fixes the #1 flaw of the entire "black-hole eating" genre (no real challenge or lose state) and gives the game a genuine skill ceiling.

---

## 🧭 Production Journey

1. **Creative Strategy** — Commissioned four distinct concepts. Selected **Event Horizon** for being the most on-title, immediately satisfying, and mechanically differentiated via the instability twist.
2. **Design** — Produced a full GDD: momentum-based mouse steering, 6 mass tiers + Galactic Core, gravity-radius scaling (`60·mass^0.42`), instability formulas, vent mechanic, scoring, procedural cosmic visuals, HUD, and difficulty pacing.
3. **Development** — Built as a single self-contained `index.html` (Canvas + inline JS, procedural everything), written via the Write tool and passing verification.
4. **Testing** — QA returned a **PASS with no critical blockers**, flagging polish items.
5. **Refinement** — Applied all polish fixes:
   - Instability explanation + floating `+INSTABILITY` / `VENTING` / `CRITICAL!` feedback
   - Edible-vs-dangerous rim outlines on nearby objects
   - Stronger critical-state HUD glow & warnings
   - Endgame movement boost + "final resonance" pull for a climactic Core chase
   - "Ascension field" object spawns to eliminate dead moments after tiering up
   - `localStorage` mute persistence
6. **Deployment** — Shipped live.

---

## ✨ Feature Highlights

- **Controls:** Momentum-based mouse steering; **hold Left** = Focus Pull (bigger gravity, more heat); **hold Right / Space** = Vent (cool down, cost mass).
- **Progression:** Six tiers — *Singularity Seed → Dust Eater → Moon Cracker → World Ender → Star Drinker → Void Sovereign* → devour **The Galactic Core** to win.
- **Feel & Visuals:** Live gravitational pull, swirling debris, procedural planets/stars/black holes, accretion-disk lensing halo, space-warp starfield, particle bursts, screen shake, vignette, and chromatic tier-ascension pulses.
- **Audio:** Procedural WebAudio cues (swallow *whumf*, vent tone, ascension chime, critical heartbeat) with a persistent mute toggle.
- **Win/Lose:** Swallow the Core = victory (with time & score); instability hits 100% = collapse.

---

## ✅ Final Status

**A new browser game titled *The Big Swallow* has been produced and deployed** — creative, surreal, cosmic, fun, readable, and fully completable, exactly in line with the studio's identity.

*Go forth and swallow the universe.* 🕳️