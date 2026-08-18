# Review Record: LISS-0027 — Qualify docs/at-tdd/process.md's close-checkpoint phrasing

Minor Fix Path confirmation, per `CLAUDE.md`'s "Minor Fix Path" section and
`docs/architecture/adr/0015-review-cost-discipline.md`. `docs/at-tdd/process.md`
is an ADR-0006 contract file (listed in
`docs/collaboration/prompt-instruction-change-control.md`'s Agent Operating
Contract Files), so Minor Fix Path status does not exempt it from
separate-context Reviewer confirmation — self-review alone cannot close it,
per `CLAUDE.md`: "Contract-file changes are never self-reviewed, regardless
of work-plan scope... including a fix that answers a Reviewer finding on a
contract-file change."

## Constraints (all three must hold)

- [x] **Context separation.** This confirmation runs in the Design & Review
      group's own standing session. This session did not write the fix — a
      separately spawned Implementation-group session (`a9da782681672e59b`)
      did, on its own worktree/branch. This review was written from the
      actual committed diff (`8798934`), the issue's own recorded
      self-review, and the AI work trace — not from the Implementer's chat
      reasoning.
- [x] **Deterministic precondition.** `scripts/check-contract-consistency.py`
      and a targeted grep for the qualified/unqualified phrasing were both
      re-run independently by this review against the actual committed
      tree. Output below.
- [x] **Falsification burden.** Failure scenarios searched for, and the
      grounds each does not occur, are named below.

## Review Target

- Artifact: commit `8798934` on `worktree-agent-a2450968f458bbc6f` (on top of
  `4718570`, the merge of `e258d6b`).
- Covering design agreement: `DA-2026-08-18-01`, as extended by its Reopening
  Log entry (2026-08-18), recorded in commit `e258d6b`.
- Specification: none (process/governance change). Acceptance criteria are
  LISS-0027's own Acceptance Notes.
- Current phase: Minor Fix Path, answering Falsification Search scenario #11
  of `docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md`.
- Producing persona: Implementer (Implementation group).
- Reviewing persona / model / tool: Reviewer, Design & Review group standing
  session, Claude Sonnet 5 via Claude Code CLI.
- Approval type: **Boundary conformance** (mirrors an already-approved
  pattern without inventing new wording; stays within Minor Fix Path
  conditions) and **Evidence sufficiency** (deterministic output present).
  Specification conformance and Phase correctness are not separately
  meaningful here — no specification exists, and there is exactly one phase
  (a single qualifying edit), already confirmed the sole phase by the
  Implementer's own Work Notes.
- Preflight Validation record: LISS-0027's own trace, "Preflight Validation"
  section (scope result: pass, single file, matches stated scope).
- Preflight result: pass (re-verified independently below).

## Deterministic Verification Output

```text
$ git show 8798934 -- docs/at-tdd/process.md
[...]
@@ -194,5 +194,9 @@ Once every issue in the work plan has reached self-reviewed completion:
 3. Findings become `Type: review-finding` local issues, resolved through
    Minor Fix Path or an escalation, as sized.
 4. Once the Reviewer approves, the Director reads the result and states the
-   next direction — or ends the engagement — in the same action. The next
-   work plan does not start without this.
+   next direction — or ends the engagement — in the same action. This
+   specific work plan's own successor does not start without this. Per
+   `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
+   Rule 3, this does not block unrelated, concurrently in-flight work plans
+   in either group — only the one work plan being closed, and what directly
+   follows from closing it, wait on this action.

$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ grep -n "does not start without" docs/at-tdd/process.md
198:   specific work plan's own successor does not start without this. Per

$ grep -c "The next work plan does not start without this\." docs/at-tdd/process.md
0

$ git branch -r --contains 8798934
(no output — not reachable from any remote branch, confirming no push)

$ git diff 8798934^ 8798934 --stat
 docs/at-tdd/process.md | 8 ++++++--
 1 file changed, 6 insertions(+), 2 deletions(-)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The bare, unqualified sentence ("The next work plan does not start without this.") still appears anywhere in `docs/at-tdd/process.md` or elsewhere in the repository as if still current | `grep -c` for the exact original sentence in the file returns 0; the broader repo-wide sweep re-run for the WP-0002 review (this session's own, independent of the Implementer's) shows only the qualified form at line 198 | not reproduced |
| 2 | The fix invents new wording instead of mirroring `design-agreement.md`'s already-reviewed "Closing a work plan" pattern | Diffed the new text directly against `design-agreement.md`'s paragraph (already reviewed in the WP-0002 pass): "This specific work plan's own successor does not start without this... Per [ADR 0016] Rule 3, this does not block unrelated, concurrently in-flight work plans in either group — only the one work plan being closed, and what directly follows from closing it, wait on this action" — carried over near-verbatim; the only difference is writing the ADR path out in full on its first mention in this file, which is consistent with how the other two files cite it on first use | not reproduced |
| 3 | The commit touched content in `docs/at-tdd/process.md` beyond the one qualified sentence, or touched any other file | `git diff 8798934^ 8798934 --stat` shows exactly one file, 6 insertions / 2 deletions, consistent with a single-sentence qualification; `git show` above confirms the diff is scoped to step 4 of "Work-Plan Review and Close" only | not reproduced |
| 4 | This change alters a specification, ADR, port, data model, dependency, or architecture boundary, exceeding what Minor Fix Path permits | The change is a wording qualification that makes `docs/at-tdd/process.md` consistent with an already-accepted rule (ADR 0016 Rule 3) that two sibling files already state; it does not restate or alter ADR 0016 itself, and introduces no new rule | not reproduced |
| 5 | The consistency checker or any cross-reference regresses as a result of this change | Re-ran `python3 scripts/check-contract-consistency.py` independently: `contract consistency: all checks passed`, matching both this fix's own trace and the pre-existing WP-0002 baseline | not reproduced |
| 6 | The commit was pushed, opened as a PR, merged to `main`, or the issue/agreement was marked `done`/`closed`/`resolved` | `git branch -r --contains 8798934` returns nothing; LISS-0027's Status field reads `review`; `DA-2026-08-18-01`'s underlying agreement status is untouched by this fix | not reproduced |
| 7 | This fix lacks its own AI work trace, relying on the original WP-0002 traces instead | `docs/collaboration/traces/2026-08-18-liss-0027-at-tdd-process-adr-0016-qualification.md` exists, is issue-specific, and was read in full before this confirmation | not reproduced |

## Scenarios Not Searched

- Whether the Director's scope-extension decision itself (the Reopening Log
  entry in commit `e258d6b`) was properly authorized outside this
  repository's own artifacts — this review verified the entry's existence,
  well-formedness, and consistency with `DA-2026-08-18-01`'s existing
  Reopening Log format, and that the commit's author identity matches this
  environment's configured git user; it did not and cannot verify human
  intent behind that commit through any channel other than the repository
  artifact itself, per this project's own "a message is a trigger, not a
  record" rule (a decision is what the repository records, not what a chat
  message claims).

## Checklist

- [x] The artifact belongs to the phase that was run (a single Minor Fix
      Path qualifying edit); no other phase or scope leaked in.
- [x] The one stated acceptance criterion (qualify the phrasing, cross-
      referencing rather than duplicating ADR 0016's prose, no other content
      changed) is met.
- [x] The dependency rule and port boundaries hold — not applicable; no
      code, only documentation.
- [x] No boundary named in the design agreement or LISS-0027 itself was
      crossed: single file, single attempt, no specification/ADR/port/data-
      model/architecture-boundary change, no push/PR/merge, nothing marked
      done.
- [x] Specifications and accepted tests were not modified to make work
      pass — not applicable (no specification exists for this change).
- [x] Every claim in the artifact states its grounds — the self-review and
      trace both paste real command output rather than a summary.
- [x] The record would let a third party re-run this same search — commands
      are the exact ones pasted above, runnable from this worktree.

## Decision

- [x] **Approved**

## Reasons

The fix does exactly what LISS-0027 and the Reopening Log entry specified:
mirrors `design-agreement.md`'s already-reviewed ADR 0016 Rule 3
qualification into `docs/at-tdd/process.md`, with no invented wording, no
scope creep beyond the one sentence, and no boundary crossed. The
consistency checker and a fresh grep sweep, both re-run independently by
this review, confirm the fix and confirm no regression. This closes the one
remaining out-of-scope finding from the original WP-0002 Reviewer pass
(Falsification Search scenario #11 there); all six ADR-0016-affected
contract files (`personas.md`, `ai-human-scheme.md`,
`cross-session-messaging.md`, `session-start-and-resume.md`,
`branch-commit-pr-discipline.md`, `design-agreement.md`) plus this seventh
(`docs/at-tdd/process.md`) are now consistent, and no push/PR/merge or
`done`/`closed`/`resolved` marking occurred — the work-plan close remains the
Director's own pending action.
