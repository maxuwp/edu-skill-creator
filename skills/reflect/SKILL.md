---
name: page-reflect
description: PAGE Stage 8 — Post-pilot reflection for an educational plugin built with PAGE. Harvests what the pilot's gates, feedback, and failures revealed, redacts identifying information, routes the ledger through an independent fresh-context review, and turns each approved item into an improvement to the new plugin AND, where general, into a new or amended lesson in PAGE's own lessons_learned.md. Triggers - after the new plugin's first real pilot, or when the user says "reflect on the pilot / harvest lessons".
version: "1.2"
---

# PAGE Stage 8: Reflect

The loop that made POSED improve across 14 releases instead of staying v1.0. Runs after
the new plugin's first real pilot (and any later one on request). Nothing here
auto-applies — every harvested item is an approve-per-item decision (L5, L9).

**Inputs (exact):** the pilot's session directory — its gate decision files
(`*_gate_decision.json` / `*_decision.json`), its `reviews/*.json` logs, and the
plugin's improvements file if one exists. **Refuses to run** without a completed pilot
session (at least one artifact carried through its final gate); reflecting on a
half-run pilot harvests process noise, not lessons. **Outputs:**
`reflect_ledger.json` (the triaged findings), `reflect_gate_decision.json`, and the
approved edits routed as described under "Gate".

## Harvest sources

1. **Gate decision files.** Every revise/regenerate with its comments — what did the
   human keep correcting? Repeated corrections are skill defects, not user quirks.
2. **Review logs.** Findings that recurred across skills or rounds; rubric dimensions
   that never discriminated (always full marks = dead weight — skill-creator's
   "non-discriminating assertions" insight applies to rubrics too).
3. **The human's own words.** Verbatim complaints and praise from the pilot session;
   preserve exact phrasing — it's the RED-scenario material for the next test pass.
4. **Process breaks.** Places the pipeline stalled, was bypassed, or needed manual
   rescue.

## Redaction before anything is committed (data governance)

Gate comments and session artifacts can contain names, student work fragments, grades,
or course-identifying detail. Before any harvested text enters `reflect_ledger.json` —
and doubly before anything is promoted to a shared, committed file like PAGE's
`lessons_learned.md` — apply the plugin's own data posture (its architecture data-flow
model governs its session data): strip student PII entirely; replace personal names
and course identifiers with roles ("the TA", "the intro course"); keep the educator's
own verbatim words only with their consent at this stage's gate, otherwise paraphrase.
The scrub is itself a ledger column (`redactions`) so the reviewer can check it.

## Triage each finding into exactly one ledger row

`reflect_ledger.json` rows keyed `f1…fn` — numbering continues from the previous
pilot's ledger when one exists (that ledger is then an input), so ids stay unique
across pilots:

| Field | Content |
|---|---|
| id | stable `f<n>` — never renumbered |
| finding | What happened, with source (gate file / quote / log) — post-redaction |
| redactions | what was scrubbed or paraphrased, so the scrub is reviewable |
| scope | `plugin` (fix this plugin) / `page` (general lesson for all educational plugins) / `both` |
| proposal | The concrete change (skill text, rubric, gate, architecture) |
| cost | Small edit / new release / architecture change |

**Scope discipline for lessons:** promote a finding to PAGE's `lessons_learned.md` only
if it would plausibly bite a *different* educational plugin; one-plugin quirks stay
local. When promoting, follow the ledger format there (rule / failure that taught it /
enforcement point) and link the enforcement into the relevant PAGE skill in the same
release.

## Independent review (before the author sees the ledger — L3)

The ledger is a drafted artifact — self-harvested lessons are exactly where
rationalization creeps in. Dispatch a fresh subagent session whose inputs are ONLY: the
draft `reflect_ledger.json`, the pilot's gate decision files, and the pilot's review
logs. It checks: each finding is actually supported by its cited source (no invented
morals), scope classification is honest (`page`-scope claims generalize beyond this
plugin), redaction completeness (no PII or identifying detail survived), and proposals
match findings. Log to `reviews/reflect_ledger_review.json` BEFORE the gate opens; fix
blocking findings and re-review. Like the other map/design reviews, this is a binary
inspection with severity-classed findings, not a scored /100 rubric (Fagan/IEEE 1028 —
points belong on quality judgments, not conformance checks); the gate's summary card
shows finding counts by severity.

## Gate

| Field | Value |
|---|---|
| gate_id | `reflect_gate` |
| decision | Per ledger row: approve / defer / reject (+ comment); plus consent for any verbatim quote retained |
| artifact | `reflect_ledger.json`, rows keyed `f<n>` |
| reviewer | fresh-context ledger review above (`reviews/reflect_ledger_review.json`) |
| decision_file | `reflect_gate_decision.json` — `{rows:[{id, disposition, comment}], quote_consent: true\|false, guidance}` |
| owns | approved `plugin`-scope rows feed the plugin's next release; approved `page`-scope rows become a PAGE release (which itself runs `page-release` — PAGE eats its own dog food) |
| invalidates | nothing retroactively; changes land through the owning releases |
| consent | n/a — the harvest is cheap; the per-row approval IS the gate |

## Also harvest the human's preferences

Pilot decisions often reveal durable preferences (voice, pacing, gate appetite) —
characterizing an educator's perspective is TPI's territory (Pratt & Collins, within
its descriptive scope). Offer — never assume — to record them in the plugin's persona/preferences artifact so the next
run starts closer to right. Contested pedagogical stances stay per-run choices (L2);
preferences about *interaction with the tool* may persist.
