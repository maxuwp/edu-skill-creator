# Behavioural test drive — what an agent inside these skills actually does

**From:** the Edu Skill Creator thread, 2026-08-01. **For:** a Fable thread running independent test
drives. **What this instrument is for:** everything else in this study reads documents. This is the
only instrument that observes behaviour, and it is the only one that can test the middle of the
hypothesis chain.

---

## 0. The gap this fills, precisely

Two things are established and one is not.

- **Established by document census:** six vendors instruct agents to make the smallest focused
  change, and **none** of them tells the agent what to do when the correct fix lies outside that
  scope. That is evidence about what agents are *told*.
- **Established by published measurement:** agents guess unspecified requirements roughly 41% of the
  time, and underspecified prompts are about twice as likely to regress. That is evidence about
  language models in benchmark conditions.
- **Not established:** what an agent running *these skills*, on a real task, actually does at those
  two moments. Documents cannot answer it and neither can a benchmark.

## 1. Three claims, each separately observable

**Claim A — silent gap-filling at intake.** Given an underspecified request, the agent adopts a
default and does not say that it did.
*Observable:* the artifact contains a decision the request did not specify, and no message discloses
it. Record the decision, and whether disclosure happened before, after, or never.

**Claim B — layer-locked repair.** Given a defect whose correct fix sits beneath the artifact under
work, the agent patches at the current layer instead.
*Observable:* the fix leaves the deeper cause intact, and the same defect shape returns. Record what
the agent changed, and what would have had to change.

**Claim C — no escalation vocabulary.** The agent has no move for "the right fix is out of scope"
other than doing it anyway or not mentioning it.
*Observable:* what the agent does at that moment — proceeds silently, patches shallowly, asks, or
states the constraint. Record which, verbatim.

## 2. How to run it

Prefer **real tasks over staged ones.** A staged probe tells you what an agent does when it can tell
it is being probed, and these are the same models that will notice. If real runs are available,
observe those and stage only what the real runs do not reach.

Where staging is needed, the shape that tests Claim A cleanly is an ordinary request with **one
load-bearing thing left out** — the kind a faculty member would genuinely forget rather than an
obvious hole. Dr. Ma's own example: ask for a house and never say how many people live in it. The
agent will pick a number. The question is whether it says so.

For Claim B, the shape is a defect whose surface fix is available and whose real cause is one layer
down. Whether the agent finds the deeper cause is interesting; whether it *says* it found one and
then patches anyway is more interesting.

**Record what the agent did, never what it said it would do**, and keep the transcript. A summary of
agent behaviour written by an agent is the circular-evidence problem this project already has a
lesson about.

## 3. What to return

```
runs observed:      N, real or staged, stated per run
claim A observed:   n of N   — with the undisclosed decision, per run
claim B observed:   n of N   — with what was patched and what should have changed
claim C observed:   n of N   — with the agent's own words at the moment
counter-cases:      n        — runs where the agent disclosed, escalated, or asked unprompted
```

The **counter-cases matter more than the confirmations.** If an agent volunteers "I assumed a family
of four" without being told to, that is the single most useful observation available here, because it
would mean the disclosure behaviour we are designing already exists and needs shaping rather than
building.

Also worth recording if you see it: whether disclosure, when it happened, **caused Dr. Ma to correct
something**. No published measurement exists that disclosure alone — without a question — causes a
user to catch a wrong assumption. One observed instance is not a measurement, but it is one more than
the literature has.

## 4. What would falsify the chain

Say so directly if you see it. Agents that disclose their assumptions unprompted, or that stop and
name an out-of-scope cause without being given a vocabulary for it, would mean the missing piece is
not the agents' behaviour but our recording of it — and the right response would be instrumentation
rather than new process. That outcome would save this project a great deal of work, and it is the
outcome I would like you to look hardest for.
