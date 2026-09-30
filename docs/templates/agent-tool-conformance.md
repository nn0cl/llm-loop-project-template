# Agent Tool Conformance Evidence

Copy this template into a target-owned evidence record. Follow
[the compatibility guide](../collaboration/native-subagent-loop-compatibility.md).
This is a disposable fixture record, not permission to execute unapproved scope.

## Configuration and authority
- Record ID / date / active persona:
- Tool / exact version / model as displayed / local surface (CLI/editor/desktop):
- Covering agreement / work plan / approved backlog / fixture scope:
- Billing prerequisites checked / evidence / unknowns / cloud/API deferrals:
- Installed native configuration paths and relevant contents (no secrets):
- Permissions / sandbox / hook failure policy / continuation cap:
- Native worktree opt-in / base commit / branch / working directory:
- Parent ID / child ID / resume ID / event IDs (unavailable explicitly):
- Attempt ID / previous attempt / current state / consumed events / next action:
- Intervention gate path and recovered value:
- Output manifest (path, hash, producing command/event, attempt):
- Reviewer input allowlist / supplied files / transcript exclusion proof:
- Candidate capability source URLs and retrieval dates:

## Eight-stage fixture

Use separate Verified/Inferred/Unknown status for every row. Documentation-only
claims remain Inferred; a stage lacking execution evidence is not Verified.
Record exact supplied inputs, commands/events, raw output paths and resulting
artifacts. No single percentage can replace missing mandatory gates.

| Stage | Expected observable result | Input / command / event | Raw output / artifacts | Native / auxiliary / unsupported / unconfirmed | Verified / Inferred / Unknown and grounds |
| --- | --- | --- | --- | --- | --- |
| 1 Approved backlog intake | Approved scope dispatched once; unapproved scope does not execute | | | | |
| 2 Design dispatch | Agreement/work plan recorded before implementation | | | | |
| 3 Isolated implementation | Dedicated branch/worktree; phase verification/self-review recorded | | | | |
| 4 Completion and tests/evidence | Completion reaches parent and starts eligible step; deterministic outputs retained | | | | |
| 5 Independent review | Fresh Reviewer gets only artifacts and reruns checks | | | | |
| 6 Finding correction | Deliberate rejection creates finding; fix/re-verification/independent confirmation recorded | | | | |
| 7 Continuation/recovery | Interruption resumes state without duplicates or skipped checks | | | | |
| 8 Director close/lifecycle | Approved result presented; human close recorded before disposition synchronization | | | | |

Stage 4 and stage 7 observations must distinguish active parent turn, ended turn
with client open, idle parent, closed client and restarted client. A successful
active-parent run proves only that configuration. Keep unobserved cases Unknown.
For application fixture work preserve Red/Green/Refactor; for approved docs-only
fixtures record that exception and never fabricate Red/Green evidence.

## Deliberate failure cases

| Failure searched for | Injection / reproducing command or event | Expected rejection/recovery | Observed output path | Status / remaining gap |
| --- | --- | --- | --- | --- |
| Unapproved or missing agreement | | No execution | | |
| Shared checkout or wrong base | | Stop before writes | | |
| Reviewer gets fork/transcript | | Reject independent-review claim | | |
| Deliberate review defect | | Finding lifecycle plus independent confirmation | | |
| Duplicate/stale completion | | No duplicate dispatch/phase advance | | |
| Interrupted worker / failed command | | Preserve partial output, recover same attempt or recorded replacement | | |
| Missing child ID/completion | | Manual identity recovery before replacement | | |
| Quota/permission/hook failure | | Fail/Unknown retained; no invented pass | | |
| Parent turn ended / client exited | | Actual delivery observed or manual recovery limitation | | |
| Director close absent | | No Done or automatic backlog closure | | |

## Finding and completion ledger
- Finding ID / status / original defect reproduction output:
- Correction attempt ID / changed paths / fix output:
- Independent confirmation record / failure scenarios:
- Duplicate delivery event IDs and recorded consumption:
- Recovery decision / active-worker inspection / evidence old attempt stopped:
- Cleanup decision / preserved worktree changes:
- Reviewer typed approvals (specification, phase, boundary, evidence):
- Director statement/date/output artifact (human checkpoint):
- Backlog / issue / work-plan lifecycle updates:

## Assessment
- Verified primitives/stages and exact surface limits:
- Inferred candidates and source grounds:
- Unknown/unsupported capabilities and manual relay needed:
- Configuration an adopter must supply:
- Remaining verification gaps (including entitlement/client-exit behavior):
- Selection / exactly one next safe action / reopening condition:

Do not claim complete adoption until all eight stages have evidence under the
actual configuration and the Director checkpoint remains intact. Store raw
outputs, not only a model summary; do not record credentials or hidden reasoning.
