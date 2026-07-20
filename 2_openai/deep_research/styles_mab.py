EXAMPLES = [
    "Most popular AI Agent frameworks in 2026",
    "Most commercially successful Agentic AI implementations in 2026",
    "Landscape analysis of embodied AI research frontiers",
]

HEADER_HTML = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap" rel="stylesheet">

<div class="mab-shell">
    <div class="mab-brand glass">
        <div class="mab-brand-top">
            <div class="mab-mark">
                <span class="mab-mark-cyan"></span>
                <span class="mab-mark-violet"></span>
                <span class="mab-mark-pink"></span>
            </div>
            <div class="mab-status">
                <span class="mab-pulse" aria-hidden="true"></span>
                Autonomous research engine active
            </div>
        </div>
        <div class="mab-titles">
            <h1>MABSTRUCT<span class="mab-sep"> / </span>CONSTRUCT</h1>
            <p>Deep Research · Multi-search web investigation</p>
        </div>
    </div>
</div>
"""

CSS = """
@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&family=Syne:wght@600;700;800&display=swap");

:root {
    --mab-bg: #050507;
    --mab-bg-glow-1: rgba(168, 85, 247, 0.14);
    --mab-bg-glow-2: rgba(6, 182, 212, 0.10);
    --mab-surface: rgba(255, 255, 255, 0.04);
    --mab-glass: rgba(255, 255, 255, 0.06);
    --mab-border: rgba(255, 255, 255, 0.08);
    --mab-border-strong: rgba(255, 255, 255, 0.14);
    --mab-text: rgba(255, 255, 255, 0.88);
    --mab-muted: rgba(255, 255, 255, 0.68);
    --mab-dim: rgba(255, 255, 255, 0.50);
    --mab-cyan: #06b6d4;
    --mab-violet: #8b5cf6;
    --mab-emerald: #10b981;
    --mab-pink: #ec4899;
    --mab-font: "Manrope", ui-sans-serif, system-ui, -apple-system, sans-serif;
    --mab-display: "Syne", ui-sans-serif, system-ui, sans-serif;
    --mab-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;

    /* Override Gradio Base (light) theme tokens so text stays readable on dark bg */
    --body-text-color: var(--mab-text);
    --block-label-text-color: var(--mab-muted);
    --block-title-text-color: #fff;
    --block-info-text-color: var(--mab-dim);
    --input-text-color: #fff;
    --button-primary-text-color: #fff;
    --button-secondary-text-color: var(--mab-text);
    --body-background-fill: transparent;
    --background-fill-primary: var(--mab-surface);
    --background-fill-secondary: var(--mab-surface);
    --block-background-fill: transparent;
    --block-border-color: var(--mab-border-strong);
    --panel-background-fill: transparent;
    --color-accent: var(--mab-cyan);
}

html {
    min-height: 100%;
    background-color: var(--mab-bg);
}

body,
gradio-app,
.app,
.main,
.wrap,
.contain,
.gradio-container {
    background: transparent !important;
}

body {
    min-height: 100vh;
    margin: 0;
    background:
        radial-gradient(circle at 18% 12%, var(--mab-bg-glow-1), transparent 42%),
        radial-gradient(circle at 82% 8%, var(--mab-bg-glow-2), transparent 38%),
        var(--mab-bg) !important;
    background-attachment: fixed;
    color: var(--mab-text) !important;
    font-family: var(--mab-font) !important;
    -webkit-font-smoothing: antialiased;
}

.gradio-container {
    max-width: 1080px !important;
    margin: 0 auto !important;
    padding: 2.5rem 2rem 4rem !important;
    color: var(--mab-text) !important;
    font-family: var(--mab-font) !important;
}

.gradio-container .markdown,
.gradio-container .prose,
.gradio-container label,
.gradio-container p,
.gradio-container span,
.gradio-container li {
    color: var(--mab-text);
}

/* === HEADER === */
.mab-shell { margin-bottom: 2rem; }

.glass, .mab-brand.glass {
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--mab-border-strong);
    border-radius: 1rem;
    box-shadow:
        0 0 0 1px rgba(255, 255, 255, 0.04),
        0 20px 60px -20px rgba(0, 0, 0, 0.7);
    padding: 1.35rem 1.5rem;
}

.mab-brand-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.1rem;
}

.mab-mark {
    display: flex;
    align-items: center;
    gap: 6px;
}

.mab-mark span {
    display: block;
    width: 10px;
    height: 10px;
    border-radius: 999px;
}

.mab-mark-cyan { background: var(--mab-cyan); box-shadow: 0 0 12px rgba(6, 182, 212, 0.55); }
.mab-mark-violet { background: var(--mab-violet); box-shadow: 0 0 12px rgba(139, 92, 246, 0.45); }
.mab-mark-pink { background: var(--mab-pink); box-shadow: 0 0 12px rgba(236, 72, 153, 0.35); }

.mab-status {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    font-family: var(--mab-mono);
    font-size: 0.68rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--mab-dim);
}

.mab-pulse {
    width: 7px;
    height: 7px;
    border-radius: 999px;
    background: var(--mab-emerald);
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.55);
    animation: mab-pulse 2s infinite;
}

@keyframes mab-pulse {
    0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.55); }
    70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
    100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
}

.mab-titles h1 {
    font-family: var(--mab-display);
    font-size: clamp(1.75rem, 4vw, 2.75rem);
    font-weight: 800;
    letter-spacing: -0.03em;
    margin: 0;
    line-height: 1;
    color: #fff;
}

.mab-sep {
    color: var(--mab-dim);
    font-weight: 600;
}

.mab-titles p {
    margin: 0.7rem 0 0;
    font-size: 0.92rem;
    color: var(--mab-muted);
    letter-spacing: 0.01em;
}

/* === QUERY ROW === */
.dr-query-row {
    gap: 0 !important;
    align-items: stretch !important;
}

#dr-query, #dr-query > div, #dr-query .wrap, #dr-query .form, #dr-query .block {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}

#dr-query textarea, #dr-query input {
    background: rgba(255, 255, 255, 0.04) !important;
    color: #fff !important;
    border: 1px solid var(--mab-border-strong) !important;
    border-radius: 0.85rem 0 0 0.85rem !important;
    padding: 1.05rem 1.2rem !important;
    font-size: 1rem !important;
    font-family: var(--mab-font) !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03) !important;
    line-height: 1.45 !important;
    resize: none !important;
    min-height: 56px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}

#dr-query textarea:focus, #dr-query input:focus {
    outline: none !important;
    border-color: rgba(6, 182, 212, 0.55) !important;
    box-shadow:
        0 0 0 1px rgba(6, 182, 212, 0.25),
        0 0 24px rgba(6, 182, 212, 0.12) !important;
}

#dr-query textarea::placeholder, #dr-query input::placeholder {
    color: var(--mab-dim) !important;
    opacity: 1 !important;
}

#dr-run {
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.95), rgba(139, 92, 246, 0.95)) !important;
    color: #fff !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-left: none !important;
    border-radius: 0 0.85rem 0.85rem 0 !important;
    font-family: var(--mab-display) !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    font-size: 0.92rem !important;
    box-shadow: 0 10px 30px -12px rgba(6, 182, 212, 0.55) !important;
    transition: transform 0.12s, box-shadow 0.2s, filter 0.2s !important;
    min-width: 160px !important;
    padding: 1rem 1.5rem !important;
}

#dr-run:hover {
    filter: brightness(1.06) !important;
    box-shadow: 0 14px 36px -10px rgba(139, 92, 246, 0.55) !important;
}

#dr-run:active { transform: translateY(1px) !important; }

/* === EXAMPLES === */
.dr-examples-label {
    font-family: var(--mab-mono);
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    color: var(--mab-dim);
    text-transform: uppercase;
    margin: 2rem 0 0.85rem 0;
    display: flex;
    align-items: center;
    gap: 0.85rem;
}

.dr-examples-label::after {
    content: "";
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--mab-border-strong), transparent);
}

#dr-examples, #dr-examples > div, #dr-examples .wrap, #dr-examples .block {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    box-shadow: none !important;
}

#dr-examples label, #dr-examples .label-wrap, #dr-examples > div > .label-wrap {
    display: none !important;
}

#dr-examples table {
    border-collapse: separate !important;
    border-spacing: 0 !important;
    width: auto !important;
    background: transparent !important;
    border: none !important;
}

#dr-examples thead { display: none !important; }
#dr-examples tbody { background: transparent !important; }

#dr-examples tr {
    background: transparent !important;
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
    border: none !important;
}

#dr-examples td, #dr-examples button {
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid var(--mab-border-strong) !important;
    padding: 0.72rem 1.05rem !important;
    cursor: pointer !important;
    transition: border-color 0.2s, background 0.2s, transform 0.12s, color 0.2s !important;
    font-size: 0.88rem !important;
    color: var(--mab-text) !important;
    border-radius: 999px !important;
    margin: 0 !important;
    text-align: left !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03) !important;
}

#dr-examples td:hover, #dr-examples button:hover {
    background: rgba(255, 255, 255, 0.07) !important;
    border-color: rgba(139, 92, 246, 0.45) !important;
    color: #fff !important;
    transform: translateY(-1px);
}

/* === REPORT === */
#dr-report {
    margin-top: 2.5rem !important;
    padding: 0 !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: var(--mab-text) !important;
    min-height: 40px;
}

#dr-report > div,
#dr-report .prose,
#dr-report .markdown,
#dr-report article {
    background: transparent !important;
    color: var(--mab-text) !important;
}

#dr-report,
#dr-report *:not(a):not(th):not(code) {
    color: var(--mab-text) !important;
}

#dr-report:not(:empty) {
    border-top: 1px solid var(--mab-border-strong) !important;
    padding-top: 1.75rem !important;
}

#dr-report h1 {
    font-family: var(--mab-display);
    font-size: 1.85rem;
    font-weight: 800;
    color: #fff !important;
    border-bottom: 1px solid var(--mab-border-strong);
    padding-bottom: 0.55rem;
    margin: 1.5rem 0 1rem;
    letter-spacing: -0.02em;
}

#dr-report h2 {
    font-family: var(--mab-display);
    font-size: 1.3rem;
    color: #fff !important;
    font-weight: 700;
    margin-top: 1.75rem;
    letter-spacing: -0.015em;
}

#dr-report h3 {
    font-family: var(--mab-display);
    font-size: 1.08rem;
    color: rgba(255, 255, 255, 0.92) !important;
    font-weight: 600;
    margin-top: 1.5rem;
}

#dr-report p, #dr-report li, #dr-report td {
    color: var(--mab-muted) !important;
    line-height: 1.7;
}

#dr-report strong, #dr-report b {
    color: #fff !important;
}

#dr-report a {
    color: var(--mab-cyan) !important;
    text-decoration: none;
    border-bottom: 1px solid rgba(6, 182, 212, 0.35);
    transition: color 0.15s, border-color 0.15s;
}

#dr-report a:hover {
    color: #fff !important;
    border-color: rgba(139, 92, 246, 0.55);
}

#dr-report code {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--mab-border);
    padding: 0.12rem 0.4rem;
    font-size: 0.88em;
    border-radius: 0.35rem;
    color: rgba(255, 255, 255, 0.9) !important;
}

#dr-report pre {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--mab-border-strong);
    border-radius: 0.75rem;
    padding: 1rem 1.25rem;
    overflow-x: auto;
}

#dr-report blockquote {
    border-left: 3px solid rgba(139, 92, 246, 0.5) !important;
    background: rgba(255, 255, 255, 0.03);
    padding: 0.85rem 1.1rem;
    margin: 1rem 0;
    color: var(--mab-muted) !important;
    font-style: italic;
    border-radius: 0 0.5rem 0.5rem 0;
}

#dr-report ul, #dr-report ol { padding-left: 1.5rem; }
#dr-report li { margin: 0.3rem 0; }

#dr-report table {
    border-collapse: collapse;
    border: 1px solid var(--mab-border-strong);
    border-radius: 0.75rem;
    overflow: hidden;
}

#dr-report th, #dr-report td {
    border: 1px solid var(--mab-border);
    padding: 0.55rem 0.85rem;
    text-align: left;
}

#dr-report th {
    background: rgba(255, 255, 255, 0.05);
    font-family: var(--mab-display);
    font-weight: 700;
    color: var(--mab-cyan) !important;
}

#dr-report hr {
    border: none;
    border-top: 1px solid var(--mab-border-strong);
    margin: 1.5rem 0;
}

footer { display: none !important; }

@media (max-width: 700px) {
    .gradio-container { padding: 1.5rem 1rem 3rem !important; }
    .dr-query-row { flex-direction: column !important; }
    #dr-query textarea, #dr-query input {
        border-radius: 0.85rem 0.85rem 0 0 !important;
    }
    #dr-run {
        border-left: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-top: none !important;
        border-radius: 0 0 0.85rem 0.85rem !important;
        width: 100% !important;
    }
}
"""

JS = """
() => {
    const focus = () => {
        const el = document.querySelector("#dr-query textarea, #dr-query input");
        if (el) { el.focus(); return true; }
        return false;
    };
    if (!focus()) {
        let tries = 0;
        const i = setInterval(() => {
            if (focus() || ++tries > 20) clearInterval(i);
        }, 100);
    }
}
"""
