# CR 1.10 rev 2 — Harvest triage: POSED 1.31–1.63, the L14–L23 proposal, and the Codex review

**Prepared by:** Claude (Fable 5) · rev 1 2026-07-28 · **rev 2 2026-07-28, after Codex review of `ea1a9ce`**
**Status:** PROPOSED. Nothing implemented.
**Decision artifact:** `reflect_ledger.json` (18 rows, `f1`–`f18`). **This document is a readable
synthesis of that ledger, not the thing being approved.** Where the two differ, the ledger governs.
**Gate:** Stage 8 per-row, after the independent ledger review in `reviews/reflect_ledger_review.json`.
Neither this CR, nor the ledger, nor any reviewing document is faculty approval.

## 0. What changed in rev 2, and why

Codex reviewed rev 1 and returned **revise before implementation** with nine findings. All nine
are accepted. Three deserve naming rather than quiet absorption.

**The harvest bypassed the process this plugin requires of everyone else.** Rev 1 was a narrative
synthesis. Stage 8 requires a `reflect_ledger.json` with stable rows, a redaction record, an
independent fresh-context review of the completed ledger, and a per-row gate. None existed. The
four harvesting readers were drafters; they are not the independent reviewer of the ledger they
helped produce. That is L3 violated at the meta level, by the drafter, on the plugin whose central
claim is that drafters do not review themselves. Rev 2 exists downstream of the real artifacts.

**Four of the six proposed lessons wrote one product's architecture into universal doctrine.**
Rev 1 made a hash-bound append-only ledger mandatory (L17), a locked process graph mandatory (L19),
bundled six unrelated verification mechanisms into one rule (L15), and prescribed a named human
pre-flight for every plugin (L18). This is the same error I had flagged in Codex's own
Recommendation 1 two turns before committing it four times. Mechanisms are now examples in an
implementation-patterns reference; the lessons state capabilities.

**Moving the index to the top was navigation, not disclosure.** Reading one lesson still loaded the
whole 3,297-word corpus, and a second stage-to-lesson map would have created exactly the drift class
L7 exists to prevent. Rev 2 proposes physical separation with one authoritative mapping.

## 1. What was read

| Source | Coverage | Method |
|---|---|---|
| POSED `CHANGELOG.md` @ `2ca8f7b` | 1.31–1.63, the whole unharvested span | Four fresh-context readers, one per range, each given the 13 shipped and 10 proposed lessons and told to decline product-specific findings |
| `docs/PROPOSED_lessons_L14_L23…` | 10 proposed lessons | Read in full; its author's stated limits respected |
| Codex improvement report | 12 recommendations | Read in full |
| Codex review of rev 1 | 9 findings | Read in full; all accepted |
| This repo @ `ea1a9ce` | Structural audit | Direct measurement |

The readers produced 16 candidates and declined **35** findings, now enumerated by range in the
ledger's `declined` block. Rev 1 said "roughly forty," which is not a checkable claim.

## 2. Progressive disclosure (ledger row `f1`)

Measured at `ea1a9ce`: 346 lines, 3,297 words, index at line 325 of 346, mean lesson 25 lines,
L13 alone 59 (an earlier figure of 81 counted to end of file and absorbed the index). The umbrella orders it read "before doing anything" while `skills/draft/SKILL.md:27-28`
tells authors that depth belongs in references "loaded on demand."

Proposed structure:

```text
reference/
  lesson_index.md          # always read: id, one-sentence rule, applicability, path
  lessons/L01_grounding.md # pulled when a stage needs it
  ...
```

Must satisfy: the umbrella reads only the compact index; each stage names the detailed files it
needs; **one** authoritative applicability mapping; lint catches dangling lesson ids and missing
enforcement targets; detailed evidence never duplicated into stage bodies. Stage-oriented bundles
are an acceptable alternative to per-lesson files.

This row is independent of every doctrine decision and should not be held hostage to them.

## 3. Proposed lessons, in implementation-neutral form

Full evidence and anchors are in the ledger rows cited. Wordings below incorporate Codex's
narrowing.

**`f2` — Check at the layer the claim is about.** For every criterion, name the observable layer
where the claim lives and verify at that layer; evidence from a proxy layer cannot satisfy the claim
unless the proxy-to-target mapping is justified and tested. Five independent discoveries across
five releases and two documents. The oral case is framed as a rubric that never inspected
spoken-language features, with zero contractions as one observed symptom rather than a universal
failure condition.

**`f3` — Verification reports are self-interested evidence.** Not a new lesson: fold into L11 as a
corollary — a verification report is evidence only when its provenance, target binding, freshness
and reproducibility are established, and a status that reduces scrutiny is assigned by the verifier,
never asserted by the producer. L11's testing requirements also gain the motivating-artifact rule
and independent threshold re-derivation.

**`f4` — Make compliant recovery paths cheap.** Make them visible, low-friction and auditable; when
the pipeline cannot proceed, provide a governed blocked-or-escalate outcome, otherwise users or
agents may stall or bypass the intended process. Stated as a system consequence; the grounding stage
should seek a usable-security or fail-safe-design anchor, with POSED incidents as examples only.

**`f5` — User decisions are authoritative constraints.** Preserve their meaning and trace them
through every downstream stage that can alter them; only a later user decision may waive or supersede
them. Ledgers, hashes and rendered-surface probes move to implementation patterns.

**`f6` — Evidence burden scales with a claim's specificity, consequence and volatility.** Precise or
time-sensitive claims need correspondingly precise and current support; low-stakes illustrative
claims are not burdened with irrelevant precision; never launder a precision claim through a
permissive category tag. Corpus provenance folds to L1, invented thresholds to L11, dated examples to
L9. No named human pre-flight is prescribed; architecture assigns owner and fallback.

**`f7` — When the subject is a process, its structure is content.** When a learning outcome requires
learners to apply a domain process or make a sequence of decisions, the instructional sequence and
assessment must preserve the grounded structure of that process. Graphs, state machines, checklists
and worked decision paths are example representations; the requirement is fidelity, not a locked graph.

## 4. Folds and concrete fixes

Folds are ledger rows `f8` and `f18`, split after independent review: `f8` carries the four folds
traceable to the L14–L23 document, `f18` the four sourced from named POSED releases, so the faculty
is not forced into one all-or-nothing call across seven destination lessons. Together they land
inside L1, L4, L6, L7, L9, L10 and L11 rather than becoming entries. Proposed-L23 is deferred per
its own author's limits.

Concrete fixes: `f9` adds a `require_bool` helper plus fixture to the validator template, which
currently has no boolean-type guidance and therefore propagates the truthiness gap into every
generated validator. `f10` adds review coverage to gate patterns **as a capability requirement**,
not as disabled controls: a gate must provide coverage evidence appropriate to the artifact, must be
accessible, must disclose what is tracked, and must not treat page visits as proof of understanding.

`f11` is POSED's missing registry rows. It stays evidence here and is **routed to a separate POSED
change request**; rev 1 wrongly placed it inside an edu-skill-creator release.

## 5. The Codex twelve

Adopt: R2 (`f12`), R5 (`f13`), R10 then R4 (`f14`), R8 and R11 via lessons rather than a parallel
rule family. **R12 changes from adopt to audit-and-complete** (`f17`): verified at `ea1a9ce`, 4 of 10
stages carry the stage-end summary instruction and 6 do not, so describing the capability as absent
was wrong. Probe before adopting: R1/R6 (`f15`), with the five falsifiable pass criteria Codex
supplied, since "completes without naming a product" was itself an unfalsifiable proxy. Later
independent slice: R3 (`f16`). Defer: R7, R9 (`f17`).

## 6. Release sequence, split by risk and ownership

| Release | Scope |
|---|---|
| 1.10 | Stage 8 artifacts complete + progressive-disclosure restructure only |
| 1.11 | Only the faculty-approved lesson rows and folds, with stage-level enforcement links |
| 1.12 | `require_bool`; review-coverage capability |
| 1.13 | Skill-versus-application classification; shared metadata parser; complete the six missing stage summaries |
| 1.14 | Permanent test corpus, then routing evaluations against it |
| Probe | R1/R6 capability-contract experiment, before any scaffold or architecture refactor |
| Later | Delta review; usage logging and pipeline graph only if a pilot demonstrates need |

Rev 1 called the restructure plus six lessons plus all folds "large but mechanical." The restructure
is mechanical; deciding doctrine, enforcement ownership and lesson boundaries is not, and bundling
them let a judgment call ride on an editorial one.

## 7. Independent review of this ledger

`reviews/reflect_ledger_review.json` — 1 blocking, 2 major, 4 minor, all addressed. It spot-checked
roughly twenty claims against POSED @`2ca8f7b` and this repo @`ea1a9ce`, confirming several verbatim
quotes letter-for-letter and the stage-summary census exactly. It caught four things worth recording:
`f3` described an AI reviewer's approval as a human one, inflating an AI-fooled-by-AI incident;
four folds had been carried through two documents on a blanket citation no reviewer could open, and
are now split to `f18` with named releases; `f8` bundled nine decisions across seven destinations,
the same over-broad gate L4 warns against; and "L13 alone 81" was measured to end-of-file, silently
absorbing the index. A re-review is required before the gate opens.

## 8. Standing caution

Two of the three evidence streams behind this CR are model-authored reviews, and this synthesis is
model-authored too. The strongest items are those where independent sources converged without
coordination — `f2` above all, discovered four times in three documents. The weakest are those
resting on a single release and no external corroboration; `f4`'s attribution of outcomes to agent
motivation is labelled `inferred` in the ledger for that reason. Per-row approval exists so those
can be declined individually.
