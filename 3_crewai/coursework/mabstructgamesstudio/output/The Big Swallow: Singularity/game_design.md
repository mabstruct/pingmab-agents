# The Big Swallow: *The Word-Eater*

## Short Idea Description
A silent alien archivist drifts through a dead library-nebula at the end of the universe, surviving by **swallowing floating words** — and every word you eat instantly rewrites the physics of the world around you. Eat `LIGHT` and hidden dangers are revealed; eat `GRAVITY` and everything plummets; swallow the wrong, corrupted word and the nebula turns your own controls against you. It's a race to keep language — and yourself — coherent as the void tries to feed you poison.

---

## Core Idea

*The Big Swallow* is a word that can mean many things, and *The Word-Eater* takes its most surreal interpretation: consuming **meaning itself**. Where a growth-and-consume loop simply fills a meter, here the very act of swallowing *changes the rules of the game* — each word is both food and a spell. The player is a lonely, silent Archivist keeping reality's last dictionary alive by devouring it, one glowing glyph at a time.

The genius of the concept for our studio is that **the mechanic isn't a skin over "eat things to grow" — it's a genuinely new verb: rule-modification through consumption.** Skill lies not in eating the *most*, but in eating the *right words in the right order* while a nebula actively tries to feed you corruption. It is cerebral, literary, deeply surreal, and unmistakably in our cosmic sci-fi voice — the poetic loneliness of a being at the heat-death of the universe, eating language to keep the dark from forgetting.

**Why it's the flagship over the alternatives:** it is the only interpretation of "swallow" that turns the word into a *mechanic* rather than a cosmetic reskin of a consume-to-grow loop. It is also the lowest-asset, most scalable build possible in a browser — *the words themselves are the art* — giving us maximum originality per kilobyte.

---

## Breakdown of Game Mechanics and Features

### The Core Gameplay Loop (the ~20-second cycle)
1. **Words drift** in from the screen edges toward the Archivist (a glowing mouth-glyph steered by the player).
2. You **steer into / target words** to swallow them — each fires its **effect instantly**.
3. Swallowed words drop into a **Sentence Buffer** (last 3 words). Matching a valid pattern triggers a **combo bonus**.
4. **Poison words** sabotage you if eaten — avoid, reveal, or purge them.
5. A **Coherence meter** drains constantly; good words refill it, poison drains it. Survive as the nebula escalates.

### Control Scheme
Two modes, chosen at start (single input device required for either):
- **Mouse Mode (default):** The Archivist follows the cursor with slight inertia (lerp ~0.15). Swallow by overlapping a word's hitbox. **Right-click / Spacebar = Regurgitate.**
- **Type Mode (fast-follow):** Type a word's letters to eat it at range, typing-shooter style. **Backspace = Regurgitate.**

### Mechanic 1 — The Word Dictionary (~18 effect-words)
Each good word is an instant, readable world-effect. Tuned starting values:

| Word | Effect | Numbers |
|---|---|---|
| `SLOW` | Word drift speed ×0.5 | 5s |
| `RUSH` | Drift ×1.6, +score multiplier | 4s |
| `GRAVITY` | Words accelerate toward bottom | 300 px/s² for 4s |
| `LIGHT` | Reveals disguised poison words | 6s |
| `GROW` | Swallow hitbox radius ×1.8 | 5s |
| `SHRINK` | Hitbox ×0.6 but +50% points | 5s |
| `CALM` | Freezes all words in place | 2s |
| `PURGE` | Destroys all poison on screen | instant |
| `ECHO` | Next word eaten counts twice | 1 use |
| `WARP` | Teleport Archivist to cursor | instant |

Words spawn from edges at base **90 px/s**, spawn interval starting **1.3s**, font ~28px, hitbox = text bounds + 8px pad.

### Mechanic 2 — Coherence Meter (life system)
- Range **0–100**, starts at **60**.
- Drains **4/second** passively.
- Good word: **+8** · Sentence combo: **+20** · Poison word: **−15** (plus a control-scramble).
- Hits 0 → **run ends** ("The archive forgets you").

### Mechanic 3 — Sentence Combos (skill ceiling)
The last 3 eaten words form a Buffer; matching hidden patterns pays off:
- `LIGHT + PURGE` → **CLEANSE**: clear screen + 3s invulnerability, +500.
- `GROW + RUSH + ECHO` → **FEAST**: 3s at ×3 points, +1000.
- `SLOW + CALM` → **STILLNESS**: 4s freeze + one full Coherence refill.
- 3 identical words → **MANTRA**: permanent +1 score multiplier.

A **Known Sentences codex** fills as players *discover* combos — a core replay hook.

### Mechanic 4 — Poison Words (tension)
Rendered corrupted/glitching (jitter + red-shift via canvas transforms). If eaten:
- `INVERT` — controls reversed 3s · `BLUR` — screen blur, words fade 3s · `NOISE` — spawns 4 decoy words · `MUTE` — disables Regurgitate 4s.
- Countered by `LIGHT` (reveals early) and `PURGE` / Regurgitate.

### Mechanic 5 — Regurgitate (mastery / panic move)
Spit back your last-eaten word, reversing its effect and clearing its Buffer slot. **Cooldown 3s, costs 5 Coherence.** The depth mechanic separating good players from great.

### Progression & Difficulty Curve — "Stanzas" (60s phases)
- **Stanza 1 (0:00–1:00):** spawn 1.3s, drift 90px/s, poison 8% — teaching phase.
- **Stanza 2 (1:00–2:00):** spawn 1.0s, drift 110px/s, poison 15% — first combo prompts.
- **Stanza 3 (2:00–3:00):** spawn 0.8s, drift 130px/s, poison 22%, drain 5/s.
- **Stanza 4 (3:00–4:00):** spawn 0.65s, drift 150px/s, poison 28% + a 6s **"Corruption Storm"** (all words disguised — `LIGHT` mandatory).
- **Stanza 5+ (4:00+):** ramps every 30s until unsurvivable; drain 6/s, poison caps 35%.

Each Stanza flashes a surreal intertitle (e.g. *"STANZA III: THE STATIC PSALM"*) for flavor and a breather beat.

### Win / Lose Conditions
- **Lose:** Coherence hits 0 — clean, immediate, fast restart.
- **Soft win:** Surviving to Stanza 5 unlocks the **"True Name" ending** — spell your chosen 3-word super-combo to end the run triumphantly with a large bonus.

### Scoring & Replay Hooks
- **Scoring:** +10 per good word (×multiplier), sentence bonuses, +5/second survived. End screen breakdown: Words Eaten / Sentences Formed / Longest Combo / Time Survived.
- **Hooks:** (1) **Daily Seed** — same word-soup for all players once a day, shareable seed + localStorage high score. (2) **Sentence Codex** completion as a meta-goal. (3) Escalating personal-best timer. (4) Emergent chaos from stacking effects — no two late runs are alike, at zero content cost.

---

## Breakdown of Game Art and Design

- **Everything is typography + particles.** No sprites required — the words *are* the art: glowing glyphs drifting in a black void. This is the lowest-asset build possible and gives us maximum visual identity for near-zero weight.
- **Palette:** deep indigo/black nebula background; cyan-white good words; red-magenta glitching poison words. The Coherence meter is a thin luminous "spine" down one screen edge.
- **The Archivist:** a simple procedural glyph — a slowly rotating rune/mouth built from a few Canvas arcs and a soft radial glow. Pulses on each swallow for tactile feedback.
- **Background:** procedural parallax star-dust plus faint drifting "torn page" shapes for the dead-library feel — all drawn with Canvas 2D primitives.
- **Motion & feel:** ink-blot dissolves as words are swallowed, screen-warp and blur on poison effects, gentle inertia on the Archivist. The tone shifts from silent and meditative to anxious static as Stanzas escalate.
- **Audio (cheap, generative, WebAudio):** each swallow plays a soft tonal note; forming a sentence plays a chord; a slowly evolving pad shifts key based on which word-types dominate. The soundscape *is* "the library remembering how to speak." Whispered, reversed voice fragments as ambience; a dissonant swell on poison.

---

## Production / Scope Note

- **Lowest-asset build of all candidates** (text rendering only), ships as a single self-contained HTML file on Canvas 2D.
- **MVP vertical slice:** Mouse Mode + 10 words + Coherence meter + poison + one combo type = fully playable.
- **Fast-follow additions:** Type Mode, full Sentence Codex, Daily Seed, and the "True Name" ending.

*Surreal, silent, cosmic, and mechanically original — a game about eating language to keep the dark from forgetting. Unmistakably ours.*