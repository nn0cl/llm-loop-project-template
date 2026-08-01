# Design Agreement: Dangling Reference Cleanup

## Identity

- Agreement ID: DA-2026-08-02-02
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none. Settles Deferred Question 1 of
  DA-2026-08-02-01, whose Reopening Log records the handover.

## Direction

The Director's instruction, in the Director's terms: remove the references to
`docs/research/`, and tidy dangling references generally.

## Scope

- In scope:
  - The one remaining live reference to the deleted rationale essay
    directory, in ADR 0012.
  - A repository-wide audit for dangling relative references and dangling
    heading anchors in documents that are read as current guidance.
  - Statements in current documents that point at a mechanism the repository
    no longer has, which are dangling references in substance even though no
    path is broken.
- Explicitly out of scope:
  - Historical records under `docs/collaboration/traces/`,
    `docs/collaboration/reviews/`, `docs/issues/`, and `docs/work-plans/`.
    They record what was true when written; editing them to match today would
    falsify the record. This continues the Director's decision in the
    2026-08-02 rewrite session.
  - The body text of accepted ADRs. Where an ADR is no longer normative, its
    Status says so; the decision itself is not rewritten.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Remove the deleted-directory reference from ADR 0012 and state why it is gone | Specifier | Architecture Path | No live document names the deleted directory; the reason and its trace are recorded in ADR 0012 | repository-wide `grep`, filtered to exclude historical records |
| 2 | Mark ADR 0003 and ADR 0012 as superseded, and index 0012/0013 in the architecture README | Specifier | Architecture Path | A reader landing on either ADR is told which decision is in force; the index lists every ADR | read-through; ADR existence check |
| 3 | Audit every current document for dangling relative references and dangling anchors | Specifier | Architecture Path | Zero unexplained dangling references; any remaining hit is a documented false positive | link checker and anchor checker over all documents |
| 4 | Correct current statements that describe a mechanism the repository no longer has | Specifier | Architecture Path | No current document asserts the `@AGENTS.md` import that was dropped on 2026-07-25 | `grep` for `@AGENTS.md` outside historical records |

Sequencing and dependencies:

- Task 3 finds what tasks 1, 2, and 4 fix. It ran first and ran again after.

## Specifications

Specification files this agreement covers:

- None. The operating contract documents are the artifacts under change.

## Boundaries

- No ADR decision text is rewritten; only Status and References change.
- No historical record is edited.
- No change to the model ADR 0013 defines.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Does "remove the references" mean scrubbing the path from records too? | No. Current documents lose the reference; dated records keep it, because a record of a deletion that cannot name what was deleted is not a record. | Planner, extending the Director's earlier decision on historical records |
| Should ADR 0012's note name the deleted path? | No. The instruction was to remove references to it; the note states that a rationale essay directory was deleted and cites the trace, without reintroducing the path. | Director's instruction, read literally |
| Are the `../docs/architecture/*.md` paths in `docs/templates/examples/` broken? | No. Those files are example content to be placed inside a target project, where the paths resolve. They are false positives of the checker, not defects. | Planner, from the files' own stated purpose |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether a dangling-reference check should run in CI rather than being re-derived by hand each time | A Director decision on whether to add a script to the distributed template, which changes what every adopting project receives |
| Whether ADR 0006's body should be revised where it describes Adjudicator review, or left as a layered record with its 2026-07-25 revisit | The next change to the prompt/instruction change-control rule itself |

## Verification

- A link checker over every `.md`, `.mdc`, `.sh`, `.yml`, and `.py` file,
  resolving markdown links and backticked paths against the working tree.
- An anchor checker resolving every `#fragment` against the target's headings.
- `grep` for the deleted directory, for `@AGENTS.md`, and for `Referee`,
  filtered to exclude historical records.
- The CI repository-sanity steps, reproduced locally.

## Falsification Criteria

- A reader following a link in a current document lands on nothing.
- A reader landing on ADR 0003 or ADR 0012 believes it is in force.
- A current document describes a mechanism the repository does not have.
- A historical record was edited to look consistent with today.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without further
      interpretation. Nothing in them requires guessing at a rule that was
      never stated.

Recorded basis: the Director's instruction in the 2026-08-02 session, given
after PR #2 merged. The instruction was two sentences; the decomposition above
is the Planner's. The Director settled the `docs/research/` question directly.
The scope boundary excluding historical records is carried from the Director's
earlier decision, not restated by the Director in this instruction — it is the
item a later objection would reopen.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
