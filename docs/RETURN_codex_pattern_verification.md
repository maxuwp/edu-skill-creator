<!-- Filed verbatim from Codex's return, 2026-08-01. One change: a path citation into the POSED repository was unbackticked so this repository's citation check does not try to resolve it locally. No content altered. -->

# Codex pattern verification

**Priming declaration:** Before this classification, I had already read
`L20_foundation_regress.md`, `L22_controlled_scope_escalation.md`, and the vivid pattern description
in the handoff. This result is therefore pattern-primed. I did not alter the independent overlap
coding completed before reading the pattern handoff.

**Contiguous run:** my four POSED 1.64 implementation-review rounds, beginning with the first
network-dependency review of the staged offline gate-page implementation and ending with the round
that found the `srcdoc` and `meta refresh` bypasses. The surviving consolidated record is
docs/HANDOFF_Claude_1.64_implementation_review_2026-07-25.md in the POSED repository (unbackticked: it belongs to another tree, and a backticked path here would be read as a citation into this one); it states that four rounds found four
distinct mechanisms, but it does not preserve a separate object declaration and finding count for
each round.

rounds examined:            4, POSED 1.64 implementation-review rounds 1 through 4
convergence:                0
governed rebase:            1
silent descent:             0
undecidable:                3

## Round classification

| Round | Surviving evidence | Verdict | Basis |
|---|---|---|---|
| 1 | One of four successively discovered network mechanisms, but no round-specific object declaration or finding count survives in the consolidated record. | undecidable | The record cannot establish whether the object held, moved, or moved downward. |
| 2 | A second mechanism was found after the first repair, but the final record does not preserve enough round structure to distinguish deeper-layer movement from broader attack-surface coverage. | undecidable | Repeated bypass discovery is not by itself evidence of foundation descent. |
| 3 | A third mechanism was found, again without a preserved round object, scope declaration, or complete findings population. | undecidable | The pattern cannot be inferred from sequence order alone. |
| 4 | The report explicitly states that URL enumeration was not the control and replaces it with deny-by-default CSP, while retaining the parser as defense in depth. | governed rebase | The control object changed from enumerating network-capable syntax to enforcing a browser policy, and the change was explicitly declared and dispositioned. |

## Strongest counter-example

This run is a limited counter-example to treating repeated review findings as foundation regress by
default. Four mechanisms were discovered across four rounds, but the earlier parser work was retained
as defense in depth rather than discarded, and the final shift to CSP was declared. The surviving
record supports repeated adversarial coverage plus one governed rebase. It does not support silent
descent. It also does not prove convergence, because the record lacks round-specific finding
populations and no later round establishes that the bypass class is closed.

## Silent-descent specimen

None can be established from this contiguous run. Assigning one would require inferring undeclared
objects from a retrospective summary, which would be coding the hypothesis into the evidence.

## Missing instrumentation

Each round would have needed:

- an object-of-record id and hash,
- declared scope and layer before review,
- enumerated review breadth,
- complete finding count and stable finding ids,
- files and dependency nodes changed by the repair,
- whether the change was declared local, rebase, or outside scope before implementation,
- carried-forward confirmed properties,
- superseded work and why,
- token, call, and elapsed-time records.

The current record preserves mechanisms and final evidence, but not enough temporal structure to
classify three of four rounds.

## Measured cost

- Measured: four review rounds and four distinct bypass mechanisms.
- Preserved rather than discarded: the parser remained as defense in depth after CSP became the
  primary control.
- Not recorded: tokens, model calls, elapsed reviewer time, or the amount of implementation work
  rewritten per round.

## Interpretation

This run does not verify the foundation-regress hypothesis. It shows that the proposed four-way
classification is usable only when round objects are recorded prospectively. It also shows that
multiple rounds can reflect expanding adversarial coverage rather than downward movement, so future
instrumentation must distinguish breadth expansion from depth descent.
