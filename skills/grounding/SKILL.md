---
name: page-grounding
description: PAGE Stage 2 — Framework grounding for a new educational plugin. Maps every anticipated pipeline stage to an established framework (instructional design, assessment, communication, review practice) BEFORE architecture, flags unanchored stages as "invented process — justify or redesign", and enforces scope discipline. Triggers - when the page umbrella dispatches Stage 2, or the user asks "what frameworks should ground this plugin".
version: "1.0"
---

# PAGE Stage 2: Framework Grounding

Runs BEFORE architecture (L1): design decisions get anchored to frameworks, not the other
way around. Output: the new plugin's `grounding_frameworks.md`, gate-approved.

## Process

1. **Enumerate candidate stages.** From the approved `intent.md`, list the pipeline
   stages the plugin will plausibly need (intake, planning, drafting per artifact,
   review, compile, reflect…). This list is provisional — architecture may still change
   it, but every candidate needs an anchor now.
2. **Anchor each stage.** Work from
   `<page-skill-dir>/reference/edu_grounding_library.md` FIRST. For each stage produce a
   map row: *stage → framework → citation → how it is applied here → scope limit (what
   the framework does NOT cover)*. One anchor per rule; note near-alternatives.
3. **Search only for gaps.** If nothing in the library fits a stage, search the
   literature for an established framework in that stage's domain. Prefer widely
   validated, citable sources; public standards only (never proprietary rubric text —
   the QM annotated rubric is the standing example).
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

## Output — the new plugin's `grounding_frameworks.md`

Header notes (scope-discipline rule, staleness note pointing at the plugin's future
refresh skill, contested-choice note) · the stage→framework map table · full citations
list. This file ships INSIDE the new plugin (umbrella skill's `reference/`), so its
drafting skills and reviewers can cite it; POSED's and p2d's versions are the worked
examples.

## Gate

Walk the author through the map stage by stage. Every unanchored-stage resolution and
every scope annotation is a separate structured decision (agree / revise). The gate
blocks while any stage's resolution is missing. On approval, write the stage-end summary
(which anchors now constrain architecture) and continue to `page-architecture`.
