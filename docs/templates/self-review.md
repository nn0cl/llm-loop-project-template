# Self-Review Template

Use this for the Implementer's own phase-transition review inside a work
plan (per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`)
and for a fix that answers a specific, already-named Reviewer finding (per
`docs/architecture/adr/0015-review-cost-discipline.md`). It carries the same
two constraints as any approval — a deterministic precondition and a
falsification burden — without context separation, which this layer waives.

**Not a substitute for the work-plan-level Reviewer's own record**
(`docs/templates/review-record.md`), which still requires all three
constraints, in a separate context.

## Short form — planning size `S`, or answering one named finding

Use this size by default. Escalate to the Full form when the change is
planning size `M` or larger, touches more than one area, or the risk is not
obvious from the diff alone.

```markdown
Phase / finding: <Red|Green|Refactor, or the Reviewer finding # this answers>
Command run: <the one command that produced the deterministic result>
Result: <its output, or a one-line summary if long>
Main risk considered: <the one failure mode most likely to be wrong here>
Why it doesn't occur: <one sentence>
```

That is the whole record. Do not add Scope Result, Routing and
Compatibility, or other sections from the Preflight or review-record
templates — those are sized for independent review, not for this.

## Full form — planning size `M` or larger

Use `docs/templates/review-record.md`'s "Deterministic Verification Output"
and "Falsification Burden" sections, filled out as the Implementer rather
than the Reviewer. Multiple failure scenarios are expected at this size; one
is not enough.

## What this is not

- Not an approval that counts toward `Evidence sufficiency` at the
  work-plan level. The work-plan-level Reviewer still reviews the whole
  plan, once, in a separate context, regardless of how many self-review
  records exist inside it.
- Not a place to restate the whole change's history. If you are describing
  more than the one phase transition or the one finding this record answers,
  you are writing the wrong record — see
  `docs/collaboration/llm-cost-reduction.md`.
