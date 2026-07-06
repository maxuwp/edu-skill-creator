# HITL Gate Design Patterns — for educational plugins

Distilled from POSED's guided app (`posed_app.py`, the reference implementation) and the
pilot failures in `lessons_learned.md` (L4, L5). `page-architecture` requires every gate
in a new plugin's design to specify the fields in "Gate specification" below.

## Principles

1. **One decision per gate.** If a gate asks the educator to judge two independent
   things, split it. A wizard of narrow steps beats one broad approval (L4).
2. **Structured input, never free text alone.** Every reviewable item gets a stable id
   (`c1`, `b3`, `s12`… — never renumbered, even after removals) and a disposition control:
   keep / revise / split / remove, plus an optional comment. Sections get section-level
   feedback controls. Reorder is a control (↑↓), not a comment.
3. **Decisions are JSON on disk.** Each gate persists a decision file, e.g.:
   ```json
   {
     "decision": "approve | approve-with-required-revision | regenerate",
     "guidance": "free-text overall note",
     "section_feedback": { "objectives": "..." },
     "items": [
       { "id": "b3", "order": 2, "disposition": "revise",
         "comment": "...", "edited_fields": { } }
     ]
   }
   ```
   Every feedback element routes to the pipeline step that OWNS that item; feedback with
   no owner is a design error.
4. **Review before gate.** The independent reviewer's log is written to disk before the
   human page renders; the gate shows the reviewer's summary card (score, top findings,
   critical flags) so the human never reviews blind.
5. **Never accept on the human's behalf.** The assistant may prefill recommended
   defaults; it may never click approve, skip a gate, or interpret "prefer defaults" as
   permission to bypass. An un-gated approval is a critical defect (POSED Stage 7
   classifies "a gate was skipped" as severity critical).
6. **Stale-state propagation.** Approving an upstream change marks every downstream
   artifact stale: manifest fields `valid_from_step` / `valid_from_stage`,
   `stale_due_to`, `needs_regeneration`, `superseded_by`. Compile/assembly refuses to run
   while anything is stale. A prior PASS does not survive edits.
7. **Stage-end summaries.** Each stage ends with a plain-language summary of what was
   decided and what becomes stale; optionally capture gate screenshots for the record.

## Gate specification (required per gate in an architecture doc)

| Field | Meaning |
|---|---|
| `gate_id` | Stable name, e.g. `outline_step3_gate` |
| `decision` | The ONE question the human answers |
| `artifact` | File(s) under review, with stable-id scheme |
| `reviewer` | The independent reviewer skill + rubric that runs first |
| `decision_file` | Path + JSON schema of the persisted decision |
| `owns` | Which step regenerates on revise/regenerate |
| `invalidates` | Downstream artifacts marked stale on approval of changes |
| `consent` | If the step is token-expensive: full/lite/skip ladder text (L6) |

## Session mechanics (borrow, don't reinvent)

POSED's guided app already solves: cloud-storage-safe sessions (staging under a local
private tmp dir when the project lives in OneDrive/iCloud; `--cloud-safe auto|always|never`),
sandboxed-harness handoff (`--status-file` with ready → submitted_to_server → completed),
and item/section gate pages. New educational plugins should adapt that app (or its
patterns) rather than writing gate UIs from scratch — `page-scaffold` copies it as a
starting point.
