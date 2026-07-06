# Educational Grounding Library — starter framework map

The starting menu for `page-grounding`. When designing a stage in a new educational
plugin, look here FIRST; search for additional frameworks only when nothing fits. Each
entry: what it grounds, and its scope limit (L1 corollary: cite a framework only for its
original, validated scope — every use must state what the framework does NOT cover).

For a worked example of a complete per-plugin grounding map, see POSED's
`grounding_frameworks.md` (github.com/maxuwp/posed) and p2d's presentation-specific map
(github.com/maxuwp/p2d).

## Curriculum & lesson design

| Framework | Grounds | Scope limit |
|---|---|---|
| Understanding by Design — Wiggins & McTighe (backward design; enduring/important/familiar priority tiers) | Planning from outcomes; content prioritization | Curriculum planning; not a delivery or slide-design method |
| Mager / ABCD objective format | Writing measurable learning objectives | Objective wording; says nothing about sequencing |
| Bloom's taxonomy (revised, Anderson & Krathwohl) | Cognitive level of objectives, activities, assessment alignment | Classification, not pedagogy; levels are not a teaching order |
| Gagné's nine events of instruction | Lesson/lecture event sequencing | Event arc for a session; not curriculum-level planning |
| Merrill's first principles | Problem-centered activation→demonstration→application→integration | Task-centered instruction; complements, not replaces, Gagné |
| Ausubel (advance organizers) | Openers that anchor new material to prior knowledge | Openers/organizers; not full lesson design |

## Learning science & engagement

| Framework | Grounds | Scope limit |
|---|---|---|
| Cognitive Load Theory (Sweller) | Pacing, chunking, worked examples, split-attention avoidance | Instructional materials; not motivation or assessment |
| ICAP (Chi & Wylie) | Activity design ladder: interactive > constructive > active > passive | Engagement mode classification; not content selection |
| Cognitive apprenticeship (Collins, Brown, Newman) | Modeling/scaffolding/fading in labs and projects | Skill-learning contexts; not declarative content |
| POGIL | Guided-inquiry activity structure with rotating roles | Structured group inquiry; validated mainly in sciences |
| UDL (CAST) | Multiple means of representation/action/engagement | Accessibility & flexibility of materials; not a quality rubric |
| TPI — Teaching Perspectives Inventory (Pratt & Collins) | Characterizing an educator's teaching perspective (persona work) | Descriptive of perspectives; not prescriptive of methods |

## Assessment & quality

| Framework | Grounds | Scope limit |
|---|---|---|
| Constructive alignment (Biggs) | SLO ↔ activity ↔ assessment alignment matrices | Alignment logic; not item writing |
| Haladyna (item-writing guidelines) | MC/short-answer item quality rules | Item construction; not blueprint design |
| Wiliam (formative assessment / embedded strategies) | In-class checks, feedback loops | Formative practice; not summative grading policy |
| Quality Matters — PUBLIC standards only | Course-level review dimensions (alignment, usability, learner support) | Use only the freely published general standards; never copy the proprietary annotated rubric text |
| Fagan (1976) inspections; IEEE Std 1028 | Defect severity classes and audit process for consistency reviews | Software review practice, borrowed for artifact audits — say so |

## Communication & materials

| Framework | Grounds | Scope limit |
|---|---|---|
| Mayer (multimedia learning principles) | Slide/media design: coherence, signaling, redundancy, segmenting | Multimedia materials; not classroom facilitation |
| Assertion–evidence (Alley) | Slide structure: full-sentence claim + evidence body | Technical presentation slides |
| Doumont (Trees, Maps, and Theorems) | Message-first communication structure | Professional/scientific communication |
| Kosslyn (Clear and to the Point) | Perception/cognition-based slide rules | Slide perception; overlaps Mayer — pick one anchor per rule |
| SIFT (Caulfield) + CRAAP | Source vetting and claim tracing | Source evaluation; SIFT for quick vetting, not deep review |

## AI-assisted development & authoring (for the plugin-building process itself)

| Framework | Grounds | Scope limit |
|---|---|---|
| Anthropic skill-creator methodology | Skill lifecycle: intent → draft → eval → iterate → package; progressive disclosure; generalization principle | Skill authoring for Claude-family agents |
| plugin-dev (anthropics/claude-code) | Plugin component structure, validation, 8-phase creation workflow | Claude Code plugin mechanics |
| obra writing-skills (Superpowers) | TDD for skills: RED baseline → GREEN minimal skill → REFACTOR loopholes | Process documentation testing; requires subagent-style test runs |
| TDD (Beck) | Test-first discipline generally | Software; applied to skills via obra's adaptation |
| NIST SP 800-218 (SSDF) | Secure development practices for shipped scripts/apps | Security practice; not pedagogy |
| Ma, ASEE 2026 "Professor + AI Team" protocol | Faculty-led AI tool development phases | **n8n-workflow development only** — do not generalize |

## Rules of use

1. **One anchor per rule.** When two frameworks could ground the same requirement, pick
   the closer-scoped one and note the alternative.
2. **State the application, not just the citation.** A grounding map entry is
   stage → framework → citation → *how it is applied here* → scope limit.
3. **No anchor = flag.** A stage requirement with no citable anchor is either (a)
   redesigned, (b) justified as genuinely novel with the justification recorded in the
   grounding map, or (c) demoted to a suggestion. Silence is not an option.
4. **Copyright.** Cite and paraphrase; never reproduce proprietary rubric text (QM
   annotated rubric is the standing example).
