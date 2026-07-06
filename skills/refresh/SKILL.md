---
name: page-refresh
description: PAGE maintenance — periodic (~90-day) refresh of PAGE's own knowledge. Checks for new skill/plugin-authoring best practices, new educational frameworks worth adding to the grounding library, and new AI capabilities that change what educational plugins can offer. Presents findings as an approve-per-item ledger; never auto-applies. Triggers - when ~90 days have passed since the last refresh, or the user says "refresh PAGE" or asks whether the authoring guidance is still current.
version: "1.0"
---

# PAGE Refresh

PAGE encodes three snapshots that go stale at different speeds (L9): authoring practice
(fast — the harness vendors iterate), AI capabilities (fast), educational frameworks
(slow). Check `last_refresh` in this file's footer; if ~90 days have passed, offer a
refresh when PAGE is next invoked. Never run one un-asked.

## Part A — Authoring practice

Check the primary sources for changes since the last refresh:

- Anthropic's skill-creator (anthropics/skills) — lifecycle, writing doctrine, eval
  mechanics.
- The official plugin-dev plugin (anthropics/claude-code) — plugin structure, manifest
  fields, validation tooling, marketplace requirements.
- obra's writing-skills (obra/superpowers) — the TDD-for-skills methodology.
- Harness release notes (Claude Code, Codex) for plugin/skill mechanism changes —
  especially manifest schema changes, which break lockstep silently.

## Part B — Grounding library

Search for new or newly prominent educational frameworks in the domains the library
covers (curriculum design, learning science, assessment, communication). Bar for
inclusion: widely citable, validated scope statable, not proprietary. Also flag library
entries whose standing has materially changed.

## Part C — AI capabilities

New model/tool capabilities that change what an educational plugin can offer its
educator — the standing example: interactive simulation support enabling personalized
visualizations (FFT/IFFT walkthroughs) that older skill text could never propose.
Frame each as a capability → the plugin stages it would enhance → contested-choice
implications (a new AI capability is still subject to the educator's AI stance — L2).

## Ledger and gate

One row per finding: source · what changed · affected PAGE file(s) or downstream plugin
pattern · proposed edit · risk of NOT applying. Present approve-per-item; apply only
approved rows, as a normal PAGE release through `page-release`. Update the footer below
in the same commit.

---
*last_refresh: 2026-07-06 (initial build — sources current as of this date)*
