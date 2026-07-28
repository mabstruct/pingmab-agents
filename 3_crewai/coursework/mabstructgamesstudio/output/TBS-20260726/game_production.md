The game has been produced through the full pipeline (concept → design → development → QA → hardening → deployment). The deployment specialist has provided the complete, ready-to-publish deployment package. Below is the final deliverable including the complete production-ready game with deployment metadata integrated into the `<head>`.

# The Big Swallow — Final Production Deliverable

*A single-player, surreal cosmic arcade survival game. Produced end-to-end: concept, design, development, QA hardening, and deployment.*

---

## Production Summary

- **Concept (Creative Strategist):** Chose *"Event Horizon Appetite"* — you **are** a newborn black hole. The signature twist: constant **Hawking-radiation decay** means you're always shrinking, so your own appetite is a countdown. *A beautiful monster racing its own death.*
- **Design (Game Designer):** Full GDD with exact formulas — cube-root mass→radius scaling, softened gravity, sublinear decay tuning, escalating object tiers (dust → asteroid → comet → moon → planet → gas giant → star → neutron star → rival black hole → **Galactic Core**), win/lose states, HUD, and difficulty curve.
- **Development (Developer):** Complete self-contained HTML5 Canvas + vanilla JS + WebAudio build. Procedural infinite parallax cosmos, gravitational lensing visuals, particle absorption, procedural audio.
- **QA (Tester):** Returned **NEEDS REFINEMENT** with 13 prioritized fixes (gravity/velocity caps to stop tunneling, NaN guards, spawn safety, early-game onboarding, rival-AI hysteresis, DPR cap, WebAudio gesture-gating, core-state clarity, etc.).
- **Refinement (Developer):** All 13 fixes applied and verified — **PASS**.
- **Deployment (Deployment Specialist):** Delivered full deployment package (Netlify/GitHub Pages/Vercel/itch.io), SEO/social metadata, and a post-deploy smoke-test checklist.

---

## How to Play

- **Move** with mouse (desktop) or drag (touch).
- **Swallow** objects smaller than you (green ring) to grow.
- **Avoid** objects larger than you (red ring) — they'll tear you apart.
- You're **constantly evaporating** via Hawking radiation — keep eating or dissipate.
- **Win** by growing to **100,000 M☉** and devouring the **Galactic Core**.

---

## Final Production-Ready Game

*Save this as `index.html` and deploy to any static host — no build step, no dependencies, no server code. The recommended deployment SEO/social `<head>` tags are integrated below.*

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>The Big Swallow</title>
<meta name="description" content="The Big Swallow is a surreal cosmic arcade survival game. Control a newborn black hole, devour smaller objects, avoid larger threats, outrun Hawking-radiation decay, and grow to swallow the Galactic Core.">
<meta name="theme-color" content="#000000">
<meta name="color-scheme" content="dark">
<meta name="robots" content="index,follow">
<!-- Open Graph -->
<meta property="og:title" content="The Big Swallow">
<meta property="og:description" content="Arcade survival in deep space: grow a black hole, avoid larger hazards, outrun Hawking decay, and devour the Galactic Core.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="The Big Swallow">
<!-- Twitter / X -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="The Big Swallow">
<meta name="twitter:description" content="Control a black hole, swallow the cosmos, and survive Hawking-radiation decay.">
<style>
  html, body {
    margin: 0; padding: 0; overflow: hidden; background: #04040a;
    width: 100%; height: 100%;
    font-family: 'Courier New', monospace;
    -webkit-user-select: none; user-select: none;
    touch-action: none;
  }
  #game { display: block; position: absolute; top: 0; left: 0; cursor: crosshair; }

  #hud {
    position: absolute; top: 12px; left: 14px; color: #cfe3ff;
    pointer-events: none; z-index: 5; text-shadow: 0 0 6px #000;
    font-size: 14px; line-height: 1.5;
  }
  #hud .label { color: #7d93c4; font-size: 11px; letter-spacing: 1px; }
  #massReadout { font-size: 20px; color: #fff; }
  #stabWrap {
    width: 220px; height: 10px; background: rgba(255,255,255,0.08);
    border: 1px solid rgba(160,190,255,0.35); border-radius: 5px;
    overflow: hidden; margin-top: 2px;
  }
  #stabBar {
    height: 100%; width: 100%;
    background: linear-gradient(90deg, #ff4d5e, #ffd76b, #4dff88);
    transition: width 0.15s linear;
  }
  #score {
    position: absolute; top: 12px; right: 14px; color: #cfe3ff; text-align: right;
    pointer-events: none; z-index: 5; text-shadow: 0 0 6px #000; font-size: 14px; line-height: 1.5;
  }

  #muteBtn {
    position: absolute; bottom: 14px; right: 14px; z-index: 20;
    pointer-events: auto;
    background: rgba(10,14,30,0.75); color: #cfe3ff;
    border: 1px solid rgba(160,190,255,0.4); border-radius: 6px;
    padding: 8px 14px; font-family: inherit; font-size: 13px; cursor: pointer;
  }
  #muteBtn:hover { background: rgba(40,55,100,0.8); }

  #overlay {
    position: absolute; inset: 0; z-index: 10;
    display: flex; align-items: center; justify-content: center; flex-direction: column;
    background: radial-gradient(ellipse at center, rgba(8,10,26,0.55) 0%, rgba(2,2,8,0.88) 100%);
    color: #e8f0ff; text-align: center;
    pointer-events: none;
    transition: opacity 0.4s;
  }
  #overlay.hidden { opacity: 0; visibility: hidden; }
  #overlay h1 {
    font-size: clamp(34px, 7vw, 64px); margin: 0 0 8px 0; letter-spacing: 6px;
    color: #fff; text-shadow: 0 0 24px #7a5cff, 0 0 60px #3a1c9e;
  }
  #overlay .sub { color: #9fb4e8; font-size: clamp(13px, 2.4vw, 17px); max-width: 640px; padding: 0 20px; }
  #overlay .rules {
    margin-top: 14px; color: #cfe3ff; font-size: clamp(12px, 2.2vw, 15px);
    max-width: 620px; padding: 8px 20px; line-height: 1.7;
    border-top: 1px solid rgba(160,190,255,0.25);
    border-bottom: 1px solid rgba(160,190,255,0.25);
  }
  #overlay .rules b.g { color: #4dff88; } #overlay .rules b.r { color: #ff4d5e; }
  #overlay .cta {
    margin-top: 22px; font-size: clamp(15px, 3vw, 20px); color: #ffd76b;
    animation: pulse 1.4s ease-in-out infinite;
  }
  @keyframes pulse { 0%,100% { opacity: 0.55; } 50% { opacity: 1; } }
  #overlay .stat { margin-top: 10px; color: #ffd76b; font-size: 16px; }
</style>
</head>
<body>
<canvas id="game"></canvas>

<div id="hud">
  <div class="label">MASS</div>
  <div id="massReadout">10 M&#9737;</div>
  <div class="label" style="margin-top:6px;">EVENT HORIZON STABILITY</div>
  <div id="stabWrap"><div id="stabBar"></div></div>
</div>
<div id="score">
  <div class="label">SCORE</div>
  <div id="scoreVal">0</div>
  <div class="label" style="margin-top:6px;">TIME</div>
  <div id="timeVal">0:00</div>
</div>

<button id="muteBtn" aria-label="Toggle sound">&#128266; SOUND ON</button>

<div id="overlay">
  <h1>THE BIG SWALLOW</h1>
  <div class="sub" id="overlaySub">You are a newborn singularity adrift in a procedural cosmos.
    Feed. Grow. Endure Hawking decay. Consume everything &mdash; even the Galactic Core itself.</div>
  <div class="rules" id="overlayRules">
    Move with <b>mouse / touch</b>. Swallow <b class="g">smaller objects (green ring)</b>.
    Avoid <b class="r">larger ones (red ring)</b>.<br>
    Grow to <b>100,000 M&#9737;</b> and eat the <b>Galactic Core</b>. Press <b>P</b> to pause.
  </div>
  <div class="stat" id="overlayStat" style="display:none;"></div>
  <div class="cta" id="overlayCta">CLICK / TAP TO BEGIN</div>
</div>

<script>
(function () {
'use strict';

/* ============================================================
   THE BIG SWALLOW — hardened final build (QA fixes 1-13 applied)
   ============================================================ */

// ---------- Canvas & DPR (FIX 8: cap DPR at 2, crisp scaling) ----------
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
let W = 0, H = 0, dpr = 1;

function resize() {
  dpr = Math.min(window.devicePixelRatio || 1, 2);
  W = window.innerWidth;
  H = window.innerHeight;
  canvas.width  = Math.floor(W * dpr);
  canvas.height = Math.floor(H * dpr);
  canvas.style.width  = W + 'px';
  canvas.style.height = H + 'px';
}
window.addEventListener('resize', resize);
resize();

// ---------- Tunables (core formulas UNCHANGED) ----------
const G = 1400;
const SOFT = 900;
const MAX_GRAV_ACCEL = 6000;
const MAX_OBJ_SPEED  = 900;
const MAX_PARTICLES  = 450;
const EARLY_SAFE_TIME = 12;
const DECAY_GRACE = 4;
const THREAT_MIN_SPAWN_DIST = 900;
const WIN_MASS = 100000;
const CORE_SPAWN_MASS = 60000;
const TARGET_OBJECTS = 26;

const playerRadius = M => 6 + 14 * Math.cbrt(Math.max(M, 0) / 10);

// ---------- Game state ----------
let state = 'start';
let elapsed = 0;
let score = 0;
let shake = 0;
let coreWarnCooldown = 0;

const player = { x: 0, y: 0, vx: 0, vy: 0, M: 10 };
let objects = [];
let particles = [];
let messages = [];
let core = null;
let rivalSpawnTimer = 0;

const mouse = { x: 0