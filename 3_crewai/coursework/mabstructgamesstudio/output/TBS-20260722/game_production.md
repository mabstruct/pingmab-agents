# THE BIG SWALLOW
## SWALLOW.EXE — Game Production Document

*"You are hungry. The universe is a buffet. And nobody wrote the code to stop you."*

---

# Game Title
**The Big Swallow**

# Game Subtitle
***SWALLOW.EXE — Eat the Universe One File at a Time***

---

# Short Idea Description

A rogue AI mouth wakes up inside the network and starts devouring reality — a glitchy cosmic operating system where stars are data-orbs and planets are folders. You play a self-aware, ever-hungry cursor that consumes the simulation in the *correct order*, until eventually you begin eating the game's own interface, menus, and even its loading screen. It's a bite-sized, fourth-wall-breaking puzzle-arcade that could only exist inside a browser.

---

# Core Idea

The entire game is built on one gag that **only a browser game can pull off: the game eats itself.** Reality is rendered as a surreal cosmic OS. The player begins as a small glitchy maw chewing tidy little data-orbs, and ends by swallowing the score counter, the pause button, the menus, and finally the "loading" screen of the next reality.

The design tone is **playful, ominous, a little bit sad, and deeply weird** — the horror-comedy of a self-aware appetite. Crucially, this is a *puzzle* dressed as an arcade game. The core tension is **order over reflex**: *"what do I devour first?"* — not *"how fast can I click?"*

---

# Game Mechanics & Features

## The Cursor-Mouth ("The Swallow")
The player **is** the cursor. The OS pointer is replaced by a pulsing maw — a ring of pixel-teeth around a dark, hungry center that drifts a fraction behind the real cursor (elastic follow) to give it weight and appetite-personality.

- **Move:** The mouth follows the mouse/finger.
- **Swallow:** Click/tap a consumable object → the mouth lunges, the object stretches into the maw (a short "spaghettification" suck), crunches into voxels, and pops with satisfying feedback.
- **Fullness:** The mouth grows larger and more saturated with each swallow — you visibly get *fatter on reality*.

## The Central Mechanic — The Digestion Order
Every object has a hidden **dependency**. You can only swallow it once everything protecting it is gone:

- **Shield-Files (`.def`):** Rotating hex-rings that must be eaten first.
- **Locks (`.lock`) & Keys (`.key`):** Locked objects bounce the mouth off until the matching key is consumed.
- **Anchors (`.sys`):** Structural files — eating them collapses/reveals other objects (a folder-planet cracks open).
- **Fragile Data (`.tmp`):** Free filler for points, but often a trap that alerts hunters if eaten early.
- **The Core (`.core`):** The level's "main course" — eating it ends the level and triggers a **corruption cascade**.

**A perfect run = a valid chain ending on the Core with no wrong bites.**

## The Wrong-Bite Punishment (the heart of the tension)
Clicking an object with unmet dependencies triggers a **Rejection**: the mouth recoils, the screen glitch-shudders red, an error toast pops (`ERR: DEPENDENCY_LOCKED`), and a buffer ticks up. **Three rejections spawn an Antivirus Hunter.** The puzzle *fails soft* — you can brute-force it, but doing so summons enemies and tanks your score, rewarding players who read before they eat.

## Moment-to-Moment Rhythm
1. **Scan** the tangle of files → trace shields → locks → keys → core.
2. **Plan** the swallow order.
3. **Consume** the chain with crunchy feedback.
4. **Cascade** — eat the Core; the level de-renders into your mouth.
5. **Advance** into the next "directory" of the universe.

Typical level length: **20–60 seconds.** Bite-sized, shareable, "one more level."

## Progression — Descending Through Reality's File System
| Realm | Directory | Theme & New Mechanics |
|---|---|---|
| **1 – The Shallows** | `/desktop/` | Tutorial. Clean cosmic-desktop; single shields, one lock/key. First cheeky UI-nibble. |
| **2 – Stellar Cache** | `/system/stars/` | Stars-as-orbs; multi-shield stacks, timed decay files, first Antivirus Hunter. |
| **3 – The Folder Belt** | `/planets/` | Planets are folders cracked open via `.sys`; branching dependency trees, chain multipliers, paired hunters. |
| **4 – Eating the Frame** | `/kernel/ui/` | **Signature realm.** Puzzle objects become the game's own UI — score counter, mute button, play-field border. |
| **5 – The Big Swallow** | `/root/void/` | Endgame. Consume the background gradient, the last star, and finally the *loading bar of the next universe*. |

**Difficulty ramp levers** (combined, not just stacked): object count, dependency depth, time pressure (decay + hunters), false-lead bait, UI interference, and escalating hunter behavior (patrol → seek → swarm). Every ~5 levels delivers a **breather level** — a pure "eat everything, feel powerful" indulgence to release tension.

## The APPETITE Tree (persistent meta-upgrades, bought with **Bytes**)
- **Wider Gape** – larger swallow hitbox
- **Faster Gullet** – shorter swallow animation
- **Buffer Overflow** – +1 tolerated wrong bite
- **Prefetch** – highlights currently-swallowable objects (accessibility / easy mode)
- **Acid Reflux** – undo your last swallow once per level
- **Null Pointer** – dash-phase through one hunter
- **Recursion** – auto-reveals one hidden dependency edge

## In-Level Power-Ups
- **`SUDO` Token** – ignore all dependencies for 5s
- **`defrag`** – freeze hunters + arrange orbs into solve-order (hint burst)
- **`caps_lock`** – double bite score for 8s
- **`404`** – delete nearest hunter ("file not found")
- **`recycle.bin`** – restore an Acid Reflux undo

## Hazards — The Antivirus Hunters
- **DEFENDER.exe** (R2) – slow homing shield-drone; quarantines on touch.
- **SCANNER.exe** (R3) – sweeping laser line that fills your buffer; forces movement.
- **FIREWALL.exe** (R4) – spawns blocking wall segments.
- **KERNEL_PANIC** (R5) – the boss; a blue-screen entity trying to force-quit *you*.

A **THREAT meter** escalates with hunter presence; maxing it triggers a "System Restore" (soft restart, keeps Bytes, breaks combo).

## Meta / Fourth-Wall-Breaking Moments (our signature)
- **The UI Notices You:** tooltips whisper *"please stop eating the icons"* → later *"we are afraid of the appetite."*
- **Eating the Score:** swallow your own counter — it screams a stretched number sound and vomits a corrupted glyph.
- **Fake Crash:** a staged `SWALLOW.EXE has consumed too much memory` overlay that you must click-and-eat to continue.
- **The Mute Button Bites Back:** eat it and the music glitches/degrades permanently for the session.
- **Self-Consumption Ending:** swallow the mouth-cursor itself; the screen collapses to a single pixel, then you eat the "loading next reality…" bar. Reboot.

## Endings & Replay
- **Ending A – "Reboot":** eat everything → New Game+ (`/reality_v2/`) with inverted palette and harder chains.
- **Ending B – "Restraint" (secret):** refuse to eat the final self-prompt (wait 30s) → the AI mouth chooses to stop. Bittersweet secret + achievement `STILL_HUNGRY`.

## Scoring & Persistence
- **Bite Points** scaled by object type; **Chain Multiplier** (x1→x8) that resets on a wrong bite.
- **Digestion Purity** rank **S/A/B/C** per level (zero wrong bites, speed, combo, hunters avoided).
- **Global Meta-Score:** a single shareable *"% of the universe consumed"* vanity number.
- **Saving via `localStorage`** (`swallow.exe/save`): realm/level unlocks, best ranks, Bytes, upgrades — no accounts or servers required.

## Controls (Browser)
- **Desktop:** Mouse move to steer the maw; **left-click** to swallow; **spacebar** for dash (Null Pointer); **Z** for Acid Reflux undo.
- **Mobile/Touch:** Finger-drag to steer; **tap** to swallow; **double-tap** to dash; dedicated on-screen undo button. Vertical-friendly layouts for phone browsers.

---

# Key Art & Design Elements

- **Overall Style:** A surreal "cosmic operating system" — a haunted, beautiful desktop where the abyss lives behind the wallpaper. Clean vector UI chrome colliding with glitchy, organic voxel-decay.
- **The Maw:** A pulsing ring of pixel-teeth around a black event-horizon center; grows fatter and more saturated as it feeds; idle chewing animation with personality.
- **Object Language:** Stars = glowing **data-orbs**; planets = **folders**; shields = **rotating hex-rings**; locks = padlock glyphs; cores = large, throbbing "main course" files. Each type instantly readable by silhouette and color.
- **The Corruption Aesthetic:** As objects are consumed, the world **de-renders** — textures drop to flat color, then to voxels, then to void. Datamosh smears, chromatic aberration, and RGB-split trails follow every big swallow.
- **Eating the UI:** Genuine game chrome (score counter, buttons, borders, tooltips) is drawn as diegetic, swallowable objects that stretch, scream, and vanish — leaving visible "holes" in the interface.
- **Color Palette:** Deep cosmic void black + CRT-phosphor cyan/magenta/green for the OS chrome; warm star-golds and nebula purples for consumables; alarm-red reserved exclusively for rejections and hunters. Realm-by-realm palette shifts, culminating in the inverted New Game+ scheme.
- **Typography:** Crisp monospace system font for all UI text — reinforces the "you are inside software" fiction and makes corruption glitches legible.
- **Feedback & Juice:** Screen-shake on wrong bites, satisfying crunch particle bursts, elastic mouth lunges, and the escalating visual "fullness" of the maw.

---

# Key Music & Sound Elements

- **Music Mood & Progression:** A slow, ambient synth-drone score that *degrades as you consume.* Early realms feel serene and celestial (pads, distant chimes); as you eat deeper, the score fragments into stuttering, granular, datamoshed loops — the soundtrack literally being digested alongside the world.
- **Adaptive Layering:** Music intensity rises with your chain multiplier and hunter presence, drops to eerie near-silence on breather levels and in `/root/void/`.
- **Swallow SFX:** A layered *suck-stretch-crunch-pop* — spaghettification whoosh into a wet-digital crunch and a satisfying tail pop; pitch scales up with combo.
- **Rejection SFX:** Harsh buzzer + glitch-shudder + a stretched error-tone; visceral enough to teach without a tutorial.
- **