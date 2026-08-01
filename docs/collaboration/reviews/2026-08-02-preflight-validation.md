# Review Record: Preflight Validation before independent review

## Constraints (all three must hold)

- [x] **Context separation.** This review ran in a separate Reviewer context.
      I relied on repository artifacts and rerun deterministic output, not on
      the producing context's reasoning.
- [x] **Deterministic precondition.** Deterministic verification was rerun in
      this review context and its actual output is recorded below.
- [x] **Falsification burden.** Failure scenarios searched for are named below,
      each with the grounds on which it does or does not occur.

## Review Target

- Artifact: `AGENTS.md`, `CLAUDE.md`,
  `docs/architecture/implementation-readiness.md`,
  `docs/collaboration/ai-human-scheme.md`,
  `docs/collaboration/definition-of-done.md`,
  `docs/collaboration/model-tool-capability-matrix.md`,
  `docs/templates/review-record.md`, `docs/templates/ai-work-trace.md`,
  `docs/architecture/ai-request-routing.md`,
  `docs/architecture/README.md`,
  `docs/architecture/adr/0013-preflight-validation-before-independent-review.md`,
  `docs/collaboration/agreements/2026-08-02-preflight-validation.md`,
  `docs/collaboration/traces/2026-08-02-preflight-validation.md`,
  `docs/specs/preflight-validation.feature.md`,
  `docs/issues/LISS-0002-preflight-validation.md`
- Covering design agreement: `DA-2026-08-02-05`
- Specification: `docs/specs/preflight-validation.feature.md`
- Current phase: Architecture Path / Tasks 2-3 Phase 2 Green document synchronization
- Producing persona: Specifier / Implementer
- Reviewing persona / model / tool: Reviewer / GPT-5 / shell checks
- Approval type: specification-conformance | phase-correctness |
  boundary-conformance | evidence-sufficiency
- Preflight Validation record:
  `docs/collaboration/traces/2026-08-02-preflight-validation.md`
- Preflight result: pass

## Deterministic Verification Output

```text
$ git diff --check

$ ls AGENTS.md CLAUDE.md docs/architecture/implementation-readiness.md docs/collaboration/ai-human-scheme.md docs/collaboration/definition-of-done.md docs/collaboration/model-tool-capability-matrix.md docs/templates/review-record.md docs/templates/ai-work-trace.md
AGENTS.md
CLAUDE.md
docs/architecture/implementation-readiness.md
docs/collaboration/ai-human-scheme.md
docs/collaboration/definition-of-done.md
docs/collaboration/model-tool-capability-matrix.md
docs/templates/ai-work-trace.md
docs/templates/review-record.md

$ grep -n 'adr/0013-preflight-validation-before-independent-review.md' docs/architecture/README.md
102:- `adr/0013-preflight-validation-before-independent-review.md`

$ rg -n 'Preflight Validation|pass|fail|independent Reviewer|not an approval|command output|scope result|next action|lightweight reasoning model|cannot establish|cannot set|executing environment' AGENTS.md CLAUDE.md docs/architecture/adr/0013-preflight-validation-before-independent-review.md docs/collaboration/agreements/2026-08-02-preflight-validation.md docs/specs/preflight-validation.feature.md docs/architecture/ai-request-routing.md docs/collaboration/model-tool-capability-matrix.md docs/architecture/implementation-readiness.md docs/collaboration/ai-human-scheme.md docs/collaboration/definition-of-done.md docs/templates/review-record.md docs/templates/ai-work-trace.md docs/collaboration/traces/2026-08-02-preflight-validation.md
docs/templates/ai-work-trace.md:70:## Preflight Validation
docs/templates/ai-work-trace.md:73:- Result: pass | fail | N/A
docs/templates/ai-work-trace.md:74:- Checks and command output:
docs/specs/preflight-validation.feature.md:1:# Feature: Preflight Validation before independent review
docs/specs/preflight-validation.feature.md:3:## Scenario: Pass a clean change to the independent Reviewer
docs/specs/preflight-validation.feature.md:6:When deterministic checks and the Preflight checklist pass
docs/specs/preflight-validation.feature.md:8:  `pass`, and the change is submitted to an independent Reviewer
docs/specs/preflight-validation.feature.md:13:When Preflight Validation runs
docs/specs/preflight-validation.feature.md:14:Then it records `fail`, names the failed check, and returns the change to the
docs/specs/preflight-validation.feature.md:21:Then a lightweight reasoning model may identify omissions or inconsistent terms
docs/specs/preflight-validation.feature.md:26:Given Preflight Validation has passed
docs/collaboration/definition-of-done.md:20:- applicable Preflight Validation was recorded with its result, command output,
docs/collaboration/definition-of-done.md:21:  scope result, and next action; Preflight pass did not replace independent
docs/collaboration/agreements/2026-08-02-preflight-validation.md:47:- `fail` は Implementer に戻す。修正後は Preflight を再実行する。
docs/collaboration/agreements/2026-08-02-preflight-validation.md:48:- `pass` でも独立 Reviewer を必ず実行する。
docs/collaboration/agreements/2026-08-02-preflight-validation.md:82:dates use the executing environment's `date` output; another context's
docs/architecture/implementation-readiness.md:44:- Preflight Validation is recorded before independent review when the covering
AGENTS.md:163:**Preflight Validation.** Before independent Reviewer review, run deterministic
AGENTS.md:164:checks and record a `pass` or `fail` result with command output, scope result,
AGENTS.md:165:and the next action. A `fail` returns the work to the Implementer. A `pass`
AGENTS.md:166:only permits submission to the independent Reviewer; it is not approval and
docs/collaboration/traces/2026-08-02-preflight-validation.md:30:## Preflight Validation
docs/collaboration/traces/2026-08-02-preflight-validation.md:33:- Result: pass
docs/collaboration/traces/2026-08-02-preflight-validation.md:34:- Checks and command output: recorded verbatim below.
docs/collaboration/traces/2026-08-02-preflight-validation.md:37:- Next action: independent Reviewer review remains required.
docs/collaboration/traces/2026-08-02-preflight-validation.md:55:wide keyword count. Artifact dates use the executing environment's `date`
docs/collaboration/model-tool-capability-matrix.md:109:| Preflight Validation | Deterministic tool first; lightweight reasoning model for checklist assistance | never issue approval; fail returns to Implementer |
docs/templates/review-record.md:33:- Preflight Validation record:
docs/templates/review-record.md:34:- Preflight result: pass | fail | N/A
docs/architecture/ai-request-routing.md:132:Preflight output must record `pass` or `fail`, each check, command/output
docs/architecture/ai-request-routing.md:133:evidence, scope result, and next action. A Preflight `pass` never replaces an
docs/collaboration/ai-human-scheme.md:73:  -> Preflight Validation        (Implementer / deterministic tool)
docs/collaboration/ai-human-scheme.md:74:  -> fail -> Implementer correction and repeat Preflight
docs/collaboration/ai-human-scheme.md:75:  -> pass
docs/collaboration/ai-human-scheme.md:92:Preflight Validation is a submission check, not an approval. It may reject a
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:18:1. Add a Preflight Validation step between Implementer completion and
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:19:   independent Reviewer review.
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:20:2. Run deterministic checks first. A lightweight reasoning model may assist
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:22:3. Record `pass` or `fail`, each check, command/output evidence, scope result,
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:24:4. On `fail`, return to the Implementer and do not issue Reviewer approval.
docs/architecture/adr/0013-preflight-validation-before-independent-review.md:26:5. On `pass`, submit to an independent Reviewer. Preflight is not an approval
CLAUDE.md:224:### Preflight Validation
CLAUDE.md:226:Before independent Reviewer review, run deterministic checks and record a
CLAUDE.md:227:`pass` or `fail` result with command output, scope result, and the next action.
CLAUDE.md:228:A `fail` returns the work to the Implementer. A `pass` only permits submission

$ sed -n '1,160p' docs/collaboration/traces/2026-08-02-preflight-validation.md
# AI Work Trace: Preflight Validation

## Request

- Date: 2026-08-02
- User request: add a cheap self-check before the heavy independent review.
- Active persona: Implementer
- Covering design agreement: `DA-2026-08-02-05`
- Current phase: Architecture Path / Phase 2 Green for contract documents
- Canonical issue or work plan: `LISS-0002`
- AI planning record: N/A; planning estimate not exposed by this environment

## Context Ledger

- Included: existing review workflow, routing matrix, agent contracts,
  deterministic verification rules, review and trace templates.
- Omitted: application source, provider SDKs, datastore schemas, private data.
- Assumptions: independent Reviewer approval remains mandatory.
- Open decisions: whether to automate Preflight in a runner.

## Routing

- Model/assistant/tool: deterministic document checks; lightweight reasoning
  model only for checklist/document consistency assistance.
- Reason: reduce expensive Reviewer work without transferring approval authority.
- Compatibility state: Unknown — no concrete external model configuration was
  exercised for this documentation change.
- Privacy constraints: no private review payloads used.

## Preflight Validation

- Required: yes
- Result: pass
- Checks and command output: recorded verbatim below.
- Scope result: only contract, ADR, specification, template, and routing files
  are in scope.
- Next action: independent Reviewer review remains required.
- Independent Reviewer still required: yes

## Verification

- Commands/checks: `git diff --check`; required-file checks; ADR index check;
  named Preflight/Reviewer non-substitution term search; date basis.
- Result: passed. The exact output was:

```text
required files: 8 OK
ADR files 0001-0013: OK
named contract coverage: 8 files
2026-08-02 04:52:36 Sunday JST +0900
```

`git diff --check` passed with no output. The named coverage count is scoped to
the eight synchronization surfaces listed in the agreement, not a repository-
wide keyword count. Artifact dates use the executing environment's `date`
output.

## Changed Files

- `docs/collaboration/agreements/2026-08-02-preflight-validation.md`
- `docs/specs/preflight-validation.feature.md`
- `docs/architecture/adr/0013-preflight-validation-before-independent-review.md`
- `docs/issues/LISS-0002-preflight-validation.md`
- agent contracts, routing tables, review/trace/work-plan templates, and process docs

## Next Safe Action

- Run deterministic checks and hand the artifacts to an independent Reviewer.

$ date '+%Y-%m-%d %H:%M:%S %A %Z %z'
2026-08-02 04:53:29 Sunday JST +0900
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | Preflight `pass` can replace independent Reviewer approval | Not reproduced. The agreement, ADR 0013, feature spec, agent contracts, routing docs, definition-of-done, and trace all preserve that Preflight is a submission check only and that independent Reviewer review remains required after `pass`. | not reproduced |
| 2 | Preflight `fail` lacks corrective return and recheck behavior | Not reproduced. The agreement, ADR 0013, `AGENTS.md`, and `docs/collaboration/ai-human-scheme.md` all require return to the Implementer and re-run of Preflight after correction. | not reproduced |
| 3 | The lightweight model gains approval or Arbiter authority | Not reproduced. The feature spec, ADR 0013, routing docs, and agent contracts all confine the lightweight model to checklist/document-consistency assistance and keep approval and Arbiter authority elsewhere. | not reproduced |
| 4 | Preflight evidence lacks command/output/scope/route/next action, or is unavailable in the review record | Not reproduced. The trace now records route, compatibility state, scope result, next action, and exact deterministic output; the review record template carries explicit Preflight fields; and this review record includes the trace as the Preflight artifact under review. | not reproduced |
| 5 | Contract index, ADR references, or coverage definition are inconsistent | Not reproduced. `docs/architecture/README.md` includes ADR 0013, and the agreement now defines the coverage count explicitly as eight named synchronization surfaces rather than a repository-wide keyword count. The rerun of those eight surfaces succeeded. | not reproduced |
| 6 | Preflight changes unrelated review-finding lifecycle behavior | Not reproduced. Review-finding lifecycle authority remains in ADR 0012 and the local-issue template. The Preflight changes only prohibit Preflight from setting `wont_do` or `closed`; they do not alter lifecycle transitions. | not reproduced |
| 7 | Artifact dates are inconsistent with the governing date basis | Not reproduced under the corrected agreement. This review context's current date is Saturday, August 1, 2026, while the executing environment's `date` output reran as Sunday, August 2, 2026 at `04:53:29 JST +0900`. The agreement and trace now explicitly ground artifact dates on the executing environment's `date` output, so that exact future-dated artifact timestamp is explained rather than inconsistent. | not reproduced |

## Scenarios Not Searched

- I did not review unrelated application source, tests, or CI behavior outside
  the ADR 0013 agreement scope.

## Checklist

- [x] The artifact belongs to the phase that was run; no later phase leaked in.
- [x] Every `Then` clause in the specification is asserted by the work.
- [x] The dependency rule and port boundaries hold.
- [x] No boundary named in the design agreement was crossed.
- [x] Specifications and accepted tests were not modified to make work pass.
- [x] Every claim in the artifact states its grounds.
- [x] The record would let a third party re-run this same search.

## Decision

- [x] Approved
- [ ] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state what
      is unsettled and what the loop needs in order to continue

## Reasons

- Approval types:
  - Specification conformance: Approved
  - Phase correctness: Approved
  - Boundary conformance: Approved
  - Evidence sufficiency: Approved
- Grounds:
  - The corrected trace now provides the required Preflight evidence bundle.
  - The agreement now defines the eight-file coverage claim precisely.
  - The artifact-date basis is explicitly grounded in the executing
    environment's `date` output, which reran in this review context.
