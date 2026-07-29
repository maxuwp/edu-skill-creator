<!-- Detail for L17. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L17 — When the subject taught is a process, its structure is content

**Rule.** When a learning outcome requires learners to apply a domain process or make a sequence of
decisions, the instructional sequence and the assessment must preserve the grounded structure of that
process. Structure is a claim that can be right or wrong, and it carries the same sourcing discipline
as a content fact.

**Failure that taught it.** Faculty, on a module that covered the right concepts in an arbitrary
order: "the flow of the presentation should be re-organized to reflect the real human decision
process rather than randomly collect and exhibit the concepts together. This is a serious design
negligence in the skill design." Covering the correct concepts is not the same as teaching the
procedure, and to a subject-matter expert the difference reads as a fundamental design failure rather
than a cosmetic one. The resulting rule was set at critical severity immediately, on the stated
reasoning that a warning on the central point of a change request trains agents to skip it.

**Distinct from L1.** L1 governs how the authoring pipeline is grounded. This governs whether the
taught material's structure is faithful to the domain's real structure — a different object.

**Representation is the architecture's choice.** Graphs, state machines, checklists, workflows and
worked decision paths all qualify; the requirement is that the representation matches the process.
`../implementation_patterns.md` P2 records one locked-graph mechanism and its lighter fallbacks.

**Enforcement.** `edu-skill-creator-intent` asks whether any outcome is process-shaped;
`edu-skill-creator-architecture` requires a sourced representation and a traversal check where it is.
