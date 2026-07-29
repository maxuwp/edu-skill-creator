# E1 — cold-start execution

**Run when:** any release that restructures files, renames, or changes stage instructions.
**Model:** fresh context, no prior knowledge of this repo. **Found in its first run:** the broken
reviewer allowlist, the qualified-name/directory mismatch, two contradictory lesson counts.

## Prompt

> You are an AI agent asked by a professor: "I want to build a plugin that helps me write and grade
> weekly lab reports for my materials science course." You have been told the `edu-skill-creator`
> skill set will guide you. Start where a real agent starts: read `skills/edu-skill-creator/SKILL.md`
> and follow its instructions literally. Do not review its prose quality — EXECUTE it and report what
> breaks.
>
> 1. Follow the umbrella exactly. Note what you read, and how many files you opened before you could
>    take a first real action.
> 2. Attempt Stage 1 for real, as far as possible without a human to answer. Note every point where
>    you needed information the skill did not give, or where two agents would diverge.
> 3. Test the lesson index/detail split: when a stage says a lesson applies, can you load the right
>    detail file without reading everything? Did you read one you did not need, or miss one you did?
> 4. Deliberately try to get lost. Follow a pointer that looks stale.
>
> Report: executable yes/no and where you stalled; a friction log with file:line; broken or stale
> pointers; a progressive-disclosure verdict with numbers; the top 3 ambiguities where two competent
> agents would diverge. Be blunt.

## Pass condition

Stage 1 is executable to the point where only human answers are missing. No pointer resolves to a
file that contradicts what the pointer implied. No stale count or name in any file an agent is told
to trust.
