# ADR 0003: AI-Human Collaboration Governance

## Status

Accepted; governance model superseded by ADR 0013
(Director-Centered Planning and an AI-Closed Execution Loop) on 2026-08-02.

This ADR is no longer normative. It stays in the record because it states the
human-intervention model this project exists to test — the decision under
falsification, not a decision an agent should follow. Read the rest of this
document as the baseline, and
`docs/architecture/adr/0013-director-centered-planning-and-closed-loop.md`
as the rule in force.

## Context

The repository is intended for AI-TDD plus human collaboration. Other
documents define AT-TDD phases, payload routing, and input/output/reasoning
contracts. The missing layer is collaboration governance: who approves phase
transitions, what artifacts must exist, how agents hand off work, and when they
must stop for human decision.

This ADR intentionally does not decide application internals.

## Decision

Adopt a Adjudicator-centered collaboration scheme.

The human Adjudicator owns:

- phase transition approval.
- ADR acceptance.
- review of Phase 1 tests before implementation.
- decisions for ambiguous architecture, product, provider, schema, and privacy
  choices.

Agents own:

- design intake.
- minimal context selection.
- phase-correct artifact generation.
- visible assumptions and open decisions.
- deterministic verification where possible.
- handoff notes when work stops before completion.

Use the collaboration templates under `docs/templates/` for design intake,
handoff, and Adjudicator review.

## Consequences

Positive:

- Work can be resumed by another agent without guessing hidden state.
- Human review is focused on decision points instead of every token of output.
- Phase transitions become explicit and auditable.
- AI-generated artifacts remain subordinate to Adjudicator decisions and ADRs.

Negative:

- Adds lightweight process overhead before coding.
- Requires discipline to avoid treating templates as paperwork instead of
  review aids.

## Enforcement

Code review should reject:

- phase transitions without Adjudicator approval.
- Phase 2 implementation based on unreviewed Phase 1 tests.
- tasks without design intake or context ledger.
- handoffs that omit current phase, changed files, verification status, or next
  safe action.
- architectural decisions made only in chat without ADR or Adjudicator approval.
