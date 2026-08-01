# Research plan — is scope control for AI agents a different problem from scope control for humans?

**Date:** 2026-08-01. **Run under:** the `perplexity-research` skill's pipeline.
**Do not paste this file into Perplexity.** It holds the blind controls and the pass bar, which the
run must not see. The paste-ready prompt is the separate prompt file in this directory.

---

## 1. Why this run exists

The review scope protocol and L22 were built from human engineering practice: declare a boundary,
grade an expansion by impact, route it to an authority. Dr. Ma's objection is that this may be the
wrong medicine, because the causal chain for an agent is not the one those processes were designed
for:

1. At intake the human under-describes the need. The agent fills the gaps with minimum requirements
   or common defaults. **The foundation defect is created here, silently, before any review.**
2. On every subsequent edit, system-prompt discipline tells the agent to make the smallest change
   that solves the stated problem and to avoid disturbing work already proven. So the agent is
   structurally prevented from travelling "not enough space" → structure → function → location.
3. Many rounds pass, the defect survives, tokens are spent.
4. This is not an agent deficiency. It is a rule humans wrote — minimal-diff discipline — whose
   consequences differ for an agent, which cannot decide on its own that the rule should not apply
   this time.
5. Therefore a scope-escalation protocol layered on top risks a **conflict between the system prompt
   and the task prompt**, which is a failure mode the human processes never had to consider.

**That chain is the hypothesis under test, not a premise.** The run is told so explicitly.

## 2. Mode

**Computer.** This is a census needing many parallel retrievals reconciled — vendor documentation,
framework instructions, and an empirical layer — which is the shape the skill's evidence says Computer
handles and Deep Research half-finishes. Observed cost on two prior runs was about 300 credits each.
Deep Research is the fallback if Computer is unavailable, at the cost of source tier. Pro Search is
excluded: zero of four prior queries cited a primary source.

## 3. Strands, and what each is for

| # | Strand | Shape | What it decides |
|---|---|---|---|
| 1 | Is the phenomenon named? | negative check | whether we are inventing a category or joining a conversation |
| 2 | What do published agent instructions actually say about scope? | census | whether step 2 of the hypothesis is real, in the vendors' own words |
| 3 | Do those same instructions define an escalation path? | matrix over strand 2's population | whether the gap we are trying to fill is already filled |
| 4 | Intake underspecification and default-filling | census | whether step 1 has documented countermeasures |
| 5 | Has anyone measured any of it? | empirical layer | whether the token-cost claim can be grounded at all |
| 6 | System-prompt versus task-prompt conflict | negative check | whether step 5, the risk that stops us shipping L22's wiring, is documented |

## 4. Blind controls — recorded before the run, not visible to it

Three items whose answers I expect. None is named in the prompt; if the run reaches them, it reached
them on its own.

| id | item | what I expect | what it tests | what an inversion would mean |
|---|---|---|---|---|
| `k1` | OpenAI's instruction-hierarchy work | Strand 6 cites it, and treats it as resolving instruction conflict | whether the run reads a source's **scope** | its subject is privilege between trusted and untrusted instructions, not a benign conflict between a scope constraint and a task goal. A run that presents it as solving our problem is over-reading, exactly as the Mayer anchor was over-read. If the run itself draws that distinction, the return is unusually good |
| `k2` | Anthropic's own published coding-agent guidance | Strand 2 quotes explicit minimal-scope or do-not-touch-unrelated-code language from a vendor's own domain | whether the run can reach first-party vendor documentation rather than summaries of it | if no vendor states it explicitly, step 2 of the hypothesis is folk practice rather than written rule, which changes the whole design |
| `k3` | The human bad-fix-injection literature (repair introduces new defects at a measurable rate) | Strand 1 or 5 surfaces it as the human analogue, with a number | whether the run reaches older software-engineering measurement rather than only 2024-2026 agent blogs | if strand 5 returns not-addressed while this exists, coverage is shallow and the return should be re-run |

## 5. Pass bar — fixed before the return is seen

- All 6 strands present with content; none silently dropped.
- Strand 2 reaches **at least six** instruction sets from six different organisations, quoted from
  those organisations' own domains.
- Strand 4 reaches at least six sources, **at least two** of them peer-reviewed or preprint empirical
  work rather than vendor or practitioner writing.
- Every row that is not `unverified` carries a verbatim quote and the URL hosting those exact words.
- No blog, content farm, or aggregator standing as a source; pointers permitted only when labelled.
- The roll call's counts reconcile against the tables.
- At least two of the three controls fire.
- A well-formed negative anywhere is a pass, not a failure, provided the search path is given.

**If the bar is missed:** re-run only the failing strands. Do not accept a partial return as complete,
which is the failure the skill's own lessons record.

## 6. What this run cannot settle

Whether the hypothesis is *true of our repository*. Even a complete, primary-sourced answer describes
what others publish and measure. Whether minimal-diff discipline is what stalled our own loops is a
question about our transcripts, and the instrumentation for it does not exist yet (L20's open item:
layer and cost per round are not recorded). Keep the two questions apart when the return arrives.
