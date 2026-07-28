<!-- Detail for L1. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L1 — Ground every stage in published frameworks; never invent process

**Rule.** No pipeline stage may invent a process, rubric, or set of criteria where a
citable, established framework exists (instructional design, assessment, presentation
design, software review — whatever the stage's domain is). Each stage carries an explicit
anchor: framework → citation → how it is applied.

**Failure that taught it.** Early POSED stages shipped home-made outline criteria and
review checklists. Pilot review kept re-litigating them ("why these seven dimensions?")
because there was no authority behind them. Once stages were re-anchored (UbD priority
tiers, Mager/ABCD objectives, Mayer multimedia principles, Fagan/IEEE 1028 inspections…),
disagreements became "does this apply the framework correctly?" — answerable.

**Corollary — scope discipline.** Cite a framework only for its original, validated scope.
POSED once over-generalized a protocol validated only for n8n-workflow development into a
universal AI-development framework; the fix was a "Scope and limitations" section. Every
grounding map entry must state what the framework does NOT cover.

**Edu Skill Creator enforcement.** `edu-skill-creator-grounding` runs before any architecture work and produces
`grounding_frameworks.md` for the new plugin; a stage with no anchor is flagged
"invented process — justify or redesign" and blocks the grounding gate.
