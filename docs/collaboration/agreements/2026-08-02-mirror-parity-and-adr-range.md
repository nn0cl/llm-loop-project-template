# Design Agreement: Mirror Parity and ADR Range

## Identity

- Agreement ID: DA-2026-08-02-06
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none. Follows DA-2026-08-02-04 and -05, whose
  changes this one brings into contract-wide parity.

## Direction

The Director's instruction: check the latest state and carry out the
continuation.

The state had moved while an independent review was running. Two ADRs
(`0012` review findings and Minor Fix Path, `0013` Preflight Validation) landed
on `main` from work outside this session, along with their agreements, specs,
issues, review records, and traces. This agreement covers the audit of that
state and the repair of what the audit found.

## Scope

- In scope:
  - Contract-file parity for the two rules added by DA-2026-08-02-04 and -05.
  - Statements of the process-ADR range in the entry documents.
  - The changelog entry for the shipped state.
- Explicitly out of scope:
  - The two new ADRs themselves. They are accepted decisions with their own
    agreements and review records; this agreement propagates them, it does not
    revise them.
  - The outstanding independent review of the `v1.0.1` fixes, which is a
    separate obligation this agreement does not discharge.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Mirror Minor Fix Path and Preflight Validation into the seven contract files that lack them | Implementer | Architecture Path | All nine contract files state both rules | per-file parity matrix |
| 2 | Correct the process-ADR range and the adopter's starting number | Implementer | Architecture Path | No document states a range that disagrees with `docs/architecture/adr/`, and adopters are told to start at `0014` | `grep` for the stale ranges; ADR existence loop |
| 3 | Record the shipped state in the changelog | Specifier | Architecture Path | One version section covers both the rejection fixes and the new rules, and says which tag shipped | read-through |
| 4 | Run Preflight Validation, then submit to an independent Reviewer | Implementer | Architecture Path | A recorded `pass` or `fail` with command output, and a submission | ADR 0013's required fields |

Sequencing and dependencies:

- Task 4 depends on 1-3. Per ADR 0013, its producer cannot review the change.

## Specifications

- None new. `docs/specs/preflight-validation.feature.md` and
  `docs/specs/review-issue-and-minor-fix-path.feature.md` describe the rules
  being propagated; this work does not change them.

## Boundaries

- The wording mirrored into the seven files is the wording already accepted in
  `AGENTS.md`. No rule is restated in a way that changes its meaning.
- No ADR is added, renumbered, or revised.
- The independent review obligation is not discharged by this work.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Is mirroring two rules across seven files a Minor Fix Path change? | No. It touches the contract set, so it is Architecture Path, and it needs an agreement, a trace, and independent review. | Planner, from `prompt-instruction-change-control.md` |
| Should adopters keep starting at `0012`? | No. The template now occupies `0012` and `0013`, so an adopter following the old instruction would collide on the next template update. Adopters start at `0014`. | Planner |
| Should `v1.0.1` be tagged retroactively? | No. It was never released and no commit contains only those fixes. Those fixes ship inside `v1.1.0`, which the changelog records as unreleased until an approving review lets it be tagged. | Planner |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether contract-file parity should be checked by CI rather than by hand each time | A Director decision on adding a checker to the distributed template |
| Whether the outstanding independent review of the `v1.0.1` fixes can be completed | Reviewer capacity; the previous attempt terminated on a session limit before reaching a decision |

## Verification

- A per-file parity matrix over the nine contract files for both new rules.
- `grep` for every stale ADR-range statement.
- ADR existence loop `0001`-`0013`.
- CI `required_files`, `bash -n`, conflict markers, copy smoke test, link and
  anchor audits.
- A Preflight Validation record per ADR 0013.

## Falsification Criteria

- An agent running under Copilot, Grok, or Cursor cannot learn from its own
  contract files that Preflight Validation is mandatory.
- An adopting project follows the documented numbering and collides with a
  template ADR.
- The changelog describes a version that was never released as if it were.
- Preflight `pass` is used as though it were an approval.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without further
      interpretation.

Recorded basis: the Director's instruction to check the latest state and
continue. The specific defects were found by audit, not named by the Director;
the decisions in Settled Ambiguities are the Planner's and are the items a
Director objection would reopen.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
