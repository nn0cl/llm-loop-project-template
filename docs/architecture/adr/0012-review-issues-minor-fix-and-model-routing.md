# ADR 0012: Review Issues, Minor Fix Path, and Capability-Based Model Routing

## Status

Accepted. Covered by `DA-2026-08-02-04`.

## Context

Review records currently describe findings, but the contract does not require
each actionable finding to have its own durable status and evidence. Small
corrections therefore risk receiving either too little traceability or the full
cost of a feature path. The existing routing documents define capability
classes but do not map them to the review-finding lifecycle.

## Decision

1. Store each actionable review finding as a `docs/issues/LISS-*.md` entry with
   `Type: review-finding` and a link to the originating review record.
2. Use this lifecycle: `proposed -> accepted -> in_progress -> resolved ->
   closed`. A disputed finding may move from `accepted` to `wont_do` only with
   an Arbiter decision record containing grounds and rejected alternatives.
3. A resolved finding requires changed files and deterministic verification.
   Only a separate Reviewer context may move it to `closed`.
4. Add Minor Fix Path for one-attempt, size-S corrections that preserve the
   accepted specification and all named boundaries. It requires a compact
   design note, deterministic verification, and separate Reviewer confirmation.
5. Route by capability class: deterministic tools for mechanical facts and
   verification; lightweight reasoning or code assistants for extraction,
   classification, and narrow corrections; strong reasoning agents for
   architecture, ambiguity, privacy, and Arbiter decisions.
6. Record the displayed model/reasoning setting and compatibility state when
   routing is non-default or materially affects safety. Concrete model/vendor
   selection remains a later ADR.

## Consequences

Positive:

- Review findings remain actionable, traceable, and auditable.
- Small corrections receive proportionate process and model cost.
- Disagreement becomes a recorded decision rather than silent dismissal.

Negative:

- The issue ledger gains a lifecycle and more synchronization fields.
- Minor Fix Path still requires independent review and deterministic evidence.

## Enforcement

Code review should reject:

- actionable review findings that exist only in prose or a session transcript.
- `wont_do` without an Arbiter record and grounds.
- Minor Fix Path work that changes an accepted specification or architecture boundary.
- routing claims that omit the capability class, compatibility state, or escalation reason when applicable.
