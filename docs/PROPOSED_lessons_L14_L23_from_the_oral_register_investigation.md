> **SUPERSEDED 2026-07-28 by release 1.11.** These ten proposals were triaged in
> `reflect_ledger.json` and gated in `reflect_gate_decision.json`. Their numbering does NOT map to
> the shipped lessons: proposed-L14 became **L14**; proposed-L15/L17/L20 folded into **L11**;
> proposed-L19 into **L1** and **L16**; proposed-L21 into **L7**; proposed-L22 into **L10**;
> proposed-L16/L18 into **L11**; proposed-L23 was deferred (row f23). Retained as historical
> evidence — do not implement from this file.

# Proposed lessons L14–L23, from the oral-register investigation

**Prepared by:** Claude (Opus 5) · 2026-07-28 · **Status:** PROPOSED, nothing implemented

Ten proposed additions to `skills/edu-skill-creator/reference/lessons_learned.md`, each with the
concrete evidence that produced it. They come from one investigation: a skill-authored narration
script that passed its own grounded review rubric and was not speech. Every lesson below is a
place where the existing pipeline would have permitted the same defect again.

The most important is **L14**, because it is a caveat to L1, the pipeline's most fundamental rule.

---

## L14 — A framework anchor can be real and still not reach the layer the criterion must judge

**Lesson.** L1 requires grounding in a published framework. That is necessary and not sufficient.
Grounding stage 2 must additionally ask: **which observable layer does this framework describe, and
does the criterion I am anchoring to it live in that layer?** A criterion anchored to a framework
that operates one layer away is unfalsifiable while appearing rigorous.

**Evidence.** The oral review rubric was correctly grounded. It cited the AAC&U Oral Communication
VALUE rubric and Mayer and Moreno's multimedia-learning principles, both legitimate and both
properly attributed. The criterion "Language is natural, comprehensible, audience-appropriate"
traced to "VALUE language; Mayer personalization."

It passed a 7,557-word script containing **zero verbal contractions** and six spoken blocks that
opened by reading a written subheading aloud.

Neither anchor could catch it. VALUE assesses live student presentations, at the level of delivery
and organisation. Mayer's personalization principle was operationalized in the source experiments
as pronoun substitution, changing "the" to "your" in twelve places, and contractions were
**explicitly never a manipulated variable**. The failure lived at the lexico-grammatical layer,
which is Biber's register dimension, and no anchor reached it.

**Diagnostic value.** The initial diagnosis was "the rubric is ungrounded." That was wrong and
checking the file disproved it. The true diagnosis, grounded in frameworks that do not reach the
layer, is both more accurate and harder to find, which is exactly why the grounding stage should
ask the question mechanically rather than leaving it to notice.

---

## L15 — Criticality without an operational definition is decorative

**Lesson.** Every criterion ships with a stated observable that would fail it, and at least one
worked example of a failing artifact. A criterion that names a principle and supplies no
behavioural anchor cannot reject anything, whatever severity it is assigned.

**Evidence.** The criterion above was scored `High`, one level below `Critical`, with four
severity levels defined generically for the whole rubric and no behavioural anchor of its own. A
reviewer scoring it had the sentence and nothing to hold the text against.

---

## L16 — A rubric change that cannot fail the artifact that motivated it has not been implemented

**Lesson.** When a defect motivates a rubric or validator change, the defective artifact becomes
part of the acceptance suite. Acceptance reads: re-review the motivating artifact unchanged and
observe it fail.

**Evidence.** This is now acceptance criterion 4 of the resulting change request. Without it the
plausible outcome is a rubric that reads better and behaves identically, which is the same class
of defect as L13, a check that tests a proxy rather than the claim.

---

## L17 — Measure the exemplars you ship

**Lesson.** Run the skill's own instrument over the skill's own examples before release. It is
cheap and it tests whether authored guidance actually produces the behaviour it describes.

**Evidence, in both directions.** A reference skill from another vendor ships 292 words of tone
exemplars with no corpus behind them. Measured with our instrument they landed at parity with real
lecture speech on the two markers that define the defect, and at zero heading-readouts. Authored
guidance, unmeasured, was right, and measuring proved it rather than assuming it.

The same measurement applied to our own artifact against our own guidance is what exposed the gap
in the first place. The instrument costs one script and answers a question that prose review had
already got wrong.

---

## L18 — Any numeric threshold is independently reimplemented from its written definition before it ships

**Lesson.** A threshold derived from a measurement must be re-derived by a second implementer
working only from the written definition, never from the code. Thresholds that do not survive do
not ship.

**Evidence.** Eight markers were defined in prose and reimplemented independently. Five agreed
closely enough to use. **Three died:**

| Marker | Original | Reimplementation | Cause |
|---|---:|---:|---|
| Verb-announced transitions | 10.26 | 3.68 | regex counted every occurrence of phrases like "let's", not topic transitions |
| Imperatives | 0.54 | 1.43 | differing verb inventories |
| Nominalization, discourse markers | inflated | lower | optional plural suffix; two extra markers in the list |

The first was inflated roughly threefold and had already been quoted in three documents and used
to support an argument about register invariance. Nothing but independent reimplementation would
have caught it.

---

## L19 — State what your corpus is an artifact of

**Lesson.** A derived corpus measures its production process as well as its subject. Name the
production process and ask which measures it contaminates before deriving any threshold.

**Evidence.** Two caption corpora of university lectures were measured for contraction rate. One
returned 0.00 to 0.10 per 1,000 words across all six disciplines sampled. The other returned 41 to
43. That gap is far too large to be a discipline effect and reflects transcription policy: one
vendor expands contractions, the other preserves them. **In a caption corpus, contraction rate
measures the transcriber.** Any threshold derived from pooled caption text would have been an
artifact of an editorial convention.

---

## L20 — Prefer a binary presence check or a reported value over an invented threshold

**Lesson.** When the literature supplies no threshold, do not invent one. A presence check answers
many questions, and a reported value shown to a human reviewer answers the rest. Both are honest;
an invented number is not, and it will be withdrawn later at cost.

**Evidence.** This project has now withdrawn invented numeric targets three times: a 600-character
description target, a 200-to-400 band, and a contraction-rate floor. In the last case, three
independent literature reviews reported the same not-found: no published per-1,000 contraction
rate exists for lecture monologue in any of the standard academic-speech corpora. Zero contractions
in 7,557 words needs no threshold to diagnose, and a script at 15 per 1,000 needs a human.

---

## L21 — Every unit must appear in the registry that governs it

**Lesson.** When a skill maintains a central registry, ship a mechanical check that every unit
appears in it. Registries decay silently at exactly the point where new units are added by a later
change request.

**Evidence.** A grounding registry mapped every pipeline stage to its named frameworks and carried
the rule that reviewers score against those frameworks rather than personal taste, with criteria
tracing back to that file. It had a row for every stage except the two newest, which shipped in a
later release and were never registered. The anchors for those stages existed in their own rubric
file and were invisible in the map that reviewers are told to consult.

---

## L22 — An anti-AI-tell rule must be checked against what the target genre actually does

**Lesson.** Rules that suppress synthetic-sounding output are written from the drafter's
perspective and can suppress the target register. Before shipping one, check it against corpus
evidence for the genre.

**Evidence.** A content rule banned shared sentence templates across output blocks, naming fixed
closers as an anti-pattern. It is reasonable against AI boilerplate. But attested lecture speech is
formulaic: one corpus study found lecturers announcing the topic in 75% of lectures with
near-identical framing, another found a single importance-marker family accounting for 33.7% of all
such tokens across 160 lectures, and a widely used practitioner framework asks explicitly for the
core idea to be restated three or more times. The anti-tell rule and the target register
contradicted each other inside the same file.

---

## L23 — Name the human verification step the source domain relies on, and what substitutes for it

**Lesson.** Most authoring domains have one central human quality-control act. Identify it during
the intent stage. If the pipeline removes it, state explicitly what mechanically replaces it, so
nobody treats the substitute as optional.

**Evidence.** Every practitioner source on script writing, across broadcast, audiobook, technical
communication and lecture coaching, puts "read it aloud and revise" at the centre of the method.
The pipeline sends the script straight to speech synthesis, and the faculty member stated plainly
that they would not read a 7,600-word script line by line. The mechanical checks are therefore not
a convenience layer, they are the entire substitute for the domain's primary quality control, and
that was nowhere written down.

---

## Where each attaches

| Lesson | Stage | Change shape |
|---|---|---|
| L14 | grounding | add the layer question to the anchor check |
| L15 | draft, test | criterion template requires an observable and a failing example |
| L16 | test | motivating artifact enters the acceptance suite |
| L17 | test | run the instrument over shipped exemplars |
| L18 | test | independent reimplementation gate for any threshold |
| L19 | grounding | corpus-provenance statement before derivation |
| L20 | architecture, draft | presence check and reported value as the defaults |
| L21 | release | mechanical registry-completeness check |
| L22 | draft | anti-pattern rules checked against genre evidence |
| L23 | intent | name the domain's verification act and its substitute |

## Honest limits

These come from one investigation in one domain. L14, L18 and L19 are the ones I would defend
anywhere; they are about how evidence behaves rather than about narration. L17, L21 and L22 are
mechanically cheap and low-risk. L23 is the least tested and may be a special case of the intent
stage's existing work rather than a new lesson.

None of this is implemented. Adopting any of it should go through the pipeline's own change
process rather than direct edits to `lessons_learned.md`.
