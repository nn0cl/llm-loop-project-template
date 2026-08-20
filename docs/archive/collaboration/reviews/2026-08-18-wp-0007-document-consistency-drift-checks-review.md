# Review Record: WP-0007 — Catch Document-Consistency Drift Deterministically

## Constraints (all three must hold)

- [x] **Context separation.** Reviewed from an independently checked-out
      detached worktree (`git worktree add --detach /tmp/verify-wp0007
      5c508ee`), produced by a separately spawned Implementation-group agent
      (`agentId a0263b247f0b615d4`), branch
      `process/document-consistency-drift-checks`.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently; the CI ADR-existence step's new logic
      reproduced locally; and — going beyond re-reading the Implementer's
      pasted synthetic-test output — this review independently constructed
      its own synthetic failure case against `check_issue_status_sync` and
      confirmed the new check catches it. See below.
- [x] **Falsification burden.** Failure scenarios below.

## Review Target

- Artifact: commit `5c508ee` on top of `4cb1e4b`, branch
  `process/document-consistency-drift-checks`, implementing LISS-0035.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-document-consistency-drift-checks.md`
  (`DA-2026-08-18-06`)
- Specification: none (tooling extension).
- Current phase: Preflight passed; work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `a0263b247f0b615d4`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, **Evidence sufficiency**.
- Preflight result: pass (re-verified below).

## Deterministic Verification Output

```text
$ git worktree add --detach /tmp/verify-wp0007 5c508ee
Preparing worktree (detached HEAD 5c508ee)

$ cd /tmp/verify-wp0007 && python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ git log --oneline -1 cf9da58
cf9da58 process: consolidate the operating contract as the first edition (v1.0.0)
$ git log --oneline -1 9fcb2d2
9fcb2d2 chore: reset the repository's record artifacts to the initial state
(both historical commits KNOWN_HISTORICAL_ID_REUSE cites are real and match
their stated descriptions)

$ ls docs/architecture/adr/*.md >/dev/null && echo "glob ok"
glob ok
$ <reproduced the CI step's new sequence-check loop locally>
sequence OK, checked up to 16

Independent synthetic-failure test against check_issue_status_sync (NOT
reusing the Implementer's own test artifacts -- constructed fresh by this
review):
$ cp -r /tmp/verify-wp0007 /tmp/verify-wp0007-synth
$ python3 -c "... flip LISS-0028's Status from 'done' to 'in_progress' ..."
replaced
$ cd /tmp/verify-wp0007-synth && python3 scripts/check-contract-consistency.py
issue status sync:
  docs/issues/LISS-0028-coordinator-message-hallucination-correction.md
  states Status: in_progress, but
  docs/work-plans/WP-0003-coordinator-message-correction.md's Issue Graph
  lists LISS-0028 as 'done'
contract consistency: 1 failure(s)
(check correctly caught the constructed mismatch)

$ git -C /tmp/verify-wp0007 status --short
(clean -- no leftover modifications in the reviewed worktree itself)
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | `check_issue_status_sync` does not actually catch a real mismatch (only the Implementer's own cherry-picked test case) | Constructed an independent synthetic mismatch, not reusing the Implementer's fixture, against a live issue/work-plan pair already in this repository (LISS-0028/WP-0003) — the check caught it with a clear, correctly-attributed message. | not reproduced |
| 2 | `KNOWN_HISTORICAL_ID_REUSE`'s cited commits (`cf9da58`, `9fcb2d2`) do not exist, or do not match their claimed descriptions | Both independently confirmed present with exactly the claimed commit messages. | not reproduced |
| 3 | The CI ADR-existence fix does not actually work dynamically (e.g. still silently requires manual edits) | Reproduced the new loop's exact logic locally against the actual `docs/architecture/adr/` directory on this branch; it correctly validated the sequence without any hardcoded number list. | not reproduced |
| 4 | `check_superseding_phrases`'s three registered anchor patterns do not actually match the real current text of their target files | Indirectly but soundly confirmed: the full `check-contract-consistency.py` run passed with zero failures on this branch, and `check_superseding_phrases` is wired into `main()` — a non-matching anchor would have produced a "superseding phrases" failure category, which did not appear. | not reproduced |
| 5 | The new checks introduce a meaning-inference heuristic (connective-word or proximity parsing), which this work plan's own boundaries forbid | Read all three new functions in full: `check_id_range_collisions` compares literal historical file paths via `git log`, `check_issue_status_sync` compares two literal `Status:` field values, `check_superseding_phrases` is exact-anchored presence-checking modeled directly on the pre-existing `check_adr_range`/`ENTRY_DOCUMENT_ADR_STATEMENTS` pattern — none infer meaning from prose. | not reproduced |
| 6 | Pattern 5 (template-copy exclusion gaps, explicitly out of scope) was duplicated here | `git diff --stat` shows no change to `scripts/lib/collaboration-template-paths.sh` in this branch's diff. | not reproduced |
| 7 | The renamed-vs-collision judgment (`git log --follow`) in `check_id_range_collisions` produces a false positive against this repository's own real, legitimate renames | The full consistency check passes clean against this repository's actual current file set — no `id range collisions` failure appears, meaning every currently-live numbered file's history is either clean or correctly registered in `KNOWN_HISTORICAL_ID_REUSE`. | not reproduced |

## Scenarios Not Searched

- Full independent construction of synthetic failures for
  `check_id_range_collisions` and `check_superseding_phrases` specifically
  (only `check_issue_status_sync` was independently re-tested from scratch;
  the other two were verified by direct code reading plus the historical
  -commit and full-clean-run evidence above, not a second independently
  constructed failure case each). Judged sufficient given the code reading
  found no meaning-inference heuristic and the clean full-repository run is
  itself a real signal (a bug in either function would very plausibly have
  produced a false positive against this repository's own real numbering
  history, which did not happen) — but this is a narrower search than the
  full re-run given to `check_issue_status_sync`, disclosed rather than
  implied as equally thorough.

## Checklist

- [x] Artifact belongs to the phase run (Architecture Path); no later phase
      leaked in.
- [x] Acceptance criteria in `DA-2026-08-18-06`'s Plan table satisfied.
- [x] No boundary named in the design agreement crossed (no
      meaning-inference heuristic; pattern 5 not duplicated;
      `check-contract-consistency.py` is not an ADR-0006 contract file, so
      no trace expected and none fabricated).
- [x] Every claim states its grounds.
- [x] Record lets a third party re-run this same search.

## Decision

- [x] Approved

## Reasons

- All seven named failure scenarios were searched for; none reproduced,
  including one independently constructed (not reused) synthetic failure
  case that the new tooling correctly caught.
- The three new checks stay within the anchored/structural-comparison
  design the script's own docstring requires, avoiding the meaning
  -inference trap three prior review rounds already rejected.
- The Implementer surfaced a genuine additional complexity (this
  template's own legitimate historical ID reuse from two real,
  Director-authorized past events) and handled it with an explicit,
  narrowly-scoped registry rather than a blanket exception — both cited
  commits independently confirmed real.
- Pattern 5 correctly stayed out of scope, per the design agreement.

## Note for the Design & Review group

`check_id_range_collisions`'s and `check_superseding_phrases`' own
independent-verification depth in this review is narrower than
`check_issue_status_sync`'s (see "Scenarios Not Searched"). If either
becomes load-bearing for a future finding, a dedicated synthetic-failure
construction for those two specifically would close that gap.

This review does not itself close WP-0007 — Director action, Backlog
layer.
