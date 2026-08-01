# Review Record: Review issues and Minor Fix Path

Use this when the Reviewer persona issues a decision inside the execution loop.

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in a context separate from the
      one that produced the work. The Implementer's reasoning was not supplied
      and is not relied on as justification.
- [x] **Deterministic precondition.** Deterministic verification was run and
      its output is recorded below. No approval is issued past a failing or
      absent signal.
- [x] **Falsification burden.** Failure scenarios searched for are named below,
      each with the grounds on which it does not occur.

## Review Target

- Artifact: `AGENTS.md`, `docs/architecture/README.md`,
  `docs/architecture/ai-request-routing.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/templates/ai-work-trace.md`, `docs/templates/local-issue.md`,
  `docs/templates/work-plan.md`,
  `docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md`,
  `docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md`,
  `docs/specs/review-issue-and-minor-fix-path.feature.md`,
  `docs/issues/LISS-0001-review-issues-minor-fix-path.md`,
  `docs/work-plans/WP-0001-review-issues-minor-fix-path.md`,
  `docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md`
- Covering design agreement: `DA-2026-08-02-04`
- Specification: `docs/specs/review-issue-and-minor-fix-path.feature.md`
- Current phase: Architecture Path / Task 4 Phase 2 Green document synchronization
- Producing persona: Planner / Specifier / Implementer
- Reviewing persona / model / tool: Reviewer / GPT-5 / shell checks
- Approval type: specification-conformance | phase-correctness |
  boundary-conformance | evidence-sufficiency

## Deterministic Verification Output

Paste the actual output. A summary of it is not evidence.

```text
$ git diff --check

$ ls docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md docs/specs/review-issue-and-minor-fix-path.feature.md docs/architecture/ai-request-routing.md docs/collaboration/model-tool-capability-matrix.md docs/templates/local-issue.md docs/templates/work-plan.md docs/templates/ai-work-trace.md docs/templates/review-record.md docs/issues/LISS-0001-review-issues-minor-fix-path.md docs/work-plans/WP-0001-review-issues-minor-fix-path.md docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md
docs/architecture/ai-request-routing.md
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md
docs/collaboration/model-tool-capability-matrix.md
docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md
docs/issues/LISS-0001-review-issues-minor-fix-path.md
docs/specs/review-issue-and-minor-fix-path.feature.md
docs/templates/ai-work-trace.md
docs/templates/local-issue.md
docs/templates/review-record.md
docs/templates/work-plan.md
docs/work-plans/WP-0001-review-issues-minor-fix-path.md

$ grep -n 'adr/00' docs/architecture/README.md
89:- `adr/0001-director-centered-planning-and-closed-loop.md` — the governing
91:- `adr/0002-design-first-ai-request-routing.md`
92:- `adr/0003-input-output-reasoning-contracts.md`
93:- `adr/0004-human-readable-source-code-quality.md`
94:- `adr/0005-local-issue-planning.md`
95:- `adr/0006-prompt-instruction-change-control.md`
96:- `adr/0007-trunk-oriented-branching.md`
97:- `adr/0008-template-update-propagation.md`
98:- `adr/0009-bug-planning-and-ai-usage-records.md`
99:- `adr/0010-ai-failure-recovery-and-runner-cli-contract.md`
100:- `adr/0011-external-resource-adoption-contract.md`
101:- `adr/0012-review-issues-minor-fix-and-model-routing.md`

$ rg -n "Status authority|sole lifecycle field|Minor Fix Path|specification, ADR, port, data model, dependency|data-model|second attempt|compatibility state|Compatibility state|wont_do|Arbiter decision record|Date basis|executing environment's `date` output|date source|leaves size S|needs a second attempt" AGENTS.md docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md docs/specs/review-issue-and-minor-fix-path.feature.md docs/architecture/ai-request-routing.md docs/collaboration/model-tool-capability-matrix.md docs/templates/local-issue.md docs/templates/work-plan.md docs/templates/ai-work-trace.md docs/issues/LISS-0001-review-issues-minor-fix-path.md docs/work-plans/WP-0001-review-issues-minor-fix-path.md docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md
AGENTS.md:152:**Minor Fix Path.** A review-finding correction may use this path only when it
AGENTS.md:154:specification, ADR, port, data model, dependency, or architecture boundary,
AGENTS.md:158:condition stops being true, including a second attempt. Actionable
AGENTS.md:161:Use `wont_do` only with a grounded Arbiter decision record.
docs/templates/work-plan.md:73:## Minor Fix Path
docs/templates/work-plan.md:80:true, including when a second attempt is needed.
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:20:  - Minor Fix Path と適用条件を定義する。
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:32:| 2 | Minor Fix Path を定義 | Specifier | Architecture Path | 適用条件、除外条件、検証、Reviewer 要件が明記される | 契約文書検索、シナリオ照合 |
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:49:- 指摘の否定は `wont_do` とし、Reviewer の単独判断ではなく Arbiter の根拠付き記録を必要とする。
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:50:- Minor Fix Path は既存仕様・既存境界の範囲内に限る。仕様、ADR、ポート、データモデル、依存関係を変える場合は通常の Architecture/Feature Path に戻る。
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:80:- `wont_do` が Arbiter の記録なしに設定できる。
docs/collaboration/agreements/2026-08-02-review-issue-and-minor-fix-path.md:81:- Minor Fix Path が仕様・境界変更を覆い隠す。
docs/work-plans/WP-0001-review-issues-minor-fix-path.md:1:# Work Plan: Review issues and Minor Fix Path
docs/work-plans/WP-0001-review-issues-minor-fix-path.md:10:- In: review-finding ISSUE lifecycle, Minor Fix Path, capability routing,
docs/work-plans/WP-0001-review-issues-minor-fix-path.md:36:- Minor Fix Path may be over-applied; boundary and one-attempt criteria are
docs/templates/local-issue.md:9:  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
docs/templates/local-issue.md:36:- Arbiter decision record:
docs/templates/local-issue.md:60:<!-- Required for planning size M or larger and when a second attempt starts. -->
docs/templates/local-issue.md:73:- Compatibility state: Verified | Inferred | Unknown (with reason)
docs/issues/LISS-0001-review-issues-minor-fix-path.md:1:# LISS-0001: Review issues, Minor Fix Path, and capability routing
docs/issues/LISS-0001-review-issues-minor-fix-path.md:14:- Status authority: Metadata `Status` is the sole lifecycle field; this issue is not a review-finding.
docs/specs/review-issue-and-minor-fix-path.feature.md:21:Then the ISSUE records status `wont_do`, the Arbiter decision, the grounds, and
docs/specs/review-issue-and-minor-fix-path.feature.md:24:## Scenario: Use the Minor Fix Path
docs/specs/review-issue-and-minor-fix-path.feature.md:28:When the task is routed through Minor Fix Path
docs/specs/review-issue-and-minor-fix-path.feature.md:32:## Scenario: Escalate a correction out of the Minor Fix Path
docs/specs/review-issue-and-minor-fix-path.feature.md:34:Given a correction changes a specification, ADR, port, data model, dependency,
docs/specs/review-issue-and-minor-fix-path.feature.md:35:  or requires a second attempt
docs/specs/review-issue-and-minor-fix-path.feature.md:38:  Minor Fix Path task
docs/specs/review-issue-and-minor-fix-path.feature.md:45:  records any escalation reason and compatibility state
docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md:1:# AI Work Trace: Review Issues and Minor Fix Path
docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md:29:- Compatibility state: Unknown — no concrete provider/model configuration was
docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md:73:Date basis: the execution environment reported `2026-08-02 04:36:05 JST`; the
docs/templates/ai-work-trace.md:24:- Compatibility state: Verified | Inferred | Unknown, with reason:
docs/templates/ai-work-trace.md:58:- Compatibility statement:
docs/collaboration/model-tool-capability-matrix.md:106:| Minor Fix Path implementation | Code assistant or lightweight reasoning model | required when it changes a specification, ADR, port, data model, dependency, architecture boundary, leaves size S, or needs a second attempt |
docs/collaboration/model-tool-capability-matrix.md:107:| Minor Fix Path closure review | Strong reasoning agent in a separate context | always required |
docs/architecture/ai-request-routing.md:123:| Narrow Minor Fix Path correction | Code assistant or lightweight reasoning model | specification, ADR, port, data-model, dependency, architecture-boundary, or second-attempt changes |
docs/architecture/ai-request-routing.md:128:reasoning setting when available, compatibility state, and escalation reason.
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:1:# ADR 0012: Review Issues, Minor Fix Path, and Capability-Based Model Routing
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:20:   closed`. A disputed finding may move from `accepted` to `wont_do` only with
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:21:   an Arbiter decision record containing grounds and rejected alternatives.
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:24:4. Add Minor Fix Path for one-attempt, size-S corrections that preserve the
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:31:6. Record the displayed model/reasoning setting and compatibility state when
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:46:- Minor Fix Path still requires independent review and deterministic evidence.
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:53:- `wont_do` without an Arbiter record and grounds.
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:54:- Minor Fix Path work that changes an accepted specification or architecture boundary.
docs/architecture/adr/0012-review-issues-minor-fix-and-model-routing.md:55:- routing claims that omit the capability class, compatibility state, or escalation reason when applicable.

$ date '+%Y-%m-%d %H:%M:%S %A %Z %z'
2026-08-02 04:37:11 Sunday JST +0900
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | Review-finding lifecycle has missing or unsafe transitions, or lacks evidence because multiple lifecycle fields remain authoritative | Not reproduced in the template set I reviewed. `docs/templates/local-issue.md` now states that metadata `Status` is the authoritative lifecycle field, and `docs/issues/LISS-0001-review-issues-minor-fix-path.md` repeats that rule for the concrete issue. | not reproduced |
| 2 | `wont_do` can be used without a grounded Arbiter record | Not reproduced. The feature spec still requires Arbiter decision, grounds, and rejected alternatives, and the local-issue template still includes an Arbiter decision record field. `AGENTS.md` also preserves the grounded-Arbiter requirement. | not reproduced |
| 3 | Minor Fix Path can hide specification, ADR, port, data-model, dependency, architecture-boundary, size-S exit, or second-attempt changes | Not reproduced. `AGENTS.md`, `docs/architecture/ai-request-routing.md`, `docs/collaboration/model-tool-capability-matrix.md`, and `docs/templates/work-plan.md` all now carry explicit escalation wording that matches the accepted exclusions materially enough for the specification’s escalation scenario. | not reproduced |
| 4 | Capability routing lacks compatibility-state recording or escalation evidence | Not reproduced for the trace/template pair. `docs/templates/ai-work-trace.md` and `docs/templates/local-issue.md` now include compatibility-state fields, and the current trace records `Unknown` with a reason. | not reproduced |
| 5 | ADR index and contract instructions are inconsistent | Not reproduced. `docs/architecture/README.md` lists twelve process ADRs and includes ADR 0012. | not reproduced |
| 6 | Evidence is internally inconsistent or future-dated without a grounded basis | Reproduced in this review context. The trace is internally consistent and now records the shell’s exact date output plus the agreement rule, but the shell check in this execution still returned `2026-08-02 04:37:11 Sunday JST +0900` while the authoritative current date for this review context is Saturday, August 1, 2026. That leaves the agreement, trace, and this review filename future-dated relative to the actual current date. | reproduced |

## Scenarios Not Searched

Name what this review did not cover, so the gap is visible rather than implied.

- I did not review unrelated application source, tests, CI workflows, or files outside the agreement-scoped contract/routing/template artifacts.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked in.
- [x] Every `Then` clause in the specification is asserted by the work.
- [x] The dependency rule and port boundaries hold.
- [x] No boundary named in the design agreement was crossed.
- [x] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds.
- [x] The record would let a third party re-run this same search.

## Decision

- [ ] Approved
- [x] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state what
      is unsettled and what the loop needs in order to continue

## Reasons

- Approval types:
  - Specification conformance: Approved
  - Phase correctness: Approved
  - Boundary conformance: Approved
  - Evidence sufficiency: Rejected
- Required corrections before approval:
  - Reconcile the shell `date` output of Sunday, August 2, 2026 with the authoritative current date for this review context, Saturday, August 1, 2026, before using August 2, 2026–dated artifacts as evidence, or explicitly reopen the date-handling rule with a grounded cross-context convention that is valid outside the producing context.
