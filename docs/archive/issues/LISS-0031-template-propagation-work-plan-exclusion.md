# LISS-0031: Exclude docs/work-plans/WP-*.md from template propagation

## Metadata

- Local issue ID: LISS-0031
- GitHub issue: none
- Status: done
- Phase: process-only
- Type: tooling-fix
- Priority: medium
- Initial planning size: S
- Current planning size: S
- Reclassification reason: N/A
- Owner/agent: Implementation group (to be assigned at dispatch)
- Related branch: process/template-propagation-work-plan-exclusion

## Summary

- `scripts/lib/collaboration-template-paths.sh`'s
  `collaboration_template_exclude_paths` excludes `docs/issues/LISS-*.md`
  and `docs/backlog/item-*.md` (this template repository's own
  target-owned planning history) from propagation into adopter projects,
  but has no equivalent entry for `docs/work-plans/WP-*.md` — found via an
  empirical copy+update test run during `DA-2026-08-18-04`'s spike, which
  showed `WP-0002-*.md`, `WP-0003-*.md`, and `WP-0004-*.md` all landing in
  a scratch adopter target as "Added (new upstream files)." Add the missing
  exclusion and its matching CI smoke-test assertion.

## Acceptance Notes

- `"docs/work-plans/WP-*.md"` added to `collaboration_template_exclude_paths`
  in `scripts/lib/collaboration-template-paths.sh`, same style as the
  existing `LISS-*.md`/`item-*.md` entries.
- `.github/workflows/ci.yml`'s "Check template copy smoke test" step gets a
  matching `! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1`
  assertion, placed near the existing `LISS-*.md`/`item-*.md` assertions.
- `docs/work-plans/.gitkeep` still copies (directory scaffolding is not
  excluded, only the numbered work-plan files).
- Empirical copy+update test (same method as `DA-2026-08-18-04`'s Spike
  Result) re-run after the fix, with actual command output pasted in Work
  Notes, showing `docs/work-plans/WP-*.md` no longer appears in either
  script's report, while `cross-session-messaging.md` and ADR 0016/0017
  auto-discovery (the original item-0005 question) still work unaffected.
- The existing CI smoke-test step's full command sequence, run locally,
  passes.

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0005-template-propagation-script-for-two-group-loop.md
- Depends on: none
- Blocks: none
- Related: `docs/architecture/adr/0008-template-update-propagation.md`

## Decisions Not Settled by the Design Agreement

- None identified at design time.

## Context

- Included: `scripts/lib/collaboration-template-paths.sh`,
  `.github/workflows/ci.yml` (smoke-test step only),
  `docs/architecture/adr/0008-template-update-propagation.md`,
  `DA-2026-08-18-04`.
- Omitted: the rest of `.github/workflows/ci.yml` (unrelated CI steps); the
  Tier 2 AI-assisted-reconciliation logic (unaffected by this fix).
- Assumptions: the empirical test method used in `DA-2026-08-18-04`'s Spike
  Result (a scratch adopter built from commit `6c78217`, updated against
  the current tree) is a valid way to re-verify the fix; if the Implementer
  finds it does not reproduce, that is a reopening trigger, not a judgment
  call to route around.

## AI Planning Records

Not required — planning size `S`, first attempt expected.

## References

- `docs/architecture/adr/0008-template-update-propagation.md`
- `docs/collaboration/agreements/2026-08-18-template-propagation-work-plan-exclusion.md`
  (`DA-2026-08-18-04`)

## Work Notes

- 2026-08-18 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0005-*.md`'s promotion, after running the empirical
  spike recorded in `DA-2026-08-18-04`. The spike's own commands and output
  (scratch adopter from commit `6c78217`, `copy-ai-collaboration-files.sh`,
  then `update-ai-collaboration-files.sh --source <this checkout>
  --non-interactive`) are reproducible against this same repository state;
  see `DA-2026-08-18-04`'s "Spike Result" for the literal command sequence
  and its output. Dispatched to the Implementation group.
- 2026-08-18 (Implementation group, Implementer): fix applied on branch
  `process/template-propagation-work-plan-exclusion`
  (commit `891b304`): added `"docs/work-plans/WP-*.md"` to
  `collaboration_template_exclude_paths` in
  `scripts/lib/collaboration-template-paths.sh`, and
  `! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1` to
  `.github/workflows/ci.yml`'s "Check template copy smoke test" step, next
  to the existing `item-*.md` assertion.

  **Self-review (short form, `docs/templates/self-review.md`)**

  ```markdown
  Phase / finding: Fast Path fix (Tasks 1-2, DA-2026-08-18-04)
  Command run: git diff -- scripts/lib/collaboration-template-paths.sh .github/workflows/ci.yml
  Result:
  diff --git a/.github/workflows/ci.yml b/.github/workflows/ci.yml
  index 4bbe5d9..9b2949d 100644
  --- a/.github/workflows/ci.yml
  +++ b/.github/workflows/ci.yml
  @@ -210,6 +210,7 @@ jobs:
             ! ls "$tmp/target/docs/specs/"*.md >/dev/null 2>&1
             ! ls -d "$tmp/target/docs/spike/"case-* >/dev/null 2>&1
             ! ls "$tmp/target/docs/backlog/"item-*.md >/dev/null 2>&1
  +          ! ls "$tmp/target/docs/work-plans/"WP-*.md >/dev/null 2>&1
             test -f "$tmp/target/scripts/check-contract-consistency.py"
             (cd "$tmp/target" && python3 scripts/check-contract-consistency.py --repo .)
             if grep -R -n -i -E '<PROJECT_NAME: one-line description|<FILL IN: e\.g\. backend' \
  diff --git a/scripts/lib/collaboration-template-paths.sh b/scripts/lib/collaboration-template-paths.sh
  index c6293dd..0236e46 100644
  --- a/scripts/lib/collaboration-template-paths.sh
  +++ b/scripts/lib/collaboration-template-paths.sh
  @@ -44,6 +44,7 @@ collaboration_template_exclude_paths=(
     "docs/specs/*.md"
     "docs/spike/case-*"
     "docs/backlog/item-*.md"
  +  "docs/work-plans/WP-*.md"
     "docs/collaboration/loop-settings.toml"
   )
  Risks considered:
  1. Over-broad glob could also exclude docs/work-plans/.gitkeep or a
     non-WP-numbered file in that directory.
  2. The new exclusion could regress the already-working auto-discovery of
     new docs/collaboration/*.md / docs/architecture/adr/*.md files
     (cross-session-messaging.md, ADR 0016) that DA-2026-08-18-04's Spike
     Result already confirmed works.
  3. The CI assertion could be placed/styled inconsistently with its
     neighbors, making it easy to miss on future edits.
  Why each does not occur:
  1. The literal shell glob pattern `docs/work-plans/WP-*.md` only matches
     filenames starting with `WP-` and ending in `.md`; `.gitkeep` has
     neither prefix nor suffix, so `case "$rel" in $pattern)` cannot match
     it. Confirmed empirically: `test -f
     /tmp/liss-0031-scratch-target/docs/work-plans/.gitkeep` succeeded
     after the fix (see the empirical re-test below).
  2. The exclusion list change is additive (one new array entry) and does
     not touch `collaboration_template_paths` (the directory-level
     inclusion list that `find "$path" -type f` walks) or
     `is_contract_persona_file`; the mechanism the Spike Result relied on
     (whole-directory discovery) is untouched. Confirmed empirically below:
     the re-run update still lists `docs/architecture/adr/0016-*.md` and
     `docs/collaboration/cross-session-messaging.md` under "Added".
  3. Placed immediately after the `item-*.md` line in both files, matching
     the existing `LISS-*.md` / `item-*.md` style exactly (same `! ls
     "$tmp/target/<dir>/"<pattern> >/dev/null 2>&1` shape in ci.yml, same
     quoted-string array entry in the exclude-paths script).
  ```

- 2026-08-18 (Implementation group, Implementer): empirical re-test of the
  fix, using the same method as `DA-2026-08-18-04`'s Spike Result.

  **Setup**

  ```
  $ git worktree add --detach /tmp/liss-0031-old-template 6c78217
  Preparing worktree (detached HEAD 6c78217)
  HEAD is now at 6c78217 process: release v2.3.0
  $ mkdir -p /tmp/liss-0031-scratch-target
  ```

  **Step 1 — initial adoption from the pre-two-group-loop commit (unchanged
  from the Spike Result; before this fix existed, so `WP-0001` still gets
  copied, matching the Spike Result's own finding):**

  ```
  $ cd /tmp/liss-0031-old-template
  $ scripts/copy-ai-collaboration-files.sh --target /tmp/liss-0031-scratch-target \
      --project-name "Test Adopter" --domain-summary "test domain" --stack "test stack"
  ...
  merge docs/work-plans
  ...
  Done.
  Target: /tmp/liss-0031-scratch-target
  ...
  $ cd /tmp/liss-0031-scratch-target && git init -q && git add -A && git commit -q -m "initial adoption"
  [master (root-commit) a1f842b] initial adoption
  $ ls docs/work-plans/
  .gitkeep  WP-0001-review-issues-minor-fix-path.md
  ```

  **Step 2 — update pull from this (fixed) checkout — the actual test of
  the fix:**

  ```
  $ scripts/update-ai-collaboration-files.sh --target /tmp/liss-0031-scratch-target \
      --source <this checkout, commit 891b304> --non-interactive
  Source: <this checkout> (6c78217beb01145c40b20dcdbc52096805c7092c -> 891b30461f0e29b2f0cf454ca9a340b88e5371e0)
  Target: /tmp/liss-0031-scratch-target

  Added (new upstream files):
    - docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md
    - docs/collaboration/cross-session-messaging.md
  Updated (Tier 1 or 2, target had not diverged from the template):
    - .github/workflows/ci.yml
    - docs/architecture/adr/0001-director-centered-planning-and-closed-loop.md
    - docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md
    - docs/at-tdd/process.md
    - docs/collaboration/design-agreement.md
    - docs/collaboration/session-start-and-resume.md
    - docs/collaboration/personas.md
    - docs/collaboration/ai-human-scheme.md
    - docs/collaboration/branch-commit-pr-discipline.md
    - docs/backlog/README.md
    - scripts/lib/collaboration-template-paths.sh
  Unchanged: 96 file(s)
  Switched to a new branch 'process/update-collab-template-20260818-891b3046'

  Committed sync on branch process/update-collab-template-20260818-891b3046.
  Target has no 'origin' remote. Push and open a PR manually once one is configured.
  ```

  **Confirmations:**
  - `docs/work-plans/WP-*.md` does **not** appear in the "Added" list —
    the fix worked. (Before the fix, `DA-2026-08-18-04`'s Spike Result
    showed `WP-0002-*.md`, `WP-0003-*.md`, `WP-0004-*.md` all listed there;
    with the fix, none of the work-plan files under
    `docs/work-plans/` in this checkout are proposed for addition.)
  - `test -f /tmp/liss-0031-scratch-target/docs/work-plans/.gitkeep`
    succeeded — the fix did not over-exclude; `.gitkeep` is untouched
    (still present from the initial adoption step, never targeted by the
    `WP-*.md` glob).
  - `docs/architecture/adr/0016-standing-two-group-topology-and-backlog-gated-autonomy.md`
    and `docs/collaboration/cross-session-messaging.md` both still appear
    under "Added (new upstream files)" — the original item-0005
    auto-discovery behavior (whole-directory `find` walk, no per-file
    manifest) is unaffected by this fix.
  - `docs/architecture/adr/0017-*.md` does not exist in this checkout as of
    this run (`ls docs/architecture/adr/ | grep 0017` — no match); per the
    task's own instruction this is noted as an observed fact, not treated
    as a problem — a concurrent work plan (`process/adr-0017-portable-loop`)
    had not landed it into this checkout at the time of this test.

  **Cleanup:**

  ```
  $ git worktree remove /tmp/liss-0031-old-template
  $ rm -rf /tmp/liss-0031-scratch-target
  ```

- 2026-08-18 (Implementation group, Implementer): broader regression check
  — ran the existing CI "Check template copy smoke test" step's full
  command sequence locally (adapted to a scratch temp dir under `/tmp`)
  against the fixed checkout. All `test -f`, `grep -q`, and `! ls`
  assertions passed, including the new `docs/work-plans/` assertion. The
  fresh-copy output itself confirmed the fix directly:

  ```
  merge docs/work-plans
  skip template-history docs/work-plans/WP-0002-two-group-send-message-loop.md
  skip template-history docs/work-plans/WP-0004-multi-agent-tool-loop-portability.md
  skip template-history docs/work-plans/WP-0003-coordinator-message-correction.md
  skip template-history docs/work-plans/WP-0001-review-issues-minor-fix-path.md
  skip template-history docs/work-plans/WP-0005-template-propagation-work-plan-exclusion.md
  ```

  One sub-step of that smoke-test sequence,
  `(cd "$tmp/target" && python3 scripts/check-contract-consistency.py --repo .)`,
  fails on the freshly-copied target — but this is a **pre-existing gap,
  not caused by this fix**. Confirmed by re-running the same copy against
  commit `3929c4b` (the commit immediately before this fix, i.e. before
  `docs/work-plans/WP-*.md` was excluded): that copy already failed the
  same check with 3 failures (missing only the 4th, WP-0002-related one,
  which did not exist as an exclusion yet):

  ```
  # against 3929c4b (pre-fix):
  references:
    docs/architecture/adr/0016-...md:6 names 'docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md', which does not exist
    docs/architecture/adr/0016-...md:80 names 'docs/backlog/item-0004-two-group-send-message-loop.md', which does not exist
    docs/collaboration/cross-session-messaging.md:77 names 'docs/backlog/item-0008-coordinator-message-hallucination-correction.md', which does not exist
  contract consistency: 3 failure(s)

  # against 891b304 (post-fix):
  references:
    docs/architecture/adr/0016-...md:6 names 'docs/collaboration/agreements/2026-08-18-two-group-send-message-loop.md', which does not exist
    docs/architecture/adr/0016-...md:23 names 'docs/work-plans/WP-0002-two-group-send-message-loop.md', which does not exist
    docs/architecture/adr/0016-...md:80 names 'docs/backlog/item-0004-two-group-send-message-loop.md', which does not exist
    docs/collaboration/cross-session-messaging.md:77 names 'docs/backlog/item-0008-coordinator-message-hallucination-correction.md', which does not exist
  contract consistency: 4 failure(s)
  ```

  The 3 pre-existing failures come from the *already-existing*
  `agreements/*.md` and `item-*.md` exclusions (present before this fix);
  this fix's `WP-*.md` exclusion adds exactly one more instance of the same
  already-existing class of gap (a checker that runs against a
  target-owned-history-stripped copy, checking references authored against
  the full template repository). This is out of `DA-2026-08-18-04`'s scope
  (which explicitly excludes "any change to `docs/collaboration/*.md`,
  `docs/architecture/adr/*.md`, or any other document content — this item
  is tooling-only"), so it is not fixed here. Flagged as a separate
  follow-up task (spawned via the session's task-suggestion mechanism) for
  the Design & Review group to pick up as its own design-agreement-first
  item, per `docs/collaboration/findings-reuse.md`.

  Run directly against this (fixed) checkout, not a copy — the actual CI
  "Check contract consistency" step (`.github/workflows/ci.yml` line
  148-152) — the check passes cleanly:

  ```
  $ python3 scripts/check-contract-consistency.py --repo .
  contract consistency: all checks passed
  ```

  Also ran, mirroring CI's "Check script syntax" step:

  ```
  $ bash -n scripts/lib/collaboration-template-paths.sh
  (no output; exit 0)
  ```

## Verification

- Fix applied: `scripts/lib/collaboration-template-paths.sh` and
  `.github/workflows/ci.yml`, commit `891b304` on
  `process/template-propagation-work-plan-exclusion`.
- Empirical copy+update re-test (Task 3): pass. `docs/work-plans/WP-*.md`
  no longer appears in the update script's "Added" report;
  `docs/work-plans/.gitkeep` still copies; `cross-session-messaging.md` and
  ADR 0016 auto-discovery still work unaffected. Full command output above.
- CI smoke-test full command sequence (Task 4): pass for every assertion
  including the new one and the fresh-copy `skip template-history` lines
  for all five `docs/work-plans/WP-*.md` files. One unrelated sub-step
  (`check-contract-consistency.py` against the copied target) fails, but
  confirmed pre-existing (already failing at commit `3929c4b`, before this
  fix) and out of this issue's scope; flagged as a separate follow-up.
  `check-contract-consistency.py` run directly against this checkout (the
  actual CI "Check contract consistency" step) passes cleanly.
  `bash -n` syntax check passes.
- Self-review recorded above (short form).
- Next: submit to the Design & Review group's separate-context Reviewer
  pass, per `DA-2026-08-18-04` Task 7.
