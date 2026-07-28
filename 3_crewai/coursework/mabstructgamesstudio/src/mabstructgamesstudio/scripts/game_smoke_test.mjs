#!/usr/bin/env node
/**
 * Tier 1 smoke test: execute inline game JS in a minimal DOM shim and
 * simulate clicking a start button. Prints JSON to stdout.
 */
import fs from "node:fs";
import vm from "node:vm";

const htmlPath = process.argv[2];
if (!htmlPath) {
  console.log(JSON.stringify({ pass: false, issues: ["usage: node game_smoke_test.mjs <index.html>"] }));
  process.exit(1);
}

const html = fs.readFileSync(htmlPath, "utf8");
const scriptBlocks = [...html.matchAll(/<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi)].map(
  (match) => match[1],
);

const htmlIds = [...html.matchAll(/\bid=["']([^"']+)["']/gi)].map((match) => match[1]);

const result = {
  pass: false,
  issues: [],
  checks: {
    script_blocks: scriptBlocks.length,
    boot_clicked: false,
    start_hidden: false,
    runtime_error: null,
    clicked_id: null,
  },
};

if (scriptBlocks.length !== 1) {
  result.issues.push(`expected 1 inline script block, found ${scriptBlocks.length}`);
  console.log(JSON.stringify(result));
  process.exit(0);
}

const nodes = {};
const listeners = {};

function makeClassList() {
  const classes = new Set();
  return {
    add(...names) {
      names.forEach((name) => classes.add(name));
    },
    remove(...names) {
      names.forEach((name) => classes.delete(name));
    },
    toggle(name) {
      if (classes.has(name)) classes.delete(name);
      else classes.add(name);
    },
    contains(name) {
      return classes.has(name);
    },
  };
}

function makeGradient() {
  return { addColorStop() {}, addStop() {} };
}

function makeContext2D() {
  const ctx = {
    canvas: { width: 800, height: 600 },
    fillStyle: "#000",
    strokeStyle: "#000",
    lineWidth: 1,
    globalAlpha: 1,
    font: "16px sans-serif",
    textAlign: "start",
    textBaseline: "alphabetic",
    save() {},
    restore() {},
    beginPath() {},
    closePath() {},
    moveTo() {},
    lineTo() {},
    arc() {},
    rect() {},
    fill() {},
    stroke() {},
    clip() {},
    clearRect() {},
    fillRect() {},
    strokeRect() {},
    fillText() {},
    strokeText() {},
    measureText(text) {
      return { width: String(text).length * 8 };
    },
    setTransform() {},
    transform() {},
    translate() {},
    rotate() {},
    scale() {},
    createLinearGradient() {
      return makeGradient();
    },
    createRadialGradient() {
      return makeGradient();
    },
    createPattern() {
      return {};
    },
    drawImage() {},
    getImageData() {
      return { data: new Uint8ClampedArray(4) };
    },
    putImageData() {},
  };
  return ctx;
}

function makeElement(id) {
  const el = {
    id,
    className: "",
    classList: makeClassList(),
    style: { display: "flex" },
    textContent: "",
    innerHTML: "",
    width: 800,
    height: 600,
    hidden: false,
    onclick: null,
    addEventListener(type, handler, _opts) {
      listeners[`${id}:${type}`] = handler;
    },
    removeEventListener() {},
    getContext(type) {
      if (type === "2d") return makeContext2D();
      return makeContext2D();
    },
    appendChild(child) {
      return child;
    },
    removeChild() {},
    setAttribute() {},
    getAttribute() {
      return null;
    },
    contains() {
      return false;
    },
    focus() {},
    blur() {},
  };
  nodes[id] = el;
  return el;
}

const document = {
  getElementById(id) {
    return nodes[id] || makeElement(id);
  },
  createElement(tag) {
    return makeElement(tag);
  },
  querySelector() {
    return null;
  },
  querySelectorAll() {
    return [];
  },
  body: makeElement("body"),
};

for (const id of new Set([...htmlIds, "c", "game", "canvas", "btnCampaign", "btnZen", "start", "startBtn", "restartBtn", "startScreen"])) {
  document.getElementById(id);
}

const rafQueue = [];
const window = {
  innerWidth: 800,
  innerHeight: 600,
  devicePixelRatio: 1,
  addEventListener(type, handler) {
    listeners[`window:${type}`] = handler;
  },
  removeEventListener() {},
  requestAnimationFrame(fn) {
    rafQueue.push(fn);
  },
  cancelAnimationFrame() {},
};

// Browsers expose these on the global object; bare calls are common in game scripts.
const browserGlobals = {
  addEventListener(type, handler, options) {
    window.addEventListener(type, handler, options);
  },
  removeEventListener(type, handler, options) {
    window.removeEventListener(type, handler, options);
  },
  requestAnimationFrame(fn) {
    return window.requestAnimationFrame(fn);
  },
  cancelAnimationFrame(id) {
    window.cancelAnimationFrame(id);
  },
  get innerWidth() {
    return window.innerWidth;
  },
  get innerHeight() {
    return window.innerHeight;
  },
  get devicePixelRatio() {
    return window.devicePixelRatio;
  },
};

const sandbox = {
  document,
  window,
  ...browserGlobals,
  console,
  Math,
  Date,
  performance: { now: () => 0 },
  setTimeout(fn) {
    fn();
  },
  clearTimeout() {},
  setInterval() {},
  clearInterval() {},
  navigator: { userAgent: "smoke-test" },
  location: { search: "", href: "http://localhost/" },
  AudioContext: undefined,
  webkitAudioContext: undefined,
  Path2D: class Path2D {
    add() {}
  },
  Image: class Image {},
  HTMLElement: function HTMLElement() {},
};

try {
  vm.runInNewContext(scriptBlocks[0], sandbox, { timeout: 5000 });
} catch (error) {
  result.issues.push(`runtime load error: ${error.message}`);
  console.log(JSON.stringify(result));
  process.exit(0);
}

const startButtonIds = [
  "startBtn",
  "btnCampaign",
  "btnZen",
  "btnStart",
  "playBtn",
  "startButton",
];

function dispatchClick(id) {
  const node = nodes[id];
  if (!node) return false;
  if (typeof node.onclick === "function") {
    node.onclick({ preventDefault() {}, button: 0 });
    return true;
  }
  const clickHandler = listeners[`${id}:click`];
  if (typeof clickHandler === "function") {
    clickHandler({ preventDefault() {}, button: 0 });
    return true;
  }
  return false;
}

try {
  let clicked = false;
  for (const id of startButtonIds) {
    if (dispatchClick(id)) {
      clicked = true;
      result.checks.boot_clicked = true;
      result.checks.clicked_id = id;
      break;
    }
  }
  if (!clicked) {
    result.issues.push(
      "no start button handler found (startBtn/btnCampaign/btnZen onclick or click listener)",
    );
  }

  const overlayIds = ["start", "startScreen", "start-screen", "overlay"];
  for (const id of overlayIds) {
    const overlay = nodes[id];
    if (!overlay) continue;
    if (overlay.classList.contains("hidden") || overlay.style.display === "none") {
      result.checks.start_hidden = true;
      break;
    }
  }
} catch (error) {
  result.issues.push(`boot click error: ${error.message}`);
  result.checks.runtime_error = error.message;
}

if (result.checks.boot_clicked && !result.checks.runtime_error) {
  result.pass = result.issues.length === 0;
}

console.log(JSON.stringify(result));
