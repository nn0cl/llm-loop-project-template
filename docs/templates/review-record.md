# Review Record Template

Use this when the Reviewer persona issues a decision inside the execution loop.

A review that does not satisfy all three constraints below does not count as an
approval, whatever this record says.

## Constraints (all three must hold)

- [ ] **Context separation.** This review runs in a context separate from the
      one that produced the work. The Implementer's reasoning was not supplied
      and is not relied on as justification.
- [ ] **Deterministic precondition.** Deterministic verification was run and
      its output is recorded below. No approval is issued past a failing or
      absent signal.
- [ ] **Falsification burden.** Failure scenarios searched for are named below,
      each with the grounds on which it does not occur.

## Review Target

- Artifact:
- Covering design agreement:
- Specification:
- Current phase:
- Producing persona:
- Reviewing persona / model / tool:
- Approval type: specification-conformance | phase-correctness |
  boundary-conformance | evidence-sufficiency

## Deterministic Verification Output

Paste the actual output. A summary of it is not evidence.

```text

```

## Falsification Search

One row per scenario. "No problems found" is not an approval — if nothing was
searched for, the review is not done.

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 |  |  | not reproduced / reproduced |
| 2 |  |  | not reproduced / reproduced |
| 3 |  |  | not reproduced / reproduced |

## Scenarios Not Searched

Name what this review did not cover, so the gap is visible rather than implied.

- 

## Checklist

- [ ] The artifact belongs to the phase that was run; no later phase leaked in.
- [ ] Every `Then` clause in the specification is asserted by the work.
- [ ] The dependency rule and port boundaries hold.
- [ ] No boundary named in the design agreement was crossed.
- [ ] Specifications and accepted tests were not modified to make work pass.
- [ ] Every claim in the artifact states its grounds.
- [ ] The record would let a third party re-run this same search.

## Decision

- [ ] Approved
- [ ] Rejected — reasons and the specific artifact changes required
- [ ] Deadlocked — escalate to Arbiter, with both positions stated
- [ ] Reopening request — the design agreement does not settle this; state what
      is unsettled and what the loop needs in order to continue

## Reasons

- 
