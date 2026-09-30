# Work Plan: Native subagent loop support

## Goal
Compare six current tools against the existing loop and deliver reusable adoption guidance grounded in research and available native evidence.

## Scope
In: DA-2026-10-01-01. Out: paid/hosted orchestration, runtime code, authority changes.

## Issue Graph
| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0074 | done | M | M | AIP-WP0027-001 | approved item-0023 | LISS-0075 | codex/native-subagent-loop-support |
| LISS-0075 | done | M | M | AIP-WP0027-001 | closed case-0005 | preflight | dedicated worktree |

## AI Planning Records
### AIP-WP0027-001
- Status: accepted
- Created: 2026-10-01
- Agent/environment: root Codex desktop; Planner
- Model as displayed: N/A; no authoritative per-call model identifier in tool output.
- Reasoning setting: N/A; not surfaced.
- Planning size: M
- Route: independent read-only research; Implementer in isolated worktree; fresh artifact-only Reviewer.
- Scope: research and reusable documentation, no runtime orchestrator.
- Token range/midpoint/metric: N/A; no reliable per-agent usage measurement available.
- Assumption/confidence: documented capabilities can be compared without paid runs; high. Live full-loop compatibility remains unconfirmed.

## Recommended Order
Research -> close case-0005 with one next action -> documentation implementation -> deterministic preflight -> separate Reviewer -> Director checkpoint.

## Current Next Issue
None. WP-0027 is closed by the Director; LISS-0074 and LISS-0075 are done.

## Preflight Validation
Implementer, docs-only Architecture Path. Result: pass. Raw outputs are linked in the packet below; contract consistency, document/link checks and isolated copy smoke passed; whitespace check passed. This pass permits review submission only.
Scope: companion guide, template, optional adoption entry, issue/status/trace records;
no runtime or new mandatory reading rule. Case-0005 closed; no plan-owned open
review findings identified. Independent review required after pass.

## Review Summary Packet
- Agreement: docs/collaboration/agreements/2026-10-01-native-subagent-loop-support.md
- Acceptance: docs/issues/LISS-0074-native-subagent-support-research.md and docs/issues/LISS-0075-native-subagent-adoption-guide.md; docs/backlog/item-0023-native-subagent-closed-loop-support.md.
- Changes: docs/collaboration/native-subagent-loop-compatibility.md; docs/templates/agent-tool-conformance.md; docs/collaboration/adoption-guide.md.
- Evidence: docs/spike/case-0005-native-subagent-loop-support/case.md; evidence/research.md; evidence/local-inventory.txt; evidence/implementation-contract-check.txt; evidence/implementation-copy-smoke.txt; evidence/implementation-document-check.txt; evidence/implementation-diff-check.txt (all evidence paths relative to that case).
- Producer trace: docs/collaboration/traces/2026-10-01-liss-0075-native-subagent-guide-implementation.md is audit metadata, not Reviewer justification; Reviewer must independently inspect source artifacts and outputs.
- Reviewer scope: whole WP-0027, four typed approvals; independently rerun deterministic checks. Artifact-only input, no fork/transcript.
- Falsification targets: false full-loop verification, shared worktree called isolated, history fork called independent, hook event called continuation, new spend, missing copied guide/template, skipped Director close.
- Limitations: source-supported candidates only; missing accounts/live surfaces, installed-version differences, idle/closed-client wake and full eight-stage fixture remain unconfirmed.
- Next action: fresh separate-context Reviewer; no final approval from Implementer.

## Work-Plan Review
Approved in all four types for the bounded documentation support package and partial active-parent fixture.
Record: ../collaboration/reviews/2026-10-01-wp-0027-source-correction-confirmation.md.
Original rejection is preserved; LISS-0076 independently confirmed and closed.

## Work-Plan Close
Closed on 2026-10-01 after independent approval and the Director statement: “クローズ、コミット、プッシュしてPRを作って”.
- Active persona recording close: Planner; Fast Path lifecycle/publication only.
- Covering agreement: DA-2026-10-01-01.
- Disposition: accepted documentation support package and partial native probe; all issues done and LISS-0076 closed.
- Backlog item-0023 remains `promoted` under the backlog status vocabulary; its promoted WP-0027 is completed. Full-loop live adoption remains conditional and no further implementation is authorized by this close.
- Next direction: commit/push the close records and publish PR #25 for review. No next work plan requested.
- Deferred scope remains unchanged: full eight-stage six-tool certification and billing-changing cloud/API adoption.
- Verification/close trace: ../collaboration/traces/2026-10-01-wp-0027-director-close.md.

## Risks
Installed Codex CLI predates researched releases. Other accounts unavailable. Native context isolation and worktree isolation must be tested separately. Source claims do not certify workflow authority or continuous runtime.

## Verification Plan
See agreement; exact outputs stored under case-0005/evidence and work trace.

## Integration and native probe supplement
- Root acting as Implementer for artifact integration only; separate Reviewer pending.
- Implementation files transferred byte-for-byte from the dedicated worktree. No producer approval of contract files.
- Actual active-parent native probe: isolated worker, completion notification, fresh artifact-only rejection, followup resume of same worker, correction and another fresh Reviewer confirmation. Raw artifacts under case-0005/evidence/native-probe.
- Probe is partial, not eight-stage adoption certification; no idle-parent/closed-client/crash/duplicate test or real backlog/Director closure.
- Full-loop adoption and unavailable billing/runtime configurations remain explicitly deferred, so this plan completes an assessment/support package rather than claiming automatic six-tool operation.

## Integrated preflight snapshot
- Result: pass; raw commands/output: ../spike/case-0005-native-subagent-loop-support/evidence/integrated-preflight.txt.
- Next approval: independent specification/phase/boundary/evidence review of documentation scope.
- Exact submitted file list (before Reviewer-owned record):
- docs/backlog/item-0023-native-subagent-closed-loop-support.md
- docs/collaboration/adoption-guide.md
- docs/collaboration/agreements/2026-10-01-native-subagent-loop-support.md
- docs/collaboration/native-subagent-loop-compatibility.md
- docs/collaboration/traces/2026-10-01-cross-tool-release-design-intake.md
- docs/collaboration/traces/2026-10-01-liss-0075-native-subagent-guide-implementation.md
- docs/issues/LISS-0074-native-subagent-support-research.md
- docs/issues/LISS-0075-native-subagent-adoption-guide.md
- docs/spike/case-0005-native-subagent-loop-support/case.md
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-contract-check.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-contract-initial.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-copy-smoke.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-diff-check.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-document-check.py
- docs/spike/case-0005-native-subagent-loop-support/evidence/implementation-document-check.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/integrated-preflight.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/local-inventory.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/acceptance.json
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/attempt-1-decision.json
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/decision.json
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/fixture-evidence.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/probe-scope.md
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/replay-output.txt
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/review-1.md
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/review-2.md
- docs/spike/case-0005-native-subagent-loop-support/evidence/native-probe/sha256.json
- docs/spike/case-0005-native-subagent-loop-support/evidence/research.md
- docs/templates/agent-tool-conformance.md
- docs/work-plans/WP-0027-native-subagent-loop-support.md

## Review finding correction
- Initial review: Rejected, record ../collaboration/reviews/2026-10-01-wp-0027-native-subagent-loop-support-review.md.
- LISS-0076: closed by independent Reviewer; source-grounding correction confirmed.
- Preflight refreshed for changed guide/source records in source-correction-check.txt; no native probe claim expanded.
- Independent whole-plan review approved; subsequent Director close is recorded above.
