# Review Scope Protocol — how a reviewer declares, holds, and escalates scope

> **Amended 2026-08-01.** This file is the operational procedure. The contract it implements — the
> three states CLARIFY / EXECUTE / REBASE, the reviewer outcomes, the packet shape and the settlement
> test — is defined once in `docs/DESIGN_clarify_execute_rebase_2026-08-01.md` and is not restated
> here (L7). Three rules below were corrected after three independent reviews: the scan order is now
> foundation first, the one-descent reserve is withdrawn as unevidenced, and escalation is decided on
> the dependency cone rather than on a layer ladder.

**Who this is for.** Both reviewer populations, with one procedure:

- **In-skill reviewers** — the fresh-context reviewers this system dispatches (Stage 2 grounding-map
  review, Stage 3 architecture review, Stage 5 skill reviews, Stage 6 test rounds, Stage 8 ledger
  review), and the equivalents inside any plugin this tool generates.
- **External development reviewers** — a different model asked to review this repository's own work
  (change requests, releases, audits).

**The problem it solves.** A review finds a defect. Fixing it needs a change one layer below the
thing under review. The reviewer follows the defect down, the round's object silently changes, and
the loop descends instead of converging — the pathology L20 names. Scope expansion is not the
failure. **Unrecorded** scope expansion is. This protocol makes scope an artifact rather than an
impression, so expansion becomes a diff between what was declared and what was touched.

**Its relationship to the other rules.** L19 says a review has two halves and the confirmed half is
a protected baseline. L20 says a fix below the declared layer is a re-scope. This protocol says what
to *do* when that happens, and it grades the response by impact — because L20 rule 1, read strictly,
would send an adjacent one-line correction through the same stop-and-re-open as a foundation
rebuild.

---

## Part 1 — Declare, before reading anything

No review starts without this block. It is the contract; everything afterwards is measured against
it.

```
scope_declaration:
  object_of_record:   <the single artifact this round may change>
  layer:              artifact | mechanism | evidence | ground
  breadth:            <the enumerated set this round must cover completely>
  budget:             <max rounds, and what a round costs>
  authority:          <who may enact a re-scope, per class>
  baseline_carried:   <the verified list from the previous round, or "first round">
```

**Layer** is the depth axis, in the vocabulary L14 already uses:

| layer | what lives there |
|---|---|
| `artifact` | the thing produced — a skill body, a deck, a rubric's text, a plan |
| `mechanism` | the thing that judges the artifact — a validator, a lint check, a rubric's arithmetic |
| `evidence` | what the mechanism reads — a review log, a report, a manifest field |
| `ground` | what the evidence rests on — repository bytes, a fetched primary source, a human decision |

**Breadth** is the horizontal axis, and it must be enumerable: "the eight rows of the grounding map",
"all sixteen lint checks", "the five stage bodies". A breadth that cannot be enumerated cannot be
completed, and a scan that cannot be completed cannot report coverage (L11's population rule).

## Part 2 — Scan the whole declared breadth before writing any finding

This is the rule that stops descent, and it is the one reviewers break first.

0. **Test the foundation and the acceptance oracle first.** Do the accepted assumptions hold, and
   can the acceptance evidence actually establish the intended outcome? If either fails, **stop the
   detailed review here** and emit one consolidated rebase packet. Reviewing the descendants of an
   invalid foundation produces findings that will be discarded, which is the waste this protocol
   exists to prevent.
1. **Then complete the horizontal pass across the declared breadth.** Every item in `breadth`, all
   of them, before any finding is written up. A reviewer who follows the first defect downward
   returns one deep finding and an unmeasured surface; the next round then rediscovers what was
   never scanned.
2. **Record the confirmed half as you go** (L19): what you checked, found correct, and *how you
   verified it* — a mechanism, not an impression. This is the do-not-break baseline for the next
   round.
3. **When a defect's fix would require a change below the declared layer, do not follow it.** Note
   it as scope pressure (Part 3) and continue the horizontal pass. The investigation may continue;
   the authority to expand does not travel with it.
4. **One consolidated report per round.** Not one finding at a time, and not a new report each time
   something deeper appears.

## Part 3 — Report: findings in scope, pressure out of scope

The report has three parts, and the third is what makes scope governable.

**A. Confirmed** — the protected baseline, per L19.
**B. Findings** — in-scope only. Each states the smallest modification and what it must not disturb.
**C. Scope pressure** — everything the scan found that cannot be fixed inside the accepted
foundation. A scope-pressure entry is not a finding and is not fixed in this round; it is a proposal
for the next loop's foundation. Where it amounts to `REBASE_REQUIRED`, fill the **rebase packet**,
whose fields are defined once in `docs/DESIGN_clarify_execute_rebase_2026-08-01.md` and are not
repeated here. Its two halves a reviewer most often skips: the **complete prior-decision inventory**,
in which every existing decision is carried forward unchanged, carried forward as a constraint,
adapted, or invalidated *with evidence*; and **confirmed_unaffected**, which is what stops a rebase
turning into a regeneration.

## Part 4 — The four classes, and who may enact each

Both dimensions matter: how deep, and how wide. A one-line correction one layer down is not the same
event as replacing the layer everything stands on, and treating them the same is what makes teams
either freeze or creep.

| class | condition | response | who enacts |
|---|---|---|---|
| **Local delta** | same layer, breadth unchanged, baseline preserved | fix it, run the targeted regression | the round's author |
| **Controlled descent** | one adjacent layer, no contract, interface, gate or approved decision changes | record a scope amendment, carry the baseline forward, spend the reserve | the round's author, **recorded**, reviewable at the gate |
| **Major re-scope** | changes an interface, a rubric's meaning, an evidence source, a gate, a shared component, or an approved decision | stop implementing; complete the impact analysis; propose | **faculty authorization required** |
| **Relocation** | the current foundation cannot satisfy the invariant, or the evidence is circular, or the loop has stopped converging | close the old approach with a written design verdict; carry implementation-neutral invariants into the replacement | **faculty authorization required** |

**The bounded reserve is withdrawn (2026-08-01).** The first version capped a round at one
controlled descent. That number was invented here, and this project's own research found that nobody
has measured whether tighter scope constraints raise or lower an agent's resolution rate. What
replaces it is not another number: the reviewer returns one of `PASS`, `REVISE_LOCAL` or
`REBASE_REQUIRED`, and on `REBASE_REQUIRED` **the harness stops calling the implementer** and opens a
separate read-only rebase task. The implementer is never asked to set aside its own minimal-change
discipline, which is what makes this reliable rather than a matter of the agent's judgement.

**Escalate on the dependency cone, not on the ladder.** Layer labels stay useful for reporting what
moved. The decision to rebase is made on the impact cone: which artifacts depend on the invalidated
assumption, which are demonstrably unaffected, and what must be re-reviewed.

**Enacting a re-scope, once authorized.** Write a new declaration block, do not edit the old one.
The superseded declaration stays, with the reason, exactly as `c7`'s ledger supersession works. If
the foundation genuinely must be replaced, **build the replacement beside the old one and migrate**
rather than rewriting underneath live work, so the artifact under review never stands on a layer
being rebuilt beneath it.

## Part 5 — Two brief blocks, ready to paste

**For an in-skill reviewer** (goes into the stage's review dispatch):

> Your review boundary is: **⟨object of record⟩**, at layer **⟨layer⟩**, covering **⟨enumerated
> breadth⟩**. Scan all of it before writing any finding. Record first what you checked and found
> correct, with how you verified it — that is the do-not-break baseline. Then report in-scope
> findings, each as the smallest modification that keeps that baseline true. Anything whose fix
> would require a change below your declared layer goes in a separate `scope_pressure` section, not
> in the fix list, and is not fixed by you. End with one recommendation: continue, amend scope,
> major re-scope, or relocate.

**For an external development reviewer** (goes into the handoff):

> **Scope contract for this pass.** Object of record: ⟨…⟩. Layer: ⟨…⟩. Breadth you must cover
> completely: ⟨enumerated list⟩. Budget: ⟨…⟩. Carried baseline: ⟨previous round's verified list —
> re-verify, do not assume⟩. Findings that require a change below the declared layer are scope
> pressure, not findings: report them separately with their impact cone and a recommended class.
> Do not propose an implementation beyond the boundary. If you believe the boundary itself is wrong,
> say so in one line marked `challenge-to-scope`; it will be routed as a re-scope proposal rather
> than folded into this pass.

## Part 6 — What this does not solve, stated

- **It does not tell you the right layer to declare.** A boundary drawn at the wrong layer produces
  a complete, well-governed, useless review. Declaring badly is cheaper to detect than descending
  silently, which is the whole trade, but it is still a judgment.
- **It does not price a re-scope.** `estimated_cost` in rounds is an estimate by the party who wants
  the expansion.
- **It is not yet enforced.** Nothing in the lint reads a declaration block or notices that a fix
  touched below the declared layer. Until that exists, this is a discipline, not a gate — and this
  repository's own history (L11, L13) says unenforced discipline drifts. Wiring it is scoped as
  future change-request rows, deliberately not folded into a change request already under gate.

## Grounding

**Graded change classification with a named change authority** is standard configuration-management
practice, not an invention here. NASA's Systems Engineering Handbook distinguishes a **"major"**
change — one "that has significant impact (i.e., requires retrofit of delivered products or affects
the baseline specification, cost, safety, compatibility with interfacing products, or operator, or
maintenance training)" — from a **"minor"** change, which "corrects or modifies configuration
documentation or processes without impact to the interchangeability of products or system elements",
and routes changes through a control board "chaired by someone with program/project change
authority" (verified at nasa.gov, 2026-08-01). *Scope limit:* this grounds the **shape** — baseline,
classification by impact, a named authority, authorization before implementation. It does not
license the four class names above, which are ours, nor the bounded reserve, which is a local rule.

Corroborating practice, not load-bearing here: incident-command systems re-declare an incident's
complexity type rather than letting one grow silently, and transfer command when the type changes.
The primary training text was not fetched in this pass, so it is recorded as an illustration rather
than an anchor.

Practitioner sources for the remaining moves — timeboxed spikes, one logical change per commit,
architecture decision records, branch-by-abstraction — are widely documented engineering practice
without a validating study behind them. They are cited as craft, and this document says so rather
than dressing them as evidence.
