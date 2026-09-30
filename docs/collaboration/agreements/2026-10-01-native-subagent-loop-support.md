# Design Agreement: Native subagent compatibility assessment

## Identity
- Agreement ID: DA-2026-10-01-01
- Date: 2026-10-01
- Director: explicit backlog approval, “バックログ承認。進めて”, for item-0023.
- Planner / Specifier: root Codex agent, acting as Planner for this record.
- Supersedes: none.

## Direction
Strengthen compatibility of the existing complete development loop with current native agent capabilities across six tools. Preserve current billing and defer separately billed cloud/API adoption.

## Scope
In: case-0005 primary-source research, coverage report, local version/feature probes, a disposable fixture when the available native tool supports it, and a reusable compatibility/evidence guide and template copied by existing template paths. Out: new hosted orchestrator, paid API runs, tool installation/upgrades, standing schedulers, changes to human approval authority, automatic real backlog closure, and claims of six-tool live certification.

## Plan
| Task | Persona | Phase | Acceptance | Verification |
| --- | --- | --- | --- | --- |
| LISS-0074 / case-0005 | Planner | phase-0-design | Six-tool sources and gaps; one selection/next action | Source retrieval, local probes, evidence files |
| LISS-0075 | Implementer | docs-only Architecture Path, after closed case-0005 | Reusable compatible handoff and fixture instructions; evidence template; adoption-copy inclusion | Contract checker, copy smoke test, document/link checks |
| Preflight | Implementer | Preflight | Recorded outputs and scope | Deterministic commands |
| Whole-plan review | Reviewer, fresh artifact-only context | Review | Four typed approvals and falsification grounds | Independent rerun and review record |

## Specifications
Documentation acceptance is in LISS-0074/0075; no runtime implementation or application behavior is promised by this plan. No production code or Red/Green phases are needed for this documentation/process assessment. A runtime orchestrator would require a later specification/agreement.

## Boundaries
Existing ADR 0016/0017 and Director close remain authoritative. New companion guidance applies existing invariants and does not replace them. A guide under docs/collaboration is a contract-file change: independent review is mandatory, never producer self-approval. No secrets or account exports. External features remain Inferred until exercised.

## Settled Ambiguities
- Research delegation: read-only source research can run in separate children without shared writes; implementation uses an isolated worktree.
- Missing account access: record Unknown/deferred and complete documentation-supported assessment; do not buy access.
- Fixture: demonstrates only actually exercised native primitives, not unattended operation after client shutdown.

## Deferred Questions
Cloud/API billing and other-tool live execution: settle only with confirmed existing entitlement and available authenticated environment. Do not block source-based deliverables or label these configurations Verified. Final full-loop adoption remains conditional on the eight-stage fixture in item-0023.

## Verification
python3 scripts/check-contract-consistency.py --repo .; git diff --check; temporary-target copy smoke; required matrix/source/template fields. Persist command output in case evidence/trace.

## Falsification Criteria
False release dates; default shared workspaces described as isolated; forked history accepted as independent review; unsupported hook continuation claimed; cloud/API spend required; fabricated live evidence; absent adoption-copy files; Director close bypassed.

## Agreement
- [x] Director: backlog-level approval cited above, under ADR 0016 Rule 2.
- [x] AI: this bounded research/documentation plan is executable without guessing. Unavailable live/billing capabilities remain explicit limitations, not implementation premises.

## Reopening Log
None.
