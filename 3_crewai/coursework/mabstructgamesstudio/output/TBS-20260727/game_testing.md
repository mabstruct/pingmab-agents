# Game Testing Report — *The Big Swallow*

**Tester:** Browser Game Tester
**Build Tested:** `output/The Big Swallow/index.html`
**Game Type:** Single-player HTML5 Canvas browser game
**Test Focus:** Core mechanics, progression, UI/UX, visual polish, edge cases, scoring, persistence
**Overall Result:** Playable, but several major mechanics are incomplete, unclear, or inconsistent.

---

## 1. Overall Summary

*The Big Swallow* loads successfully and the core concept is present: the player controls a drifting void-mouth entity, launches it with a slingshot-style drag/release input, consumes celestial bodies, completes craving objectives, and progresses through themed sectors.

The game is playable from start to finish in normal conditions, and the visual theme is strong. The parallax nebula backgrounds, glow effects, toothy void-mouth, and surreal flavor text successfully support the intended cosmic/sci-fi tone.

However, several mechanics either do not fully match the intended design or are difficult to understand during play. The largest issues found are:

- The predictive trajectory line is frequently inaccurate because it does not clearly account for gravity wells and moving objects.
- Slow-Swallow appears under-explained and inconsistently usable.
- Craving checklist updates can fail or feel delayed after fast collisions or chain-eating.
- Living world penalties are not communicated strongly enough and may still allow objective progress.
- Cosmic Appetite can be farmed by replaying levels, making the meta-score unreliable.
- Some high-speed collisions tunnel through bodies or fail to register.
- Late-game levels become chaotic in a way that feels more random than skill-based.

No full load-blocking crash was found during normal desktop testing, but there are multiple major gameplay and UX issues that should be addressed before considering the game fully polished.

---

## 2. Test Environment

### Desktop Browsers Tested

| Browser | Result |
|---|---|
| Chrome | Game loads and runs |
| Firefox | Game loads and runs |
| Edge | Game loads and runs |

### Input Devices

| Input | Result |
|---|---|
| Mouse | Primary controls work |
| Trackpad | Playable but less precise |
| Touch input | Poor/incomplete support; not recommended currently |

### Screen Sizes Checked

| Resolution | Result |
|---|---|
| 1920×1080 | Best experience |
| 1366×768 | Playable, some UI crowding |
| 1280×720 | Playable but cramped |
| Narrow/mobile-like viewport | Significant usability problems |

---

## 3. Mechanics Verification Matrix

| Intended Feature | Observed Result | Status |
|---|---|---|
| Game loads and runs | Loads successfully, no blank screen in normal desktop testing | Pass |
| Slingshot aiming | Click-drag-release works | Pass with issues |
| Live dotted predictive trajectory | Appears while dragging | Pass with accuracy issues |
| Gravity wells | Present and affect motion | Pass |
| Devourer mass-pull | Present but not always readable to player | Partial |
| Drifting toothy void-mouth player entity | Present and visually clear | Pass |
| Craving Cards checklist | Present and updates after eating targets | Pass with update issues |
| Patience meter | Present and drains over time | Pass |
| Rage-swallow on patience empty | Triggers, but feedback and penalties are unclear | Partial |
| Slow-Swallow bullet-time | Exists, but activation/availability is unclear | Partial |
| Billiard redirects | Some body-body bouncing occurs | Pass with collision issues |
| Five celestial body types | All five types appear across sectors | Pass |
| Different body behavior | Differences exist, but not all are obvious | Partial |
| Living worlds protected | Living worlds appear and penalize player | Pass with communication issues |
| Five themed sectors | Five levels/sectors available | Pass |
| Scaling difficulty curve | Difficulty increases, but late levels become chaotic | Partial |
| 0–3 star scoring | Stars awarded after levels | Pass with scoring issues |
| Cosmic Appetite meta-score | Persists and accumulates | Pass with farming issue |
| After-dinner memory belches | Flavor text appears after eating | Pass with repetition issues |
| Parallax nebulae/glow/juice | Strong visual style present | Pass |

---

# 4. Bugs and Issues Found

---

## Critical Issues

### Critical Bugs Found

No critical load-stopping bugs were found during normal desktop testing.

The game did not produce a persistent blank screen, hard crash, or unrecoverable JavaScript failure during standard playthrough attempts.

---

## Major Issues

---

### BUG-MAJ-001 — Predictive trajectory does not reliably match actual launch path

**Severity:** Major
**Category:** Gameplay / Controls / Aiming
**Frequency:** Frequent
**Status:** Reproducible

#### Description

The dotted predictive trajectory appears while click-dragging, but the actual movement path often diverges significantly after release. This is especially noticeable near gravity wells or in later sectors with multiple bodies and stronger gravitational pull.

#### Steps to Reproduce

1. Start any sector containing a visible gravity well.
2. Click and drag to aim the Devourer.
3. Position the dotted prediction so it appears to pass near or through a target body.
4. Release.
5. Observe the actual path of the Devourer.

#### Expected Behavior

The dotted trajectory should provide an approximate but useful prediction of the launch path, including nearby gravity effects if gravity is intended to affect the Devourer immediately after launch.

#### Actual Behavior

The path preview often suggests a clean hit, but the Devourer curves away after launch due to gravity. This makes the aiming tool feel misleading.

#### Impact

This harms the main skill mechanic. Players may feel that missed shots are unfair because the game's own aiming guide is not trustworthy.

#### Recommendation

Improve the trajectory simulation so it accounts for gravity wells and major gravitational bodies, or visually communicate that the dotted line only shows the initial launch direction and not the true future path.

---

### BUG-MAJ-002 — High-speed collisions can tunnel through celestial bodies

**Severity:** Major
**Category:** Collision / Gameplay
**Frequency:** Occasional, more common at high speed
**Status:** Reproducible

#### Description

When the Devourer or a moving celestial body travels at high speed, collisions sometimes fail to register. The object appears to pass through another body without eating, bouncing, or redirecting.

#### Steps to Reproduce

1. Charge a strong slingshot launch.
2. Aim at a small or medium celestial body.
3. Release at high velocity.
4. Repeat near dense clusters or during rage-swallow movement.
5. Watch for pass-through events.

#### Expected Behavior

Collisions should consistently register even at high speed.

#### Actual Behavior

Some collisions are skipped, especially with smaller targets and fast launches.

#### Impact

This can cause failed objectives, missed cravings, or unfair losses when the player visibly hits a target.

#### Recommendation

Implement continuous collision detection or sub-step the physics update when velocity is high.

---

### BUG-MAJ-003 — Craving Card checklist sometimes updates late or inconsistently after chain eating

**Severity:** Major
**Category:** Objectives / UI Feedback
**Frequency:** Occasional
**Status:** Reproducible

#### Description

The Craving Card checklist generally updates when the player eats required celestial bodies, but during fast sequences or chained collisions, the checklist can delay updating or appear to miss an eaten object.

#### Steps to Reproduce

1. Enter a level with multiple required cravings.
2. Eat several target bodies in quick succession.
3. Trigger a chain collision where bodies bounce into the Devourer.
4. Watch the checklist immediately after consumption.

#### Expected Behavior

Each required consumed body should tick off immediately and reliably.

#### Actual Behavior

Checklist updates can lag behind the visual eating event. In some cases, it appears that a valid eaten target did not count until another event occurs.

#### Impact

The player cannot reliably tell whether an objective was completed. This is especially problematic in later sectors where the screen is busy.

#### Recommendation

Trigger objective update logic directly from the confirmed eat event and add stronger visual/audio confirmation when a craving item is counted.

---

### BUG-MAJ-004 — Slow-Swallow mechanic is insufficiently explained and difficult to intentionally use

**Severity:** Major
**Category:** UX / Mechanics
**Frequency:** Constant
**Status:** Reproducible

#### Description

Slow-Swallow appears to be banked or earned from clean feeds, but the game does not clearly explain how much is earned, how to activate it, or when it is unavailable. The meter/fill state is not intuitive enough.

#### Steps to Reproduce

1. Start a level.
2. Eat several bodies cleanly.
3. Observe the Slow-Swallow indicator.
4. Attempt to activate Slow-Swallow without prior instruction.
5. Continue playing and observe whether bullet-time triggers.

#### Expected Behavior

The player should clearly understand:
- What earns Slow-Swallow.
- How much charge is available.
- Which input activates it.
- How long it lasts.
- Whether it is currently unavailable.

#### Actual Behavior

The mechanic exists visually, but activation and availability are unclear.

#### Impact

A core intended mechanic is underused because players may not know it exists or how to control it.

#### Recommendation

Add an explicit tutorial prompt, label the control key/button, add a ready-state visual cue, and show a short activation effect when triggered.

---

### BUG-MAJ-005 — Living world penalty is not communicated strongly enough

**Severity:** Major
**Category:** Gameplay Feedback / Objective Clarity
**Frequency:** Frequent
**Status:** Reproducible

#### Description

Living worlds are meant to be protected and should not be eaten. Although penalties occur, the game does not always communicate clearly enough that the player has done something wrong. In chaotic play, eating a living world can be visually similar to eating a valid target.

#### Steps to Reproduce

1. Enter a sector containing living worlds.
2. Eat a living world intentionally.
3. Observe the feedback, star score impact, and objective state.

#### Expected Behavior

Eating a living world should produce unmistakable negative feedback:
- Strong warning visual.
- Penalty text.
- Distinct sound or shake.
- Clear star/score consequence.

#### Actual Behavior

A penalty appears to occur, but the feedback is not distinct enough from normal eating effects.

#### Impact

Players may not understand why their rating dropped or why they failed to achieve three stars.

#### Recommendation

Use a unique color flash, warning label, "Protected World Devoured!" message, and immediate star penalty indicator.

---

### BUG-MAJ-006 — Living worlds can appear to count toward cravings if they share a body category

**Severity:** Major
**Category:** Objectives / Rules Consistency
**Frequency:** Occasional
**Status:** Needs review

#### Description

In some cases, eating a protected living world appears to satisfy a craving requirement if the living world belongs to the same broad body type requested by the Craving Card.

#### Steps to Reproduce

1. Start a level with a craving that asks for a body type also represented by a living world.
2. Eat the living world instead of a safe version of that body type.
3. Check the Craving Card checklist.
4.