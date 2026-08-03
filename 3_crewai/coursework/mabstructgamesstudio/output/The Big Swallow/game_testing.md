# Game Testing Report — The Big Swallow

**Artifact:** `output/The Big Swallow/game_testing.json`  
**Test Target:** `output/The Big Swallow/index.html`  
**Overall Result:** **FAIL**  
**Status:** **BLOCKED**

Automated game tests were run first as required. The JSON artifact reports `overall=fail`, so the game is **BLOCKED** and cannot be claimed playable.

---

# Summary

- **Overall:** `fail`
- **Tier 0:** `pass`
- **Tier 1:** `fail`
- **Blocking Issue:** Tier 1 boot smoke test failed because no recognized start button click handler was found.

Evidence from test output:

```text
overall=fail
artifact=output/The Big Swallow/game_testing.json
tier0=pass
tier1=fail
tier1 issues: no start button handler found (startBtn/btnCampaign/btnZen onclick or click listener)
Do NOT claim the game is playable unless overall=pass. Report BLOCKED if tests failed.
```

---

# Tier 0 Results

**Result:** `pass`

Tier 0 validation passed according to `game_testing.json`.

Verified from JSON/tool output:

- The game file was structurally parseable enough to pass Tier 0.
- No Tier 0 blocking issue was reported by the automated test.

---

# Tier 1 Results

**Result:** `fail`

Tier 1 boot smoke testing failed.

## Tier 1 Issue

- **Issue:** No recognized start button handler was found.
- **Evidence:** `no start button handler found (startBtn/btnCampaign/btnZen onclick or click listener)`

This prevents the automated boot/click flow from confirming that the game can start correctly.

---

# Playability Contract Coverage

The playability contract is based on the supplied `game_design.md` expectations for **The Big Swallow**.

Because `overall=fail`, all runtime gameplay claims are treated as **blocked unless directly verified by the JSON artifact**.

## Verified

- **HTML/boot structure passed Tier 0**
  - **Status:** Verified
  - **Evidence:** `tier0=pass`

## Blocked

- **Game can be started from the initial screen**
  - **Status:** Blocked
  - **Evidence:** `tier1=fail`
  - **Reason:** The test could not find a recognized start button handler.

- **Mouse-only control loop**
  - **Status:** Blocked
  - **Design Contract:** Left mouse inhale, right mouse exhale, scroll wheel cone width.
  - **Reason:** Runtime play could not be confirmed because Tier 1 failed.

- **Fixed central Maw**
  - **Status:** Blocked
  - **Design Contract:** Maw remains fixed at `(480, 300)`.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Inhale cone behavior**
  - **Status:** Blocked
  - **Design Contract:** Cursor-aimed suction cone with pull force and cosine falloff.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Breath system and GASP punish**
  - **Status:** Blocked
  - **Design Contract:** Breath drains during inhale, regenerates after delay, and triggers GASP at zero.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Exhale / pellet shotgun**
  - **Status:** Blocked
  - **Design Contract:** RMB or LMB-release fires gullet pellets.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Gullet and Swallow transition**
  - **Status:** Blocked
  - **Design Contract:** Filling gullet triggers the “STILL HUNGRY” transition to the next course.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Four-course progression**
  - **Status:** Blocked
  - **Design Contract:** Bedroom → Seaside Town → Orbit → The Observer.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Finale / edible frame concept**
  - **Status:** Blocked
  - **Design Contract:** Final course involves eating UI/frame/lens/title-card elements.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

- **Instant restart**
  - **Status:** Blocked
  - **Design Contract:** Restart should be instant.
  - **Reason:** Not verified by JSON due to Tier 1 boot failure.

---

# Bugs Found

## BUG-001 — Missing Recognized Start Button Handler

**Severity:** Blocker  
**Status:** Open  
**Detected In:** Tier 1 boot smoke test  
**Evidence:**

```text
tier1=fail
tier1 issues: no start button handler found (startBtn/btnCampaign/btnZen onclick or click listener)
```

## Description

The automated Tier 1 smoke test could not find a recognized clickable start handler using the expected patterns:

- `startBtn`
- `btnCampaign`
- `btnZen`
- `onclick`
- registered `click` listener

Because of this, the game failed the boot smoke test.

## Impact

The test harness cannot confirm that the game starts. Per the testing requirement, since `overall=fail`, the game is **BLOCKED** and must not be reported as playable.

## Expected Result

The game should expose a recognizable start button or click handler that the automated Tier 1 test can detect and activate.

## Actual Result

No recognized start button handler was found.

---

# Final Verdict

**BLOCKED**

`game_testing.json` reports:

```text
overall=fail
tier0=pass
tier1=fail
```

The game cannot be claimed playable until the Tier 1 boot smoke failure is fixed and the automated tests report `overall=pass`.