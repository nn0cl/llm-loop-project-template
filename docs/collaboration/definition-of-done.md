# Definition of Done for AI-TDD Collaboration

This document defines completion criteria for collaboration phases. It does not
define application internals.

## Universal Done

A task is not done unless:

- the current phase is explicit.
- local issue, GitHub issue, work plan, or explicit no-issue reason is stated
  when the task is more than a tiny documentation edit.
- planned feature or bug work states its planning size, or explains why size is
  not applicable.
- size `M`, `L`, or `XL` work has a linked AI planning record.
- second-attempt bug fixes have a linked trace and updated planning size.
- changed files are listed in the final response or handoff.
- assumptions and open decisions are visible.
- deterministic verification was run or explicitly marked not applicable.
- applicable Preflight Validation was recorded with its result, command output,
  scope result, and next action; Preflight pass did not replace independent
  Reviewer approval.
- the active persona, covering design agreement, current phase, and approval
  type are explicit when review or phase work is involved.
- deterministic verification output is recorded, not merely asserted.
- self-review at the phase level, and Reviewer approval at the work-plan
  level, both name the failure scenarios searched for. The work-plan-level
  Reviewer approval was issued by a context separate from the one that
  produced the work; self-review, by design, was not — see
  `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.
- issue status, phase, applicable work-plan row, and completion evidence are synchronized in the same reviewable unit when issue work changes status.
- no unrelated context, secrets, or full private data exports were used
  outside what the design agreement and the privacy policy permit.
- generated code, if any, is readable and appropriately split.

## Phase 0 Done: Design Intake

Done when:

- target behavior or question is stated.
- issue dependencies are identified or marked not applicable.
- included context is listed.
- omitted context is listed.
- AI payload and model/tool routing are stated.
- input/output/reasoning contract is stated when AI output is involved.
- decisions the design agreement does not settle are identified, each as a
  reopening request or an explicit deferral with its settling condition.
- next phase is proposed, not silently executed.

## Phase 1 Done: Red

Done when:

- only tests or accepted test-only scaffolding were changed.
- tests map to accepted EARS/Gherkin behavior.
- external dependencies are mocked through ports or interfaces.
- expected Red state is reported.
- Phase 2 is not started before the Implementer has self-reviewed the tests
  on the record — deterministic output and named failure scenarios. "On the
  record" means a self-review record, not a separate-context Reviewer
  approval. See
  `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`.

## Phase 2 Done: Green

Done when:

- tests were not modified to pass.
- implementation is the smallest readable code needed to pass.
- business logic remains out of adapters, UI, commands, provider clients, and
  persistence structs.
- deterministic verification is run where available.
- any unreadable minimal code is either refactored immediately or marked as a
  Phase 3 readability risk.
- self-reviewed before Phase 3, same terms as Phase 1.

## Phase 3 Done: Refactor

Done when:

- behavior and assertions are unchanged.
- separation of concerns is improved or preserved.
- readability is improved or preserved.
- deterministic verification is run where available.
- self-reviewed, same terms as Phase 1, including a verification gap
  statement.

## Work Plan Done

Done when every issue in the work plan is individually Done (above), and in
addition:

- Preflight Validation ran over the whole work plan and recorded `pass`.
- the Reviewer persona, running in a context separate from the one that
  produced the work, approved the work plan as a whole — the review record
  names the failure scenarios searched for and is stored under
  `docs/collaboration/reviews/`.
- any review findings are resolved (Minor Fix Path or escalation) and closed,
  not left `proposed` or `accepted` (or `wont_do` only with an Arbiter
  record). When `docs/collaboration/loop-settings.toml` has
  `[findings].must_apply` / `block_work_plan_done_on_open_findings` true
  (defaults), open findings block Work Plan Done. See
  `docs/collaboration/findings-reuse.md`.
- post-hoc audit artifacts exist for the plan: agreement, review record,
  verification output, and traces required by size — a later reader must not
  need the chat session (`docs/collaboration/post-hoc-audit.md`).
- the Director has read the approved result and recorded the next direction,
  or the end of the engagement, in the same action. A work plan is not Done
  on Reviewer approval alone.

## Documentation-Only Done

Done when:

- the document scope is explicit.
- internal application design is not introduced accidentally.
- new ADRs are listed in README and CI checks when accepted.
- instruction files are updated when agent behavior changes.
- YAML or other structured files are validated when touched.

## Issue Status Synchronization

Issue status drift is a process failure, not an optional documentation task. When an issue reaches
`done`, `review`, `blocked`, or `wont_do`, update all of the following before reporting completion:

1. `docs/issues/LISS-*.md` metadata and completion/current-status evidence.
2. The corresponding row and `Current Next Issue` in the active work plan, when a work plan exists.
3. Any accepted-spec or ADR references whose decision boundary changed.

The implementation commit and the status/documentation update should be the same reviewable unit,
or the handoff must explicitly identify the pending synchronization. A status is not considered
complete from code and tests alone.

## Handoff Done

Done when:

- current phase is stated.
- completed artifacts are listed.
- changed files are listed.
- verification status is stated.
- blockers are stated.
- next safe action is stated.
