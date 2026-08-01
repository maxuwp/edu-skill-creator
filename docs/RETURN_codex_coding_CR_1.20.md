# Codex independent coding of CR 1.20 reviews

**Blindness declaration:** I did not open `docs/DATA_reviewer_overlap_2026-08-01.md`,
`docs/HANDOFF_pattern_verification_codex_grok.md`, or another coder's return before completing this
table. I recognize the confirm-first framing as prior work in which Codex participated, but I did
not author either numbered review being coded.

| # | concern, one sentence in my own words | Fable finding ids | Grok finding ids | raised by |
|---|---|---|---|---|
| 1 | The before and after reopening figures use different denominators and leave the final fix-set unobserved. | F1 | | Fable only |
| 2 | The claimed causal effect of the review brief is confounded by suite growth, reviewer changes, and accumulated surface hardening. | F2 | B6 | both |
| 3 | Baseline verification can be asserted with vague prose unless the schema and lint require a structured, rerunnable verification mechanism and reject vacuous entries. | F3 | B2, B7 | both |
| 4 | A wrong protected ledger entry lacks a governed supersession lifecycle, evidence burden, durable history, and named human authority. | F4 | B3, B8 | both |
| 5 | Unexamined author testimony carries a broader claim than its evidence permits. | F5 | | Fable only |
| 6 | The proposed ledger seed is not durable because the enumerated source rows are absent from the repository. | F6 | | Fable only |
| 7 | Calling POSED's mechanism "solved" overstates feasibility evidence as outcome evidence. | F7 | | Fable only |
| 8 | The evidence narrative incorrectly treats two brief changes as one intervention. | F8 | | Fable only |
| 9 | The generated contract would impose a heavyweight adversarial-review mechanism on plugins that do not have a multi-round review loop. | | B1 | Grok only |
| 10 | Requiring a non-empty verified set cannot honestly represent an unsalvageable artifact unless verified negative ground is allowed. | | B4 | Grok only |
| 11 | Treating a missing contract version as pre-era creates a permanent fail-open exemption. | | B5 | Grok only |
| 12 | Wiring downstream generators before the local schema and ledger have survived a real round can propagate a defective contract. | | B9 | Grok only |

total distinct concerns: 12
raised by both reviewers: 3
raised by exactly one: 9
percentage raised by exactly one: 75%

## Borderline merges

- Row 3 is the closest call. A defensible alternative splits it into an entry-level concern
  (`F3` + `B2`, structured and rerunnable `how_verified`) and a log-level concern (`B7`, at least
  one substantive non-boilerplate verification). I merged them because the same schema-and-lint
  modification package closes the common failure, a vacuous assertion becoming protected ground.
- Row 4 could be split into the supersession authorization/evidence workflow (`F4` + `B3`) and the
  orthogonal data-model rule that lifecycle status is not a truth verdict (`B8`). I merged them
  because a single first-class supersession lifecycle modification closes both.

## Findings not placed

- `B10` is not a defect claim. It confirms that `c17` is correctly deferred and asks only that its
  already-stated dependency on two rounds of the new schema remain explicit.

## Severity record

- Fable labelled F1-F4 major and F5-F8 minor.
- Grok labelled B1-B2 critical, B3-B7 major, and B8-B10 minor.
- Grok's critical B1 was raised by Grok alone. Critical B2 overlaps Fable F3, which Fable labelled
  major. Neither reviewer used a separate `blocking` label for these numbered findings.
