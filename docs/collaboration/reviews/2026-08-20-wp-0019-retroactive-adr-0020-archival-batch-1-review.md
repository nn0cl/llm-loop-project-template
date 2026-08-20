# Review Record: WP-0019 (retroactive ADR 0020 archival, batch 1)

## Constraints (all three must hold)

- [x] **Context separation.** This review runs in the Design & Review
      group's standing session, which produced the work plan, design
      agreement, and issue text, but did not perform the file moves
      themselves — those were executed by a separate Implementation-group
      subagent session in its own dedicated worktree/branch
      (`wp-0019-execution`, spawned off `process/promote-item-0016`
      commit `6f49fb6`). This review does not rely on that Implementer
      session's own reasoning as justification; every claim below is
      independently re-run against the actual committed tree by this
      review itself.
- [x] **Deterministic precondition.** Deterministic verification was run,
      independently, by this review, and its output is recorded below —
      not copied from the work plan's own Preflight section, though that
      section's own results were cross-checked and matched.
- [x] **Falsification burden.** Failure scenarios searched for are named
      below, each with the grounds it does not occur, based on this
      review's own independent commands.

## Review Target

- Artifact: `wp-0019-execution` branch (commits `dfe5030`..`58de2f4`,
  7 commits), to be merged into `process/promote-item-0016`.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-20-retroactive-adr-0020-batch-1.md`
  (`DA-2026-08-20-02`)
- Specification: none (pure archival/process work; no `docs/specs/` file
  covers this work plan, per the design agreement's own Specifications
  section).
- Current phase: `docs-only` (both issues); Preflight Validation recorded
  as `pass` in `docs/work-plans/WP-0019-...md`.
- Producing persona: Implementer (Implementation group, separate context).
- Reviewing persona / model / tool: Reviewer (Design & Review group,
  standing session, same tool/model as the Planner that built the plan —
  context separation comes from the separate Implementation-group
  worktree/session that did the actual archival, not from a different
  model).
- Approval type: boundary-conformance, evidence-sufficiency (the two types
  the work plan's own Review Summary Packet names as at stake for a pure
  archival move).
- Preflight Validation record: `docs/work-plans/WP-0019-...md`'s own
  "Preflight Validation" section.
- Preflight result: pass.

## Deterministic Verification Output

All commands below were run independently by this review, against the
actual `wp-0019-execution` branch content (via `git archive
wp-0019-execution | tar -x` into a scratch directory, and via direct `git
show`/`git log`/`git diff` against the branch itself) — not pasted from
the work plan's own Preflight section.

```text
$ git archive wp-0019-execution | tar -x -C /tmp/wp19-verify
$ python3 /tmp/wp19-verify/scripts/check-contract-consistency.py --repo /tmp/wp19-verify
contract consistency: all checks passed

$ git diff process/promote-item-0016...wp-0019-execution --stat
 29 files changed, 363 insertions(+), 36 deletions(-)
 (matches the work plan's own stated scope: 23 moved files, restoration
 ledger, 2 Canonical-document reference edits, 3 tracking-file updates)

$ git show --name-status dfe5030   # LISS-0056 move commit
R100  docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md -> docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path-arbiter.md
R100  docs/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md -> docs/archive/collaboration/reviews/2026-08-02-review-issues-minor-fix-path.md
R100  docs/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md -> docs/archive/collaboration/traces/2026-08-02-review-issues-minor-fix-path.md
R100  docs/issues/LISS-0001-review-issues-minor-fix-path.md -> docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md
R100  docs/work-plans/WP-0001-review-issues-minor-fix-path.md -> docs/archive/work-plans/WP-0001-review-issues-minor-fix-path.md
M     docs/collaboration/restoration-ledger.md
M     docs/issues/LISS-0056-archive-wp-0001-under-adr-0020.md

$ git show --name-status 81ddf2a | grep -c '^R100'   # LISS-0057 move commit
18
(all 18 WP-0002-batch files show R100 — 100% content-preserving rename,
none combined with a content edit; 5 + 18 = 23 total, all R100)

$ git log --follow --oneline wp-0019-execution -- docs/archive/issues/LISS-0001-review-issues-minor-fix-path.md
dfe5030 process: archive WP-0001 and its owned records under ADR 0020 (LISS-0056)
39cf12f process: add review issues minor fixes and preflight validation
(pre-move history preserved, not delete+recreate)

$ grep -c "| archived |" /tmp/wp19-verify/docs/collaboration/restoration-ledger.md
23

$ git diff process/promote-item-0016...wp-0019-execution -- docs/collaboration/agreements/
(no output — confirms DA-2026-08-02-04 and DA-2026-08-18-01 are byte-for-byte
untouched, not moved, not edited)

$ git show wp-0019-execution:docs/backlog/item-0004-two-group-send-message-loop.md | head -1
# Backlog item: item-0004-two-group-send-message-loop
(confirms item-0004 still present at its original, un-archived path, as
the design agreement's Scope requires)

$ git diff process/promote-item-0016...wp-0019-execution -- docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md docs/collaboration/design-review-perspectives.md
(shows exactly 3 one-line path edits: ADR 0016's Status-section pointer to
WP-0002's file, and design-review-perspectives.md's two citations of
WP-0002's review record — each old path replaced with the corresponding
docs/archive/ path, no other content changed)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | A moved file's content was silently altered rather than moved verbatim | `git show --name-status` on both move commits shows all 23 entries as `R100` — 100% similarity is git's own rename-detection signal that the blob content is byte-identical between old and new path; any edit combined with the move would show a lower percentage or a separate content diff | not reproduced |
| 2 | A current Canonical document other than the two named still points at an old (now-archived) path | Independent `git diff` restricted to `docs/architecture/`, `docs/collaboration/*.md` (top level), and `docs/templates/` shows exactly the 3 expected one-line edits and nothing else changed in those directories; `check-contract-consistency.py`'s own dangling-reference and Entry-archive-reference checks pass clean against the full archived tree | not reproduced |
| 3 | `DA-2026-08-02-04` or `DA-2026-08-18-01` (the two design agreements this batch must leave untouched) was moved, edited, or deleted | `git diff process/promote-item-0016...wp-0019-execution -- docs/collaboration/agreements/` produces zero output — both files are byte-identical to their pre-batch state at their original paths | not reproduced |
| 4 | A restoration-ledger row's `source_commit` does not match the actual move commit that produced it | Cross-checked all 23 rows' `source_commit` values against the two move commits' own hashes (`dfe5030a7ead7e8e1bcf472e47ce6af4022f287c` for the 5 WP-0001-batch rows, `81ddf2a8afcdda027f713fcb35242eb0d793c168` for the 18 WP-0002-batch rows) — both match exactly; the two small follow-up correction commits (`d02eb3c`, `42f4ea6`) that replaced an initial `PENDING` placeholder are themselves a defensible resolution of a genuine self-referential constraint (a commit cannot contain its own final hash at creation time), not a shortcut around Rule 5's "same commit as the move" requirement (the row and the move landed together; only the row's own hash value needed a follow-up correction) | not reproduced |
| 5 | `docs/backlog/item-0004-...md`'s deliberate exclusion from this batch was actually a silent omission rather than a stated, grounded scope decision | Confirmed the exclusion is explicitly named, with grounds, in three places this review cross-checked independently: LISS-0057's own "Explicit exclusion" section, the design agreement's Scope/Settled Ambiguities, and WP-0019's own Scope "Out" list and Deferred Questions — all three state the same reason (larger, untriaged reference graph) consistently, and the file itself is confirmed present and unmoved (see Deterministic Verification Output) | not reproduced |
| 6 | The two flagged Implementer deviations (hash-amend mechanic; the literal Verification-section grep command that cannot pass post-fix by construction) mask an actual defect rather than a genuine plan-wording gap | Independently re-derived both: (a) amending a commit to insert its own hash is mathematically self-referential — the amended commit's hash necessarily differs from the hash being inserted, so no single-commit solution exists; a same-commit-then-correct pattern is the correct resolution, and Rule 5's own requirement ("row in the same commit as the move") is satisfied for the move itself, with only the row's own commit-hash *value* needing the follow-up; (b) re-ran the literal grep command from LISS-0057's Verification section myself (`grep -rn "docs/collaboration/reviews/2026-08-18-wp-0002-two-group-send-message-loop-review.md" docs/collaboration/design-review-perspectives.md`) against the fixed tree and independently got zero hits, then the corrected filename-only search and got both expected hits — confirms the Implementer's own diagnosis was accurate, not a cover story | not reproduced |

## Scenarios Not Searched

- Whether every document in the repository outside
  `docs/architecture/adr/*.md`, `docs/collaboration/*.md` (top level), and
  `docs/templates/*.md` still correctly resolves any of the 23 old paths
  it might informally mention — Evidence-layer documents (other issues,
  traces, review records) are expected under ADR 0020's own layer model to
  keep ID-only or historical references and are not required to track a
  moved path; `check-contract-consistency.py`'s own dangling-reference
  check covers current-document path resolution generally and passed
  clean, which is the check this repository's own contract relies on for
  this class of defect.
- `docs/backlog/item-0004-...md`'s own internal reference graph
  (`DA-2026-08-18-04`, ADR 0016, LISS-0040, WP-0011, item-0005, item-0007,
  item-0012, LISS-0031) — explicitly out of this batch's scope per the
  design agreement's Deferred Questions; a later batch's own job.
- Whether WP-0003 through WP-0018 are themselves correctly archival-
  ineligible or eligible — out of this work plan's scope entirely.

## Checklist

- [x] The artifact belongs to the phase that was run (`docs-only`); no
      later phase leaked in — no content rewriting beyond the two
      authorized reference edits, confirmed by the `R100` rename evidence.
- [x] Every `Then` clause in the specification is asserted by the work —
      N/A, no specification covers this work plan (design agreement's own
      Specifications section states this explicitly).
- [x] The dependency rule and port boundaries hold — N/A, no application
      architecture touched.
- [x] No boundary named in the design agreement was crossed — confirmed:
      no content rewriting beyond the two named edits, no redirect stub
      created, `DA-2026-08-02-04`/`DA-2026-08-18-01` untouched, item-0004
      untouched, WP-0003–WP-0018 untouched, ADR 0020's own text untouched.
- [x] Specifications and accepted tests were not modified to make work
      pass — N/A.
- [x] Every claim in the artifact states its grounds — each ledger row
      names its ADR 0020 Rule 2 trigger; both flagged deviations state
      their own reasoning rather than silently resolving.
- [x] The record would let a third party re-run this same search — every
      command above is copy-pasteable and was in fact independently
      re-run by this review, not merely copied from the Implementer's own
      output.

## Decision

- [x] Approved

## Reasons

All 23 files scoped by LISS-0056/LISS-0057 were moved via `git mv` with
verified 100%-similarity renames (no content alteration), each backed by a
real restoration-ledger row whose `source_commit` matches the actual move
commit. Both mandatory Rule-3 reference updates (ADR 0016, `design-review-
perspectives.md`) landed correctly and were independently confirmed. The
two design agreements and the backlog item this batch deliberately
excludes were independently confirmed untouched. `check-contract-
consistency.py` passes clean against the full archived tree, both via this
review's own fresh `git archive` extraction and via the branch's tracked
content directly. The two deviations the Implementation group flagged
(the hash self-reference resolution, and the Verification-section grep
wording) are both genuine plan-text imprecisions rather than defects in
the actual archival work, and both were handled by disclosure rather than
silent correction — exactly the behavior this repository's own review
discipline requires. No `Type: review-finding` issue is warranted; nothing
found here rises to a defect requiring correction before Director close.

**Note for the record**: `docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
Rule 5's "same commit as the move" wording does not, and cannot, literally
accommodate a ledger row containing its own commit's hash in one atomic
commit — this batch's same-commit-then-immediate-correction-commit pattern
is a reasonable, disclosed resolution, but future batches would benefit
from ADR 0020 itself (or `restoration-ledger.md`'s own "How to read a row"
section) stating this pattern as the expected mechanic, rather than each
batch re-discovering and re-justifying it independently. Not a blocking
finding against this work plan — a suggestion for a future, separate,
low-cost documentation clarification.