---
name: edu-skill-creator-intent
description: Edu Skill Creator Stage 1 — Intent interview for a new educational plugin. Captures purpose, users, artifacts, gates, and the contested-choices inventory (pedagogical decisions that must become explicit options, never defaults). Triggers - when the edu-skill-creator umbrella dispatches Stage 1, or the user says "let's scope the new educational plugin".
version: "1.4"
---

# Edu Skill Creator Stage 1: Intent Interview

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
7. **Data, privacy & security** *(anchors: FERPA/PPRA + Dept. of Education PTAC
   guidance, NIST SSDF — see the grounding library's privacy/security/accessibility
   section)*. Will the plugin ever see student work, grades, names, or other
   identifiable student information (PII)? If yes, each of these gets an explicit
   answer recorded in the profile — an educational tool that touches student data
   without governance is a liability, not a convenience:
   - Which privacy regimes apply — FERPA/PPRA (US), institutional policy, anything
     stricter the institution has adopted?
   - Retention and deletion: how long may artifacts containing student data live, and
     who deletes them?
   - De-identification: can the pipeline run on de-identified data (it usually can —
     prefer it); where is re-identification actually necessary?
   - External exposure: does any stage send content to an external API or vendor?
     Which content, to whom, disclosed where?
   - Logging and redaction: what do session logs, review logs, and gate decision files
     capture — and what must be redacted from them?
   - Permissions: who may run the plugin, who may read its artifacts?
8. **Accessibility** *(anchors: WCAG 2.2 for conformance, UDL 3.0 for learning-design
   depth)*. What accessibility requirements bind the outputs (institutional
   WCAG mandate? student accommodations the artifacts must support?) — and note that
   any HITL web pages the plugin generates are themselves a UI that must be operable
   by keyboard and screen reader (the gate human may be the one who needs it).

## Part B — Contested-choices inventory (mandatory, L2)

List every pedagogically contested decision the plugin's outputs would embody. Work the
probes one at a time — surface an item, agree on its option set and neutral intros, then
move to the next; dumping the whole synthesis on the author at once is exactly the gate
overload L4 warns about. Standard probes — go beyond them if the domain suggests more:

- Student AI use (the POSED four-stance model: no-ai / ai-permitted / ai-guided /
  ai-central) — relevant to any plugin producing student-facing work.
- Assessment philosophy: formative vs. summative weighting, partial credit, rubric
  strictness, curve policy.
- Collaboration: individual vs. group defaults; role structures (e.g. POGIL) vs. free.
- Rigor/pace calibration; prerequisite assumptions.
- Accessibility posture: legal minimum (WCAG conformance) vs. UDL-deep design — a real
  choice with real authoring cost, so it is the educator's, not the author's.
- Student-data handling posture: no-student-data (pipeline refuses PII) /
  de-identified-only / identified-with-governance (retention, permissions, redaction
  all specified).
- External-service posture: local-only / disclosed external APIs with per-run consent /
  institution-approved vendors only.
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
Data, privacy & accessibility profile (Part A.7–A.8 answers) · Contested-choices
inventory (table) · Gate sketch · Open questions.

## Gate

Present `intent.md` to the author section by section; collect structured feedback
(agree / revise + comment per section) and persist it as
`intent_gate_decision.json` (`{decision, section_feedback{}, guidance}` — the
decision-JSON discipline from gate_design_patterns.md, applied to Edu Skill Creator itself). Do not
proceed to `edu-skill-creator-grounding` until the author approves. Never approve on their behalf.
If `intent.md` is revised after approval, downstream Edu Skill Creator artifacts go stale per the
umbrella's operating rules.
