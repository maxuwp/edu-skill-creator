<!-- Detail for L9. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L9 — Knowledge snapshots go stale; build the refresh loop in

**Rule.** A plugin that encodes frameworks, tool capabilities, or model behavior needs a
periodic (~90-day) refresh skill: check for new frameworks and new AI capabilities,
present findings as an approve-per-item ledger, never auto-apply. Likewise, after every
pilot, a reflect skill harvests what the gates revealed into persistent improvements.

**Failure that taught it.** New AI capabilities (e.g. interactive simulation) enabled
lecture designs — personalized FFT/IFFT visualizations — that the frozen skill text could
never propose; and pilot lessons kept accumulating in chat transcripts instead of the
plugin.

**Edu Skill Creator enforcement.** `edu-skill-creator-architecture` includes refresh + reflect stages in every
educational plugin's design by default (the educator can decline — see L2); Edu Skill Creator itself
ships `edu-skill-creator-refresh` and `edu-skill-creator-reflect`.
