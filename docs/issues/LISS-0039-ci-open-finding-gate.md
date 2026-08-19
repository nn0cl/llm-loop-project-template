# LISS-0039: Deterministic gate for open review-finding issues

## Metadata

- Local issue ID: LISS-0039
- GitHub issue: none
- Status: done
- Phase: phase-0-design
- Type: tooling-enhancement
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A
- Owner/agent: Implementer, Claude Sonnet 5 via Claude Code, Implementation
  group session
- Related branch: process/ci-open-finding-gate

## Summary

- Add `check_open_findings_gate` to `scripts/check-contract-consistency.py`:
  for each `docs/work-plans/WP-*.md` whose "Work-Plan Close" section states
  a non-placeholder `Date:`, read its "Work-Plan Review" findings table;
  for each listed issue ID, read the issue's own live `Status:`; if
  `[findings].block_work_plan_done_on_open_findings` is `true` (from
  `docs/collaboration/loop-settings.toml`, default `true` when absent) and
  the status is neither `closed` nor `wont_do`, report a failure.

## Acceptance Notes

- Clean pass against current `HEAD`.
- Constructed synthetic failure case (open finding, flag `true`) correctly
  flagged, with actual command output pasted.
- Constructed synthetic pass case (same finding, flag `false`) correctly
  passes, confirming the flag is actually read, not ignored.
- Module docstring's numbered check list updated.
- Reuses existing script helpers (`read`, `glob`) rather than new
  infrastructure or a separate script.
- Self-review recorded (full form — planning size `M`).

## Review Finding Record

N/A.

## Dependencies

- Parent: docs/backlog/item-0003-ci-open-finding-gate.md
- Depends on: none
- Blocks: none
- Related: `docs/collaboration/findings-reuse.md`,
  `docs/collaboration/loop-settings.toml`, WP-0007/LISS-0035 (the sibling
  infrastructure this issue extends)

## Decisions Not Settled by the Design Agreement

- None identified.

## Context

- Included: `docs/backlog/item-0003-*.md`, `DA-2026-08-19-03`,
  `scripts/check-contract-consistency.py` (whole file), every current
  `docs/work-plans/WP-*.md`'s "Work-Plan Review"/"Work-Plan Close" section
  shape, `docs/collaboration/loop-settings.toml`,
  `docs/collaboration/findings-reuse.md`.
- Omitted: `docs/issues/LISS-0003-*.md`'s own correction (explicitly out of
  scope).
- Assumptions: none beyond the design agreement's own settled points.

## AI Planning Records

### AIP-0039-001

- Status: accepted
- Created by:
  - Agent/environment: Claude Sonnet 5 via Claude Code, Design & Review
    group standing session
  - Model as displayed: Claude Sonnet 5
  - Reasoning setting as displayed: N/A
  - N/A reason: not surfaced in this environment
- Created at: 2026-08-19
- Planning size: M
- Intended execution route: Implementation-group agent, Architecture Path,
  one new function plus its wiring
- Compatibility state: Verified — confirmed the exact findings-table shape
  by reading several real work-plan files
- Intended scope: `scripts/check-contract-consistency.py` only
- Estimated token range: 6,000-14,000 tokens
- Estimated token midpoint: 9,000
- Token metric: approximate output tokens including synthetic-test
  construction
- Estimation basis: comparable to WP-0007's individual check functions
- Assumptions: single execution attempt
- Confidence: medium
- Revises: none
- Revision reason: N/A
- Superseded by: none

## References

- `docs/collaboration/agreements/2026-08-19-ci-open-finding-gate.md`
  (`DA-2026-08-19-03`)

## Work Notes

- 2026-08-19 (Design & Review group, Planner/Specifier): issue created from
  `docs/backlog/item-0003-*.md`'s promotion. Found `LISS-0003` as a real,
  currently-live `Type: review-finding`/`Status: resolved` case during the
  spike, confirmed it does not trigger the new gate (not referenced in any
  work plan's findings table) and disclosed that explicitly rather than
  silently. Dispatched to the Implementation group.
- 2026-08-19 (Implementation group, Implementer persona): the dispatched
  child worktree's own `HEAD` (`11d5898`) did not contain
  `DA-2026-08-19-03` or this issue file — confirmed `6161241` (the commit
  that introduced them) was reachable and branched
  `process/ci-open-finding-gate` from it directly, per the task's own
  branch-setup instructions. Implemented `check_open_findings_gate` and its
  `_block_work_plan_done_on_open_findings` helper in
  `scripts/check-contract-consistency.py`, wired into `main()` and the
  module docstring's numbered Checks list (now 9 entries: the pre-existing
  8 plus this one). Self-review below.

### Self-review (full form, planning size `M`)

- Artifact: `scripts/check-contract-consistency.py` —
  `check_open_findings_gate`, `_block_work_plan_done_on_open_findings`, the
  `main()` wiring, and the docstring's Checks list update.
- Covering design agreement: `DA-2026-08-19-03`.
- Findings-table parsing approach: bound each `docs/work-plans/WP-*.md`
  file's `## Work-Plan Review` section with the same
  `r"^## <heading>\n(.*?)(?=^## |\Z)"` anchor `check_issue_status_sync`
  already uses for `## Issue Graph`, then scan only lines shaped
  `^\| (LISS-\d{4}) \|` inside that bounded section for the Issue column.
  This reads the structured table row only, never a finding's own free-text
  content — directly answering `DA-2026-08-19-03`'s first Falsification
  Criterion.
- `Date:` placeholder-detection logic: bound `## Work-Plan Close` the same
  way, extract the `- Date: (.+)` value, and treat the plan as closed only
  if that value contains a `\d{4}-\d{2}-\d{2}`-shaped substring. Every real
  `Date:` value currently in this repository is either that exact ISO shape
  (7 work plans) or the literal placeholder `_pending Director action_` (3
  work plans, including this one, `WP-0011`) — confirmed by direct
  inspection (below), so the substring test correctly separates them without
  needing to anchor on the placeholder's exact wording.

### Deterministic Verification Output

Clean pass on current `HEAD` (this branch, after the change):

```text
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
```

Direct inspection confirming the clean pass is genuine (no closed work plan
currently has a filled findings-table row to react to), not merely assumed:

```text
$ python3 - <<'PYEOF'
import re, glob, os
repo = "."
for path in sorted(glob.glob(os.path.join(repo, "docs/work-plans/WP-*.md"))):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    close_section = re.search(r"^## Work-Plan Close\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if close_section is None:
        print(path, "NO CLOSE SECTION")
        continue
    date_match = re.search(r"^- Date: (.+)$", close_section.group(1), re.MULTILINE)
    is_closed = bool(date_match and re.search(r"\d{4}-\d{2}-\d{2}", date_match.group(1)))
    review_section = re.search(r"^## Work-Plan Review\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    rows = re.findall(r"^\| (LISS-\d{4}) \|", review_section.group(1), re.MULTILINE) if review_section else []
    print(os.path.basename(path), "closed=", is_closed, "rows=", rows)
PYEOF
./docs/work-plans/WP-0001-review-issues-minor-fix-path.md NO CLOSE SECTION
WP-0002-two-group-send-message-loop.md closed= True rows= []
WP-0003-coordinator-message-correction.md closed= True rows= []
WP-0004-multi-agent-tool-loop-portability.md closed= True rows= []
WP-0005-template-propagation-work-plan-exclusion.md closed= True rows= []
WP-0006-quality-gate-hooks-and-perspectives-doc.md closed= True rows= []
WP-0007-document-consistency-drift-checks.md closed= True rows= []
WP-0008-coordinator-role-inoculation-rule.md closed= True rows= []
WP-0009-contract-reviewer-v230.md closed= False rows= []
WP-0010-adr-loop-ledgers.md closed= False rows= []
WP-0011-ci-open-finding-gate.md closed= False rows= []
```

Synthetic failure case: copied the whole worktree to an isolated scratch
directory (`.git` removed, so `check_id_range_collisions`/
`check_version_claims` degrade to no-op rather than reading this
repository's real git history), edited the copy's `WP-0006`'s empty
findings-table row to `| LISS-0003 | resolved | synthetic test row for
open-findings-gate verification |` (a closed work plan, `Date: 2026-08-18`,
pointing at the real `LISS-0003`, whose real `Status:` is `resolved` — the
exact shape `DA-2026-08-19-03`'s Spike Result names), left
`block_work_plan_done_on_open_findings = true` (the fixture's inherited
default), and ran:

```text
$ python3 scripts/check-contract-consistency.py --repo <scratch>/fixture-fail
open findings gate:
  docs/work-plans/WP-0006-quality-gate-hooks-and-perspectives-doc.md lists LISS-0003 in its Work-Plan Review findings table, but docs/issues/LISS-0003-code-path-filter-and-disclosure-history.md states Status: 'resolved' — neither 'closed' nor 'wont_do'

contract consistency: 1 failure(s)
[exit code 1]
```

Synthetic pass case: copied `fixture-fail` to `fixture-pass`, changed only
`docs/collaboration/loop-settings.toml`'s
`block_work_plan_done_on_open_findings` from `true` to `false` (same
synthetic `WP-0006` finding row, unchanged), and ran:

```text
$ python3 scripts/check-contract-consistency.py --repo <scratch>/fixture-pass
contract consistency: all checks passed
```

This proves the setting is actually read, not hardcoded: the only variable
between the two fixture runs is the flag, and the outcome flips with it.

Real working tree, confirmed clean after removing both scratch fixtures:

```text
$ git status --short
 M scripts/check-contract-consistency.py
```

(Only this issue's/work-plan's own doc edits and the script change are
expected here; the fixture directories never existed inside this worktree.)

### Falsification Search

| # | Failure scenario searched for | Grounds it does not occur | Result |
|---|---|---|---|
| 1 | The check infers a finding-to-work-plan link from a finding's own free text instead of the work plan's structured findings table (`DA-2026-08-19-03` Falsification Criterion 1). | The row regex (`^\| (LISS-\d{4}) \|`) only matches inside the bounded `## Work-Plan Review` section and only a `\|`-prefixed table row; plain-text mentions of an issue ID elsewhere in that section (e.g. `WP-0003`'s "Reviewer's approval record... that produced LISS-0028" sentence) are not table rows and do not match. | not reproduced |
| 2 | The check ignores `[findings].block_work_plan_done_on_open_findings` and always/never fires regardless of its value (`DA-2026-08-19-03` Falsification Criterion 2). | The synthetic failure case (flag `true`, default) and synthetic pass case (flag `false`) are identical in every other respect (same copied fixture, same synthetic finding row) and produce opposite results — the flag alone changes the outcome. | not reproduced |
| 3 | The check is built as a parallel script/mechanism instead of extending `scripts/check-contract-consistency.py` (`DA-2026-08-19-03` Falsification Criterion 3). | `check_open_findings_gate` and its helper are functions added to that one existing file, reusing its `read`, `read_optional`, and `glob` helpers, wired into that file's own `main()`. No new file was created. | not reproduced |
| 4 | False positive against this repository's own real work-plan history — the check fires on `HEAD` where nothing should be flagged. | Clean pass on `HEAD`, confirmed by the direct-inspection script above: all 7 currently-closed work plans have an empty findings-table row (`rows=[]`); there is nothing for the check to react to yet, by enumeration rather than by assumption. | not reproduced |
| 5 | The placeholder `Date:` value (`_pending Director action_`) is misdetected as a real closing date, prematurely gating a still-open work plan (e.g. `WP-0009`, `WP-0010`, `WP-0011` itself). | The literal placeholder string contains no `\d{4}-\d{2}-\d{2}`-shaped substring, so the regex correctly reports `is_closed=False` for all three still-open work plans in the direct-inspection output above. | not reproduced |
| 6 | A findings-table row names a `LISS-*` issue file that no longer exists (deleted issue), causing a crash or a fabricated status. | Guarded by `if not issue_paths: continue` — the row is skipped silently rather than raising or inventing a status. Not exercised by a real file today (no currently-live findings-table row names a deleted issue), but confirmed by code inspection. | not reproduced |

### Scenarios Not Searched

- A findings-table row whose Issue column cell contains more than one issue
  ID, or malformed markdown that still partially matches the row regex —
  not constructed as a synthetic case; every real and synthetic row used one
  well-formed ID per row, matching every existing work plan's actual usage.
- Behavior when `docs/collaboration/loop-settings.toml`'s `[findings]`
  section itself is malformed (e.g. the key present twice with different
  values) — not exercised; the regex takes the first match via
  `re.search`, which is the same first-match behavior the rest of this
  script's regex-based parsing already relies on throughout.

## Verification

- Clean pass on `HEAD`: `contract consistency: all checks passed` (see
  Deterministic Verification Output above).
- Synthetic failure case: constructed and confirmed to fail with the
  expected, correctly attributed message (above).
- Synthetic pass case (same finding, flag `false`): constructed and
  confirmed to pass, proving the flag is read rather than hardcoded
  (above).
- Full-form self-review recorded above (planning size `M`).
- Real working tree confirmed clean after fixture cleanup (above).
- Work-plan-level Reviewer pass: pending, per `DA-2026-08-19-03`'s Plan
  Task 5 — to independently construct its own synthetic failure case, not
  only re-read this one.
