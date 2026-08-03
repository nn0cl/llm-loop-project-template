# Grok Agent Instructions: Collaboration and Completion

## Design Intake

When a decision affects architecture, capture it as an ADR. When a decision
is unknown, list it in the path-appropriate design note as an ambiguity
boundary.

Every request starts from design intake. Select only the AI payload context
needed for the task, define lightweight VO or DTO candidates when clear, and
route subtasks to an appropriate model, code assistant, or deterministic
tool. When AI or model output is involved, define input, output, and
reasoning evidence contracts before implementation.

Use the full `[DESIGN CHECK]` scaffold only for Feature Path and Architecture
Path work. For Fast Path work, use a compact design note that states scope,
omitted context, deterministic checks, and why the full scaffold is
unnecessary.

## Reopening Gates

Stop the loop and return a reopening request to the Director when:

- no recorded design agreement covers the task.
- the phase or persona for the task is not named.
- issue dependencies are unclear or unresolved.
- requirements imply a new architecture decision not covered by an accepted
  ADR.
- a boundary named in the design agreement would have to be crossed.
- a payload would need unrelated large context.
- a task requires secrets, full source documents, or full private data
  exports.
- an external provider, SDK, model, DB product, or schema convention must be
  chosen and the agreement does not choose it.
- a change would alter an accepted specification or accepted tests.
- deterministic verification contradicts an assumption the agreement rests on.
- the Arbiter finds neither side of a dispute grounded.
- a falsification criterion named in the agreement is met.

A reopening request names what is unsettled and what the loop needs to
continue. It is not a request to approve work already produced. Do not guess
past an unsettled question, and do not stop quietly.

## Minor Fix Path and Preflight Validation

**Minor Fix Path.** A review-finding correction may use this path only when it
is planning size `S`, preserves the accepted specification, changes no
specification, ADR, port, data model, dependency, or architecture boundary,
and is expected to finish in one attempt. Record a compact design note, make
the minimum correction, run deterministic verification, and obtain separate
Reviewer confirmation. Escalate to Feature Path or Architecture Path when any
condition stops being true, including a second attempt. Actionable review
findings are tracked as `Type: review-finding` in `docs/issues/LISS-*.md`;
their lifecycle is `proposed -> accepted -> in_progress -> resolved ->
closed`. Use `wont_do` only with a grounded Arbiter decision record.

**Preflight Validation.** Before independent Reviewer review, run deterministic
checks and record a `pass` or `fail` result with command output, scope result,
and the next action. A `fail` returns the work to the Implementer. A `pass`
only permits submission to the independent Reviewer; it is not approval and
cannot set `wont_do` or `closed`. A lightweight model may assist with checklist
and document-consistency checks but may not issue final approval. The producer
of Preflight cannot review the same change.

Contract-file changes are never self-reviewed, regardless of work-plan scope:
`docs/collaboration/prompt-instruction-change-control.md` (per ADR 0006)
always requires a separate-context Reviewer — including a fix that answers a
Reviewer finding on a contract-file change; the short form below documents
that fix, it does not exempt it from separate-context approval.

For a review finding on a **non-contract-file** change: do not restate the
whole change's verification history. Use `docs/templates/self-review.md`'s
short form: which finding this answers, the command that reproduces the
original defect, the command that shows the fix. See
`docs/architecture/adr/0015-review-cost-discipline.md`.

## Handoff and Completion

When handing off or stopping before completion, use
`docs/templates/agent-handoff.md`, stating active persona, covering design
agreement, current phase, completed artifacts, next safe action, blockers,
files changed, and verification status with output. When issuing a review
decision, use `docs/templates/review-record.md` and store the record under
`docs/collaboration/reviews/`.

Generated source code must minimize cognitive load for whoever reads it next —
a reviewing persona, a future agent, or the Director inspecting artifacts.
Prefer clear responsibility boundaries, small functions, straightforward
names, and reviewable tests. Do not compress implementation into dense code
just to be minimal.

Before reporting completion, check `docs/collaboration/definition-of-done.md`.
Create AI work traces under `docs/collaboration/traces/` when the trace
policy requires it. Use feature-unit branches for feature work; do not
implement issue work directly on `main` or the trunk branch, per
`docs/collaboration/branch-commit-pr-discipline.md`.

For feature work, identify local issue (`docs/issues/LISS-*`) or GitHub
issue dependencies before creating the branch, per
`docs/collaboration/local-issue-planning.md`.
