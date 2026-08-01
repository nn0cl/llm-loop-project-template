# Design Agreement: Post-Rewrite Documentation Consistency

## Identity

- Agreement ID: DA-2026-08-02-01
- Date: 2026-08-02
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Opus 5 via Claude
  Code
- Supersedes agreement (if any): none. This is the first design agreement
  recorded under the mechanism introduced by ADR 0013.

## Direction

The Director's instruction, in the Director's terms: after merging the
Director-centered rewrite, update the READMEs for `llm-loop-project-template`
and check the adoption scripts, QUICKSTART, and related documents for anything
the rewrite left inconsistent.

The rewrite changed the operating model but was verified for *residual*
references (`Adjudicator`, `docs/research`). It was not verified for
*missing* ones: places where the new model needs a location, a count, or a
term that no document supplies. This agreement covers closing that gap.

## Scope

- In scope:
  - `README.md`, `README.ja.md`, `QUICKSTART.md`, `QUICKSTART.ja.md`.
  - The adoption path: `scripts/init-llm-context.sh`,
    `docs/templates/examples/adoption-prompts.md`.
  - Naming a storage location for Reviewer decisions, which the rewrite left
    undefined, and distributing that directory to adopting projects.
  - `.github/workflows/ci.yml` assertions for anything newly distributed.
- Explicitly out of scope:
  - Accepted ADRs 0001-0012 and the historical records under
    `docs/collaboration/traces/`, `docs/collaboration/reviews/`,
    `docs/issues/`, and `docs/work-plans/`. Their `Adjudicator` and `Referee`
    wording is a fact about when they were written.
  - Any change to the model ADR 0013 defines. This is a consistency pass, not
    a revision.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Give Reviewer decisions a distributed home at `docs/collaboration/reviews/` and name it in the normative documents | Specifier | Architecture Path | `personas.md`, `ai-human-scheme.md`, `definition-of-done.md`, and `review-record.md` all name the same path; the directory ships with a `.gitkeep` and no historical `*.md` | CI `required_files` entry; copy smoke test asserting the `.gitkeep` is present and no `*.md` is copied |
| 2 | Replace the stale `Referee` term in both QUICKSTART files | Specifier | Architecture Path | No `Referee` outside historical records | repository-wide `grep -i referee` |
| 3 | Correct the process-ADR range from 0001-0011 to 0001-0013 wherever it is stated as guidance | Specifier | Architecture Path | README and both QUICKSTART files state 0001-0013 and start project ADRs at 0014 | `grep` for `0001-0011` / `0001〜0011` outside historical records |
| 4 | Route the adoption path through the design agreement and the persona definitions | Specifier | Architecture Path | The adoption prompts and the generated setup prompt name the agreement location, the persona definitions, and the review-record location | local run of `scripts/init-llm-context.sh`; read-through of the changed prompts |

Sequencing and dependencies:

- Task 1 settles the path that tasks 2-4 cite. It runs first.
- Every task is documentation or configuration. None of them has a Red phase;
  the whole change is Architecture Path.

## Specifications

Specification files this agreement covers:

- None. This repository ships no application specification; the operating
  contract documents are the artifacts under change.

## Boundaries

- The model defined by ADR 0013 is not revised here. A change that would alter
  it reopens this agreement.
- Historical records are not rewritten to match current terminology.
- No file is added to the distribution without a matching CI assertion.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Where do Reviewer decisions live? | `docs/collaboration/reviews/`, the directory that already held the one historical review record. Excluded from copies as target-owned history, distributed as an empty `.gitkeep`, exactly like `agreements/` and `traces/`. | Planner, on the existing directory layout; not contradicted by the Director |
| Should the historical `Adjudicator`/`Referee` wording in ADRs, traces, issues, and work plans be rewritten? | No. Rewriting them would falsify the record of what was decided when. | Director, in the preceding session |
| Does the adoption flow need the Director after the rewrite? | Yes. Adoption happens in the design phase, before any closed loop exists, so the Director is present throughout it — this is not a reintroduced deliverable gate. | Planner, from ADR 0013 |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Whether ADR 0012 should be superseded rather than left with a link to the deleted `docs/research/` file | The next time an ADR in this repository is amended for any reason, or a Director decision to supersede it |
| Whether the Reviewer must run on a different model from the Implementer | A first execution loop producing enough review records to show whether same-model review misses what cross-model review catches |

## Verification

- `bash -n` on all four shell scripts.
- Existence check over every entry of the CI `required_files` list.
- ADR existence check for `0001`-`0013`.
- Local run of the CI template-copy smoke test, including the new
  `docs/collaboration/reviews/` assertions.
- Local run of `scripts/init-llm-context.sh` against a copied target.
- `grep -rIn -i 'referee'` and `grep -rIn '0001-0011'` outside historical
  records.

## Falsification Criteria

- A reader following the documents cannot tell where a Reviewer decision is
  written down. That is the defect this change exists to remove; if it
  survives, the change failed.
- An adopting project receives a `reviews/` directory that carries this
  repository's own history into it.
- Any statement of the process-ADR range disagrees with what
  `docs/architecture/adr/` actually contains.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones.
- [x] **AI**: this plan and these specifications are executable without further
      interpretation. Nothing in them requires guessing at a rule that was
      never stated.

Recorded basis: the Director's instruction in the 2026-08-02 session, given
after reviewing the merge of the Director-centered rewrite. The Director's
statement was scope-level ("update the READMEs for this project, and the
adoption scripts and QUICKSTART need checking"); the task decomposition above
is the Planner's, and the Director did not contest it. The review-record
location in Settled Ambiguities was decided by the Planner from the existing
layout rather than stated by the Director — it is the one item here that a
later Director objection would reopen.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
