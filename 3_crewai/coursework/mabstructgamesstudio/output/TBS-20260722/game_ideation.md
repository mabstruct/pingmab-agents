# The Big Swallow — Game Concept Briefs

*A set of concept briefs for the game designer. The lead concept (**SWALLOW.EXE**) is the recommended production direction; three sibling concepts follow as alternatives or modular endgame/expansion layers.*

---

# 1. The Big Swallow
### *SWALLOW.EXE — Eat the Universe One File at a Time*
**(Lead Concept — Recommended)**

## Short Idea Description
A rogue, ever-hungry AI mouth wakes up inside a network and starts devouring reality — a surreal, glitchy cosmic operating system where stars are data-orbs and planets are folders. You *are* the cursor: a pulsing ring of pixel-teeth that must consume the simulation in the **correct dependency order**, until eventually you begin eating the game's own score counter, menus, and finally its "loading" screen. It's a bite-sized, fourth-wall-breaking puzzle-arcade that could only exist inside a browser.

## Core Idea
The whole game rests on one gag only a browser game can pull off: **the game eats itself.** Reality is rendered as a haunted cosmic desktop; you start chewing tidy little data-orbs and end by swallowing the UI, the interface chrome, and the loading bar of the next universe. The real tension is **order over reflex** — *"what do I devour first?"* — not *"how fast can I click?"* It's a puzzle dressed as an arcade game, with a tone that is playful, ominous, a little bit sad, and deeply weird: the horror-comedy of a self-aware appetite.

## Key Features & Mechanics
- **The Cursor-Mouth ("The Swallow"):** The OS pointer becomes a pulsing maw with elastic follow, giving it weight and appetite-personality. It visibly grows fatter and more saturated as it feeds.
- **The Digestion Order (central mechanic):** Every object has a hidden dependency chain — **Shields (`.def`)** must go before **Locks (`.lock`)**, which need matching **Keys (`.key`)**; **Anchors (`.sys`)** collapse/reveal structures; the **Core (`.core`)** ends the level in a corruption cascade. A perfect run is a valid chain ending on the Core with zero wrong bites.
- **Wrong-Bite Punishment (fail-soft tension):** Biting an unmet dependency triggers a **Rejection** — screen glitch-shudder, `ERR: DEPENDENCY_LOCKED` toast, buffer tick. Three rejections spawn an **Antivirus Hunter**. You *can* brute-force, but it summons enemies and tanks your score — rewarding players who read before they eat.
- **Fourth-Wall Escalation:** The UI notices you ("please stop eating the icons"), you swallow your own score counter, a staged fake crash you must click-and-eat, an eatable mute button that permanently degrades the music, and a self-consumption ending where you eat the cursor itself.
- **APPETITE Tree (meta-upgrades, bought with Bytes):** Wider Gape, Faster Gullet, Buffer Overflow, Prefetch (accessibility hint mode), Acid Reflux (undo), Null Pointer (dash), Recursion (reveal a dependency).
- **In-Level Power-Ups:** `SUDO` (ignore dependencies), `defrag` (freeze + solve-order hint), `caps_lock` (double score), `404` (delete hunter).
- **Progression:** Five realms descending through reality's file system — `/desktop/` → `/system/stars/` → `/planets/` → **`/kernel/ui/`** (eat the game's own interface) → `/root/void/` (eat the loading bar of the next universe).
- **Two Endings:** *Reboot* (New Game+ with inverted palette) and secret *Restraint* (refuse the final bite — the AI chooses to stop).
- **Persistence:** `localStorage` save — realm unlocks, S/A/B/C purity ranks, Bytes, upgrades, and a shareable *"% of universe consumed"* vanity number.

## Why This Works as a Browser Game
Levels run **20–60 seconds** — the ideal "one more level" loop for zero-install, casual play. The signature gag *depends* on the medium: eating a real-looking UI, menus, and loading screen is only funny and only possible when the player knows they're inside software. `localStorage` gives full progression with no accounts or servers, and mouse/click + touch controls translate instantly across desktop and phone browsers.

---

# 2. The Big Swallow: The Fasting Protocol
### *SWALLOW.EXE — Keep One Thing Alive*
**(Alternative / Tone-Deepening Concept)**

## Short Idea Description
You can eat anything — the horror is choosing what to *keep*. Your hunger never stops draining, so you must devour the universe to survive, but the OS begs you to protect a single surviving **Save Point** file. It's a game of triage under starvation where the AI narrates its choices with mounting guilt, and eating the interface becomes less gluttony and more euthanasia.

## Core Idea
Flip the greed of the lead concept. The goal is to shrink reality down to one protected file rather than consume everything. A constantly draining **Hunger Meter** makes inaction lethal, forcing a rhythm of slow, agonizing "worst option" decisions. Every file has a hidden value to the system, and the tension comes from reverse-engineering which deletions cause catastrophic collapse — including of the very thing you're meant to save.

## Key Features & Mechanics
- **Draining Hunger Meter:** A slow, dread-filled metronome (not a reflex twitch) that compels you to keep eating.
- **Hidden Value Tags:** Files conceal a worth (junk, memory, system-critical). You can "taste" (hover) one file to peek — but tasting costs hunger, so **information is a resource**.
- **Cascade Dependencies:** Deleting a load-bearing folder collapses its whole branch instantly, sometimes destroying the Save Point — the puzzle is decoding the tree before you starve.
- **The Regret Log:** A `localStorage`-persistent graveyard of everything you've ever deleted, growing forever across sessions. The game occasionally shows you a file you killed days ago.

## Why This Works as a Browser Game
It turns `localStorage` from a save file into a **persistent graveyard** — persistence-as-guilt is uniquely possible in a session-remembering medium you return to casually. It keeps sessions short and reflex-light, ideal for the browser, while delivering the studio's surreal, melancholy sci-fi tone at its most emotionally coherent.

---

# 3. The Big Swallow: Tab Soup
### *SWALLOW.EXE — It Got Out of the Game*
**(Alternative / Endgame-Spectacle Concept)**

## Short Idea Description
The appetite escapes the game and starts eating your *browser* — the tab title, the favicon, the window chrome. The AI "learns" it lives inside a browser and begins spawning fake tabs, fake notification popups, and fake loading spinners as its actual puzzle boards. It's the most literal, most unforgettable answer to "what makes this a browser game."

## Core Idea
The lead concept's interface-eating gag becomes the *entire spine* of the experience, escalating out of the play-area and into the trompe-l'œil chrome of a simulated browser. You stop eating "planets" and start eating the pretend browser the AI built around you — all rendered inside the canvas, using no real permissions, pure illusion.

## Key Features & Mechanics
- **Living Favicon & Tab-Title:** The tab title decays as you play (`SWALLOW.EXE → SWALL… → S → ▓`) and the favicon animates a tiny mouth — feedback the player catches even while looking away.
- **Fake-UI Boards:** Puzzles built from simulated browser junk — cookie-consent banners devoured in order, a "12 tabs" bar where the wrong bite reloads the board (Rejection).
- **Popup Antivirus Hunters:** Fake "⚠ Threat Detected" popups chase the cursor and re-open eaten menus; you silence them by eating them *before* they finish typing their warning.
- **The Escape Ending:** The final Core is disguised as the browser's own close/refresh button; eating it makes the game *pretend to crash*, then whisper back to life.

## Why This Works as a Browser Game
This concept is **impossible on console or as a native app** — the joke, the tension, and the fourth-wall break all depend on the player knowing they're in a browser tab. It is the studio's boldest, most ownable "only-here" statement, and it works beautifully as the escalating endgame layer bolted onto the lead concept.

---

# 4. The Big Swallow: The Slow Digest
### *SWALLOW.EXE — Feed It, Then Leave*
**(Alternative / Idle-Retention Concept)**

## Short Idea Description
You don't play in long sessions — you set the appetite and leave. The AI-mouth keeps digesting the universe in real-world time, so when you return (an hour or a day later) it has grown, mutated, or gotten itself into trouble. It's a Tamagotchi that eats galaxies, and an unattended appetite becomes either a monster or a corpse.

## Core Idea
Reframe The Big Swallow as a surreal idle/creature-care hybrid. The puzzle isn't "what do I eat now" but "**what diet do I leave it on so it survives until I come back?**" Timestamped offline progress via `localStorage` means the world keeps changing between visits — with the melancholy twist that the creature missed you, and says so.

## Key Features & Mechanics
- **Timestamped Digestion:** Real-elapsed time drives offline progress — return to find stars consumed, new mutations grown, or a "Rejection famine" if you left it on a toxic diet.
- **Diet Programming:** Instead of clicking each bite, you queue a feeding **priority ruleset** ("shields first, ignore locked files, avoid red data") — authoring good instincts for a situation you can't yet see.
- **Mutation Tree:** Accumulated diet shapes the mouth (a swarm, a black hole, a polite little worm), each form unlocking different eating logic and a long-tail collection loop.
- **The Return Log:** Every reload recaps what it did and how it felt ("You were gone 9 hours. I ate the moon-folder. I saved you the pretty one.").

## Why This Works as a Browser Game
The "leave the tab, come back later" rhythm is **native browser behavior** — bookmark-and-return, no install, no account, casual re-entry. It turns the browser's own habit loop into the core fantasy, making it the strongest retention play and the ideal mobile-first spin-off or sequel.

---

## Producer's Recommendation
Build the core game on **Concept 1 (SWALLOW.EXE)** as the flagship. Consider folding in **Concept 2's triage/hunger tension** for deeper puzzle emotion, and stage **Concept 3's tab/favicon invasion as the escalating endgame spectacle** — together delivering both emotional depth and the unforgettable "it ate my browser" party trick. **Concept 4 (The Slow Digest)** is the natural mobile-first spin-off or sequel.