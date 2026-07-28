<!-- Detail for L6. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L6 — Expensive AI runs are consent-gated with a cost ladder

**Rule.** Token-heavy operations (multi-agent simulations, full eval sweeps) are opt-in:
offer full / lite (~1/5 cost, described concretely) / skip, state the cost in plain
language, record the chosen mode in the manifest, re-offer on every re-run. Exception:
when no human will ever rehearse the output (e.g. self-study decks), the simulation is
the only rehearsal — auto-invoke and say why.

**Failure that taught it.** The two-role (professor/student) dry-run simulation was
valuable but "very token consuming" — the author asked that it never run without asking.

**Edu Skill Creator enforcement.** `edu-skill-creator-test`'s eval sweeps and any simulation stage designed into a
new plugin must carry the full/lite/skip consent gate with a recorded mode field.
