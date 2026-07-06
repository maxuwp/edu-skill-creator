---
name: page-intent
description: PAGE Stage 1 — Intent interview for a new educational plugin. Captures purpose, users, artifacts, gates, and the contested-choices inventory (pedagogical decisions that must become explicit options, never defaults). Triggers - when the page umbrella dispatches Stage 1, or the user says "let's scope the new educational plugin".
version: "1.0"
---

# PAGE Stage 1: Intent Interview

Borrowed from Anthropic's skill-creator ("capture intent, then interview") and hardened
by lesson L2. Output: `intent.md`, approved by the author at the stage gate.

## Part A — Core intent (interview, don't assume)

Ask, in the author's language, and record verbatim answers:

1. **Job.** What teaching task does this plugin do end-to-end? What does "done" look
   like — name the concrete artifacts (deck, lab sheet, quiz bank, rubric, feedback…)?
2. **Human.** Who sits at the gates — faculty, TA, instructional designer, student?
   How much time will they realistically give per gate? (This bounds gate count — L4.)
3. **Inputs.** What does the human bring (syllabus, paper, plan, past materials)? Which
   inputs are ground truth that later stages must never contradict (→ canonical facts)?
4. **Trigger.** When should the plugin activate? Draft 3 should-trigger and 3
   should-not-trigger phrasings (near-misses, not strawmen) for the description.
5. **Scale.** One-off aid or repeated workflow? Repeated workflows justify manifests,
   versioned artifact snapshots, and reflect loops; one-offs may not.
6. **Existing practice.** How does the human do this today, without AI? (The existing
   practice usually IS the grounded process — capture it before proposing anything.)

## Part B — Contested-choices inventory (mandatory, L2)

List every pedagogically contested decision the plugin's outputs would embody. Standard
probes — go beyond them if the domain suggests more:

- Student AI use (the POSED four-stance model: no-ai / ai-permitted / ai-guided /
  ai-central) — relevant to any plugin producing student-facing work.
- Assessment philosophy: formative vs. summative weighting, partial credit, rubric
  strictness, curve policy.
- Collaboration: individual vs. group defaults; role structures (e.g. POGIL) vs. free.
- Rigor/pace calibration; prerequisite assumptions.
- Accessibility posture beyond legal minimums (UDL depth).
- Instructor voice: how much of the author's persona flavors generated text.

For each item record: the option set, a neutral one-sentence introduction for each
option, and where in the new plugin's intake it gets asked. **The plugin author's own
preference may appear as one option among several — flag any spot where a draft would
bake it in as the default.**

## Part C — Gate sketch

Rough count and placement of human gates (final design happens in Stage 3). Sanity check
against Part A.2: if the sketch demands more gate-minutes than the human will give,
record the tension now — architecture must resolve it (fewer, narrower gates or an
express mode), not ignore it.

## Output — `intent.md`

Sections: Job & artifacts · Human-in-the-loop & gate budget · Inputs & canonical facts ·
Trigger phrasings (should / should-not) · Scale & lifecycle · Existing practice ·
Contested-choices inventory (table) · Gate sketch · Open questions.

## Gate

Present `intent.md` to the author section by section; collect structured feedback
(agree / revise + comment per section). Do not proceed to `page-grounding` until the
author approves. Never approve on their behalf.
