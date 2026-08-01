<!-- Detail for L22. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L22 — Controlled scope escalation: scope is an artifact, and expansion is graded by impact

**Rule.** Every review loop and every fix round **declares its scope before it starts** — the object
of record, the breadth it must cover, its budget, and what the accepted foundation is. A finding
whose fix would land outside that foundation is **scope pressure**, reported separately and never
fixed in the same pass. Expansion is graded by impact rather than treated uniformly, and the
response is a state change rather than a licence: the reviewer returns `REBASE_REQUIRED`, and the
harness stops calling the implementer instead of asking it to set its own constraint aside. The
contract — the three states, the reviewer outcomes, the packet shape and the settlement test — is
defined once in `docs/DESIGN_clarify_execute_rebase_2026-08-01.md`; the runnable reviewer procedure
is `<edu-skill-creator-skill-dir>/reference/review_scope_protocol.md`.

**Amended 2026-08-01, after three independent reviews.** Three parts of the first version did not
survive, and the corrections matter more than the original text:

1. **The one-controlled-descent reserve is withdrawn.** It was invented here, and this project's own
   research found that nobody has measured whether tighter scope constraints raise or lower an
   agent's resolution rate. An unevidenced cap in a lesson is the failure L16 names.
2. **A single layer ladder is not the decision rule.** Escalation is decided on the dependency and
   impact cone; layer labels stay as reporting vocabulary. A control plane such as the release lint
   is not merely "deeper", and defects travel laterally through shared dependencies as often as down.
3. **Faculty authority was drawn too wide.** It attaches to pedagogical intent, approved decisions,
   risk and cost — not to every technical boundary adjustment (L4).

What survived unchanged: declaring scope before starting, separating scope pressure from findings,
and grading the response by impact rather than treating every lower-layer change as a restart.

**Rebase, do not restart — the rule the first version was missing entirely.** When the foundation
changes, **every prior decision is protected by default and must be given a recorded disposition**:
carried forward unchanged, carried forward as a constraint on the new foundation, adapted because its
dependencies moved, or invalidated with the evidence for why it could not survive. Nothing is
regenerated merely because its upstream changed; regeneration requires a demonstrated
incompatibility. And the new foundation is chosen using **all** the requirements gathered so far,
including the ones that only surfaced while building on the wrong one — those are inputs to the new
choice, not casualties of it.

This is the part that is specific to doing the work with an agent rather than with a project team. An
agent holds the whole history — the conversation, the requirements, the rejected alternatives and
why they were rejected — and can consume it in one pass to choose a better foundation. A human team
re-derives that history slowly and partially, which is why human change control treats a relocation
as expensive and mostly avoids it. Discarding the accumulated design in order to "start clean" throws
away the one advantage the medium actually provides, and it converts a rebase into the relocation
amnesia L20 names. An invalidated decision still carries knowledge: keep it as a candidate, a
constraint, a preference signal, or a negative example.

**Why this is not already L20.** L20 names the pathology: when a fix changes a layer below the
artifact under review, the loop is descending rather than converging. It is right about detection
and wrong about response, in one direction — read strictly, its stop-and-re-open applies equally to a
one-line adjacent correction and to replacing the foundation everything stands on. That symmetry is
what makes teams either freeze (nobody dares touch anything below the line) or creep (everyone
touches it and calls it small). **Every lower-layer change is a re-scope; not every re-scope is a
restart.** L20 supplies the signal, L22 supplies the graded response, and neither works alone.

**The reviewer failure this fixes, which is upstream of the process failure.** Reviewers follow the
first defect downward. The result is a deep finding and an unmeasured surface: the horizontal scan
was never completed, so the next round rediscovers what nobody looked at, and the loop's findings
never fall for a reason that has nothing to do with quality. The rule is order, not effort — and the
order is **foundation first, then breadth**: test the foundation assumptions and the acceptance
oracle, and only if they hold, complete the declared breadth and report once. A reviewer who returns
one new issue per round, each deeper than the last, is producing descent and it will read as
diligence.

**Corrected 2026-08-01:** the first version required the complete horizontal scan before any finding
was written, with no exception. That is wrong in the case that matters most — once a foundation
assumption is demonstrably invalid, reviewing its descendants produces findings that will be
discarded, which is the token waste this lesson exists to prevent. Foundation invalidation
interrupts the scan and produces one consolidated rebase packet instead.

**Failure that taught it.** Three loops, independently, in this project's own records. A validator
audit descended artifact → mechanism → evidence across three rounds and roughly forty findings that
reduced to one defect shape. This repository's own audit rounds 1 to 3 each replaced a mechanism
wholesale and each replacement carried the next round's defect. A POSED release loop moved from
check-outcome prose to the definition of the operand to a bands file to an era gate to a lint pin,
five objects in a row, while the findings chart looked healthy. In none of the three did anyone
decide to expand; in all three the scope expanded. That is the tell: **unrecorded expansion is the
failure, not expansion.**

Three external reviewers, asked independently how to control this, returned the same structure from
three different traditions — timeboxed spikes that convert an over-running fix into a re-scope
proposal, one-logical-change commit discipline that files a deeper defect instead of absorbing it,
and incident command re-declaring an incident's type rather than letting one quietly grow. The
convergence is the argument: the mechanism they share is that **scope must be a declared artifact
with an owner**, and everything else is local detail.

**Grounding.** Graded change classification with a named change authority is standard
configuration-management practice. NASA's Systems Engineering Handbook separates a *major* change
(significant impact — baseline specification, cost, safety, interface compatibility, training) from a
*minor* one (documentation or process, no impact on interchangeability), and routes changes through a
board chaired by someone with change authority. Scope limit: that grounds the shape — baseline,
classification by impact, named authority, authorization before implementation. It does not license
our four class names or the one-descent reserve, which are local rules and are labelled as such in
the protocol.

**Applies to.** `edu-skill-creator-architecture` (each reviewer pairing declares its boundary,
classes, authority and reserve), `edu-skill-creator-draft` (review briefs separate in-scope findings
from scope pressure), `edu-skill-creator-test` (each round records its layer and breadth),
`edu-skill-creator-reflect` (abandoned repairs are harvested as implementation-neutral invariants,
never as patches to the thing being abandoned), `edu-skill-creator-release` (a silent layer descent
blocks a release).

**Related.** L20 supplies the detection signal and the convergence-versus-descent metric this lesson
routes on. L19 supplies the protected baseline a re-scope must carry across. L14 supplies the layer
vocabulary. L4's gate budget is the reason the two cheap classes do not reach the faculty member at
all. L5 is why the two expensive ones must.

**Status of enforcement.** Prose and procedure only, as of 2026-08-01. Nothing reads a declaration
block, nothing detects that a fix touched outside the accepted foundation, and no harness yet stops
an implementer on `REBASE_REQUIRED`. Treat an unwired rule as unenforced (L13) and do not cite this
lesson as a gate. The contract this lesson routes to is
`docs/DESIGN_clarify_execute_rebase_2026-08-01.md`, which also records what is **not** established:
that any of it saves tokens, and that minimal-diff discipline is what stalled our own loops. Both
remain hypotheses until the per-round instrumentation exists.
