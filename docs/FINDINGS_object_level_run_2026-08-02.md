# Findings from the first object-level run

**What this is.** Edu Skill Creator has built nothing. Every audit round to date has reviewed its
own skills, lints and lessons, which means every defect found so far is one the subject layer could
report about itself. On 2026-08-02 the author dispatched the umbrella for real, to build
`handwritten-to-deck`, a small skill converting handwritten teaching material into a deck. This file
records what running the process reveals about the process. It is a findings log, not a change
request: nothing here is fixed while the run is in progress, per L20, because a fix to the stage
skill is a change to the layer beneath the artifact under construction.

Status of each row: `observed` until it has a CR, then `carried to CR <n>`.

---

## F1 — `edu-skill-creator-intent` item 6 asks for the pre-AI practice, and the author rejected it

**Status:** observed.

**What the stage skill says.** Part A item 6 of `skills/intent/SKILL.md`: *"Existing practice. How
does the human do this today, without AI? (The existing practice usually IS the grounded process,
capture it before proposing anything.)"* The umbrella's Stage 1 output schema carries an
`Existing practice` section, so the question is not optional.

**What happened.** Asked directly, the author rejected the question:

> "it is bullshit. why should we follow the steps without ai. why don't you ask what i will do
> without electricity? you should figure out what you should do. first understand the topic,
> understand the logic, understand the potential flow, record every concept and expand the details.
> try to use pedagogical method for padding and explaining and then make the deck."

**Why the objection is sound, and not merely a preference.** Item 6's premise is that the manual
process encodes the real requirements. That holds when the tool automates a workflow the human
already runs. It fails when the tool does something the human could not previously do at all, and
in that case the manual practice encodes the workarounds a constraint forced, not the requirements.
For this skill the point is sharp: the pre-AI practice for a page of handwritten notes is to retype
it or project it, both of which are transcription, and anchoring to them would have produced a
transcription tool. The author's direction is a comprehension tool, which no manual practice
demonstrates because no human does it by hand.

**This repository already carries the lesson that names the error.** L23: *preserve the need,
reconsider the means, an expressed requirement may be a workaround for a limitation the new
foundation removes.* Item 6 instructs the opposite, and does so in the one stage whose output every
later stage inherits. The lesson index lists L23 as applying to `edu-skill-creator-intent`'s
assumption audit, so the two are already meant to meet and do not.

**What a fix would have to do, when a CR takes it.** Not delete item 6. The existing practice is
genuinely informative where one exists, and discarding it would trade one blind spot for another.
The item needs to ask two questions rather than one: what the human does today, and what part of
that is a workaround for a limitation this tool removes. It also needs to stop being mandatory in
the output schema, since "no manual practice exists, and here is why" is a complete answer that the
current section shape cannot express.

**Second-order note.** The same premise sits in `edu-skill-creator-grounding`, which grounds the
new plugin's stages in published frameworks. That is a different and safer question, because
published pedagogy is not a workaround for the absence of AI. No change is indicated there, and it
is recorded so a later sweep does not widen the fix by reflex (L13 sweeps the class, L22 keeps the
class from swallowing the neighbourhood).

---

## F2 — the interview's cost lands before the author sees anything

**Status:** observed, weaker than F1 and recorded so it is not lost.

Part A is nine items and Part B is eight probes, worked one at a time by instruction. For a plugin
the size of POSED that is proportionate. For a single small skill the interview is a larger artifact
than the thing being built, and the pressure to compress it is what produced this run's four-question
intake, which is a deviation from the stage skill's own procedure rather than an option it offers.

A stage that is routinely deviated from is a stage that has an unstated mode. Whether the fix is a
declared short form for small builds, or a rule that the interview's length scales with the gate
budget captured in item 2, is a design question for a CR rather than something to settle here.
