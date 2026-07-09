---
name: edu-skill-creator-refresh
description: Edu Skill Creator maintenance — periodic (~90-day) refresh of Edu Skill Creator's own knowledge. Checks for new skill/plugin-authoring best practices, new educational frameworks worth adding to the grounding library, and new AI capabilities that change what educational plugins can offer. Consent-gated research sweep; findings land in a dated ledger reviewed approve-per-item; never auto-applies. Triggers - when ~90 days have passed since the last refresh, or the user says "refresh Edu Skill Creator" or asks whether the authoring guidance is still current.
version: "1.5"
---

# Edu Skill Creator Refresh

Edu Skill Creator encodes three snapshots that go stale at different speeds (L9): authoring practice
(fast — the harness vendors iterate), AI capabilities (fast), educational frameworks
(slow). Check `last_refresh` in this file's footer; if ~90 days have passed, offer a
refresh when Edu Skill Creator is next invoked. Never run one un-asked.

## Consent first (L6)

A refresh is a multi-source research sweep — web searches, repo reads, release-note
trawls. Offer the ladder before starting and record the mode in the ledger header:

- **full** — Parts A + B + C below.
- **lite** (~1/3 cost) — Part A only (authoring practice: the fastest-staling and the
  one whose drift breaks builds, e.g. manifest schema changes).
- **skip** — record the skip; the `last_refresh` footer still moves (see Gate).

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
covers (curriculum design, learning science, assessment, communication,
privacy/security/accessibility). Bar for inclusion: the library's own "Rules of use" —
widely citable, validated scope statable, not proprietary. Also flag library entries
whose standing has materially changed.

## Part C — AI capabilities

New model/tool capabilities that change what an educational plugin can offer its
educator — the standing example: interactive simulation support enabling personalized
visualizations (FFT/IFFT walkthroughs) that older skill text could never propose.
Frame each as capability → the plugin stages it would enhance → contested-choice
implications (a new AI capability is still subject to the educator's AI stance — L2).

*Grounding note (L1, resolution b — recorded justification):* unlike Parts A and B,
no published framework governs "watch for AI-capability change"; this part is an
invented process justified by L9's documented failure (the frozen-skill-text /
FFT-IFFT case in `<edu-skill-creator-skill-dir>/reference/lessons_learned.md`). If a citable
practice for capability-watch emerges, a future refresh should anchor Part C to it and
retire this note.

## Ledger — `docs/refresh_ledger_<YYYY-MM-DD>.md`

One row per finding, keyed `r1…rn` (stable, never renumbered):

| Field | Content |
|---|---|
| id | `r<n>` |
| source | which Part / which primary source |
| change | what changed since last refresh |
| affects | the Edu Skill Creator file(s) to edit, and — where the change alters a pattern that `edu-skill-creator-scaffold`/`edu-skill-creator-draft` generate into new plugins — which already-built plugins carry the old pattern (informational: their own maintainers decide; Edu Skill Creator never edits downstream repos) |
| proposal | the concrete edit |
| risk_of_not | what breaks or goes stale if rejected |

## Independent review of Parts B and C (before the gate — L3)

Part A reports external facts (release notes, repo diffs) with sources the author can
check directly — no drafter judgment to re-derive, so no independent reviewer
(recorded, scoped deviation from L3). Parts B and C involve judgment: B judges
inclusion-bar fit and "materially changed standing"; C maps capabilities to "the plugin
stages it would enhance" and their contested-choice implications. Dispatch a fresh
subagent session whose inputs are ONLY the Part B + C ledger rows,
`lessons_learned.md`, and `edu_grounding_library.md`; it checks that each claim is
sourced, each inclusion/enhancement judgment is supported by the row's own evidence
against the library's "Rules of use" bar, and no row smuggles a pedagogical stance
(L2). Log to `docs/refresh_ledger_<date>_review.json` BEFORE the gate opens.

## Gate

| Field | Value |
|---|---|
| gate_id | `refresh_gate` |
| decision | Per ledger row: apply / defer / reject (+ comment) |
| artifact | the dated ledger, rows keyed `r<n>` |
| reviewer | Part A: none (scoped waiver above); Parts B/C: the fresh-context review above |
| decision_file | `docs/refresh_ledger_<date>_decision.json` — `{rows:[{id, disposition, comment}], guidance}` |
| owns | approved rows are applied as a normal Edu Skill Creator release through `edu-skill-creator-release` |
| invalidates | rows that change lessons_learned.md or the grounding library mark dependent Edu Skill Creator skills for the semantic-drift grep in that release |
| consent | the full/lite/skip ladder above, recorded in the ledger header |

**After the gate closes** (explicit steps, not implied): (1) update the `last_refresh`
footer below in the same commit as the applied rows — an interrupted cycle whose footer
never moved is simply re-run; a ledger with no decision file is an open cycle, and a new
refresh must not start until it is closed or discarded; (2) write the stage-end
plain-language summary (rows applied / deferred / rejected, what changed in Edu Skill Creator).

---
*last_refresh: 2026-07-06 (initial build — sources current as of this date)*
