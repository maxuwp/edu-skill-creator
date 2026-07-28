<!-- Detail for L13. The always-read card is ../lesson_index.md; this file is pulled when a stage needs it. -->

## L13 — Instructions must not teach what the validators refuse; sweep the class, never the cited line

**Rule.** The moment a skill ships both prose and enforcement, the prose acquires a new
failure mode: teaching a path the code rejects. Whenever a rule changes, or a validator's
real behaviour is discovered, **sweep every instructional surface for that rule and fix
them in one pass** — SKILL bodies, references, READMEs, harness-adaptation notes,
sub-skills. A reviewer's file:line is a symptom; the defect is the class. And superseded
instructions are **deleted or moved to a marked historical section, never annotated in
place**: a warning above an executable-looking instruction loses to the instruction.

**Failure that taught it.** POSED 1.66 set out to extract platform mechanism from one
block and instead spent six review rounds on a single defect that had four more homes than
anyone first counted. `hitl_protocol.md` listed `approved: true` as the manifest effect of
a terminal "Approve as-is" that `approval_provenance.py` refuses in every contract era,
unversioned sessions included — verified by forging one. Round 3 fixed the SKILL.md
pointer and deferred the reference table; round 4 found the table; round 5 found the
harness-adaptation note; round 6 found the README and the outline skill's "Upload an
override" path, which saved pasted content *as the approved outline*. One
`grep -rn "Approve as-is" skills/` at round 3 would have found all of them. Each partial
fix bought exactly one more round. An interim repair was worse than the defect: it
contract-gated the prohibition at `>= 1.29`, which reads as licence for everything below
it — and a fresh session carries no contract version until its first genuine submission,
so the exception covered every new session.

**Corollaries, each also paid for:**
- **Annotation is not repair.** The four-option table survived a round *with an explicit
  non-approval warning above it*, because a Manifest-effect column reading `approved: true`
  is an instruction and prose above it is commentary. It ended when the table became three
  feedback-only options and the historical wording moved to the extracted-source folder.
  This is Anthropic's "old patterns" rule applied to superseded procedure, not just to
  time-sensitive facts.
- **When each round finds a new instance, the fix is at the wrong layer.** The same shape
  produced POSED's offline-gate arms race: regex, then an HTML parser, then `srcdoc`, then
  meta refresh, converging only when a deny-by-default Content Security Policy replaced the
  enumeration. Stop patching instances; remove the affordance.
- **A contradiction inside one instruction set is one defect with two locations.** Deferring
  half of it as "scope discipline" is not discipline, it is a scheduled regression. Scope
  protects against unrelated work, not against the other half of the same sentence.
- **Report the count, not the fix.** Answer a cited line by publishing how many siblings
  the sweep found. A count is falsifiable; "fixed as suggested" is not.
- **Measure the region, not the file.** Four successive word-drop acceptance bars were
  withdrawn because the whole-file number stopped isolating the change as soon as the CR
  also corrected text elsewhere. Choose the measurement that brackets the edit before the
  first review round.
- **A dispute between two competent reviewers usually indicts your own rule.** Codex read
  the two-clock versioning rule to require a contract bump for any instruction change; Grok
  read it to require one only for enforceable floors. Both readings fit the sentence. The
  durable fix was rewriting the sentence, not winning the argument.

**Edu Skill Creator enforcement.** `edu-skill-creator-release` step 2 is the class sweep
(both triggers, count reported, delete rather than annotate); `edu-skill-creator-test`
scenario 15 plants one instruction in four surfaces and cites one; `skill_quality_rubric`
critical flag 12 blocks the shipped defect. And because this lesson's own "Enforced at"
column is an instructional surface, `release_lint` check 11 resolves every NUMBERED
enforcement claim in the table below — which is why claims cite numbered units: a bare
skill name plus a noun cannot be checked. That check found this lesson's own broken claim.
