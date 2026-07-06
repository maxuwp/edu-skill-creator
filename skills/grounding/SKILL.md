---
name: edu-skill-creator-grounding
description: Edu Skill Creator Stage 2 — Framework grounding for a new educational plugin. Maps every anticipated pipeline stage to an established framework (instructional design, assessment, communication, review practice) BEFORE architecture, flags unanchored stages as "invented process — justify or redesign", and enforces scope discipline. Includes an independent fresh-context review of the map before the author gate. Triggers - when the edu-skill-creator umbrella dispatches Stage 2, or the user asks "what frameworks should ground this plugin".
version: "1.4"
---

# Edu Skill Creator Stage 2: Framework Grounding

Runs BEFORE architecture: design decisions get anchored to frameworks, not the other way
around. This ordering is itself grounded — lesson L1 in
`<edu-skill-creator-skill-dir>/reference/lessons_learned.md` (the POSED grounding releases,
posed_skill.1.10/1.11, where re-anchoring ended the re-litigating of home-made criteria).
Output: the new plugin's `grounding_frameworks.md`, independently reviewed, then
gate-approved.

**Refuses to run** unless `intent.md` exists and its gate decision is approved. If
`intent.md` (especially its contested-choices inventory) is revised after this stage's
gate, the grounding map is stale (`needs_regeneration`) and architecture must not
proceed until the affected rows are redone and re-approved — the umbrella's operating
rules track this in BUILD_PLAN.

## Process

1. **Enumerate candidate stages.** From the approved `intent.md`, list the pipeline
   stages the plugin will plausibly need (intake, planning, drafting per artifact,
   review, compile, reflect…). This list is provisional — architecture may still change
   it, but every candidate needs an anchor now.
2. **Anchor each stage.** Work from
   `<edu-skill-creator-skill-dir>/reference/edu_grounding_library.md` FIRST. For each stage produce a
   map row: *stage → framework → citation → how it is applied here → scope limit (what
   the framework does NOT cover)*. One anchor per rule; note near-alternatives.
   Worked example row:
   *objective-writing step → Mager/ABCD → Mager (1997) → every SLO drafted in
   audience/behavior/condition/degree form → scope limit: objective wording only, says
   nothing about sequencing.*
3. **Search only for gaps.** If nothing in the library fits a stage, search for an
   established framework in that stage's domain. The vetting bar is the library's own
   "Rules of use" section — widely validated, citable, public standards only, never
   proprietary rubric text — not a standard invented here.
4. **Flag the unanchored.** A stage with no citable anchor gets one of exactly three
   resolutions, recorded in the map: **(a) redesign** the stage so an anchor applies;
   **(b) justify** it as genuinely novel — the justification (why no framework exists,
   what evidence supports the invented process) goes in the map; **(c) demote** the
   requirement to a suggestion. Silence blocks the gate.
5. **Scope-discipline pass.** Re-read the finished map hunting over-generalization: any
   framework cited beyond its validated scope (the standing example: a protocol
   validated for n8n workflow development cited as a universal AI-development method).
   Fix or annotate every hit.
6. **Contested-choice cross-check (L2).** For each contested choice in the intent
   inventory, verify the map doesn't smuggle a stance in — e.g. grounding activities
   exclusively in AI-centric practice when the AI stance is supposed to be a choice.

## Independent review (before the author sees the map — L3)

The map is a drafted artifact, so it gets a fresh-context reviewer like any other.
Dispatch a fresh subagent session whose inputs are ONLY: the draft map, the approved
`intent.md`, and `edu_grounding_library.md`. It checks four things — framework-fit
accuracy (does each framework actually ground what the row claims?), scope-limit
correctness, no silently unanchored stage (every stage has a row with an anchor or a
recorded resolution), no stance smuggling — and writes findings to
`reviews/grounding_map_review.json` in the build session BEFORE the gate edu-skill-creator renders.
Fix blocking findings and re-review; the gate shows the reviewer's summary card. (Like
the architecture design review, this is a binary inspection with severity-classed
findings, not a scored /100 rubric — Fagan/IEEE 1028: points belong on quality
judgments, not conformance checks.)

## Output — the new plugin's `grounding_frameworks.md`

Header notes (scope-discipline rule, staleness note pointing at the plugin's future
refresh skill, contested-choice note) · the stage→framework map table · full citations
list. Target path inside the new plugin `<x>`:
`skills/<x>/reference/grounding_frameworks.md` (the umbrella skill's reference dir), so
its drafting skills and reviewers can cite it. POSED's and p2d's versions are the worked
examples.

## Gate

| Field | Value |
|---|---|
| gate_id | `grounding_gate` |
| decision | Is this map the right grounding for the plugin? (per-row: agree / revise + comment) |
| artifact | draft `grounding_frameworks.md`; rows keyed by stage name |
| reviewer | fresh-context map review above (`reviews/grounding_map_review.json`) |
| decision_file | `grounding_gate_decision.json` — `{decision, rows:[{stage, disposition, comment}], guidance}` |
| owns | `edu-skill-creator-grounding` re-runs Process step 2 for revised rows |
| invalidates | on approval of changes: `architecture.md` and everything after it (stale per umbrella rules) |
| consent | n/a — not token-expensive |

Walk the author through the map stage by stage. The gate blocks while any stage's
resolution is missing. On approval, write the stage-end summary (which anchors now
constrain architecture) and continue to `edu-skill-creator-architecture`.
