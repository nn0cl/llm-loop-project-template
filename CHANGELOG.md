# Changelog

Editions of this template's operating contract. The contract is what adopting
projects install; this file records what changed in it and why.

Versioning: the major number changes when a rule an adopting project relies on
changes meaning. The minor number changes when rules are added without
invalidating existing ones. The patch number covers wording, examples, and
tooling that leave every rule intact.

## v1.1.0 — Independent review, and the rules it produced (2026-08-02)

Reviewed and approved by a Reviewer persona in a separate context, on a
different model, after six rounds. Review records:
`docs/collaboration/reviews/2026-08-02-mirror-parity-and-v101-review.md`,
`2026-08-02-mirror-parity-review-2.md`,
`2026-08-02-contract-consistency-review.md` through `-review-6.md`.

Two rules were added and five defects fixed. `v1.0.1` was drafted for the fixes
alone but never tagged, and no commit isolates them, so they shipped inside
`v1.1.0` rather than as a release of their own.

The consistency checker below went through six review rounds before approval —
four of its own rejections were the checker claiming a check it did not
actually have, the shape ADR 0013 warns a passing Preflight can hide. Its
`ENTRY_DOCUMENT_ADR_STATEMENTS` design and its documented "What this cannot
check, and who does" section are the direct result of that process, not
initial design choices.

### New rules

- **Preflight Validation** (ADR 0013). A deterministic submission check between
  Implementer completion and independent review, recording `pass` or `fail`
  with command output. A `pass` permits submission only — it is not an approval
  and cannot close anything. The producer of a Preflight cannot review the same
  change.
- **Minor Fix Path and the review-finding lifecycle** (ADR 0012). Actionable
  review findings become `docs/issues/LISS-*.md` entries with
  `proposed -> accepted -> in_progress -> resolved -> closed`; `wont_do`
  requires a grounded Arbiter record. Size-`S`, one-attempt corrections that
  change no specification or boundary get a proportionate path that still
  requires deterministic verification and separate Reviewer confirmation.

Adopting projects now number their own ADRs from `0014` up.

### Contract consistency is now checked, not audited

Three review rounds found the same defect class: a rule reaching some contract
files and not others, with every link intact and CI green. Each was caught by a
hand-built comparison that had to be rebuilt from scratch every round.

`scripts/check-contract-consistency.py` makes that comparison a command, and CI
runs it. It checks mirror parity against `AGENTS.md`, that no `AGENTS.md`
section is left unclassified as mirrored or deliberately not, that every
relative path a current document names resolves, that stated process-ADR ranges
match the ADR files, and that no document claims a released version with no tag
behind it.

On its first run it found three further defects: the review-record directory
was named in one of nine contract files, and `copilot-instructions.md` had no
Prime Directive at all. Both are fixed.

### Mirror parity

The two rules above landed in `AGENTS.md` and `CLAUDE.md` only. An agent
running under Copilot, Grok, or Cursor would not have known Preflight was
mandatory. Both rules are now in all nine contract files, as ADR 0006
requires. `README.md` and both QUICKSTART files still described an
eleven-ADR set and told adopting projects to number from `0012` — the range
the template had just taken for itself.

### Reviewer rejection fixes


The first edition was reviewed by a Reviewer persona in a separate context, on
a different model, and **rejected**. Five defects, all reproduced
independently before being fixed. No rule changed meaning; the mirrors were
brought into agreement and the tooling was corrected.

- **CI rejected the Reviewer's own output.** The traceability gate's `case`
  pattern `docs/collaboration/*.md` also matched nested record directories,
  because `*` matches `/` in a shell `case` glob. A pull request containing
  only a review record was classified as a contract change with no
  accompanying trace, and failed. The Reviewer persona's single deliverable
  was therefore unlandable. Record directories are now matched before the
  contract pattern, and
  `docs/collaboration/prompt-instruction-change-control.md` names all three of
  them as records rather than only `traces/`.
- `AGENTS.md` did not point to `external-resource-adoption-contract.md`,
  `ai-failure-recovery.md`, or `runner-cli-contract.md`. Only `CLAUDE.md` did.
- `.github/copilot-instructions.md` had no reopening-trigger list, which every
  other contract file carries.
- `CLAUDE.md`'s `Selected Stack` section used a placeholder whose wording the
  copy script never substituted and CI's smoke test never checked, so it
  shipped unfilled while CI reported the target clean. The placeholder now
  matches, and the smoke test's check is case-insensitive.
- `CHANGELOG.md` was not asserted by CI's `required_files`.

The review record is at
`docs/collaboration/reviews/2026-08-02-contract-first-edition-review.md`.

## v1.0.0 — First edition (2026-08-02)

The first edition an adopting project can install and cite by version. It is
also the first edition of a **Director-centered** contract: earlier states of
this repository were built around a human standing inside the execution loop,
and that model is no longer what the template ships.

The `v0.0.1`–`v0.1.1` tags predate this. They mark development snapshots of
the human-approval contract, not editions of the one described here, and no
migration path from them is offered — a project on one of those tags is
running a different contract.

### The contract

- **One human gate.** The design agreement, reached before the loop starts and
  recorded under `docs/collaboration/agreements/`. Nothing else stops for a
  human.
- **AI approval inside the loop**, issued by the Reviewer persona under three
  constraints that make self-approval mean something: context separation, a
  deterministic-verification precondition, and a falsification burden.
- **Five personas** with admissible inputs and required outputs — Planner,
  Specifier, Implementer, Reviewer, Arbiter — plus a rule for adding
  task-specific ones.
- **Three invariants** that hold in every phase: every decision produces a
  document, every executed fact leaves evidence, every claim states its
  grounds.
- **Three record directories**: agreements, reviews, traces.

### ADRs

The set was renumbered as a first edition. `0001` is now the governing
decision; `0002`–`0011` operate under it. Two ADRs were retired: the
superseded human-approval governance model, and a role rename whose terms no
longer appear anywhere in the contract. Adopting projects number their own
decisions from `0012` up.

Records of the retired decisions remain in git history.

### Repository state

The local issues, work plans, traces, review records, and sample spec
accumulated while building the template were cleared, so the repository
presents the same initial state an adopting project starts from. The
`.collaboration-template-version` marker now also records the template edition
alongside the commit ref.
