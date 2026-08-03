# ADR 0015: Review Cost Discipline

## Status

Accepted, following correction. This ADR originally merged (as part of pull
request #11, tag `v2.1.0`) on a Director instruction to skip independent
Reviewer approval for that one change. A retroactive fresh-context review
(`docs/collaboration/reviews/2026-08-03-review-cost-discipline-review.md`)
rejected that as invalid: no provision in this contract grants the Director
authority to waive ADR 0006's separate-context Reviewer requirement, and
disclosing the skip openly — which the original version of this section did
— is not the same thing as having authority to make it. That gap is now
closed directly in
`docs/collaboration/prompt-instruction-change-control.md`: no Director
instruction waives the separate-context requirement, and this incident is
not precedent for a future one. This ADR's content (rules 1-4 below) was
resubmitted for genuine independent review under
`docs/collaboration/agreements/2026-08-03-review-cost-discipline-correction.md`
(DA-2026-08-03-03) before being treated as Accepted.

## Context

Measured from this repository's own session history: self-authored process
records (design agreements, traces, Preflight records) totaled roughly 3,200
lines against roughly 4,000 lines of actual contract/tooling content — near
parity between the record and what it records. Independent-context Reviewer
records added another ~4,700 lines. `docs/collaboration/llm-cost-reduction.md`
already names the pattern as a warning sign ("many traces say Architecture
Path for small edits") and already asks for short entries; neither was
followed in practice.

Two distinct, compounding causes were found:

1. **No proportional format existed for self-review or for answering a
   specific Reviewer finding.** In their absence, every record defaulted to
   the heaviest available template (the Preflight/review-record shape:
   Command Output, Scope Result, Routing and Compatibility), regardless of
   how small the actual change was. A one-line citation fix received a
   97-line Preflight record.
2. **Multi-round independent review resumed the same Reviewer agent
   identity across rounds** rather than spawning a fresh, narrowly-scoped
   review each time. Confirmed directly: round-6 review records in this
   repository's history refer to "my own round-5 rejection" as the same
   reviewing identity's memory, not a fresh assessment. This does not
   violate context separation from the *producer* — the Reviewer never saw
   the Implementer's reasoning — but it means the Reviewer's own context
   grew every round, compounding the cost of each subsequent round on top of
   the last.

## Decision

1. **Self-review and a fix answering one named Reviewer finding use
   `docs/templates/self-review.md`'s short form by default.** The short form
   bounds the *record*, not the *search*: the Implementer looks for what a
   separate-context Reviewer would look for, because the work-plan-level
   Reviewer sees this issue once, at the work plan's close, not at this
   phase transition. What is recorded is every failure mode the search
   actually found, each with why it does not occur — one line each when the
   search found one, more lines when it found more. Escalate to the full
   form (`review-record.md`'s shape, filled out as the Implementer) at
   planning size `M` or larger, or when risk is not obvious from the diff.
2. **A response to a specific Reviewer finding does not restate the whole
   change.** It names the finding it answers, reproduces the original defect,
   shows the fix, and stops there. It does not re-derive Scope, Routing, or a
   full verification narrative already covered by the original submission.
3. **When independent review needs more than one round, spawn a fresh
   review invocation by default rather than resuming the prior round's
   session.** Give it only: the specific finding(s) from the prior round, the
   diff since then, and how to reproduce and verify the fix — not the full
   prior transcript. State explicitly when a fresh context is deliberately
   skipped because the change is too intertwined to review incrementally;
   that is a judgment call to name, not a default.
4. `docs/collaboration/llm-cost-reduction.md`'s "keep entries short" guidance
   applies to self-review and Preflight records with the same force it
   already has for trace entries. A record padded with full-weight
   boilerplate for a small change is itself a warning sign under that
   document's existing "Warning Signs" section — this ADR does not add a new
   category, it makes an existing one apply where it was being skipped.

This ADR does not change any approval's constraints. Self-review still
requires the deterministic precondition and the falsification burden;
Reviewer approval still requires all three, in a separate context, over the
whole work plan. It changes how much is written to satisfy them, and how
much context a repeat reviewer round carries forward.

## Consequences

Positive:

- Records proportional to what they document; a size-S fix costs roughly
  what a size-S fix should cost, at both the self-authored and the
  independent-review layer.
- Multi-round review cost grows closer to linearly with round count instead
  of compounding, since each round's reviewer starts from a bounded, scoped
  context instead of the full prior transcript.
- Existing guidance (`llm-cost-reduction.md`) gains actual enforcement
  instead of being available but unused.

Negative:

- A fresh-context reviewer each round has less continuity; an ambiguous
  finding may need to be re-explained rather than simply remembered.
- The boundary between "the change is small enough for the short form" and
  "it needs the full form" is a judgment call, not mechanically checked —
  the same shape of risk this repository's own consistency checker
  eventually gave up trying to resolve by regex for ADR ranges, and disclosed
  instead of chasing.
- This ADR's first merge shipped without independent review, on a Director
  instruction the contract grants no authority to give. That is not a
  disclosed trade-off this ADR chose; it was a boundary violation, found by a
  retroactive review and corrected afterward (see Status). It is named here
  as a negative consequence of the original decision, not as an accepted
  cost of the design.

## Enforcement

Code review (a future Reviewer persona, or the Director) should reject:

- a self-review or finding-response record with Scope Result, Routing and
  Compatibility, or other independent-review-sized sections for a
  planning-size-`S` change.
- a multi-round review response that restates verification already covered
  by an earlier round's record, instead of pointing to it.
- a second or later review round that resumes a prior reviewing session's
  full transcript without stating why a fresh, scoped context would not have
  worked.
- a contract-file change merged on a Director instruction to skip the
  separate-context Reviewer requirement. No such instruction is a valid
  substitute for that approval; see
  `docs/collaboration/prompt-instruction-change-control.md`.
