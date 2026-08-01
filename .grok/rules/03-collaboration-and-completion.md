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

## Handoff and Completion

When handing off or stopping before completion, use
`docs/templates/agent-handoff.md`, stating active persona, covering design
agreement, current phase, completed artifacts, next safe action, blockers,
files changed, and verification status with output. When issuing a review
decision, use `docs/templates/review-record.md`.

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
