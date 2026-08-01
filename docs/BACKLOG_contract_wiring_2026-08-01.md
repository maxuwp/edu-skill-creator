# Backlog — deferred from contract reviews, not blockers

**Purpose.** L24 says a disposition check records what it would have designed rather than raising it
as a finding. This is where those items go. An item here is **not** an open defect and does not
reopen a settled artifact; it is a consideration for whoever wires the contracts into a skill.

Reopening a settled artifact requires a named member of the L24 reopen class: a critical
contradiction, a false approval, an irreversibility or data-loss risk, or a broken protected
property. Nothing in this file qualifies as recorded.

---

## From Codex's review of the fixer contract, revision 0 (2026-08-01)

The review returned six major and three minor findings, then withdrew that disposition and settled on
two local corrections, both now applied in revision 1. The remaining substance is recorded here.
Return filed at, outside this repository:
/Users/max/Library/CloudStorage/OneDrive-UniversityofWisconsin-Platteville/Research/2026 nsf/CODEX_REVIEW_fixer_contract_rev0_2026-08-01.md

| # | Item | Why it is not a blocker |
|---|---|---|
| B1 | Stale-input binding — the fixer should record the reviewer envelope's version or hash, so a fix implemented against a superseded review is detectable | The contract is not wired; there is no envelope with a version to bind to yet. Becomes real at wiring. |
| B2 | Outcome routing — the fixer's return has no field mapping its result back to the reviewer's four outcomes | The reviewer contract owns routing; duplicating it in the fixer contract risks the two drifting. Settle it once, in the harness. |
| B3 | Partial-edit reporting — a fix abandoned mid-way leaves the artifact in a state neither `completed` nor `unrunnable` describes | Real, and only observable once an actual harness can be interrupted. Add the state when there is a harness to interrupt. |
| B4 | Authorized supporting changes — an import, a fixture, a call-site rename that the named change strictly requires is currently indistinguishable from scope creep | The §4 return path covers it safely, if verbosely. Optimising the common case needs data on how often it fires. |
| B5 | Richer routing schema for `not_implemented` reasons | Enumerating reasons before observing them is the error L16 names. Collect the free-text reasons first. |

## From Codex's disposition check on the reviewer contracts, revision 1 (2026-08-01)

Closed by revision 2 of the designer contract. Carried here only as wiring notes.

| # | Item | Note |
|---|---|---|
| B6 | Do not inject both contracts into every reviewer prompt; maintain one compact operative core and link the rationale | Untested. Test retention through the actual harness before fixing a word limit. |
| B7 | Whether `REBASE_REQUIRED` should be renamed `RESCOPE_REQUIRED` with foundation rebase as its subtype | Cosmetic while unwired. Decide at wiring, once, and not again. |

## Open questions no contract settles

Carried across all three reviews, and unchanged: whether separate finder and fixer agents justify
their cost; whether delta-only model review preserves semantic defect yield; the measured frequency
of spontaneous escalation under verified opportunities; and whether same-brief parallel reviewers add
enough unique valid findings to justify routine use. All four need the per-round instrumentation that
does not exist yet, and none of them is answerable by another review round.
