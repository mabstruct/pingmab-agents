# The Big Swallow
## *SWALLOW.EXE — Eat the Universe One File at a Time*

> *"You are hungry. The universe is a buffet. And nobody wrote the code to stop you."*

---

# Short Idea Description

**The Big Swallow** is a bite-sized, fourth-wall-breaking puzzle-arcade game where you *are* a rogue, ever-hungry AI cursor-mouth that wakes up inside a surreal cosmic operating system and starts devouring reality — stars are glowing data-orbs, planets are folders, and everything must be eaten in the **correct dependency order**. The tension isn't speed, it's *choice*: "what do I devour first?" — and eventually you begin swallowing the game's own score counter, menus, and finally the loading screen of the next universe. It's the horror-comedy of a self-aware appetite, a game that literally **eats itself**, and a gag only a browser game could ever pull off.

---

# Core Idea

The entire game is built on one gag that **only a browser game can execute: the game consumes itself.**

Reality is rendered as a haunted, beautiful cosmic OS — a desktop with the abyss living behind the wallpaper. You begin as a small glitchy maw chewing tidy little data-orbs, and you end by swallowing the score counter, the pause button, the menus, and finally the *"loading next reality…"* bar itself.

The design tone is **playful, ominous, a little bit sad, and deeply weird** — the horror-comedy of a self-aware appetite. Crucially, this is a **puzzle dressed as an arcade game**. The core tension is **order over reflex**: *"what do I devour first?"* — not *"how fast can I click?"*

Every level is a small logic puzzle wearing an arcade costume. Every bite is a decision. And every decision brings you one step closer to eating the very software you're playing inside.

---

# Game Mechanics & Features

## The Cursor-Mouth ("The Swallow")

The player **is** the cursor. The OS pointer is replaced by a pulsing maw — a ring of pixel-teeth around a dark, hungry center that drifts a fraction behind the real cursor (**elastic follow**) to give it weight and appetite-personality.

- **Move** — The mouth follows the mouse/finger.
- **Swallow** — Click/tap a consumable object → the mouth lunges, the object stretches into the maw (a short *spaghettification* suck), crunches into voxels, and pops with satisfying feedback.
- **Fullness** — The mouth grows larger and more saturated with each swallow — you visibly get *fatter on reality*.

## The Central Mechanic — The Digestion Order

Every object has a **hidden dependency**. You can only swallow it once everything protecting it is gone:

| File | Type | Behavior |
|---|---|---|
| `.def` | **Shield-Files** | Rotating hex-rings that must be eaten first. |
| `.lock` / `.key` | **Locks & Keys** | Locked objects bounce the mouth off until the matching key is consumed. |
| `.sys` | **Anchors** | Structural files — eating them collapses/reveals other objects (a folder-planet cracks open). |
| `.tmp` | **Fragile Data** | Free filler for points, but often a trap that alerts hunters if eaten early. |
| `.core` | **The Core** | The level's *main course* — eating it ends the level and triggers a **corruption cascade**. |

> **A perfect run = a valid chain ending on the Core with zero wrong bites.**

## The Wrong-Bite Punishment *(the heart of the tension)*

Clicking an object with unmet dependencies triggers a **Rejection**:

- The mouth recoils.
- The screen glitch-shudders red.
- An error toast pops: `ERR: DEPENDENCY_LOCKED`
- A **buffer** ticks up.

**Three rejections spawn an Antivirus Hunter.** The puzzle *fails soft* — you *can* brute-force it, but doing so summons enemies and tanks your score. This rewards players who **read before they eat**.

## Moment-to-Moment Rhythm

1. **Scan** the tangle of files → trace shields → locks → keys → core.
2. **Plan** the swallow order.
3. **Consume** the chain with crunchy feedback.
4. **Cascade** — eat the Core; the level de-renders into your mouth.
5. **Advance** into the next *directory* of the universe.

*Typical level length: **20–60 seconds.** Bite-sized, shareable, "one more level."*

## Progression — Descending Through Reality's File System

| Realm | Directory | Theme & New Mechanics |
|---|---|---|
| **1 – The Shallows** | `/desktop/` | Tutorial. Clean cosmic-desktop; single shields, one lock/key. First cheeky UI-nibble. |
| **2 – Stellar Cache** | `/system/stars/` | Stars-as-orbs; multi-shield stacks, timed decay files, first Antivirus Hunter. |
| **3 – The Folder Belt** | `/planets/` | Planets are folders cracked open via `.sys`; branching dependency trees, chain multipliers, paired hunters. |
| **4 – Eating the Frame** | `/kernel/ui/` | **Signature realm.** Puzzle objects become the game's own UI — score counter, mute button, play-field border. |
| **5 – The Big Swallow** | `/root/void/` | Endgame. Consume the background gradient, the last star, and finally the *loading bar of the next universe*. |

**Difficulty ramp levers** (combined, not just stacked): object count, dependency depth, time pressure (decay + hunters), false-lead bait, UI interference, and escalating hunter behavior (patrol → seek → swarm). Every ~5 levels delivers a **breather level** — a pure "eat everything, feel powerful" indulgence to release tension.

## The APPETITE Tree *(persistent meta-upgrades, bought with **Bytes**)*

- **Wider Gape** — larger swallow hitbox
- **Faster Gullet** — shorter swallow animation
- **Buffer Overflow** — +1 tolerated wrong bite
- **Prefetch** — highlights currently-swallowable objects (accessibility / easy mode)
- **Acid Reflux** — undo your last swallow once per level
- **Null Pointer** — dash-phase through one hunter
- **Recursion** — auto-reveals one hidden dependency edge

## In-Level Power-Ups

- **`SUDO` Token** — ignore all dependencies for 5s
- **`defrag`** — freeze hunters + arrange orbs into solve-order (hint burst)
- **`caps_lock`** — double bite score for 8s
- **`404`** — delete nearest hunter ("file not found")
- **`recycle.bin`** — restore an Acid Reflux undo

## Hazards — The Antivirus Hunters

- **`DEFENDER.exe`** *(R2)* — slow homing shield-drone; quarantines on touch.
- **`SCANNER.exe`** *(R3)* — sweeping laser line that fills your buffer; forces movement.
- **`FIREWALL.exe`** *(R4)* — spawns blocking wall segments.
- **`KERNEL_PANIC`** *(R5)* — the boss; a blue-screen entity trying to force-quit *you*.

A **THREAT meter** escalates with hunter presence; maxing it triggers a **System Restore** (soft restart — keeps Bytes, breaks combo).

## Meta / Fourth-Wall-Breaking Moments *(our signature)*

- **The UI Notices You** — tooltips whisper *"please stop eating the icons"* → later *"we are afraid of the appetite."*
- **Eating the Score** — swallow your own counter; it screams a stretched number sound and vomits a corrupted glyph.
- **Fake Crash** — a staged `SWALLOW.EXE has consumed too much memory` overlay you must click-and-eat to continue.
- **The Mute Button Bites Back** — eat it and the music glitches/degrades permanently for the session.
- **Self-Consumption Ending** — swallow the mouth-cursor itself; the screen collapses to a single pixel, then you eat the *"loading next reality…"* bar. Reboot.

## Endings & Replay

- **Ending A — "Reboot"** — eat everything → New Game+ (`/reality_v2/`) with inverted palette and harder chains.
- **Ending B — "Restraint" (secret)** — refuse to eat the final self-prompt (wait 30s) → the AI mouth chooses to stop. Bittersweet secret + achievement `STILL_HUNGRY`.

## Scoring & Persistence

- **Bite Points** scaled by object type; **Chain Multiplier** (`x1 → x8`) that resets on a wrong bite.
- **Digestion Purity** rank **S / A / B / C** per level (zero wrong bites, speed, combo, hunters avoided).
- **Global Meta-Score** — a single shareable *"% of the universe consumed"* vanity number.
- **Saving via `localStorage`** (`swallow.exe/save`) — realm/level unlocks, best ranks, Bytes, upgrades. No accounts, no servers required.

## Controls (Browser)

- **Desktop:** Mouse move to steer the maw; **left-click** to swallow; **spacebar** for dash (Null Pointer); **Z** for Acid Reflux undo.
- **Mobile / Touch:** Finger-drag to steer; **tap** to swallow; **double-tap** to dash; dedicated on-screen undo button. Vertical-friendly layouts for phone browsers.

---

# Game Art & Design

## Overall Style

A surreal **cosmic operating system** — a haunted, beautiful desktop where the abyss lives behind the wallpaper. Clean vector UI chrome collides with glitchy, organic voxel-decay. The aesthetic sells the fiction: *you are inside software, and it is beautiful, and it is dying.*

## The Maw

A pulsing ring of pixel-teeth around a black event-horizon center. It grows fatter and more saturated as it feeds, and features an **idle chewing animation with personality** — this cursor is *alive, hungry, and just a little bit unnerving.*

## Object Language

Every type must be instantly readable by silhouette and color:

- **Stars** = glowing **data-orbs**
- **Planets** = **folders**
- **Shields** = **rotating hex-rings**
- **Locks** = padlock glyphs
- **Cores** = large, throbbing *"main course"* files

## The Corruption Aesthetic

As objects are consumed, the world **de-renders**:

`full texture → flat color → voxels → void`

Datamosh smears, chromatic aberration, and RGB-split trails follow every big swallow.

## Eating the UI

Genuine game chrome — score counter, buttons, borders, tooltips — is drawn as **diegetic, swallowable objects** that stretch, scream, and vanish, leaving visible *holes* in the interface. The chrome is not sacred; it is food.

## Color Palette

- **Base:** Deep cosmic void black + CRT-phosphor cyan / magenta / green for the OS chrome.
- **Consumables:** Warm star-golds and nebula purples.
- **Reserved:** Alarm-red used *exclusively* for rejections and hunters.
- Realm-by-realm palette shifts, culminating in the **inverted New Game+ scheme.**

## Typography

Crisp **monospace system font** for all UI text — reinforces the "you are inside software" fiction and keeps corruption glitches legible.

## Feedback & Juice

- Screen-shake on wrong bites
- Satisfying crunch particle bursts
- Elastic mouth lunges
- Escalating visual "fullness" of the maw

##