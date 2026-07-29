# E2 — semantic enforcement audit

**Run when:** any release that adds a lesson, a fold, a rubric flag, or a test scenario.
**Found in its first run:** a false claim that registry completeness was "implemented as check 11"
when no such check existed, which had survived two independent review rounds.

## Prompt

> Audit whether a skill set's claimed enforcement actually enforces anything. This is SEMANTIC, not
> structural — a lint already verifies that cited item NUMBERS exist. Verify the cited items actually
> SAY what is claimed.
>
> The claim table is `skills/edu-skill-creator/reference/lesson_index.md`: one row per lesson, with an
> "Applies to" column naming where it is enforced. For every row:
> 1. Open each cited target. Does it enforce THIS lesson? A number that exists but discusses something
>    unrelated is a FALSE CLAIM and your highest-value finding.
> 2. Is the enforcement real or decorative? "The reviewer should consider X" is not enforcement; a
>    blocking flag, a refusal condition, a required artifact or a computed check is.
> 3. Check three-way consistency: index row vs lesson detail file vs the target skill.
> 4. Any mechanism a lesson stopped mandating must appear in `implementation_patterns.md`. If it was
>    dropped and did not land there, that is a deletion masquerading as a relocation.
> 5. Any claim that something is "implemented as <check/script>" — open it and confirm it does that.
>
> Report false claims first, with file:line and what the target actually says. Then decorative
> enforcement, three-way inconsistencies, lost mechanisms, and a verdict table.

## Pass condition

Zero false claims. Every lesson either cites real enforcement or states explicitly that it is
guidance only.
