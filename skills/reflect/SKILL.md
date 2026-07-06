---
name: page-reflect
description: PAGE Stage 8 — Post-pilot reflection for an educational plugin built with PAGE. Harvests what the pilot's gates, feedback, and failures revealed, turns each into a proposed improvement to the new plugin AND, where general, into a new or amended lesson in PAGE's own lessons_learned.md. Triggers - after the new plugin's first real pilot, or when the user says "reflect on the pilot / harvest lessons".
version: "1.0"
---

# PAGE Stage 8: Reflect

The loop that made POSED improve across 14 releases instead of staying v1.0. Runs after
the new plugin's first real pilot (and any later one on request). Nothing here
auto-applies — every harvested item is an approve-per-item decision (L5, L9).

## Harvest sources

1. **Gate decision files.** Every revise/regenerate with its comments — what did the
   human keep correcting? Repeated corrections are skill defects, not user quirks.
2. **Review logs.** Findings that recurred across skills or rounds; rubric dimensions
   that never discriminated (always full marks = dead weight — skill-creator's
   "non-discriminating assertions" insight applies to rubrics too).
3. **The human's own words.** Verbatim complaints and praise from the pilot session;
   preserve exact phrasing — it's the RED-scenario material for the next test pass.
4. **Process breaks.** Places the pipeline stalled, was bypassed, or needed manual
   rescue.

## Triage each finding into exactly one ledger row

| Field | Content |
|---|---|
| finding | What happened, with source (gate file / quote / log) |
| scope | `plugin` (fix this plugin) / `page` (general lesson for all educational plugins) / `both` |
| proposal | The concrete change (skill text, rubric, gate, architecture) |
| cost | Small edit / new release / architecture change |

**Scope discipline for lessons:** promote a finding to PAGE's `lessons_learned.md` only
if it would plausibly bite a *different* educational plugin; one-plugin quirks stay
local. When promoting, follow the ledger format there (rule / failure that taught it /
enforcement point) and link the enforcement into the relevant PAGE skill in the same
release.

## Gate

Present the ledger item by item (approve / defer / reject, with comment). Approved
`plugin`-scope items feed the plugin's next release via its own changelog; approved
`page`-scope items become a PAGE release (which follows `page-release` itself — PAGE
eats its own dog food).

## Also harvest the human's preferences

Pilot decisions often reveal durable preferences (voice, pacing, gate appetite). Offer —
never assume — to record them in the plugin's persona/preferences artifact so the next
run starts closer to right. Contested pedagogical stances stay per-run choices (L2);
preferences about *interaction with the tool* may persist.
