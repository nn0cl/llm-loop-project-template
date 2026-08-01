# ADR 0013: Preflight Validation Before Independent Review

## Status

Accepted. Covered by `DA-2026-08-02-05`.

## Context

Independent review is intentionally expensive because it requires a fresh
context, artifact reconstruction, deterministic evidence, and named
falsification scenarios. Many failures found there are mechanical: missing
links, inconsistent status fields, absent verification output, or scope drift.
The process needs a cheaper submission check without weakening independent
review.

## Decision

1. Add a Preflight Validation step between Implementer completion and
   independent Reviewer review.
2. Run deterministic checks first. A lightweight reasoning model may assist
   with checklist and document-consistency checks after those signals exist.
3. Record `pass` or `fail`, each check, command/output evidence, scope result,
   routing/compatibility state, and the next action.
4. On `fail`, return to the Implementer and do not issue Reviewer approval.
   Re-run Preflight after correction.
5. On `pass`, submit to an independent Reviewer. Preflight is not an approval
   and cannot establish specification conformance, `wont_do`, or `closed`.
6. The Preflight producer cannot approve the same change as Reviewer.

## Consequences

Positive:

- Mechanical defects are caught with less reasoning and review cost.
- Reviewer context is reserved for semantic falsification and boundary judgment.
- The handoff contains a compact, repeatable evidence bundle.

Negative:

- The process gains another artifact and one more possible loop.
- A weak checklist can create false confidence, so independent review remains mandatory.

## Enforcement

Code review should reject:

- a Preflight `pass` used as a substitute for independent review.
- a Preflight `fail` with no named failed check or corrective next action.
- lightweight-model output treated as final approval or an Arbiter decision.
- a review record that omits the Preflight evidence when the path requires it.
