# Implementation patterns — mechanisms, not doctrine

**Everything in this file is an example, not a requirement.** The lessons state capabilities; this
file records concrete mechanisms that have satisfied them, so that a lesson can say "trace the user's
decisions" without forcing every plugin to build one product's machinery. Created as gate row `f31`,
in the same release that stripped these mechanisms out of the lesson text — otherwise the relocation
would have been a deletion.

Each pattern records: the capability it satisfies, the product type it suits, portability
implications, a simpler fallback, and where it was actually run.

---

## P1 — Hash-bound decision ledger (satisfies L15, tracing user decisions)

**Suits:** multi-stage pipelines with several stages able to alter an artifact after the user's
decision. **Overkill for:** a skill-only product, or any pipeline with one drafting stage.

An append-only record of each explicit user decision, keyed by a stable id, with a hash of the
artifact the decision was about. Every downstream stage able to touch the item re-checks its own
output against the record and reports satisfied or unsatisfied. Verified against the **rendered**
surface, not a source-path grep, since a source reference can be present while the item is absent
from what ships.

**Portability:** needs durable session storage and a hashing routine; no network or UI required.
**Simpler fallback:** a checklist in the session manifest that the final review reads aloud against
the artifact. Weaker, but it satisfies the capability for small products.
**Run in:** POSED 1.57–1.59 (text probes first, extended to binary assets after a text-only probe
missed an omitted approved chart).

## P2 — Locked process graph (satisfies L17, teaching a process faithfully)

**Suits:** modules whose learning outcome is a decision procedure with branches.
**Overkill for:** linear procedures, or a checklist the learner follows once.

Nodes are decision points, edges are outcomes, each node carries provenance (published framework,
faculty framework, hybrid, or explicit pedagogical rationale). The teaching sequence must walk
declared transitions, and any deviation is declared rather than silent.

**Portability:** a JSON graph and a traversal check; no special runtime.
**Simpler fallbacks:** an ordered checklist with stated entry conditions; a worked decision path
through one realistic case; a state table. Any representation works if it matches the real process.
**Run in:** POSED 1.54.

## P3 — Server-stamped gate decisions (satisfies L5 and L11, decision provenance)

**Suits:** any product where an agent could write the decision file the gate reads.
**Overkill for:** a gate the human operates directly in a tool the agent cannot write to.

The process that serves the gate stamps each submission with its own timestamp, a content-derived
decision id, and the submitting surface. A hand-written decision is then mechanically detectable,
because it lacks stamps the agent cannot forge.

**Portability:** needs a local process serving the gate. Where the environment provides no such
surface, the capability is met instead by having the human record the decision somewhere the agent
cannot write, and disclosing that limitation rather than claiming a stamp.
**Run in:** POSED 1.29 (F3/F4), after a completion claim was found resting on hand-written gates.

## P4 — Rendered-surface probes (satisfies L14, checking at the claim's layer)

**Suits:** any pipeline authoring in one format and delivering in another.
**Overkill for:** artifacts whose authored form is the delivered form.

The check runs against the compiled output — extracted text, the DOM, the rendered page — rather
than the source. A requirement about what the audience perceives cannot be satisfied by metadata
the audience never sees.

**Portability:** needs whatever renders the artifact, which the pipeline already has at compile time.
**Simpler fallback:** open the rendered artifact and inspect the specific claim by hand, recording
what was inspected.
**Run in:** POSED 1.40, 1.46, 1.51.
