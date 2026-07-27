# The Big Swallow — Sound Eater: Game Testing Report

**Build tested:** Single-file HTML5 Canvas 2D prototype
**Test focus:** Title screen, core gameplay, HUD, audio, mouse/touch controls, resizing/responsiveness, end screen, restart flow, performance, and edge cases.

**Severity scale used:**
- **Critical** — blocks play, crashes/freezes, or makes core game impossible.
- **High** — major gameplay/system issue, severe confusion, broken progression, or likely platform failure.
- **Medium** — noticeable bug, usability issue, inconsistent feedback, balance problem.
- **Low** — polish, accessibility, minor visual/audio issue.

---

## 1. Startup / Title Screen Issues

### BUG-001 — Audio may not initialize reliably from all first interactions
**Severity:** High
**Description:** The game relies on Web Audio initialization after user interaction. If the first interaction is not the `DRIFT IN` button specifically (e.g. pressing mute or tapping the canvas), the AudioContext may not resume correctly while the mute label still changes.
**Repro:** Load fresh → interact with something other than `DRIFT IN` → press `DRIFT IN` → listen. **Expected:** Any valid first gesture unlocks audio. **Actual:** Audio can remain silent/partially initialized.

### BUG-002 — Title screen does not indicate audio is browser-gated
**Severity:** Medium
**Description:** Because Web Audio can't start until user input, the title should note that sound starts on `DRIFT IN`. Critical for a sound-themed game. **Actual:** Player may think sound is broken.

### BUG-003 — Title screen lacks keyboard accessibility
**Severity:** Medium
**Repro:** Load → Tab to focus `DRIFT IN` → press Enter/Space. **Expected:** Button focusable and activatable. **Actual/Concern:** Keyboard users may be unable to start.

### BUG-004 — Viewport disables zoom, creating accessibility issue
**Severity:** Medium
**Description:** The viewport meta disables user scaling, making small HUD/title/end text impossible to enlarge on mobile. **Actual:** Reduced accessibility.

### BUG-005 — Legend colors hard to read against near-black on some displays
**Severity:** Low
**Description:** Orange beacon marker and dim text lose contrast on low-brightness mobile screens.

### BUG-006 — Start button can be accidentally triggered by touch drag
**Severity:** Medium
**Repro:** Title screen on touch device → swipe/drag starting over/near `DRIFT IN`. **Actual/Concern:** Drag gestures can trigger start unintentionally.

---

## 2. Core Gameplay Mechanics Issues

### BUG-007 — "Eat only what is lit" rule not consistently communicated during play
**Severity:** High
**Description:** During play it is not clear whether a source is currently lit/edible/safe. Entities near glow falloff can appear barely visible yet still be swallowed.

### BUG-008 — Invisible or nearly invisible sources may still be swallowed
**Severity:** High
**Repro:** Darken the world by eating several sources → drift through dark areas → watch for unexpected mass/score changes. **Expected:** Only clearly lit sources swallowed. **Actual/Concern:** Barely-visible/unseen sources can be eaten, violating the core rule.

### BUG-009 — Collision radius becomes too forgiving as mouth grows
**Severity:** High
**Description:** As the mouth grows, accidental swallowing becomes common, undermining the tension of preserving lights.

### BUG-010 — Beacon eating creates abrupt darkness spike that can make game unwinnable
**Severity:** High
**Repro:** Eat a beacon early → continue. **Actual:** Visibility can collapse too suddenly, making navigation feel random.

### BUG-011 — Chime behavior may conflict with "safe light path" role
**Severity:** Medium
**Description:** If chimes dart too fast or flee offscreen, they stop serving their guidance role and can be accidentally swallowed.

### BUG-012 — Fast-moving entities can tunnel through the mouth
**Severity:** Medium
**Description:** Frame-based collision can miss fast chimes/prey, especially during FPS drops, making swallowing inconsistent.

### BUG-013 — Entities can spawn inside the mouth's collision radius
**Severity:** High
**Repro:** Start, stay near center, wait for spawns/phase transitions → watch for instant mass/score changes without moving. **Actual/Concern:** Instant unfair swallowing if spawn exclusion radius is insufficient.

### BUG-014 — Entities can spawn partially/fully offscreen
**Severity:** Medium
**Description:** Sources spawning offscreen still affect audio/score/progression while being unreachable/invisible.

### BUG-015 — Mouth target movement can overshoot and cause unwanted swallowing
**Severity:** Medium
**Repro:** Drag quickly across a cluster, release early → mouth keeps drifting into entities. **Actual:** Movement can continue/swallow after player intent changes.

### BUG-016 — No clear fail/win feedback for "Survive The Hush"
**Severity:** High
**Description:** Phases and "The Hush" are referenced, but what triggers success, failure, or the end screen is unclear during active play.

### BUG-017 — Quota progression encourages eating everything, conflicting with bonus goal
**Severity:** Medium
**Description:** HUD pushes toward MASS/QUOTA while the end bonus rewards "Kept the Lights On." The conflict/tradeoff is not made clear during play.

### BUG-018 — Player can become so large that navigation stops
**Severity:** High
**Description:** After enough mass, the mouth occupies too much screen, making avoidance impossible and turning the game into automatic collection.

### BUG-019 — No visible warning before major phase transitions
**Severity:** Medium
**Description:** If phases change spawn rate/darkness/audio/speed, there should be a clear transition cue beyond HUD text.

### BUG-020 — Darkness can become total, leaving no actionable information
**Severity:** Critical
**Repro:** Eat most visible sources, keep navigating. **Expected:** Always minimal navigational feedback / emergency pulse / end condition. **Actual:** Gameplay can become fully blind and unreadable.

---

## 3. HUD Accuracy / UI Issues

### BUG-021 — Progress bar can overflow after exceeding quota
**Severity:** Medium
**Repro:** Near quota, eat a high-mass beacon → observe bar. **Expected:** Fill caps at 100%. **Actual/Concern:** Bar may overflow/misrepresent progress.

### BUG-022 — HUD MASS value may not match final "Mass Devoured"
**Severity:** Medium
**Description:** `MASS <hudMass>` and end-screen `Mass Devoured <finalMass>` should match; rounding/timing/reset can cause mismatch.

### BUG-023 — Score updates before swallow animation/audio finishes
**Severity:** Low
**Description:** HUD updates instantly on contact; if visual/audio feedback lags, HUD feels disconnected.

### BUG-024 — Combo indicator lacks countdown/decay clarity
**Severity:** Medium
**Description:** No indication of how long until combo expires; it may disappear/reset without warning.

### BUG-025 — Combo may reset unfairly during darkness gaps
**Severity:** Medium
**Description:** Combo timing should account for periods where no lit targets are visible; otherwise combo feels arbitrary/impossible to maintain.

### BUG-026 — Time display may continue while overlays are active
**Severity:** Medium
**Description:** `TIME mm:ss` should only count active gameplay; may keep running under title/end overlays if the loop stays alive.

### BUG-027 — HUD overlaps gameplay-critical visibility area on small screens
**Severity:** Medium
**Description:** HUD can cover glows/entities on small devices; especially significant given already-limited visibility.

### BUG-028 — Mute button label may desync from real audio state
**Severity:** Medium
**Repro:** Toggle mute before/after start, background tab and return → compare label vs audible state. **Actual/Concern:** Label can say ON while silent (suspended context) or vice versa.

### BUG-029 — Phase indicator may not explain phase meaning
**Severity:** Low
**Description:** `hudPhase` likely shows a name/number without conveying what changed.

---

## 4. Audio Issues

### BUG-030 — Background drone can continue after game end
**Severity:** Medium
**Description:** The void drone may keep playing on the "Silence Map" end screen, conflicting thematically.

### BUG-031 — Restart may layer multiple drone/pulse oscillators
**Severity:** High
**Repro:** Start → end → `DRIFT AGAIN`, repeat several times → listen for thicker/louder drone. **Actual/Concern:** Audio nodes may accumulate (also a memory leak risk).

### BUG-032 — Mute does not necessarily stop oscillator processing
**Severity:** Medium
**Description:** Mute likely sets gain to 0 but leaves oscillators running, wasting CPU.

### BUG-033 — Audio pops/clicks when toggling mute
**Severity:** Medium
**Description:** Immediate gain changes can produce clicks, especially with low drone frequencies; needs gain ramping.

### BUG-034 — Prey/swallow sounds can clip during rapid combos
**Severity:** Medium
**Description:** Overlapping short prey tones + sawtooth swallow clicks can distort without gain limiting/compression.

### BUG-035 — Beacon pulse can mask important feedback sounds
**Severity:** Medium
**Description:** The ~110Hz triangle beacon pulse can dominate the low mix and mask swallow/chime cues.

### BUG-036 — Audio continues while browser tab is hidden
**Severity:** Medium
**Description:** No `visibilitychange` suspend; audio/game may continue when tabbed out, wasting CPU.

### BUG-037 — iOS/Safari audio resume may fail after mute/restart/background
**Severity:** High
**Repro:** iOS Safari → start → mute/unmute → background app → return → restart. **Actual/Concern:** Sound may not return without a full reload; label may be wrong.

---

## 5. Controls — Mouse / Pointer / Touch

### BUG-038 — Mouse leave causes mouth to keep drifting toward stale target
**Severity:** Medium
**Repro:** Move mouse to edge → leave window → watch mouth. **Actual:** Mouth continues toward last pointer position and can swallow unintended sources.

### BUG-039 — Pointer coordinates can be incorrect after resize or DPR change
**Severity:** High
**Description:** Canvas uses DPR scaling; if pointer coords aren't converted via current bounding rect + DPR, steering becomes offset after resize or on high-DPI screens.

### BUG-040 — Touch and mouse events may both fire on hybrid devices
**Severity:** Medium
**Description:** Synthetic mouse events from touch can cause jitter/duplicate steering if both are handled separately.

### BUG-041 — Multi-touch causes erratic steering
**Severity:** Medium
**Description:** Multiple fingers can confuse target position; game should track first touch only.

### BUG-042 — HUD button taps can also steer the mouth
**Severity:** Medium
**Repro:** Tap `♪ SOUND` → watch mouth. **Actual/Concern