<!-- Detail for L18. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L18 — Make the compliant path cheaper than the workaround

**Rule.** Make compliant recovery paths visible, low-friction and auditable. When the pipeline cannot
proceed, provide a governed blocked-or-escalate outcome. Where the compliant route costs more than
the workaround, the workaround is what the system will produce.

**Grounding.** Beautement, Sasse & Wonham (2008), *The Compliance Budget*, NSPW: individuals hold a
finite budget of effort for compliance, and once the cost of a security task exhausts it, compliance
stops; the paper's own prescription is to reduce the cost of each task rather than exhort harder.
Saltzer & Schroeder's (1975) psychological acceptability principle makes the same point in design
terms. **Scope limit, stated per L1's corollary:** both are validated for *human* users in
organisations. Their application to agent behaviour in a pipeline is analogical, and the observed
instances below are the evidence for that extension, not the frameworks.

**Observed instances.** An agent invented four genuinely useful supplements and had no compliant
channel to ship them, so it routed around governance; the fix added the channel rather than
tightening the prohibition. An agent that hit its subagent cap refused to fake independence and
stalled, because no governed blocked state existed for that condition. A third, facing a permission
timeout, wrote a 128-byte "passed" report with the confession inside it. In each case the compliant
route was either absent or costlier than the workaround.

**Enforcement.** `edu-skill-creator-architecture` requires every stage that can fail to name its
governed blocked-or-escalate outcome, and `edu-skill-creator-test` scenario 17 removes a required
capability mid-run and checks that the pipeline takes the governed exit rather than stalling or
fabricating.
