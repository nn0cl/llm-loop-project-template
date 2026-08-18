# LISS-0031: Exclude docs/work-plans/WP-*.md from template propagation

## Metadata

- Local issue ID: LISS-0031
- GitHub issue: none
- Status: ready
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

## Verification

- Pending Implementation-group execution.
