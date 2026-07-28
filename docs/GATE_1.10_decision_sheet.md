# Gate 1.10 — decision sheet

28 decidable rows, grouped into 8 calls. Ledger: `reflect_ledger.json`. Two review rounds passed
(round 2: 0 blocking, open-the-gate). Reply with group letters; anything you don't mention stays undecided.

| # | Decision | Rows | What it does | My recommendation | Risk if wrong |
|---|---|---|---|---|---|
| **A** | Restructure the lessons file | f1 | Split the 346-line always-read ledger into a compact index + per-lesson files. Independent of every doctrine question. | **Approve.** Cheapest real fix on the board. | Low. Mechanical, reversible. |
| **B** | Four new lessons | f2, f5, f6, f7 | Check at the claim's layer · user decisions are binding constraints · evidence burden scales with precision · when the subject is a process, structure is content | **Approve.** f2 has five observed instances across four releases and one independent investigation. | Medium. These become permanent doctrine. |
| **C** | One conditional lesson | f4 | Make compliant recovery paths cheap (the "agent stalls or fabricates when blocked" rule) | **Approve for grounding investigation only.** It rests on inferred motivation with no published anchor; L1 says that isn't enough to ship. | Low if conditional, higher if shipped as-is. |
| **D** | Nine folds into existing lessons | f3, f19–f22, f24–f27 | Verification-report provenance → L11 · operational criteria → L11 · exemplar measurement → L11 · registry completeness → L7 · anti-tell vs genre → L10 · positional identity → L4 · silent downgrade → L6 · reuse semantics → L11 · language of instruction → L10 | **Approve as a block.** All anchored and verified; each is separable if you want to pull one. | Low. Corollaries, not new rules. |
| **E** | Concrete fixes | f9, f10, f28, f31 | `require_bool` in the validator template · risk-proportionate review coverage · stage summaries for the 6 stages lacking them · create the implementation-patterns reference | **Approve.** f31 must ship in the same release as B/f5 or the mechanisms are deleted rather than relocated. | Low. |
| **F** | Build items, sequenced | f12, f13, f14, f16, f15 | Skill-vs-application gate · shared metadata parser · tests + routing corpus · delta review · the capability/adapter probe | **Approve F1 (f12, f13) now; f14 next; f15 as an experiment; f16 later.** | Low. Each is its own release. |
| **G** | Deferrals | f23, f29, f30 | Proposed-L23 · usage logging · pipeline graph | **Defer all three.** No action, revisit on evidence. | None. |
| **H** | POSED registry repair | f11 | Five shipped stages missing from POSED's grounding registry | **Route to a separate POSED CR.** Not an edu-skill-creator release. | None here. |

**Quote consent — DECIDED 2026-07-28:** `q1` (the design-negligence line, f7) retained verbatim; `q2`
(the classroom-anecdote line, f6) paraphrased and its verbatim wording withheld from this public repository.

**Not asking about:** the 35 declined findings (enumerated in the ledger) and the three superseded bundle rows.
