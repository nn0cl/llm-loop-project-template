# Changelog

Editions of this template's operating contract. The contract is what adopting
projects install; this file records what changed in it and why.

Versioning: the major number changes when a rule an adopting project relies on
changes meaning. The minor number changes when rules are added without
invalidating existing ones. The patch number covers wording, examples, and
tooling that leave every rule intact.

## v2.0.0 — Work-plan-scoped self-review and a combined human checkpoint (2026-08-03)

Reviewed and approved by a Reviewer persona in a separate context, on a
different model, across two rounds. Review records under
`docs/collaboration/reviews/`:
`2026-08-03-work-plan-scoped-governance-review.md` and
`2026-08-03-work-plan-scoped-governance-review-2.md`.

**Major**, because this changes the meaning of a rule adopting projects rely
on: `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`
supersedes ADR 0001's execution-loop provisions.

- **Self-review replaces per-phase, separate-context Reviewer approval
  inside a work plan.** Red-to-Green and Green-to-Refactor transitions are
  now validated by the Implementer, in the same context that did the work.
  Self-review still requires recorded deterministic verification output and
  named failure scenarios — only context separation is waived, and only at
  this layer.
- **The Reviewer now runs once per work plan**, in a separate context, over
  every issue's result together, after Preflight Validation passes — not
  once per phase per issue.
- **Closing a work plan is one combined Director action**, not two: read the
  Reviewer-approved result and state the next direction (or end the
  engagement) in the same turn. This is a new, mandatory human checkpoint;
  previously the Director had no required touchpoint after the initial
  design agreement.
- **Contract-file changes are unaffected.** ADR 0006 still requires a
  separate-context Reviewer for those, at any work-plan scope — this release
  was itself reviewed under that rule, not under the model it introduces.
- The process-ADR count moves from thirteen to fourteen; adopting projects
  now number their own decisions from `0015` up.
- `scripts/check-contract-consistency.py` gained three mirror rules for the
  new vocabulary (self-review, work-plan-level Reviewer, work-plan close).
  Its first full run on this change reported clean; several genuine gaps
  across seven documents were found only by a manual sweep the checker does
  not run — consistent with its own disclosure that a green run means "no
  mechanical drift found," not "the contract is consistent."

### The tradeoff, on the record

ADR 0014 and its covering design agreement name the risk this trades away
explicitly: this repository's own history is six review rounds against the
consistency checker, four of which found it claiming coverage it did not
have — findings the context that wrote it could not have made about itself.
Self-review does not remove that risk; it relocates it from "next phase
boundary" to "work-plan close," and the severity scales with how large a
work plan is allowed to get. Accepted in exchange for fewer separate-context
invocations and human involvement scoped to work-plan boundaries, not
overlooked.

## v1.1.0 — Independent review, and the rules it produced (2026-08-02)

Reviewed and approved by a Reviewer persona in a separate context, on a
different model, after six rounds. Review records under
`docs/collaboration/reviews/`: `2026-08-02-mirror-parity-and-v101-review.md`,
`2026-08-02-mirror-parity-review-2.md`, and
`2026-08-02-contract-consistency-review.md` through
`2026-08-02-contract-consistency-review-6.md`.

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
