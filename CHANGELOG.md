# Changelog

Editions of this template's operating contract. The contract is what adopting
projects install; this file records what changed in it and why.

Versioning: the major number changes when a rule an adopting project relies on
changes meaning. The minor number changes when rules are added without
invalidating existing ones. The patch number covers wording, examples, and
tooling that leave every rule intact.

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
