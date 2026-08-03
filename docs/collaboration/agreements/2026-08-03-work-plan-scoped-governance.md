# Design Agreement: Work-Plan-Scoped Governance

## Identity

- Agreement ID: DA-2026-08-03-01
- Date: 2026-08-03
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none directly. Supersedes, in effect, the
  execution-loop portion of ADR 0001's model, via the new ADR this agreement
  covers.

## Direction

The Director's framing, reached through dialogue across several turns:

- TDD is still performed. Within a single ISSUE's Red/Green/Refactor cycle,
  review and approval happen in the **same context** that produced the work
  (self-review), not a separate-context Reviewer.
- A work plan's initial direction is still decided by the Director and AI
  together, through dialogue — unchanged from the current design-agreement
  phase.
- Once all issues in a work plan are self-reviewed and complete, review and
  resolution of the work plan happen **AI-to-AI**, in a separate context —
  the existing Reviewer/Preflight/Minor-Fix-Path machinery, applied at the
  work-plan level instead of the phase level.
- Review of the completed work plan, and the decision to proceed to the next
  one, are **one combined human action** — not two separate gates. The
  Director reads the AI-approved work plan's result and, in the same turn,
  states the next direction (or ends the engagement).
- Fixes remain AI work (Implementer), as today.

The Director's own falsification concern, raised and accepted during
dialogue: this changes the review model from "always caught fast, per phase"
to "caught at the end of a work plan, less often." The empirical grounds for
that risk — six review rounds against the contract-consistency checker in
this repository's own recent history, all of them separate-context review
catching what self-review structurally cannot — apply here directly. This
agreement is explicit that the tradeoff is accepted, not overlooked: smaller
work plans bound the risk, and the record of accepting this tradeoff should
survive so a future reader does not mistake it for an oversight.

## Scope

- In scope:
  - A new ADR superseding the execution-loop portions of ADR 0001 (the
    per-phase context-separation requirement, and the single-gate model).
  - Every document that states the superseded rule: `ai-human-scheme.md`,
    `personas.md`, `design-agreement.md`, the nine agent operating contract
    files, `docs/at-tdd/process.md`, `docs/collaboration/definition-of-done.md`,
    `docs/templates/work-plan.md`, `docs/collaboration/local-issue-planning.md`,
    both READMEs, and `scripts/check-contract-consistency.py`'s parity
    definitions.
- Explicitly out of scope:
  - Contract-file change governance itself (ADR 0006's separate-context
    Reviewer requirement for changes to the agent operating contract files).
    That is a distinct decision, not superseded here, and this very change is
    reviewed under it.
  - Any change to what counts as an accepted specification, an architecture
    boundary, or a dependency policy.
  - The Minor Fix Path and Preflight Validation mechanisms themselves (ADRs
    0012, 0013) — reused at a different granularity, not redesigned.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write the superseding ADR | Specifier | Architecture Path | States the new rule precisely: self-review within an issue, work-plan-level Reviewer, combined human checkpoint | read-through against the Direction above |
| 2 | Propagate into every normative document and all nine contract files | Implementer | Architecture Path | No document states the superseded per-phase Reviewer rule as current; every document states the new one consistently | `scripts/check-contract-consistency.py`; targeted `grep` sweep |
| 3 | Update templates (`work-plan.md`) and planning docs to carry the work-plan-level review and closing checkpoint | Implementer | Architecture Path | The work-plan template has a place to record the AI review and the Director's combined closing action | read-through |
| 4 | Verify, record a trace, and submit for independent review under the *current* (pre-change) contract | Implementer | Architecture Path | A Reviewer in a separate context, using the process this change has not yet altered, approves | review record |

Sequencing and dependencies:

- Task 4 must use the model in force *before* this change, since a change
  cannot be validated by the rules it is in the process of replacing. This is
  the same bootstrapping discipline this repository has already followed for
  its own founding rewrite.

## Specifications

- None. This is a governance/process change; there is no application
  specification.

## Boundaries

- ADR 0006 (contract-file change control, requiring separate-context Reviewer
  approval for contract changes) is not altered or weakened by this change.
- The three constraints on any approval that still occurs in a separate
  context — context separation, deterministic precondition, falsification
  burden — are unchanged in substance for the Reviewer persona. Only the
  *layer* at which context separation is required changes: it no longer
  applies to the Implementer's self-review of its own phase transitions
  within an issue.
- Self-review must still satisfy the deterministic precondition and the
  falsification burden. Waiving context separation does not waive evidence.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does self-review drop all three Reviewer constraints, or only context separation? | Only context separation. Deterministic verification output and named failure scenarios remain required even in self-review. | Director, confirmed explicitly in dialogue |
| Are the post-completion review and the next-direction decision one action or two? | One. The Director reviews the completed, AI-approved work plan and states the next direction in the same turn. | Director, confirmed explicitly in dialogue |
| Does this change how contract-file changes themselves are reviewed? | No. ADR 0006 governs contract-file changes independently and is untouched. This very change is reviewed under ADR 0006, not under the model it introduces. | Planner, from reading ADR 0006's scope |
| What version number does this ship as? | Major — `v2.0.0`. It changes the meaning of a rule adopting projects rely on (ADR 0001's execution-loop shape), per `CHANGELOG.md`'s own versioning rule. | Planner, applying the existing versioning rule |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should work-plan size be bounded (e.g., a maximum issue count) to keep the self-review risk window small? | Evidence from running under this model — whether defects that reach work-plan-level review are proportional to plan size in practice |
| Should the Arbiter role change under this model? | Not currently — deferred until a dispute actually arises under work-plan-level review that the current Arbiter definition does not cover |

## Verification

- `scripts/check-contract-consistency.py` passing on the full contract set
  after propagation.
- A targeted `grep` sweep for the superseded phrasing ("Reviewer persona, in
  a separate context, before Phase 2 starts" and equivalents) across all
  updated documents, confirming none remain describing it as current.
- CI's repository-sanity steps reproduced locally.
- A copy-script smoke test into a fresh target, confirming the new model
  propagates correctly to an adopting project.
- Independent Reviewer approval, under the pre-change contract, in a separate
  context.

## Falsification Criteria

- Any of the nine contract files describes the superseded per-phase
  separate-context requirement as still current.
- The self-review layer is used to approve a contract-file change (which
  belongs to ADR 0006's separate-context requirement, not this change).
- The combined human checkpoint is documented as two separate gates rather
  than one.
- The tradeoff being accepted (delayed defect discovery in exchange for fewer
  review invocations) is not stated anywhere a future reader would find it.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation.

Recorded basis: a multi-turn dialogue in which the Director stated the model
piece by piece, the AI restated it back for confirmation at each step
(including a clarifying question about combining the two post-completion
checkpoints, resolved as "combine them"), and the Director confirmed with
"はい。進めて" after the full synthesis was presented.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
