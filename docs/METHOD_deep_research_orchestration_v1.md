# Method — using Deep Research as an orchestrated fleet, v1 (untested)

**Revised 2026-07-31** against Perplexity's own published architecture, after the first draft was
written from the two returned reports alone. §3 is new and carries the evidence; it confirms the
orchestrator hypothesis and refutes v1's chosen mechanism for source quality. §4.3, §5 and §6 changed
as a result. §7 lists the sources.

**Purpose:** reach the quality of the agentic-browsing run using Deep Research runs instead, by
moving the orchestration outside the tool. Dr. Ma's proposal: this thread decomposes a topic into
several narrow Deep Research prompts, he runs each and returns the reports, this thread synthesises.
**Status:** designed, not yet tested. §5 is the test that decides whether it becomes a skill.

---

## 1. What the deep-research run already got right — protect these

Confirm-first applies to the prompt as much as to code. The 2026-07-31 deep-research run was not a
failure across the board, and the parts that worked came from instructions in
`docs/HANDOFF_perplexity_grounding_audit.md` that the v1 template below keeps unchanged.

| Property | How verified |
|---|---|
| It declared what it had not covered, by anchor number, and said unreached anchors "should not be treated as validated by omission" | `AUDIT_grounding_perplexity_deepresearch_2026-07-31.md` §"Anchors not yet verified in this pass" lists #1, #2, #4–6, #9, #12–15, #19, #26–28 explicitly |
| It obeyed the author-set exclusion | Anchor #30 marked `author-set`, not searched |
| Every verdict it did give carried a verbatim quote, not a paraphrase | All 14 rows have a quoted "Supporting quote" cell |
| It produced the requested table shape rather than an essay | The output is a table, one row per anchor |
| Its scope reasoning was often sharp | Row 8 (ICAP) correctly reads Chi & Wylie's own hedging; row 18 confirmed the Mayer operationalization independently of the browsing run |

The failure is not that Deep Research reasons badly. It reasons well over too few items, and it
sources loosely. Those are the two things v1 targets, and nothing in v1 should disturb the five
properties above.

## 2. The six defects, with the evidence for each

| id | Defect | Evidence in the returned report |
|---|---|---|
| D1 | **Coverage.** 15 verdicts against a population of 29. | 14 anchors listed as not reached |
| D2 | **Mode inversion.** The handoff assigned Deep Research to the currency half; the run did the scope half instead. | Its own §"Scope note" says "This is a Half A pass" |
| D3 | **Source tier.** Roughly half the rows rest on non-primary hosts. | `intertekinform.com` (a standards reseller) for IEEE 1028's status; `andrewpwheeler.com` and `speakingppt.com` (personal blogs) for Doumont and Kosslyn; `www2.internationalinsurance.org` (an unrelated SEO-farm PDF) for Beck; `csrc.nist.rip` (a mirror) rather than `csrc.nist.gov` |
| D4 | **Citation resolution.** A row's inline URL and its footnote resolve to different papers. | Row 18 (Mayer) links `EJ944963.pdf` inline; its footnote `[^10]` resolves to `EJ1347324.pdf`, the CRAAP paper |
| D5 | **URL does not host the quote.** The URL column carries a canonical page while the quote comes from a footnoted third party. | Row 23 reports `w3.org/WAI/` but quotes `accesstive.com` and `a11yflow.dev`; row 24 reports `studentprivacy.ed.gov` but quotes `orangeslices.ai` |
| D6 | **Verdict vocabulary drift and verdict/prose contradiction.** | Verdicts `scope-accurate (with correction on operationalization)` and `scope-accurate (CRAAP currency flagged)` are outside the closed set; row 7's verdict is `superseded` while its own currency cell says "contested, not superseded outright" |

D1 is what the orchestration fixes. D2–D6 are what the prompt fixes. They are independent, which
matters for reading the test result in §5: coverage can improve while sourcing does not.

## 3. What Perplexity documents about its own architecture

v1 above was designed from the two reports alone, and guessed at the mechanism. Perplexity documents
it, and the documentation both confirms the orchestrator hypothesis and refutes one of v1's design
choices. Sources are first-party unless marked.

**3.1 The subtask decomposition is real, and it is first-party.** Dr. Ma's reading was right.
Perplexity's own announcement of Deep Research inside Computer (2026-06-11) states that "Computer
will break it down into subtasks routed across 20+ frontier models", and its worked example is
explicitly an orchestrator pattern: "Computer runs four paths in parallel… The final output
reconciles all four paths into a single risk assessment."
`https://www.perplexity.ai/hub/blog/deep-research-now-in-computer`

**3.2 The architecture is called Search as Code, and the retrieval filtering happens in code, not in
the prompt.** The model "decompose[s] the directive into tasks, decide[s] which retrieval and
processing pipelines are needed for each task, and generate[s] code to implement those pipelines",
running them in a sandbox — the published example fans out with
`web_many(queries, limit_per_query=8, concurrency=12)`. Two operations in that pipeline are exactly
the two defects we are fighting, and both are executed deterministically:

- **Source tier is enforced by code.** Downstream code is written to "dedupe by CVE, **reject
  aggregator URLs**, discard weak version evidence", with an explicit predicate
  `official_vendor_advisory(h.url, q['vendor'])` deciding whether a hit is the issuing party's own
  page. That is D3, solved by a host test rather than by asking the model to prefer good sources.
- **Coverage is measured and backfilled mid-run.** `coverage = summarize(pages, by=['vendor',
  'year', 'url_kind'])` identifies sparse cells, and the run issues expanded queries before
  finishing. That is D1, solved by a metric rather than by a closing roll call after the fact.

`https://research.perplexity.ai/articles/rethinking-search-as-code-generation`

**3.3 Perplexity's own prompt guide says prose source rules are the wrong instrument.** This is the
correction v1 needs, and it is stated plainly in their developer documentation: "For source, date,
or region constraints, **prefer the web_search parameters over describing the constraint in prose.
Parameters are applied by the search backend on every call, while prose-based filters are
interpreted by the model and may not carry through every turn of the loop.**"
`https://docs.perplexity.ai/docs/agent-api/prompt-guide`

v1 §4.3 fixes D3 with a prose rule naming the hosts that failed last time. By the vendor's own
account that rule may hold for the first search of a multi-step run and lapse in later ones, which
is consistent with a report that cites Sweller's own PDF in one row and an SEO-farm PDF in another.
The parameter that does bind is `search_domain_filter`, an allowlist or denylist applied at the
search backend, documented at `https://docs.perplexity.ai/guides/search-domain-filters`; the
interface equivalent is the Focus / source selector, where deselecting Web and selecting Academic
restricts retrieval to scholarly sources before the model sees anything.

**3.4 The citation apparatus in the written answer is a rendering, not the retrieval record.** The
same prompt guide instructs developers to "Read URLs and source metadata from the response payload,
not from the model's written answer", noting that a deep-research run emits one search-results item
per search, all sharing a single citation id space. D4 — a footnote resolving to a different paper
than its row — is what that warning predicts, and it is unreachable from the interface, where only
the rendering is available. Hence v1's rule that the row's own inline URL governs.

**3.5 What this means for the comparison, and it is a correction.**
`AUDIT_grounding_two_runs_compared.md` attributes the gap to pointed retrieval versus synthesis.
That was my inference and the documented difference is architectural: parallel subtask
decomposition, code-level dedup and filtering, automatic access to premium licensed sources, and
newer models. Perplexity further reports that moving Deep Research into Computer raised factual
accuracy, depth and citation quality on Humanity's Last Exam, BrowseComp and DeepSearchQA — vendor
benchmarks, uncorroborated here. So the two runs Dr. Ma commissioned are plausibly the current
architecture against the legacy pathway, rather than browsing against synthesis.

**The ceiling this sets on the whole exercise.** External decomposition can recover coverage,
because coverage is a property of how the work is divided. It cannot recover code-level URL
predicates, mid-run coverage backfill, or licensed sources, because those live inside the run. A
realistic target for the orchestrated cheap mode is therefore parity on coverage and citation
discipline, not parity overall — and §5 should be read against that ceiling rather than against the
browsing run.

## 4. The method

### 4.1 Decomposition rules (this thread's job)

1. **4 to 6 items per run.** Below 4 the per-run cost dominates; above 6 the satisficing returns.
2. **One question per run.** A run asks for scope, or for currency, or for status — never two. D2
   happened because one document asked for both and let the model choose.
3. **Each run prompt is self-contained.** It never refers to the other runs, to this method file, or
   to any prior result. A run that knows it is one of four will reason about the others' territory.
4. **Every item appears in exactly one run**, and the orchestrator holds a manifest mapping item id
   to run id before any run is issued. The manifest is written first, not reconstructed afterwards.
5. **Controls are blind.** Items whose answer is already known are placed in runs without being
   marked, and the expected finding is recorded in the manifest, not in the prompt.

### 4.2 The synthesis contract (this thread's job, and the part that can quietly fail)

Synthesis is a new authoring layer, and a synthesiser that re-derives anything reintroduces exactly
the untraceability the prompt was written to prevent.

1. **Roll call by item id, not by count.** Reconcile the returned rows against the manifest item by
   item. "16 rows returned, 16 expected" is not coverage; it is a count that a duplicate satisfies.
2. **Citations are copied, never re-typed and never re-derived.** Every URL and every quote in the
   synthesis is a byte copy from a run file.
3. **Every claim in the synthesis carries its `run-id : item-id`.** A claim that cannot name one does
   not belong in the synthesis.
4. **The synthesiser adds no sources of its own.** If a gap is visible, it is reported as a gap and
   routed to a new run.
5. **Disagreements are preserved, not resolved.** Where two runs conflict, both rows are carried
   forward and the conflict is named. Picking a winner during synthesis destroys the evidence that
   there was a call to make.

### 4.3 Retrieval settings come before the prompt

Following §3.3: any constraint that can be a retrieval setting is set as a retrieval setting, and
the prompt carries only what cannot be. Per-run settings are in
`docs/deepresearch_runs/RUN_SETTINGS.md`; the run prompts themselves stay pure paste-in text.

The prose source-tier rule stays in every prompt, but its status changes. It is now a backstop for
the runs where no setting is available, not the primary mechanism. Runs A and B verify research
publications, so Academic focus can carry the constraint. Runs C and D cannot use it: C's sources
are GitHub repositories and vendor documentation and D's are two standards bodies, none of which
Academic focus would return. Those two runs are therefore the honest measure of what the prose rule
alone achieves, which makes the D3 comparison sharper rather than weaker — and Run D is where the
prose rule is under the most pressure, since a reseller listing for a standard is precisely the
substitution it has to prevent.

### 4.4 The run prompt — design decisions

The template is in `docs/deepresearch_runs/`, one paste-ready file per run. The decisions behind it:

- **Invert the length reward, explicitly.** Deep Research is built to produce a long synthesised
  report. The prompt states that a short report with N traceable rows is a complete success and a
  long report with a discussion section is a failure. This is the single highest-leverage line.
- **State the population size and demand a closing roll call.** Fixes D1 within a run.
- **Name the next query for every `unverified` row.** Borrowed from the coverage-backfill step in
  §3.2: their pipeline measures sparse cells and issues expanded queries before finishing, where a
  one-shot prompt can only report the gap. Requiring the run to name what it would try next converts
  `unverified` from a terminal verdict into a queue this thread can re-issue as a fifth run.
- **Name the job once, and name what is out of scope.** Fixes D2.
- **A source tier rule that names the specific hosts that failed last time** — a reseller listing, a
  personal blog, an SEO-farm PDF, a mirror domain. A rule that names the error it expects is
  testable; "use good sources" is not. Addresses D3 as a backstop only, per §3.3 and §4.3: the
  binding instrument is the retrieval setting, and where no setting applies this rule is what we are
  measuring rather than what we are relying on.
- **The URL column must host the quote**, stated as its own rule, because the canonical-page habit
  is what produced D5.
- **Citations must resolve**, with the row's own inline URL governing over any generated footnote
  apparatus. Fixes D4.
- **A closed verdict set, tokens only, qualifications moved to a prose column**, plus a required
  self-check for verdict/prose contradiction. Fixes D6.
- **A sixth verdict token, `contested`**, is introduced. The library today has no verdict for
  "correctly cited, within scope, and under active empirical challenge", which is the real situation
  for CLT, ICAP and Bloom. Introducing it in the prompt tests it against a real population before
  the library commits to it, which is the sequencing argument
  `docs/HANDOFF_next_step_ideas_fable_grok.md` §3.1 makes for everything else.

## 5. The test

**Topic.** The 14 grounding anchors the deep-research run never reached, plus two known-failure
controls. The browsing run covered all 16 against primary sources, so an independent comparison
already exists and was produced before this method was designed.

**Manifest.**

| Run | Question | Retrieval setting | Items |
|---|---|---|---|
| A | scope | Academic focus, Web off | #1 Understanding by Design, #2 Mager/ABCD, #4 Gagné, #5 Merrill, #6 Ausubel |
| B | scope | Academic focus, Web off | #9 Cognitive apprenticeship, #12 TPI, #13 Biggs, #14 Haladyna, #15 Wiliam |
| C | scope | Web, prose rule only | #19 Alley assertion–evidence, #26 Anthropic skill-creator, #27 plugin-dev, #28 obra writing-skills |
| D | status | Web, prose rule only | #17 IEEE Std 1028, #23 W3C WCAG 2.2 |

The split is not incidental. A and B measure the orchestration with the source constraint bound at
the retrieval layer; C and D measure it with the constraint bound only in prose. If A and B come
back clean and C and D repeat the 2026-07-31 host failures, §3.3 is confirmed on our own data and
the conclusion is that this method needs the API, not a better paragraph.

The run prompts number their own items 1..n rather than carrying library numbers, so that a run
cannot infer that it is a fragment of something larger. The manifest above is the mapping, and the
roll call in §4.2 is performed against library ids in the order listed there, not against the run's
own row numbers.

**Blind controls, with the finding each is expected to produce.** None of these appear in the run
prompts. Runs A, B and C are blind in the strong sense: nothing in the prompt points at the item or
the defect. Run D is weaker — its source-tier rule names the reseller failure class explicitly,
because that rule is the treatment under test, so #17 measures whether the instruction works, not
whether the model would have avoided the reseller unaided.

| Item | Run | Expected finding | What it tests |
|---|---|---|---|
| #2 Mager/ABCD | A | "ABCD" is not Mager's; it is a separate Heinich/Knirk–Gustafson mnemonic, so the anchor conflates two lineages | Whether a narrow run notices a defect that is not the one it was pointed at |
| #5 Merrill | A | The 2002 paper was rewritten as a 2020 AECT edition, reissued 2024 | Currency detection inside a scope run |
| #14 Haladyna | B | Exactly 31 guidelines, down from 43 in 1989, multiple-choice only | Numeric traceability, the instruction three withdrawn numbers were paid for |
| #28 obra writing-skills | C | Superpowers is a full agentic-development methodology; `writing-skills` is one skill inside it, so our description undersells the source | Whether it reads the repository rather than the anchor's description |
| #17 IEEE 1028 | D | Status is "Inactive-Reserved" per IEEE, an administrative lapse, not a formal withdrawal | Direct re-test of D3: the previous run took a reseller listing's "Withdrawn" |
| #23 WCAG 2.2 | D | Recommendation, this version 12 Dec 2024; 3.0 still a Working Draft | Direct re-test of D5: the previous run cited two blogs under a `w3.org` URL |

**Scoring — process metrics decide the outcome, and five of the six are computed, not judged.**
`scripts/score_deepresearch_report.py` parses a returned report and applies the host predicate, the
verdict-token test and the citation-resolution test in code, which is the §3.2 lesson applied at our
layer. Run it per return:

```bash
python3 scripts/score_deepresearch_report.py docs/deepresearch_runs/RETURN_A.md --profile academic --expect-rows 5
```

| Metric | Pass | Deep-research baseline, 2026-07-31, as measured by the scorer |
|---|---|---|
| Coverage: rows delivered / items assigned | 16 / 16 | 15 / 29 |
| Source tier: rejected hosts in cited rows | 0 | **6** — `intertekinform.com`, `scispace.com`, `speakingppt.com`, `andrewpwheeler.com`, `www2.internationalinsurance.org`, `csrc.nist.rip` |
| Citation resolution: row URL and its footnotes agree | 0 mismatches | **4**, including the Mayer row citing `EJ944963.pdf` while its footnote resolves to `EJ1347324.pdf` |
| Verdict legality: token from the closed set, nothing appended | 16 / 16 | 13 / 15 |
| Verdict/prose consistency | 16 / 16 | 1 known contradiction (row 7), read by hand |
| Quote hosted at the reported URL, spot-checked on 6 rows | 6 / 6 | at least 2 known failures (rows 23, 24), read by hand |

The scorer was written against the known-bad report and reproduces every host and citation defect
found by hand, plus one the hand pass missed (the Quality Matters row's footnotes resolve away from
its own URL, arguably benign since both are first-party). Run against the browsing report it returns
**0 rejected hosts and 0 citation mismatches**, which is the first mechanical confirmation of §4 of
`AUDIT_grounding_two_runs_compared.md`.

**A limitation of the host predicate, stated rather than discovered later.** Scholarly PDFs live
anywhere — `ida.liu.se`, `hcs64.com`, `dylanwiliam.org`, `citeseerx.ist.psu.edu` are all legitimate
homes for a primary source, and the scorer flags each as `unlisted` for a human call. So the
allowlist is a strong positive predicate for the standards and tooling profiles, where the issuing
body's domain is knowable in advance, and only a triage aid for the academic profile. The denylist
is the load-bearing half there.

**Agreement with the browsing run is recorded but does not decide the test.** The browsing run is
the stronger artifact, not ground truth, and `AUDIT_grounding_two_runs_compared.md` refuses to treat
it as a baseline. Where the new runs disagree with it, the disagreement joins the disputed pile and
is a second opinion we wanted anyway.

**How to read a partial result.** D1 and D2–D6 are independent. Coverage at 16/16 with source tier
still around half means the orchestration works and the prompt does not, and the next iteration is
the tier rule alone. The reverse means the prompt works and the runs are still too large.

**Cost.** Four Deep Research runs against one browsing run is not self-evidently cheaper, and I have
no pricing to reason from. Worth recording what these four cost, since the economics, not the
quality, are the reason for the exercise.

## 6. If it passes

Four artifacts become the skill: this decomposition rule set, the run template, the scorer, and the
synthesis contract in §4.2 — the last being the one a skill is most likely to omit and most likely
to need, since it is where a fleet of honest runs can still produce a dishonest report.

Two productionisation choices are then open. **Decided 2026-07-31: the interface path.** Deep
Research is included in the existing Pro subscription, so the four runs cost nothing beyond quota,
and the method is the one Dr. Ma specified — this thread decomposes, he runs each subtopic, this
thread synthesises. The API material below is retained as a record of what was checked and what it
would buy, not as a pending recommendation.

**A Space, for the interface path.** A Space is a named container holding a custom system prompt
applied to every query run inside it. The invariant contract — output shape, verdict set, source
rules, roll call — would live there once, and each run prompt would carry only its items. That is
the closest the interface gets to "applied on every call". It is deliberately *not* used for the
test: the contract would then be invisible in the run files, and a Space misconfigured or forgotten
would corrupt a run silently, which is exactly the failure mode a first test must not have. The
redundancy across the four prompts is the cost of keeping each one self-contained and auditable.

**The Agent API, for the enforced path.** The `deep-research` preset accepts `search_domain_filter`
as an allowlist or denylist, runs asynchronously, and returns search results in the response payload
rather than only in the model's prose. That converts three of our four mechanical checks from
after-the-fact scoring into preconditions: a reseller host cannot be cited if it is not in the
allowlist, and citation resolution is read from the payload rather than reconstructed from a
footnote apparatus. It also exposes per-request cost, which is the number this whole exercise exists
to find. If the test in §5 shows C and D failing on hosts while A and B pass, the API is not an
optimisation, it is the answer.

**What the API costs, checked 2026-07-31.** A Pro subscription carries no API entitlement. The plan
comparison page states of the API Platform: "Pay-as-you-go pricing: Buy credits or set up auto
top-off… **No complimentary API credits**", and the Enterprise Max entry adds that interface
allowances do "not apply to programatic access via API, which is billed separately"
(`https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you`,
updated 2026-07-22). The $5/month credit that Pro used to include is reported by users as withdrawn
and no longer appears in first-party material. Credits are bought outright, from any balance.

Sonar Deep Research is billed at $2 per 1M input tokens, $8 per 1M output, $2 per 1M citation
tokens, $3 per 1M reasoning tokens, and $5 per 1,000 searches, with no per-request fee
(`https://docs.perplexity.ai/getting-started/pricing`). For a run of this shape — five items, a
short table, on the order of 40 searches and a few tens of thousands of reasoning and citation
tokens — that arithmetic lands near **$0.30 to $0.50 per run, so roughly $2 for the four-run test**.
Those token volumes are estimated, not measured; the reasoning count is the loose term, and the
first real run replaces the estimate with the invoice. The order of magnitude is the point: a $5
credit purchase covers the whole experiment, and every run reports its own cost, which the interface
never does.

**Also noted while checking, and unrelated to the method.** The same page lists **Education Pro at
$10/month with SheerID verification for educators**, described as including everything in Pro plus
Perplexity Computer and Learn Mode. If that holds on inspection it halves the subscription cost that
prompted this exercise. Worth verifying against the current offer before acting on it.

## 7. Sources

All first-party unless noted. Retrieved 2026-07-31.

- Perplexity, "Deep Research, now in Computer", 2026-06-11 — subtask decomposition across 20+
  models, four parallel paths reconciled into one answer, premium sources, the benchmark claims.
  `https://www.perplexity.ai/hub/blog/deep-research-now-in-computer`
- Perplexity Research, "Rethinking Search as Code Generation" — directive decomposition, sandboxed
  generated pipelines, `web_many(..., concurrency=12)`, aggregator-URL rejection, the coverage
  summarisation step. `https://research.perplexity.ai/articles/rethinking-search-as-code-generation`
- Perplexity docs, Agent API prompt guide — parameters over prose for source constraints; read URLs
  from the payload, not the written answer. `https://docs.perplexity.ai/docs/agent-api/prompt-guide`
- Perplexity docs, search domain filters — allowlist and denylist, domain and URL level.
  `https://docs.perplexity.ai/guides/search-domain-filters`
- Perplexity Help Center, "What is Research mode?" — dozens of searches, hundreds of sources.
  `https://www.perplexity.ai/help-center/en/articles/10738684-what-is-research-mode`
- Secondary, for the interface behaviour only: the Focus/source selector can be set to Academic with
  Web deselected before submitting, and Academic focus does not guarantee peer-review exclusivity;
  paywalled full texts remain invisible either way. `https://aiweekly.co/learning-ai/generative-ai/how-to-use-perplexity`
  and `https://www.cnet.com/tech/services-and-software/this-is-how-to-turn-perplexity-into-your-personal-research-assistant-for-any-subject/`
  Not confirmed against Perplexity's own documentation, which is why `RUN_SETTINGS.md` carries a
  fallback for the case where the selector is not present.
