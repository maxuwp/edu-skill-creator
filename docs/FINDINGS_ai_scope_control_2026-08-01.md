# What the research return establishes about AI scope control

**Run:** Perplexity Deep Research, 2026-08-01, six strands, 41 rows, 105 sources. Return filed
verbatim at `docs/RESEARCH_ai_scope_control_perplexity_2026-08-01.md`. Plan, controls and pass bar
at `docs/RESEARCH_PLAN_ai_scope_control_2026-08-01.md`.
**Question under test:** Dr. Ma's objection that the review scope protocol and L22 are human project
management applied to a problem whose causal chain, for an agent, is different.

---

## 1. The run scored against the bar written before it

| bar item | result |
|---|---|
| all six strands with content | **met** — 8/6/6/7/8/6 rows, none dropped |
| Strand 2 reaches six organisations, own domains | **met** — Anthropic, OpenAI, Cursor, GitHub, Amazon, Google, each quoted from its own documentation |
| Strand 4 reaches six sources, two of them empirical | **exceeded** — seven sources, five empirical |
| verbatim quote plus hosting URL on every non-negative row | **met** — 37 of 41; the four exceptions are the `not-attested` and `not-addressed` rows, which carry the search path instead, as the contract requires |
| no blog or aggregator standing as a source | **met with one weak row** — the CodeRabbit AI-versus-human comparison is read through a LinkedIn summary and is labelled `secondary` with the canonical publisher named but unreached. That row is not load-bearing below |
| roll call reconciles | **one defect** — the host-class tally sums to 39 against 41 rows, and the explanatory note contradicts itself about which rows lack a class. Honest but muddled; the row counts themselves check out |
| two of three blind controls fire | **three of three** |

**The controls are worth reporting separately, because one of them inverted in our favour.** Control
`k1` predicted the run would cite the instruction-hierarchy literature and over-read it as resolving
instruction conflict in general. It did cite it — and then stated, unprompted, that the work
addresses "the injected/adversarial case, not a benign scope-vs-goal conflict", and closed the strand
with "No source located treats specifically and exclusively the benign case". A run that distinguishes
a source's scope from its topic is reading, not pattern-matching. `k2` fired (vendor documentation
quoted from first-party domains). `k3` fired in kind rather than exactly: the human-era measurement
that surfaced was Boehm's cost-to-fix-by-phase rather than bad-fix injection.

## 2. What the return establishes, against the four-step hypothesis

**(a) The agent fills an underspecified request with defaults. Confirmed, and measured.** Three
independent studies: agents "can often (41.1%) guess unspecified requirements by default", and
"underspecified prompts are 2x more likely to regress over model or prompt changes, sometimes with
accuracy drops by more than 20%"; separately, models "default to non-interactive behavior without
explicit encouragement, and even with it, they struggle to distinguish between underspecified and
well-specified inputs." This is Dr. Ma's step (a), and it is the best-evidenced part of the chain.

**(b) Minimal-scope discipline is a real, written instruction. Confirmed in the vendors' own words.**
Four of six state it explicitly, one implicitly, one not at all. The most literal is Amazon's: "Your
feature shouldn't require updates to more than 5 files at a time… If your file diff includes changes
to many files, try reducing the scope of your feature description."

**(c) The escalation hole is real, and it is universal. This is the finding.** Across all six
organisations, **not one document tells the agent what to do when the correct fix lies outside the
assigned scope.** Two define a plan-first workflow (Anthropic, Cursor), but as pre-emptive planning
rather than as a branch for the out-of-scope case; two mention planning without a mechanism (OpenAI,
GitHub); one is silent (Amazon); one could not be located (Google). Amazon's is the sharpest
illustration of the asymmetry: when the diff grows, the instruction is that **the human** should
shrink the feature description. The agent is given no move at all.

**(d) The pathology has a name in the literature, and a measured rate.** "Non-convergent repair
loop" is `named-and-defined`: repair convergence is formally "the fraction of scenario families whose
repair process terminates with all remaining tests passing within the observed retry window", and
"3 of 10 scenario families (30%) failed to converge", mean 4.4 iterations, with one case reaching 113
consecutive reports at the maximum retry depth of 16. Our L20 name, Foundation Regress, is for
something narrower and still unnamed elsewhere: the loop descending through layers rather than merely
failing to terminate.

**(e) The conflict Dr. Ma feared has a documented shape, and it is not the one the literature is
about.** Instruction-hierarchy work is overwhelmingly framed around adversarial conflict — a user
trying to override a safety constraint. The one source addressing the benign case directly is
OpenAI's Codex base instructions: "Direct system/developer/user instructions (as part of a prompt)
take precedence over AGENTS.md instructions." That is a precedence rule for exactly our situation: a
standing repository-level constraint versus an immediate task instruction, with the task winning.

## 3. Two negatives, and they are load-bearing

Both are well-formed, with the search path recorded.

- **Nobody has measured whether constraining an agent to a minimal change raises or lowers its
  resolution rate.** The central empirical question behind this entire discussion is open. The
  minimal-scope rule is, as far as the published record goes, an untested convention.
- **Nobody has measured the token or dollar cost of iterative repair loops.** Only iteration caps.
  So the token-saving claim behind this work has no external baseline to borrow, which is consistent
  with what L20 already records about our own missing instrumentation.

One adjacent number does exist and is the agent-era analogue of bad-fix injection: across 302,579
commits in 6,299 repositories, "more than 15% of commits from every studied assistant introduced at
least one issue", from 17.4% to 29.1% by tool, and "22.7% of tracked AI-introduced issues still
survived at the latest repository head."

## 4. What this means for L22, stated as consequences rather than as a plan

1. **L22 is not redundant.** It fills a hole that six vendors leave open in their own documentation.
   Dr. Ma's objection was that the solution was human-shaped, not that the problem was imaginary; the
   return separates those, and the problem is real.
2. **But the protocol is aimed at the wrong half of the chain.** Its four classes and authority table
   govern step (c), the escalation. The evidence is strongest and the measured countermeasures exist
   at step (a), intake: clarification-seeking scaffolds, with "interactivity can boost performance on
   underspecified inputs by up to 74% over the non-interactive settings" and an ask-or-assume scaffold
   reaching a "69.40% task resolve rate". Nothing in the protocol makes an agent ask before it fills a
   gap, and that is where the foundation defect is born.
3. **The conflict risk is manageable and has a known shape: precedence, not persuasion.** A
   scope-escalation rule that competes with a standing minimal-scope instruction will lose or produce
   incoherent behaviour. Written instead as a **permission at the right precedence level** — the task
   instruction outranks the standing repository file, per the one benign-case source found — it does
   not compete. The practical form is that a scope declaration must arrive with the task, not sit in a
   repository file hoping to override the system prompt.
4. **Grading by impact survives, but its authority table is the human-shaped part.** A change-control
   board is a human institution. What an agent needs from that table is not who signs, but that the
   response is *graded*, so a one-line adjacent correction is not treated as a relocation.

## 5. What this run cannot settle

Whether any of this is what stalled **our** loops. Every finding above describes what others publish
and measure. Our own claim still rests on transcripts and on instrumentation that does not exist yet
(L20's open item: layer and cost per round are not recorded). Keep the two questions apart, and do not
let a well-sourced external finding be quoted back as evidence about this repository.
