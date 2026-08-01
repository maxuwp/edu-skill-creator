# Educational Grounding Library — starter framework map

The starting menu for `edu-skill-creator-grounding`. When designing a stage in a new educational
plugin, look here FIRST; search for additional frameworks only when nothing fits. Each
entry: what it grounds, and its scope limit (L1 corollary: cite a framework only for its
original, validated scope — every use must state what the framework does NOT cover).

For a worked example of a complete per-plugin grounding map, see POSED's
`grounding_frameworks.md` (github.com/maxuwp/posed) and p2d's presentation-specific map
(github.com/maxuwp/p2d).

## Audit status — read before load-bearing on any row

**Last audited 2026-07-31**, every anchor against primary sources, twice and independently
(agentic browsing and deep research). Full results and the disagreements between the two runs are
in `docs/AUDIT_grounding_two_runs_compared.md`. What the audit settled, and what it did not, is
stated here rather than left to be assumed:

- **Corrected on agreed evidence.** Rows carrying `[audited 2026-07-31]` were changed because both
  runs agreed, or because only the complete run reached the anchor and quoted a primary source with
  no contradicting reading. The correction is recorded in the row, not just in the audit file.
- **Verified and deliberately left alone.** Gagné, POGIL, UDL 3.0, TPI, Biggs, Wiliam, Alley,
  plugin-dev and TDD were checked and found within scope. Their sentences are unchanged on purpose:
  a verified property is a baseline to protect, not an invitation to re-draft (L19).
- **Disputed and NOT re-verified.** The two runs disagreed on eight anchors. Bloom, Cognitive Load
  Theory, ICAP, Kosslyn and SIFT/CRAAP are therefore untouched, and their scope sentences carry no
  more authority today than they did before the audit. Quality Matters, Mayer and NIST SSDF were
  edited **only** on the sub-claim both runs made identically; the disputed part of each is
  flagged in the row and left open.
- **Contested rather than wrong.** Cognitive Load Theory (germane load formally dropped by Kalyuga
  & Plass, 2025), ICAP (the I>C>A>P ordering is not replicating, one reversed result) and Bloom (the
  two dimensions found non-independent in a 940-item study). These are real, correctly cited, and
  under active empirical challenge. The library has no contested-anchor vocabulary yet; until it
  does, do not let one of these three sole-authorize a fail-closed gate.
- **Open currency item.** FERPA enforcement routing: one run found a June 2026 interagency
  agreement involving DOJ, the other did not look. Unsettled, and not relied on below.

---

## Curriculum & lesson design

| Framework | Grounds | Scope limit |
|---|---|---|
| Understanding by Design — Wiggins & McTighe (backward design; enduring/important/familiar priority tiers) | Planning from outcomes; content prioritization | Plans curriculum, assessment **and** instruction — UbD's own Stage 3 plans learning experiences and names teaching roles; not a slide-design or presentation method `[audited 2026-07-31]` |
| Mager (1997), *Preparing Instructional Objectives* | Writing measurable learning objectives: performance, conditions, criterion | Outcome-statement wording only. Mager explicitly forbids embedding instructional procedures in an objective, and states no numeric criterion threshold; says nothing about sequencing `[audited 2026-07-31]` |
| ABCD objective mnemonic (audience, behavior, condition, degree) | A four-part checklist shape for objective statements | **Not Mager's format** — a separate mnemonic from the instructional-media lineage, conflated with Mager in this library until 2026-07-31. One anchor per rule: prefer Mager where an objective must be defensible. The attribution rests on one audit run and has not been independently re-verified `[audited 2026-07-31]` |
| Bloom's taxonomy (revised, Anderson & Krathwohl) | Cognitive level of objectives, activities, assessment alignment | Classification, not pedagogy; levels are not a teaching order — *disputed row, see audit status above* |
| Gagné's nine events of instruction | Lesson/lecture event sequencing | Event arc for a session; not curriculum-level planning |
| Merrill's first principles | Problem-centered activation→demonstration→application→integration | "Problem-centered" is Merrill's own term; "task-centered" is his later formulation. Complements, not replaces, Gagné. Cite the 2020 AECT revised edition (reissued 2024) — the 2002 paper is a synthesis of prior theories with no empirical population of its own `[audited 2026-07-31]` |
| Ausubel (advance organizers) | Openers that anchor new material to prior knowledge | Validated for prose organizers placed before unfamiliar written expository text (1960, university students) — a reading-comprehension manipulation, not a general lesson-opener method. Historically important, empirically contested (pooled g≈0.42) `[audited 2026-07-31]` |

## Learning science & engagement

| Framework | Grounds | Scope limit |
|---|---|---|
| Cognitive Load Theory (Sweller) | Pacing, chunking, worked examples, split-attention avoidance | Instructional materials; not motivation or assessment — *disputed row, and contested in the literature; germane load is a superseded construct, and no working-memory or chunk-size number is traceable to Sweller 1988* |
| ICAP (Chi & Wylie) | Activity design ladder: interactive > constructive > active > passive | Engagement mode classification; not content selection — *disputed row; the authors present the ordering as a hypothesis, and it is not replicating* |
| Cognitive apprenticeship (Collins, Brown, Newman) | Modeling/scaffolding/fading in labs and projects | Skill-learning contexts, **including** conceptual and factual knowledge where it is situated in use — the previous "not declarative content" exclusion was narrower than the source; not a curriculum-planning method `[audited 2026-07-31]` |
| POGIL | Guided-inquiry activity structure with rotating roles | Structured group inquiry; validated mainly in sciences |
| UDL 3.0 (CAST, 2024 guidelines) | Multiple means of representation/action/engagement | Design flexibility of materials; not a conformance standard — pair with WCAG for that |
| TPI — Teaching Perspectives Inventory (Pratt & Collins) | Characterizing an educator's teaching perspective (persona work) | Descriptive of perspectives; not prescriptive of methods |

## Assessment & quality

| Framework | Grounds | Scope limit |
|---|---|---|
| Constructive alignment (Biggs) | SLO ↔ activity ↔ assessment alignment matrices | Alignment logic; not item writing |
| Haladyna, Downing & Rodriguez (2002) — 31 item-writing guidelines | Multiple-choice / selected-response item quality rules | Multiple-choice and selected-response items in classroom assessment only; does **not** cover short-answer or constructed-response. Guideline 1 anchors items to a test blueprint, so this is not a "blueprint-free" boundary — the guidelines simply do not design one `[audited 2026-07-31]` |
| Wiliam (formative assessment / embedded strategies) | In-class checks, feedback loops | Formative practice; not summative grading policy |
| Quality Matters — PUBLIC standards only | Course-level review dimensions (alignment, usability, learner support) | Use only the freely published standards, and never reproduce QM's published text: the free PDF is itself copyright-restricted against duplication, not only the annotated rubric `[audited 2026-07-31]`. *Which standards the free material contains is disputed between the two audit runs and is not settled here* |
| Fagan (1976) inspections | Defect severity classes and audit process for consistency reviews | Fagan's validated scope is IBM programming work products, with exactly **two** severity classes (major/minor) — not a 3+ ladder. Borrowed here for artifact audits; say so. **IEEE Std 1028 is not an active standard** — IEEE lists 1028-2008 "Inactive-Reserved" since 2019-11-07 with no successor in that working group (verified at standards.ieee.org, 2026-07-31). Do not cite it as current; the severity-class borrowing stands on Fagan alone `[audited 2026-07-31]` |

## Communication & materials

| Framework | Grounds | Scope limit |
|---|---|---|
| Mayer (multimedia learning principles) | Multimedia lesson design: coherence, signaling, redundancy, segmenting | Narration/graphics pairing in short instructional lessons, tested mostly on college students. **Explicitly not applicable to prose or lexico-grammatical editing at any layer**: the personalization principle was operationalized as a 12-place "the"→"your" substitution in a narrated science animation, and cannot license general text-editing judgments. Not classroom facilitation. This is the anchor behind the recorded failure in L14 `[audited 2026-07-31]` |
| Assertion–evidence (Alley) | Slide structure: full-sentence claim + evidence body | Technical presentation slides; the visual-evidence body applies to data/figure content — precision text (definitions, equations, code) is its own evidence (L10) |
| Doumont (Trees, Maps, and Theorems) | Message-first communication structure | Professional/scientific communication; non-empirical, explicitly based on experience rather than controlled studies. The commonly quoted "rule of three" is not traceable in the book's public sample pages — do not attribute it to Doumont without the page `[audited 2026-07-31]` |
| Kosslyn (Clear and to the Point) | Perception/cognition-based slide rules | Slide perception; overlaps Mayer — pick one anchor per rule — *disputed row, see audit status above* |
| SIFT (Caulfield) + CRAAP | Source vetting and claim tracing | Source evaluation; SIFT for quick vetting, not deep review — *disputed row; both halves are moving targets* |

## Privacy, security & accessibility (mandatory review for any plugin touching student data or generating UI)

| Framework | Grounds | Scope limit |
|---|---|---|
| W3C WCAG 2.2 | Accessibility conformance of generated web artifacts AND of the plugin's own HITL gate pages (keyboard operability, contrast, screen-reader semantics) | Web content; success criteria, not pedagogy — pair with UDL 3.0 for learning design. W3C Recommendation since 2023-10-05, current version 2024-12-12; WCAG 3.0 is still a Working Draft, so 2.2 is the citation (verified at w3.org, 2026-07-31) `[audited 2026-07-31]` |
| FERPA / PPRA + U.S. Dept. of Education PTAC guidance | Governance of student education records: what counts as PII, permissible disclosure, retention, de-identification best practice | U.S. federal law administered by ED's Student Privacy Policy Office (SPPO); PTAC is SPPO's technical-assistance arm, so its output is guidance, not law. Institutional policy may be stricter — always ask (intent Part A.7); not legal advice `[audited 2026-07-31]` |
| NIST SP 800-218 (SSDF) | Secure development of any scripts/apps the plugin ships (gate apps, compile scripts): input handling, secrets, dependency hygiene | Security practice for shipped software; not a privacy regime. Cite v1.1 (Feb 2022); a Rev.1 draft exists but is not final — *the breadth of this row is disputed between the two audit runs* |
| NIST SP 800-218A (SSDF community profile for generative AI and dual-use foundation models, 2024) | Secure development practices specific to AI model and AI-system development — the companion profile that applies when a plugin ships AI-authored or AI-driven code | Augments 800-218, does not replace it; practices for AI development, not a privacy or educational-ethics regime `[added 2026-07-31, flagged as missing by both audit runs]` |

Rule of thumb: a plugin that handles student work, grades, or identifiable student
information — or sends anything to an external service — must carry a data-flow/security
model in its architecture (see `edu-skill-creator-architecture`), grounded in this section.

## AI-assisted development & authoring (for the plugin-building process itself)

| Framework | Grounds | Scope limit |
|---|---|---|
| Anthropic skill-creator methodology | Skill lifecycle: intent → draft → eval → iterate → package; progressive disclosure; generalization principle | Skill authoring for Claude-family agents |
| plugin-dev (anthropics/claude-code) | Plugin component structure, validation, 8-phase creation workflow | Claude Code plugin mechanics |
| obra "Superpowers" — a complete agentic software-development methodology, of which `writing-skills` is one Meta skill | TDD for skills: RED baseline → GREEN minimal skill → REFACTOR loopholes | Process documentation testing; requires subagent-style test runs. We borrow one skill selectively from a much broader methodology — do not cite Superpowers as though it were a skill-writing guide `[audited 2026-07-31]` |
| TDD (Beck) | Test-first discipline generally | Software; applied to skills via obra's adaptation |
| NASA Systems Engineering Handbook — configuration management (baselines; major vs. minor change; change board with named authority) | Graded change control: classify a proposed change by impact, and authorize it before implementing | The shape only — baseline, classification by impact, a named authority, authorization before implementation. Validated for engineered systems under formal CM, not for review loops; our four scope classes and the one-descent reserve are local rules, not NASA's `[added 2026-08-01, primary source fetched]` |
| Ma, ASEE 2026 "Professor + AI Team" protocol | Faculty-led AI tool development phases | **n8n-workflow development only** — do not generalize |

## Rules of use

1. **One anchor per rule.** When two frameworks could ground the same requirement, pick
   the closer-scoped one and note the alternative.
2. **State the application, not just the citation.** A grounding map entry is
   stage → framework → citation → *how it is applied here* → scope limit.
3. **No anchor = flag.** A stage requirement with no citable anchor is either (a)
   redesigned, (b) justified as genuinely novel with the justification recorded in the
   grounding map, or (c) demoted to a suggestion. Silence is not an option.
4. **Copyright.** Cite and paraphrase; never reproduce proprietary rubric text (QM is the
   standing example, and its freely published PDF is restricted against duplication too).
5. **Audit before load-bearing.** A row's scope sentence is only as good as its last audit.
   Check the audit-status section above before grounding a fail-closed gate on any row marked
   disputed or contested.
