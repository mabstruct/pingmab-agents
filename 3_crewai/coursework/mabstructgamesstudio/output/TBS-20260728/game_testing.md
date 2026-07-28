# The Big Swallow — Browser Game Test Report

**Test artifact:** `output/The Big Swallow/game_testing.json`  
**Build under test:** `output/The Big Swallow/index.html`  
**Result source:** Automated `Run game tests` output only

## Overall Result

**Overall: FAIL**

**Status: BLOCKED**

The automated test artifact reports `overall=fail`. Per test requirements, the game must be reported as **BLOCKED** and must not be claimed playable.

## Tier Results

### Tier 0 — Parse / Structure

**Result: PASS**

Evidence from `game_testing.json` / tool output:

- `tier0=pass`

### Tier 1 — Boot Smoke

**Result: FAIL**

Evidence from `game_testing.json` / tool output:

- `tier1=fail`
- Runtime load error:

```text
addEventListener is not defined
```

Because Tier 1 failed during runtime load, boot/play interaction could not be verified.

## Boot Click Results

**Result: BLOCKED**

Boot click behavior could not be verified because the game failed Tier 1 boot smoke with a runtime load error:

```text
addEventListener is not defined
```

No gameplay observations are available from the automated test output.

## Playability Contract Coverage

Compared against the playability expectations described in `game_design.md`.

### Verified

- **HTML / script parse and structure smoke:** Verified by `tier0=pass`.

### Unverified / Blocked

The following contract items are **blocked** because Tier 1 failed before playable boot could be confirmed:

- **Game boots successfully in browser context**
- **First user interaction / boot click works**
- **Core inhale mechanic**
- **Belch propulsion**
- **Gut queue and digestion**
- **Void Charge behavior**
- **Swallow size gate**
- **Fold / tier progression**
- **The Other Mouth behavior**
- **Damage, recovery, death, and win states**
- **Audio initialization on first gesture**
- **No playable runtime regression after load**

No gameplay mechanics can be reported as working because the automated tests did not reach a playable state.

## Bugs Found

### BUG-001 — Runtime load failure blocks Tier 1 boot

**Severity:** Blocker  
**Status:** Open  
**Evidence:** `game_testing.json` / automated test output

```text
tier1=fail
runtime load error: addEventListener is not defined
```

**Impact:**

- The game fails boot smoke testing.
- Boot click behavior cannot be verified.
- Playability contract coverage is blocked.
- The game cannot be reported playable.

## Final Assessment

**BLOCKED**

`output/The Big Swallow/game_testing.json` reports `overall=fail` due to a Tier 1 runtime load error:

```text
addEventListener is not defined
```

The game must not be considered playable until this runtime error is fixed and automated tests pass.