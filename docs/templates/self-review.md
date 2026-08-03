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

**Short form bounds the record, not the search.** Look for what an
independent, separate-context Reviewer would look for — the work-plan-level
Reviewer sees this issue only once, at the work plan's close, not at this
phase transition, so the search has to be as if it were the only check this
work will ever get. "Short" means the write-up states the result of that
search concisely; it does not mean the search itself stopped at the first
plausible answer.

```markdown
Phase / finding: <Red|Green|Refactor, or the Reviewer finding # this answers>
Command run: <the one command that produced the deterministic result>
Result: <the actual output, pasted>
Risks considered: <every failure mode actually looked for, not just the
  first one — one line each>
Why each does not occur: <one line per risk above>
```

If the search turned up only one real candidate, the two fields above are
one line each and the record stays short by itself — the form does not force
padding. If it turned up several, list all of them; do not pick one
arbitrarily to keep the record shorter than the search actually was.

**`Result` is the actual output, always.** Not a summary — the Prime
Directive states unconditionally that "'Tests pass' without output is a
claim, not evidence," and this template does not get an exception. If the
output is too long to paste whole, paste the last 20–30 lines and the exact
command a reader can re-run to see the rest; do not replace the output with
a hand-written description of what it said. "Short form" bounds how much
*narrative* surrounds the evidence — it never bounds the evidence itself.

That is the whole record otherwise. Do not add Scope Result, Routing and
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
