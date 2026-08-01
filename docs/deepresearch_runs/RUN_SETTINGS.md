# Run settings — set these in the interface before pasting each prompt

Do not paste this file. It records what to set in Perplexity before pasting each run prompt, and why.

Perplexity's own prompt guide states that source constraints belong in the retrieval parameters
rather than in prose, because "Parameters are applied by the search backend on every call, while
prose-based filters are interpreted by the model and may not carry through every turn of the loop"
(`https://docs.perplexity.ai/docs/agent-api/prompt-guide`). Every run prompt still carries the prose
source rule, but for runs A and B the setting below is what is actually expected to hold the line.

| Run | Mode | Sources / Focus | Why |
|---|---|---|---|
| A — `RUN_A_curriculum_scope.md` | Deep Research | Academic on, **Web off** | All five items are research publications. Academic focus restricts retrieval to scholarly sources before the model sees anything, which is the only mechanism that can make a personal blog review structurally unavailable rather than merely discouraged. |
| B — `RUN_B_assessment_scope.md` | Deep Research | Academic on, **Web off** | Same, and this run also asks for exact counts and effect sizes, which are precisely the numbers that get corrupted when a secondary source restates them. |
| C — `RUN_C_communication_tooling_scope.md` | Deep Research | **Web on** | Three of four items are GitHub repositories and vendor documentation. Academic focus would exclude the correct sources entirely. |
| D — `RUN_D_standards_status.md` | Deep Research | **Web on** | Both items are standards bodies. Academic focus would not return an IEEE catalogue entry or a W3C status page. |

**One run per thread.** Do not ask follow-up questions in the same thread before saving the report;
a follow-up rewrites the context the closing roll call was computed against.

**Save each report as its own file** into this folder, named `RETURN_A.md` … `RETURN_D.md`, keeping
the reference list and any footnote apparatus intact. The footnote apparatus is one of the things
being scored, so trimming it removes evidence.

**Record the cost of each run.** The reason for this exercise is that the agentic mode is expensive.
Four Deep Research runs against one browsing run is not self-evidently cheaper, and the comparison
is only possible if the numbers are captured while they are visible.

## If the interface does not expose a source selector in Deep Research

Then runs A and B fall back to prose-only, the same as C and D. Say so when returning the reports,
because it changes what the result means: a clean sweep would then be evidence that the prose rule
does bind after all, which would be a more interesting finding than the one this design expects.
