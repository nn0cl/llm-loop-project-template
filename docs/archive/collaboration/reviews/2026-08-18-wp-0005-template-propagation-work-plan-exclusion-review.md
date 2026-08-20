# Review Record: WP-0005 — Exclude Work-Plan History From Template Propagation

## Constraints (all three must hold)

- [x] **Context separation.** Reviewed from an independently checked-out
      detached worktree (`git worktree add --detach /tmp/verify-wp0005
      3d4e968`), produced by a separately spawned Implementation-group
      agent (`agentId a902bd0ac175ba803`), branch
      `process/template-propagation-work-plan-exclusion`.
- [x] **Deterministic precondition.** `python3 scripts/check-contract-consistency.py`
      re-run independently, plus a full independent re-run of the empirical
      copy+update test (not a re-read of the Implementer's pasted output) —
      see below.
- [x] **Falsification burden.** Failure scenarios below.

## Review Target

- Artifact: commit `3d4e968` on top of `3929c4b`, branch
  `process/template-propagation-work-plan-exclusion`, implementing
  LISS-0031.
- Covering design agreement:
  `docs/collaboration/agreements/2026-08-18-template-propagation-work-plan-exclusion.md`
  (`DA-2026-08-18-04`)
- Specification: none (tooling fix).
- Current phase: Preflight passed; work-plan-level Review.
- Producing persona: Implementer (Implementation group, spawned agent
  `a902bd0ac175ba803`).
- Reviewing persona / model / tool: Reviewer, Design & Review group
  standing session, Claude Sonnet 5 via Claude Code.
- Approval type: **Specification conformance**, **Phase correctness**,
  **Boundary conformance**, **Evidence sufficiency**.
- Preflight result: pass (re-verified below).

## Deterministic Verification Output

```text
$ git worktree add --detach /tmp/verify-wp0005 3d4e968
Preparing worktree (detached HEAD 3d4e968)

$ cd /tmp/verify-wp0005 && python3 scripts/check-contract-consistency.py
contract consistency: all checks passed

$ bash -n scripts/lib/collaboration-template-paths.sh
(exit 0)

$ git diff --stat 3929c4b process/template-propagation-work-plan-exclusion
 .github/workflows/ci.yml                           |   1 +
 .../LISS-0031-template-propagation-work-plan-exclusion.md | 250 ++++++++
 .../WP-0005-template-propagation-work-plan-exclusion.md   | 114 ++++
 scripts/lib/collaboration-template-paths.sh        |   1 +
 4 files changed, 359 insertions(+), 7 deletions(-)

Independent re-run of the full empirical copy+update test cycle (not the
Implementer's pasted output -- reproduced from scratch by this review):

$ git worktree add --detach /tmp/liss-0031-old-template 6c78217
Preparing worktree (detached HEAD 6c78217)

$ cd /tmp/liss-0031-old-template && bash scripts/copy-ai-collaboration-files.sh \
    --target /tmp/liss-0031-scratch-target --project-name "Test Adopter" \
    --domain-summary "test domain" --stack "test stack"
(copy completed)

$ cd /tmp/liss-0031-scratch-target && git init -q && git add -A && git commit -q -m "initial adoption"

$ bash /tmp/verify-wp0005/scripts/update-ai-collaboration-files.sh \
    --target /tmp/liss-0031-scratch-target --source /tmp/verify-wp0005 --non-interactive
Added (new upstream files):
  - docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md
  - docs/collaboration/cross-session-messaging.md
Updated (Tier 1 or 2, target had not diverged from the template): [11 files]
Unchanged: 96 file(s)

-- docs/work-plans/WP-*.md is absent from the "Added" list. Before this
fix, the same test (run during DA-2026-08-18-04's spike) showed
WP-0002-*.md, WP-0003-*.md, and WP-0004-*.md all listed under "Added." The
two originally-working cases (cross-session-messaging.md, ADR 0016) remain
correctly auto-discovered.

$ test -f /tmp/liss-0031-scratch-target/docs/work-plans/.gitkeep && echo present
present
```

## Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | `docs/work-plans/WP-*.md` still propagates after the fix | Independently re-ran the full empirical copy+update cycle from scratch (not reusing the Implementer's test artifacts); the "Added" list contains no `WP-*.md` entry, versus three such entries before the fix. | not reproduced |
| 2 | The fix over-excludes and drops `docs/work-plans/.gitkeep` | Confirmed present in the independently re-created scratch target after the update. | not reproduced |
| 3 | The two originally-working auto-discovery cases (`cross-session-messaging.md`, ADR 0016) regressed | Both still appear correctly under "Added" in this review's own independent re-run. | not reproduced |
| 4 | The exclusion pattern is malformed or has a shell-syntax defect | `bash -n` on the edited file passes; the pattern matches exactly the style of the adjacent `LISS-*.md`/`item-*.md` entries it was modeled on. | not reproduced |
| 5 | The CI smoke-test assertion was added in the wrong place or wrong style relative to the existing `LISS-*.md`/`item-*.md` assertions | Diff shows it inserted directly adjacent to `! ls "$tmp/target/docs/backlog/"item-*.md`, same `>/dev/null 2>&1` style. | not reproduced |

## Scenarios Not Searched

- A previously-adopted target's already-copied `WP-*.md` files are not
  retroactively removed by this fix (confirmed as expected behavior, not a
  gap: this review's own independent test showed `WP-0001-*.md`, copied
  during the pre-fix initial-adoption step used to build the test's
  baseline, remaining present after the update — consistent with ADR
  0008's own design, where exclusion prevents future propagation and does
  not retroactively delete files a target already has). Not treated as a
  defect; not further pursued.

## Checklist

- [x] Artifact belongs to the phase run (Fast Path); no later phase leaked
      in.
- [x] Acceptance criteria in `DA-2026-08-18-04`'s Plan table satisfied.
- [x] No boundary named in the design agreement crossed (Tier 1/Tier 2
      classification untouched; no document content changed).
- [x] Every claim states its grounds.
- [x] Record lets a third party re-run this same search (every command
      above is independently reproducible against commit `3d4e968`).

## Decision

- [x] Approved

## Reasons

- The fix works exactly as claimed, confirmed by an independent, from-scratch
  re-run of the empirical test — not merely trusting the Implementer's
  pasted output.
- No over-exclusion; `.gitkeep` and the originally-working auto-discovery
  cases are unaffected.
- Narrow, minimal, exactly-scoped diff.

This review does not itself close WP-0005 — Director action, Backlog layer.
