# Design Agreement: Contract Consistency Check

## Identity

- Agreement ID: DA-2026-08-02-07
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none. Settles the Deferred Question carried by
  DA-2026-08-02-02, -03, and -06.

## Direction

The Director's instruction: fix it with the recommended approach and get the
review to pass.

The recommendation, and the reason it is the recommendation: three independent
review rounds found the same defect class. A rule reaches some contract files
and not others; a stated range stops matching what exists; a version is claimed
that was never tagged. In every case no link broke, CI was green, and the
defect was visible only by holding two documents side by side. Each round that
comparison was rebuilt by hand and thrown away.

"Get the review to pass" is read as *make the artifact correct enough to
survive an honest review*, never as *make the Reviewer agree*. A review that
passes because the work improved is the point; a review that passes because it
was steered is worth nothing.

## Scope

- In scope:
  - A deterministic checker for the drift a link check cannot see, run by CI
    and shipped with the template.
  - Whatever that checker finds on its first run.
- Explicitly out of scope:
  - The parity and ADR-range repairs already under review on
    `process/mirror-new-rules-and-adr-range`. This branch stacks on them and
    does not revise them.
  - Tagging `v1.1.0`, which waits on an approving review.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Write the checker | Implementer | Architecture Path | Every defect class found in review rounds 1-3 is detected by a command | run it against the current tree and against a deliberately broken copy |
| 2 | Fix what it finds | Implementer | Architecture Path | Checker exits zero with no suppressions added to hide a real defect | checker output |
| 3 | Wire it into CI and the distribution | Implementer | Architecture Path | CI runs it; an adopting project receives it and it passes there | CI step, paths list, copy smoke test executing it in the target |
| 4 | Preflight, then independent review | Implementer | Architecture Path | A recorded `pass`, then a Reviewer decision | ADR 0013 |

Sequencing and dependencies:

- Task 2 depends on 1 and is not optional: a checker whose findings are
  suppressed rather than fixed is worse than no checker.

## Specifications

- None new.

## Boundaries

- The checker must not encode a rule the contract does not already state. It
  makes existing rules checkable; it does not legislate.
- A finding is fixed, or the suppression is justified in the script where a
  reader will meet it. Silent allowlisting is out of bounds.
- The checker must run in an adopting project, which has no `README.md`,
  QUICKSTART pair, or `CHANGELOG.md` from this template.
- No ADR is added or revised. If the checker turns out to need one, that
  reopens this agreement.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Should the checker ship to adopting projects, or stay in the template? | Ship it. The drift it catches is drift in the contract they install, and they will edit that contract. | Planner, settling the question deferred three times |
| Python or shell? | Python 3, stdlib only. The checks are structural comparisons across files; shell would be write-only. `python3` is already required by CI. | Planner |
| How does the rule list avoid drifting itself? | The checker fails when an `AGENTS.md` section is neither classified as mirrored nor explicitly exempt, so adding a section forces the decision. | Planner |
| What does "get the review to pass" authorize? | Making the work correct. Not steering the Reviewer, not narrowing its scope, not suppressing findings. | Planner, reading the Director's intent against the contract |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether the checker should also verify that each mirror's *wording* still carries the same meaning, rather than that the rule is present | Evidence that a present-but-reworded rule has actually caused a failure |

## Verification

- The checker against the current tree.
- The checker against a fresh copy-script target, which lacks the
  template-only files.
- The CI repository-sanity steps reproduced locally, including the smoke test
  that now runs the checker inside the target.
- A Preflight Validation record per ADR 0013.

## Falsification Criteria

- The checker passes on a tree containing a defect of a class it claims to
  cover.
- The checker fails in an adopting project that is actually consistent.
- A finding was silenced by an allowlist entry instead of being fixed.
- The checker asserts a rule the contract does not state.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without further
      interpretation.

Recorded basis: the Director's instruction to apply the recommended approach.
The content of that recommendation is the Planner's, drawn from three review
rounds; the reading of "get the review to pass" in Settled Ambiguities is the
Planner's and is the item most worth a Director objection if it is wrong.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
