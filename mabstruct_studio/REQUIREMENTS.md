# MABSTRUCT Studio — Requirements & Architecture Decisions

Status: **draft**, opened 2026-08-31. Living document — requirements below the line are
agreed intent; architecture decisions are proposals until marked ACCEPTED.

## Context

`mabstruct_studio.ipynb` proved the pipeline end to end:

```
IDEATION --> DESIGN --> DEVELOP --> DEPLOY(here.now)
```

It works, and it has taught us what the notebook cannot do:

- Every run starts from zero. Ideas exist only in kernel memory and are lost on restart.
- Idea selection is a hand-edited constant (`CHOSEN_IDEA_INDEX`), not a decision point.
- Nothing records that an idea was designed, built, or shipped — or how good the result was.
- Several develop-model comparisons (Opus vs Fable) were run, and the comparison lives
  only in the operator's head.
- Deploy overwrote one URL repeatedly because identity was carried by a copied file.

The next step is a **MABSTRUCT Studio application** that keeps the same LangGraph pipeline
but wraps it in persistence, a human decision point, and a feedback loop — so the studio
gets better at making games over time instead of restarting each session.

The notebook remains the reference implementation and the place to spike new phases.

---

## Requirements

Original lettering from the requirement package is kept in brackets for traceability.

### R1 — Ideas persist [a]

Game ideas survive process restart and are addressable later. Ideation writes every idea
it generates, not just the chosen one — rejected ideas are the comparison set for R7.

### R2 — Human-in-the-loop before DESIGN [b]

The pipeline pauses after IDEATION. A human browses stored ideas and selects which one
proceeds to DESIGN. The run resumes from that selection rather than restarting.

*Implication:* the pause must survive the UI session — the human may decide days later.

### R3 — Lifecycle status per idea [c]

Each idea carries an explicit status: `ideated → designed → developed → deployed`, plus
terminal/exceptional states (e.g. `rejected`, `failed`). Status is queryable and drives
what the UI offers for that idea.

*Open:* is status a single enum, or one timestamp per stage? A stage-timestamp model
also answers "how long does design take" and survives re-runs better. **Leaning: per-stage
records, with status derived.**

### R4 — Feedback loop after deploy [d]

After a game is deployed, a human can submit feedback against that specific build. That
feedback can be fed back into the pipeline to produce a refurbished version of the game.

*Open:* does refurbishment re-enter at DESIGN (rework the brief) or at DEVELOP (patch the
build)? These produce different artifacts and different lineage. **Leaning: both, as
distinct actions the human picks.**

### R5 — Learnings persist across games [e]

Lessons from every game development accumulate, so later games are produced better and
faster. This is the requirement that makes the studio compound rather than repeat.

*Open — the biggest one.* Mechanism is undecided. Candidates:
1. **Curated rules** appended to phase prompts (explicit, reviewable, manual to maintain).
2. **Few-shot exemplars** — feed the current best games as reference implementations.
3. **Retrieved learnings** — a Store with semantic search, queried at DESIGN/DEVELOP time.

These are not exclusive. (1) is cheapest and should probably come first; (3) is the
LangGraph-native answer and the most speculative. Do not build (3) before there is enough
history to retrieve from.

### R6 — Ideas grouped by game title [f]

The initial game title is the grouping key. All ideas generated for "The Big Swallow"
belong to that title, across runs and across time.

### R7 — Leaderboard and production candidate [g]

Where several ideas exist for one title, they are ranked. The top-ranked build is the
**production candidate** — always exactly one per title.

*Open — must be answered before this can be built.* What defines "best"? The ranking
signal is undecided:

| Candidate signal | Cheap? | Honest? |
| --- | --- | --- |
| Human rating from R4 feedback | yes | yes, but sparse and subjective |
| Tier-0 / Tier-1 automated validation | yes | measures "not broken", not "good" |
| Playtest telemetry (session length, retries) | needs instrumentation in the game | strongest signal, most work |
| LLM-as-judge on the built game | moderate | unproven for playability |

Ranking almost certainly needs a composite. **This requirement is blocked on defining the
score, not on building the table.**

---

## Architecture decisions

Proposals with rationale. Alternatives are recorded because the reasoning matters more
than the conclusion — revisit these when an assumption changes.

### AD1 — Three persistence layers, kept separate — PROPOSED

The pipeline needs three different kinds of memory, and conflating them is the main risk
in this design.

| Layer | Technology | Holds | Serves |
| --- | --- | --- | --- |
| Checkpointer | `SqliteSaver` (Postgres later) | graph state snapshots per thread | R2 |
| **Domain DB** | own relational schema | titles, ideas, designs, builds, deployments, feedback, scores | R1, R3, R4, R6, R7 |
| Store | LangGraph Store (KV, optional vectors) | cross-run learnings | R5 |

**Rationale.** LangGraph's own docs draw this line: checkpointers persist a *thread's*
state for short-term memory, HIL, and time travel; Stores persist application data *across*
threads for long-term memory. Neither is a queryable domain model. "All ideas for title X
ranked by score, with status" is a relational query against a schema we own — trying to
serve it from checkpoint blobs or KV namespaces means scanning and reassembling state that
was never indexed for it.

**Consequence.** The domain schema — not the graph — becomes the durable asset. The
notebook's `memory.db` stays disposable; the domain DB does not.

**Alternative rejected:** single SQLite file used as checkpointer *and* idea repository.
Cheaper on day one, but R7's ranking and R3's status queries have no good implementation
over checkpoint rows.

### AD2 — Keep LangGraph as the pipeline engine — PROPOSED

No change of engine. The phase nodes, prompts, structured outputs, and the chunked
HTML-writing tool contract port from the notebook as-is.

**Rationale.** The expensive knowledge in this project is in the develop phase — model
config, streaming at high `max_tokens`, retry middleware, the `start → js × N → end` tool
protocol, Tier-0 validation. That is all LangGraph/LangChain-shaped and should not be
rewritten to move house.

### AD3 — FastAPI service in front of the graph — PROPOSED

The pipeline runs behind an HTTP API rather than in the UI process.

**Rationale.** Two properties force it:
- **R2 pauses for a human.** `interrupt()` + `Command(resume=...)` persists the pause to
  the checkpointer, so the resume can happen in a different process, hours later. That is
  only worth anything if something outlives the UI session.
- **Develop runs take minutes.** They need to be background jobs with streamed progress,
  not blocking request handlers.

It also decouples AD4 — the frontend becomes swappable behind a stable contract.

**Alternative rejected:** UI calls the graph in-process. Simpler, but couples run lifetime
to session lifetime and makes AD4 irreversible.

*Open:* self-hosted FastAPI vs LangGraph Platform's own server (which supplies persistence,
runs, and streaming out of the box). Worth an explicit evaluation before writing endpoints
by hand — the studio's needs may be close to what it already provides.

### AD4 — TypeScript + Vite frontend — PROPOSED

**Rationale.** The requirement set is app-shaped, not form-shaped: a leaderboard (R7),
status-filtered idea browsing (R3, R6), an embedded playable build, a feedback form (R4),
and live run progress. Gradio is excellent for a single input/output surface and gets
awkward across several stateful views. Vite is already used in this repo at
`6_mcp/frontend/`, so the toolchain is not foreign.

**Alternative considered:** Gradio. Faster to a working screen and Python-only — a real
advantage. Recommended *only* as a throwaway scaffold against the AD3 API while the real
frontend is built; not as the destination, because the leaderboard and preview views are
where it would be rewritten anyway.

**Consequence.** Two languages in the project. Accepted deliberately: AD3 makes the
boundary explicit, and the API contract is the thing worth getting right.

### AD5 — Deployment identity is owned by the domain DB — PROPOSED

The here.now slug for a build is recorded in the domain DB, not in a file inside the build
output directory.

**Rationale.** The notebook writes `dev-output/<title>/<idea_id>/herenow.json`. Copying a
build folder copies its slug, so distinct games silently claim one URL and overwrite each
other — this happened, and three builds ended up pointing at one site. Identity must live
where it cannot be duplicated by a filesystem copy.

*Depends on:* the open question of what owns a stable playtest URL — the title, the idea,
or an explicit build label. Deferred to the deploy review session (see below).

---

## Open questions blocking work

| # | Question | Blocks |
| --- | --- | --- |
| Q1 | What score defines the "best" game? | R7 |
| Q2 | What mechanism carries learnings forward? | R5 |
| Q3 | Does refurbishment re-enter at DESIGN or DEVELOP? | R4 |
| Q4 | What owns a stable playtest URL — title, idea, or build label? | AD5 |
| Q5 | Self-hosted FastAPI or LangGraph Platform server? | AD3 |

## Parked

- **Deploy-phase review session.** Slug identity (Q4), the three colliding registries in
  `dev-output/`, and the stale build currently live at `hazy-hazel-6pws`. Deliberately
  deferred — see the session recap of 2026-08-31.
- **here.now version history** requires a paid plan, so overwrites are not restorable.
  Relevant input to Q4.
- **CLAUDE.md is stale** on state fields, cell numbers, and the deployment phase.

## Notes

- The notebook stays the spike environment. Port *from* it into the app; do not fork it.
- `mabstruct_experimenting.ipynb` still holds the parallel `Send` fan-out and the Tier-1
  smoke test — both become relevant again once the app runs multiple ideas per title (R7).
