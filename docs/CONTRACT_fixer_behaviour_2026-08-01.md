# Fixer contract — for the agent that implements what a reviewer found

**Status: PROPOSED, not yet wired.** Nothing loads it. Companion to
`docs/CONTRACT_reviewer_behaviour_2026-08-01.md` and
`docs/CONTRACT_designing_reviewers_in_skills_2026-08-01.md`, and deliberately shorter than both: a
fixer reads its contract while holding a diff in its head.

**Why it exists.** The reviewer contract ends at "a separate pass implements it." Nothing then told
that pass how to behave, and the gap is where measured damage came from: in one recorded round,
**three findings were defects introduced by the previous round's own fixes**, and in another, a
protected-baseline property was broken by a fix and had to be repaired by narrowing the fix.

---

## 1. What you receive, and what you refuse to start without

A review envelope carrying `findings` (each with its `finding_id`, `acceptance_constraints`,
`smallest_change`, `affected_dependencies`, `preserve`) and `do_not_break` referencing
`confirmed_id`s.

If the finding you were handed has no `smallest_change` and no `acceptance_constraints`, do not
invent them. Return `implementation_status: unrunnable` with the reason. A fixer that infers the
intended repair is the failure mode the reviewer contract's §4 exists to prevent, arriving one step
later.

## 2. Implement the named change. Nothing else.

- **Only the findings you were given.** Not the ones you notice on the way.
- **The smallest change that satisfies the acceptance constraints** — not the change you would have
  designed, and not a redesign of the surrounding surface.
- **No opportunistic cleanup.** A rename, a reformat, a "while I'm here" is a separate pass. It also
  destroys the delta review, because a reviewer that has to read unrelated churn cannot review the
  fix.

## 3. Re-establish the protected baseline, and say how

Every `do_not_break` entry must still hold when you finish, and you state **how you checked each
one** — by re-running its recorded `how_verified`, not by reasoning that your change could not have
affected it.

*Evidence: a property recorded as confirmed in one round was later found unreachable on a real
session, so it had never been true. A baseline re-checked by argument is not re-checked.*

## 4. When the named change turns out to be wrong, stop

Three cases, and all three are returns rather than improvisations:

```
the fix does not satisfy its own acceptance constraints  -> return, with what you observed
the fix requires touching something outside the finding  -> return as scope pressure
the finding rests on a wrong assumption about the need   -> return CLARIFICATION_REQUIRED
```

**Do not fix a bigger thing than you were asked to fix, and do not fix a smaller one and call it
done.** Either is a silent renegotiation of a contract someone else authorized.

## 5. Report what you did NOT do

This is the section that is always skipped and is the most useful one to whoever reviews the delta:

```
implemented:            [finding_id]
not_implemented:        [{finding_id, reason}]
deliberately_untouched: [things you noticed and left alone]
scope_pressure:         [{issue, load_bearing, required_boundary}]
baseline_recheck:       [{confirmed_id, how_rechecked, result}]
changed_units:          [what you edited]
dependency_affected:    [what depends on it and must be re-reviewed]
believed_unaffected:    [what you deemed out of the cone, and why]
implementation_status:  completed | unrunnable
unrunnable_reason:
cost:                   calls, tokens, elapsed — or "not recorded"
```

`believed_unaffected` is the field that makes delta review honest. A reviewer re-reading only the
delta is trusting your cone; say what you excluded so that trust is auditable rather than assumed.

## 6. Closure language, same rules as the reviewer

Never write fixed, closed, or done without saying which:

```
local repair    — this instance now behaves correctly
class closure   — this defect class cannot recur within a stated population or model
```

You are almost never entitled to the second. A fix closes an instance; whether the class is closed is
a judgement about the control model, and that is the reviewer's call on the next pass.

## 7. What this contract does not claim

That separating the finder from the fixer is worth its cost. It is supported by observed damage from
combining them, and the cost side is unmeasured — one of the open questions the reviewer contracts
also carry. Record `cost` honestly so that question can eventually be answered rather than argued.
