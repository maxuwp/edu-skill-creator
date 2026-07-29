# tests/ — the suite that found what review did not

Built as ledger row `f14` after three one-off testers found, in a single pass, defects that three
review rounds and a passing lint had cleared: a reviewer allowlist pointing at a gutted file, a
false enforcement claim, three fail-open lint checks, and three crashes in the validator template.

Two layers, deliberately separate.

**Deterministic** — `run_deterministic.py`. Seeds a violation for every lint check and asserts it
fires; probes the validator template's fail-closed contract; checks lesson reachability. Runs in
seconds, no model calls, and is the layer `release_lint.py` check 13 enforces before a push.

**Behavioural** — `evals/*.md`. Prompts for fresh-context agents that cannot be scripted: can an
agent execute the skills cold, do enforcement claims survive semantic inspection. Run these before
any release that changes doctrine or restructures files. Their findings are reported separately from
deterministic results and never overwrite them.

The suite is not proof of correctness. It is proof that specific known failures stay fixed.
