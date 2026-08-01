# Review request — fixer contract, revision 0

**For:** Codex. **From:** the Edu Skill Creator thread, 2026-08-01.
**Artifact:** `docs/CONTRACT_fixer_behaviour_2026-08-01.md`, revision 0, at HEAD `44ecce2`.
**Same discipline as your two previous passes**: one consolidated report, confirmed properties first,
findings as the smallest change naming what they must not disturb.

---

## 1. What it is and why it exists

The reviewer contract ends at "a separate pass implements it" and says nothing about how that pass
behaves. This fills that gap. It is deliberately shorter than both companions, on the reasoning that
a fixer reads its contract while holding a diff.

It has been through **no independent review**. Its companions are at revision 1 and revision 2.

## 2. Must not break — the agreed vocabulary

These are settled across the two reviewed contracts and this one must be consistent with them, not
re-litigate them:

- `review_status` / `implementation_status` orthogonal to the semantic outcome, with `unrunnable`
  never authorizing progress.
- `confirmed_id`, `finding_id`, and `preserve` resolving to declared ids.
- `scope_pressure` structured with `load_bearing`, `required_boundary`, `authorized_route`.
- The three-way closure language, and class closure bounded by a stated population or model.
- Escalation outcomes requiring a named consumer, persistence, and closing state.
- Cost recorded honestly, `not recorded` rather than estimated.

**If this contract's field names or semantics diverge from the reviewer envelope, that is a finding**
— an envelope that does not compose across the two roles is worse than no envelope, because a
mismatch surfaces only when something is already half-implemented.

## 3. Five places I am specifically unsure

1. **`believed_unaffected`.** I invented it. The claim is that delta review is only honest if the
   fixer states what it excluded from the dependency cone. It may be unfillable in practice, or it
   may be the field that makes the whole delta-review economy work. I cannot tell.
2. **"You are almost never entitled to class closure."** Possibly too strong. A fixer that replaces
   an enumerative control with a categorical one has arguably closed the class, and my rule would
   forbid it saying so.
3. **The three return cases in §4** — fails its acceptance constraints, needs something outside the
   finding, rests on a wrong assumption about the need. Are they exhaustive? A fourth I suspect but
   did not write: the finding is correct and the fix is trivial, but implementing it would break a
   `do_not_break` entry.
4. **Brevity.** Your disposition on revision 1 recommended a compact operative core rather than a
   word limit. I wrote this one short from the start. Check whether brevity dropped something
   load-bearing rather than something decorative.
5. **§2's "no opportunistic cleanup".** Absolute as written. Real diffs sometimes require an
   adjacent rename to compile. There may need to be a declared-and-listed exception rather than a
   prohibition.

## 4. Not in scope for this pass

Whether any of the three contracts should be wired into a skill — that is Dr. Ma's open decision.
Whether separating finder from fixer is worth its cost stays on the open-questions list; this
contract already declines to claim it.
