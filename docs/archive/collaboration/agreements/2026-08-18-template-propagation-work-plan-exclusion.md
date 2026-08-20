# Design Agreement: Exclude Work-Plan History From Template Propagation

## Identity

- Agreement ID: DA-2026-08-18-04
- Date: 2026-08-18
- Director: nn0cl
- Planner / Specifier personas (model or tool used): Claude Sonnet 5 via
  Claude Code, Design & Review group standing session
- Supersedes agreement (if any): none.

## Direction

Per `docs/backlog/item-0005-template-propagation-script-for-two-group-loop.md`
(`Status: promoted`), whose Promotion notes are this agreement's Director
authorization under ADR 0016 Rule 2: check whether
`scripts/copy-ai-collaboration-files.sh` /
`scripts/update-ai-collaboration-files.sh` already pick up new files under
`docs/collaboration/*.md` and `docs/architecture/adr/*.md` automatically
(item-0004/WP-0002's new documents: ADR 0016, `cross-session-messaging.md`,
and the updated `personas.md`, `ai-human-scheme.md`,
`session-start-and-resume.md`, `branch-commit-pr-discipline.md`,
`design-agreement.md`, `docs/backlog/README.md`), or whether the tooling
needs an explicit update.

## Spike Result (run by the Design & Review group before this agreement)

Read `docs/architecture/adr/0008-template-update-propagation.md` and
`scripts/lib/collaboration-template-paths.sh`, then ran a real empirical
test, not just a code read:

1. Confirmed `collaboration_template_paths` lists whole directories
   (`docs/collaboration`, `docs/architecture`, etc.), and both scripts walk
   them with `find "$path" -type f` — a directory-level entry, not a
   per-file manifest, so a new file added under an already-listed directory
   requires no script change to be discovered.
2. Built a real scratch adopter: `git worktree add --detach
   /tmp/liss-0005-old-template 6c78217` (a commit predating
   `cross-session-messaging.md` and ADR 0016 entirely), ran
   `scripts/copy-ai-collaboration-files.sh` from that old checkout into a
   fresh scratch target, confirmed the target genuinely lacked both new
   files, then ran `scripts/update-ai-collaboration-files.sh --target
   <scratch> --source <this checkout, which has the new files>
   --non-interactive`.
3. **Result: confirmed, empirically, not just by code reading.** The
   update script's own report listed both new files under "Added (new
   upstream files)":
   `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
   and `docs/collaboration/cross-session-messaging.md`, with zero script
   changes. **Item-0005's core question is answered: no code change is
   needed for this part.**
4. **A real, separate gap was found in the same test run**, worth fixing
   under this same item since it was surfaced by the same investigation and
   is the same class of concern (what does/does not propagate): the update
   script's "Added" list also included
   `docs/work-plans/WP-0002-two-group-send-message-loop.md`,
   `docs/work-plans/WP-0003-coordinator-message-correction.md`, and
   `docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md` — this
   template repository's own work-plan execution history, copied into the
   adopter target as if it were reusable template content.
   `scripts/lib/collaboration-template-paths.sh`'s
   `collaboration_template_exclude_paths` already excludes the equivalent
   target-owned-planning-history classes `docs/issues/LISS-*.md` and
   `docs/backlog/item-*.md`, but has no matching entry for
   `docs/work-plans/WP-*.md` — an inconsistency, not an intentional
   difference (nothing in ADR 0008 or the exclude list's own comment
   distinguishes work plans from local issues or backlog items on this
   point). The CI smoke test
   (`.github/workflows/ci.yml`, "Check template copy smoke test") has a
   matching gap: it asserts `! ls docs/issues/LISS-*.md` and
   `! ls docs/backlog/item-*.md` are absent from a fresh copy, but has no
   equivalent assertion for `docs/work-plans/WP-*.md`.

## Scope

- In scope:
  - Add `"docs/work-plans/WP-*.md"` to
    `collaboration_template_exclude_paths` in
    `scripts/lib/collaboration-template-paths.sh`, matching the existing
    `LISS-*.md` / `item-*.md` pattern exactly.
  - Add the matching CI smoke-test assertion in `.github/workflows/ci.yml`'s
    "Check template copy smoke test" step:
    `! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1`, placed
    alongside the existing `LISS-*.md`/`item-*.md` assertions.
  - Confirm `docs/work-plans/.gitkeep` still copies (it must — only the
    numbered `WP-*.md` files are target-owned history, not the directory
    itself, mirroring how `docs/issues/.gitkeep` still copies today).
  - Re-run the same empirical copy+update test performed in this
    agreement's Spike Result, after the fix, to confirm work plans are now
    excluded and the two already-working new-file cases
    (`cross-session-messaging.md`, ADR 0016) are unaffected by this change.
  - Record, in this issue's own Work Notes or a short spike note, that
    "does the tooling already pick up new `docs/collaboration/*.md` and
    `docs/architecture/adr/*.md` files automatically" is answered **yes, no
    change needed** — so a future reader does not re-ask the same question
    `item-0005` was created to answer.
- Explicitly out of scope:
  - Any change to the Tier 1/Tier 2 classification logic itself
    (`is_contract_persona_file`) — unaffected by this finding.
  - The CI workflow's separate, unrelated hardcoded ADR-number list
    (`for n in 0001 ... 0016`) needing a `0017` entry once WP-0004 lands —
    a genuinely separate, already-flagged item (spawned as its own
    follow-up task by the Design & Review group; not part of this backlog
    item's own scope, which is specifically the propagation *script*, not
    the ADR-count CI check).
  - Any change to `docs/collaboration/*.md`, `docs/architecture/adr/*.md`,
    or any other document content — this item is tooling-only.

## Plan

| # | Task | Persona | Phase | Acceptance criterion | Verification method |
|---|---|---|---|---|---|
| 1 | Add `docs/work-plans/WP-*.md` to `collaboration_template_exclude_paths` | Implementer | Fast Path (mechanical, one-line, no behavior/architecture change beyond the stated exclusion) | Pattern added, matching existing style; `docs/work-plans/.gitkeep` still not excluded | read-through diff |
| 2 | Add CI smoke-test assertion for the new exclusion | Implementer | Fast Path | New `! ls` assertion present, in the same style/location as the `LISS-*.md`/`item-*.md` assertions | read-through diff of `.github/workflows/ci.yml` |
| 3 | Re-run the empirical copy+update test from this agreement's Spike Result, after the fix | Implementer | Fast Path | `docs/work-plans/WP-*.md` no longer appears in either script's output for a fresh copy or an update pull; `docs/work-plans/.gitkeep` still present; the two already-working cases (`cross-session-messaging.md`, ADR 0016 auto-discovery) still work | actual command output pasted in LISS-0031 Work Notes |
| 4 | Run the existing CI smoke-test step's full command sequence locally as a broader regression check | Implementer | Fast Path | `.github/workflows/ci.yml`'s "Check template copy smoke test" step's commands, run locally against a scratch target, all pass | command output pasted in Work Notes |
| 5 | Self-review | Implementer | Fast Path | Short-form self-review per `docs/templates/self-review.md` | self-review record in LISS-0031 Work Notes |
| 6 | Preflight Validation | Implementer / deterministic tool | Fast Path | `pass` recorded with command output | Preflight section in WP-0005 |
| 7 | Separate-context Reviewer pass | Reviewer (Design & Review group, separate context) | Fast Path | Review record confirms the fix and the re-run empirical test independently | review record under `docs/collaboration/reviews/` |

Sequencing: Task 1 blocks 2-4. Tasks 2-4 may run in any order after Task 1.
Task 5 follows 1-4. Task 6 follows 5. Task 7 follows 6.

Note on phase labeling: none of these files are ADR-0006 agent operating
contract files (`scripts/lib/collaboration-template-paths.sh` and
`.github/workflows/ci.yml` are not in that list), so no trace is required —
this is ordinary tooling maintenance, not a contract-file change. It is
still Architecture-Path-adjacent in spirit (a template-propagation-policy
change) but the change itself is small and mechanical enough, and
sufficiently bounded by this agreement's own acceptance criteria, that Fast
Path framing per `docs/architecture/agent-quickstart.md` fits; the Reviewer
pass is still required at the work-plan level regardless of path, per
`docs/collaboration/design-agreement.md`.

## Specifications

- None. Tooling/process change; no application specification.

## Boundaries

- No change to the Tier 1/Tier 2 classification logic.
- No change to any document's content.
- No push, PR, or merge to `main`; nothing marked `done`/`closed` until the
  Director's own work-plan-close action.

## Settled Ambiguities

| Question | Answer | Decided by |
|---|---|---|
| Is a code change needed for new `docs/collaboration/*.md`/`docs/architecture/adr/*.md` files to propagate? | No — confirmed empirically via a real copy+update test cycle against a scratch adopter built from a pre-two-group-loop commit. This item's own scope becomes the *adjacent* gap the same test surfaced (work-plan exclusion), not the originally-suspected gap (which does not exist). | Design & Review group (Planner), via direct empirical test, not inference from code reading alone |
| Should the CI ADR-number hardcoded list's missing `0017` entry (once WP-0004 lands) be fixed under this item too? | No — genuinely separate concern (ADR-count CI check, not the propagation script); flagged as its own follow-up rather than scope-creeping this item. | Design & Review group (Planner) |

## Deferred Questions

| Question | Condition that will settle it |
|---|---|
| Should `docs/spike/case-*` also get an equivalent CI smoke-test assertion (it is already in the exclude list but has no smoke-test line, unlike `LISS-*.md`/`item-*.md`)? | A future backlog item or Reviewer finding, if this asymmetry is judged worth closing — out of this item's own narrow scope (which is the missing *exclusion*, not smoke-test coverage completeness generally; `docs/spike/case-*` is already correctly excluded, only its smoke-test assertion is thin) |

## Verification

- The empirical copy+update test re-run after the fix (Task 3), with actual
  command output.
- The existing CI smoke-test step's command sequence, run locally (Task 4).
- Separate-context Reviewer approval.

## Falsification Criteria

- After the fix, `docs/work-plans/WP-*.md` still appears in a fresh copy or
  update-script "Added"/"Updated" output.
- `docs/work-plans/.gitkeep` is also excluded (over-broad fix breaking
  legitimate directory scaffolding).
- The already-working new-file auto-discovery for
  `docs/collaboration/*.md`/`docs/architecture/adr/*.md` regresses as a
  side effect of this change.
- The fix lands without a Reviewer pass.

## Agreement

- [x] **Director**: this plan and these specifications describe what I want
      built, and the stated boundaries are the right ones. Recorded basis:
      `docs/backlog/item-0005-template-propagation-script-for-two-group-loop.md`,
      `Status: promoted`, Promotion notes, per ADR 0016 Rule 2.
- [x] **AI**: this plan and these specifications are executable without
      further interpretation. Made fresh by the Design & Review group
      against this actual plan and the empirical spike result above.

## Reopening Log

| Date | What was unsettled | Resolution |
|---|---|---|
|  |  |  |
