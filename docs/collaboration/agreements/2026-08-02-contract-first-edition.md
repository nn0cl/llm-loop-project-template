# Design Agreement: Contract First Edition

## Identity

- Agreement ID: DA-2026-08-02-03
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none. The two earlier agreements of
  2026-08-02 were cleared in the record reset; their decisions are in git
  history and in the contract they produced.

## Direction

The Director's instruction: tidy the contract, in order to make this state the
first edition.

Asked how deep the tidying should go, the Director selected the deepest of
four options: consistency and deduplication across the contract set, removal
of the archaeological references in the ADR bodies, **and** renumbering the
ADRs into a fresh `0001..N` first-edition set — with a version declared.

## Scope

- In scope:
  - The nine agent operating contract files and the normative documents under
    `docs/collaboration/`, `docs/architecture/`, and `docs/at-tdd/`.
  - The ADR set: renumbering, retiring decisions that no longer bind, and
    removing citations to records that no longer exist.
  - A version declaration: `CHANGELOG.md`, the README banners, and the
    template version marker.
- Explicitly out of scope:
  - The model itself. This edition freezes what ADR 0001 already decided; it
    does not revise it.
  - The `docs/templates/examples/` example files, whose relative paths resolve
    inside a target project rather than here.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Renumber the ADRs into a first-edition set, retiring those that no longer bind | Specifier | Architecture Path | Every filename matches its title; no reference anywhere points at a retired or old number | filename/title check; repository-wide `grep` for old numbers |
| 2 | Remove archaeology from ADR bodies and normative documents | Specifier | Architecture Path | No citation to a record that does not exist; no retired role name | `grep` for `LISS-`, `Adjudicator`, `Referee`, excluding the `LISS-0000` ID format |
| 3 | Bring the contract files into effective-content agreement | Specifier | Architecture Path | No contract file states a rule another one lacks; every file names the product and stack | per-file parity matrix; copy smoke test asserting placeholder fill in the target |
| 4 | Declare the edition | Specifier | Architecture Path | A reader can tell which edition they installed, from the repository and from the target marker | `CHANGELOG.md` present; marker output inspected in a smoke-test target |

Sequencing and dependencies:

- Task 1 changes the numbers task 2 edits around; it runs first.
- Task 4 depends on nothing and lands last, so the edition describes the final
  state.

## Specifications

- None. The contract documents are the artifacts under change.

## Boundaries

- No rule changes meaning in this edition. A change that would alter what ADR
  0001 decided reopens this agreement.
- Retired ADRs are deleted, not rewritten; their content stays in git history.
- No new state is introduced that duplicates git — the edition in the version
  marker is derived from tags.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| How deep does "tidy" go? | Renumber the ADRs, not merely mark statuses. | Director, by explicit selection |
| Does ADR 0001 become the governing decision's number? | Yes. A first edition should open with the decision every other ADR operates under. | Planner; the Director chose renumbering without specifying an order |
| Do the retired ADRs stay as files marked superseded? | No. They are deleted; git history holds them. Keeping a superseded decision in a first edition invites an agent to follow it. | Planner |
| Why v1.0.0 when v0.x tags exist? | Those tags mark development snapshots of the human-approval contract. They are not earlier editions of this one, and no migration is offered. | Planner |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether the dangling-reference audit becomes a CI step, which would add a script to the distribution | A Director decision about what adopting projects receive |
| Whether `CLAUDE.md` should be shortened toward the 200-line adherence guidance ADR 0006 cites | Evidence that length, not content, is what costs adherence in practice |

## Verification

- Filename/title agreement across the ADR set.
- Repository-wide `grep` for retired ADR numbers, `LISS-` citations, and the
  retired role names.
- A per-file parity matrix over the nine contract files.
- Link and anchor audits over every document.
- The CI repository-sanity steps, reproduced locally, including a copy smoke
  test that inspects the placeholder fill and the version marker in the
  target.

## Falsification Criteria

- An agent reading any single contract file follows a rule the others do not
  state.
- A reference points at an ADR number that no longer exists.
- An adopting project cannot tell which edition it installed.
- A retired decision is still readable as if it were in force.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without further
      interpretation.

Recorded basis: the Director's instruction plus an explicit selection among
four scopes. The ADR ordering and the deletion-versus-marking choice were the
Planner's, made inside the scope the Director selected.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
