# Perplexity handoff — grounding library audit (scope, currency, citation truth)

**For:** Perplexity, run by Dr. Xiaoguang Ma. **From:** the edu-skill-creator thread, 2026-07-31.
**Subject:** the 30 framework anchors in `skills/edu-skill-creator/reference/edu_grounding_library.md`,
reproduced in full in §4 so this document is self-contained.
**Why it matters:** every stage of this plugin, and of every plugin it generates, is required to
anchor its design to one of these entries. No refresh has ever been run. The code above this
library is well tested; the library itself is unaudited.

---

## 1. The question is NOT "does this citation exist"

It almost always does. The question that has actually caused failures here is narrower:

> **What did this source actually validate, and is our stated scope limit true to that?**

The recorded failure: a rubric cited the AAC&U Oral Communication VALUE rubric and Mayer's
multimedia principles — both real, both correctly attributed — to judge defects at the
lexico-grammatical layer, which **neither framework reaches**. VALUE assesses live student
presentations at the level of delivery and organisation; Mayer's personalization principle was
operationalized in its source experiments as pronoun substitution. The citation was not wrong. The
*scope* was.

So for each anchor below, three questions, in this order:

1. **Scope truth.** What population, task type, and observable layer did the source actually study
   or specify? Is the "Scope limit" column in §4 accurate, too broad, or too narrow?
2. **Currency.** Superseded, revised, or contested since publication? Name the current edition or
   the successor. (UDL 3.0, WCAG 2.2, PTAC guidance and NIST SSDF are the volatile ones.)
3. **Numbers.** Does the source state any numeric threshold we might be quoting? Three invented
   numeric targets have already been withdrawn from this project at cost, so any number that cannot
   be traced to a source should be reported as untraceable rather than approximated.

## 2. Output format — this part is not optional

Return **one row per anchor**, in this shape. A fluent summary is unusable here.

| # | Anchor | Verdict | Actual validated scope | Supporting quote | Source URL | Currency |
|---|---|---|---|---|---|---|

- **Verdict** is one of: `scope-accurate` · `scope-too-broad` (we claim more than the source
  supports) · `scope-too-narrow` · `superseded` · **`unverified`**.
- **Supporting quote** is a sentence or two **quoted from the source**, not paraphrased, that
  supports your verdict.
- **If you cannot produce a quote and a URL, the verdict is `unverified`.** Not `scope-accurate`.
  This is the single most important instruction in this document: a confident summary with no
  traceable quote is exactly the kind of evidence this project has learned to refuse, and it will be
  treated as unverified regardless of how plausible it reads.
- Paywalled or offline sources: `unverified`, and say so. That is a useful result, not a failure.

At the end, a short list: **which anchors would you retire, add, or re-scope**, with reasons.

## 3. Suggested mode split

The job has two halves that want different settings. Whatever the current mode names are, the
distinction that matters is *pointed and traceable* versus *broad and synthesised*.

- **Half A — scope verification (§1 questions 1 and 3), the larger half.** Use the **pointed
  search** mode, in batches of 4–6 anchors, one batch per cluster in §4. Do **not** use Deep
  Research here: it synthesises across sources, and synthesis is what destroys the traceability
  this half depends on. I need "Mayer's personalization principle was operationalized as X in study
  Y", tied to one source, not a blended paragraph about multimedia learning.
- **Half B — currency (§1 question 2).** Here Deep Research **is** the right tool, one run per
  cluster, asking the genuinely open question: *what has changed in this area since these sources,
  and is anything here superseded or contested?* Breadth helps; a long report is fine.

If you are using an agentic browsing mode rather than plain search, the output-format rule in §2
matters **more**, not less: an agent that reads a page and summarises it is the highest-risk path
for an untraceable claim.

Run Half A first. Its results tell us which anchors are worth spending Half B's depth on.

## 4. The anchors

Scope limits below are **our current claims, under test** — not established fact. Quoted verbatim
from the library.

### Curriculum & lesson design
1. **Understanding by Design (Wiggins & McTighe)** — grounds planning from outcomes and content
   prioritization. *Our scope limit:* "Curriculum planning; not a delivery or slide-design method."
2. **Mager / ABCD objective format** — grounds writing measurable objectives. *Our limit:*
   "Objective wording; says nothing about sequencing."
3. **Bloom's taxonomy, revised (Anderson & Krathwohl)** — grounds cognitive level and alignment.
   *Our limit:* "Classification, not pedagogy; levels are not a teaching order." **Priority: this is
   the most-cited and most-abused anchor in educational tooling; check the revised taxonomy's own
   position on hierarchy and ordering.**
4. **Gagné's nine events of instruction** — grounds session event sequencing. *Our limit:* "Event
   arc for a session; not curriculum-level planning."
5. **Merrill's first principles** — grounds problem-centred instruction. *Our limit:* "Task-centered
   instruction; complements, not replaces, Gagné."
6. **Ausubel (advance organizers)** — grounds openers. *Our limit:* "Openers/organizers; not full
   lesson design."

### Learning science & engagement
7. **Cognitive Load Theory (Sweller)** — grounds pacing, chunking, worked examples,
   split-attention. *Our limit:* "Instructional materials; not motivation or assessment."
   **Priority: CLT's measurement claims have been actively contested; report the state of that
   debate.**
8. **ICAP (Chi & Wylie)** — grounds an activity ladder interactive > constructive > active >
   passive. *Our limit:* "Engagement mode classification; not content selection." **Check whether
   the ordering is validated as a strict ranking or as a tendency.**
9. **Cognitive apprenticeship (Collins, Brown, Newman)** — grounds modeling/scaffolding/fading.
   *Our limit:* "Skill-learning contexts; not declarative content."
10. **POGIL** — grounds guided-inquiry structure with rotating roles. *Our limit:* "Structured group
    inquiry; validated mainly in sciences." **Check that "mainly in sciences" is accurate.**
11. **UDL 3.0 (CAST, 2024 guidelines)** — grounds multiple means of representation/action/
    engagement. *Our limit:* "Design flexibility of materials; not a conformance standard."
    **Currency-critical: confirm 3.0 is current and the 2024 date is right.**
12. **TPI — Teaching Perspectives Inventory (Pratt & Collins)** — grounds persona work. *Our
    limit:* "Descriptive of perspectives; not prescriptive of methods."

### Assessment & quality
13. **Constructive alignment (Biggs)** — grounds SLO↔activity↔assessment matrices. *Our limit:*
    "Alignment logic; not item writing."
14. **Haladyna (item-writing guidelines)** — grounds MC/short-answer item rules. *Our limit:* "Item
    construction; not blueprint design." **If the source states a count of rules or any numeric
    guidance, report it exactly.**
15. **Wiliam (formative assessment)** — grounds in-class checks and feedback loops. *Our limit:*
    "Formative practice; not summative grading policy."
16. **Quality Matters — PUBLIC standards only** — grounds course-level review dimensions. *Our
    limit:* "Use only the freely published general standards; never copy the proprietary annotated
    rubric text." **Confirm which standards are genuinely public and what the current edition is;
    this one carries a copyright constraint, so accuracy matters more than usual.**
17. **Fagan (1976) inspections; IEEE Std 1028** — grounds defect severity classes and audit
    process. *Our limit:* "Software review practice, borrowed for artifact audits — say so."
    **Confirm IEEE 1028's current status (is it active, withdrawn, or superseded?).**

### Communication & materials
18. **Mayer (multimedia learning principles)** — grounds slide/media design: coherence, signaling,
    redundancy, segmenting. *Our limit:* "Multimedia materials; not classroom facilitation."
    **Priority, and the source of the recorded failure above: for each principle we name, what was
    the actual experimental operationalization and population?**
19. **Assertion–evidence (Alley)** — grounds full-sentence claim + evidence body. *Our limit:*
    "Technical presentation slides."
20. **Doumont (Trees, Maps, and Theorems)** — grounds message-first structure. *Our limit:*
    "Professional/scientific communication."
21. **Kosslyn (Clear and to the Point)** — grounds perception-based slide rules. *Our limit:*
    "Slide perception; overlaps Mayer — pick one anchor per rule."
22. **SIFT (Caulfield) + CRAAP** — grounds source vetting. *Our limit:* "Source evaluation; SIFT for
    quick vetting, not deep review." **CRAAP has been criticised in the information-literacy
    literature; report that if so.**

### Privacy, security & accessibility
23. **W3C WCAG 2.2** — grounds accessibility conformance of generated artifacts and gate pages.
    *Our limit:* "Web content; success criteria, not pedagogy." **Currency-critical: is 2.2 current,
    and what is the status of 3.0?**
24. **FERPA / PPRA + U.S. Dept. of Education PTAC guidance** — grounds student-record governance.
    *Our limit:* "U.S. federal law + official guidance; institutional policy may be stricter; not
    legal advice." **Currency-critical: is PTAC still the operating body, and is its guidance
    current? Report any change in its status or hosting.**
25. **NIST SP 800-218 (SSDF)** — grounds secure development of shipped scripts. *Our limit:*
    "Security practice for shipped software; not a privacy regime." **Confirm the current version
    (1.1?) and whether an AI-specific companion profile now exists.**

### AI-assisted development & authoring
26. **Anthropic skill-creator methodology** · 27. **plugin-dev (anthropics/claude-code)** ·
28. **obra writing-skills (Superpowers)** — vendor/community documentation for agent authoring.
    Lower priority: check only whether each still exists and is current, since these are tooling
    docs rather than research claims.
29. **TDD (Beck)** — grounds test-first discipline. *Our limit:* "Software; applied to skills via
    obra's adaptation."
30. **Ma, ASEE 2026 "Professor + AI Team" protocol** — grounds faculty-led AI tool development
    phases. *Our limit:* "**n8n-workflow development only — do not generalize.**" **This is Dr. Ma's
    own paper. Do not search for it or evaluate it; the scope limit was set by the author. Skip and
    mark `author-set`.**

## 5. What this audit cannot settle

Whether the pipeline is pedagogically *sound* — that is faculty judgment. This audit establishes
only whether each anchor exists, is used within what it actually validated, and is current. A
`scope-accurate` verdict on all 29 examinable anchors would still leave the design question open.

Also note: the "Scope limit" text in §4 is our claim, written by an AI, and never checked against
the sources. Treat it as the hypothesis under test, not as context to reason from.
