# Review record: LISS-0045 / item-0014 (WP-0014 post-close CI fixes)

## Metadata

- Reviewer persona: Reviewer, separate context (fresh session; no prior
  memory of this fix; state recovered only from repository artifacts and
  live `gh`/`python3` output, not from any chat transcript or summary).
- Review type: Minor Fix Path separate-context Reviewer confirmation, per
  `CLAUDE.md`'s "Minor Fix Path" and `docs/architecture/adr/0015-review-cost-discipline.md`
  (short form; not a full work-plan Reviewer pass).
- Subject: `docs/issues/LISS-0045-wp-0014-post-close-ci-fixes.md`, authorized
  by `docs/backlog/item-0014-wp-0014-post-close-ci-fixes.md`
  (`Status: promoted`).
- Commit reviewed: `68cf5d6` (`fix: resolve PR #17 CI failures in WP-0014
  content (LISS-0045, item-0014)`) on `process/backlog-item-0012-and-0013`,
  fetched fresh from `origin` and checked out detached for this review.
- Date: 2026-08-19

## What was checked

1. **Original CI failure real, now fixed.**
   - `gh pr checks 17 --repo nn0cl/llm-loop-project-template` — `Repository
     sanity  pass  9s`.
   - `gh pr view 17 --repo nn0cl/llm-loop-project-template --json
     state,mergeable,statusCheckRollup` — one check run, `Repository
     sanity`, `conclusion: SUCCESS`; PR `state: OPEN`, `mergeable:
     MERGEABLE`.
   - Independently re-ran `python3 scripts/check-contract-consistency.py`
     against the actual current tree at `68cf5d6` (not trusted from
     LISS-0045's own report): output is `contract consistency: all checks
     passed`, exit code `0`. Neither a `references:` nor an `open findings
     gate:` section header appears in the output — both previously-failing
     checks are confirmed silent.

2. **Fix 1 correct and structurally sound, not just "passes today."**
   - Read `scripts/check-contract-consistency.py`'s reference-scanning
     regexes directly: `CODE_PATH = re.compile(r"` `([^`\s]+\.(?:md|mdc|sh|py|yml|yaml|toml|json))` `")`
     only matches a target **wrapped in backticks**. The new ADR 0020 Rule 4
     wording states `trace-topic-register.md` as plain prose (no backticks
     around it) — structurally outside what `CODE_PATH` can ever match,
     regardless of whether the file exists anywhere. The one backticked,
     `.md`-suffixed target the new sentence does contain,
     `` `docs/spike/case-0001-document-log-lifecycle-management/case.md` ``,
     is a real in-repo relative path — confirmed to exist
     (`ls docs/spike/case-0001-document-log-lifecycle-management/case.md`)
     — so it resolves cleanly rather than by exemption.
   - `docs/architecture/adr/` is not in `RECORD_DIRS`, so ADR files are
     scanned (this is why the original absolute-path citation was caught);
     `docs/spike/` is in `RECORD_DIRS`, which is why the spike case
     document's own backticked `qpex` absolute paths (used as sourcing
     evidence, several still present) are correctly never scanned. This is
     consistent, not a coincidence the fix relies on.

3. **Fix 1 preserves ADR 0020's meaning.**
   - `git show d57606a:docs/architecture/adr/0020-document-and-log-lifecycle-model.md`
     diffed against the current file: exactly one hunk, lines ~150-153,
     Rule 4's citation sentence. Before: `` `qpex`'s own stated rule
     (`/Users/nn0cl/Documents/git/qpex/docs/architecture/trace-topic-register.md`,
     a different, external repository's file, quoted and endorsed by
     item-0012 itself) ``. After: `` `qpex`'s own stated rule — a file named
     trace-topic-register.md in a different, external repository, not part
     of this template (full citation in
     `docs/spike/case-0001-document-log-lifecycle-management/case.md`'s
     Research Log), quoted and endorsed by item-0012 itself ``. Same claims
     preserved (external `qpex` file, not part of this template, cited and
     endorsed by item-0012); only the checkable-path formatting is removed,
     with a real in-repo pointer substituted for anyone who wants the full
     citation. No other line in the diff — Rules 1-3, 5-7, and the rest of
     the document are untouched.

4. **Fix 2 correct and complete, Work-Plan Close untouched.**
   - `git show d57606a:docs/work-plans/WP-0014-document-log-lifecycle-model.md`
     diffed against the current file: one hunk, the Work-Plan Review
     findings table (previously one `LISS-0044 | proposed | ...` row) and
     the prose beneath it. `LISS-0044` no longer appears as a table row;
     the table's header/separator remain, followed by one further blank
     `|  |  |  |` row (see Note below), then new prose naming `LISS-0044`,
     its `proposed` status, and the reason it is deliberately excluded from
     the blocking table, with links to the issue and the WP-0014 review
     record.
   - `check_open_findings_gate`'s own row-matching regex
     (`r"^\| (LISS-\d{4}) \|"`) requires a literal `LISS-####` token in the
     first cell — the leftover blank row does not match this pattern, so it
     is inert to the gate. Confirmed by direct reading of the check
     function's source, not by inference from the passing run alone.
   - Confirmed via line-range check that the diff's only hunk sits above
     line 150; the `## Work-Plan Close` section (line 150 onward, `Date:
     2026-08-19`, Director close narrative) is byte-identical before and
     after — outside the diff entirely.

5. **LISS-0044 itself untouched.**
   - `git log --oneline -- docs/issues/LISS-0044-record-dirs-archive-exclusion-gap.md`
     shows its last touching commit is `ead81f5` (WP-0014's own Reviewer
     approval, well before `d57606a`/item-0014's promotion) — no commit in
     `d57606a..68cf5d6` touches this path at all.
   - Direct read of the file at `68cf5d6`: `Status: proposed`, matching the
     boundary item-0014 and LISS-0045 both state.

6. **Scope discipline.**
   - `git diff d57606a..68cf5d6 --stat`:
     `docs/architecture/adr/0020-document-and-log-lifecycle-model.md` (9
     lines), `docs/issues/LISS-0045-wp-0014-post-close-ci-fixes.md` (new,
     225 lines — the correction's own issue record), and
     `docs/work-plans/WP-0014-document-log-lifecycle-model.md` (14 lines).
     Nothing else changed. Matches item-0014's authorized scope exactly.

7. **Context separation of this confirmation.**
   - LISS-0045's own Metadata (`Owner/agent`) and Work Notes state plainly
     that the fix was made directly by the Design & Review group (not
     dispatched to an Implementer), and that "separate-context Reviewer
     confirmation still required and obtained per Minor Fix Path"; its
     Verification section lists the confirmation as "pending — dispatched
     as a fresh agent." This review is that dispatched fresh context: no
     chat transcript was read, and every claim above was independently
     re-derived from `git`, `gh`, and the script's own current source
     rather than accepted from LISS-0045's narrative.

## Deterministic verification (this review's own run)

```
$ python3 scripts/check-contract-consistency.py
contract consistency: all checks passed
$ echo $?
0
```

```
$ gh pr checks 17 --repo nn0cl/llm-loop-project-template
Repository sanity	pass	9s	https://github.com/nn0cl/llm-loop-project-template/actions/runs/32263166210/job/96101092337
```

## Falsification search

- Could the reference scanner still flag the new ADR 0020 wording under a
  different code path (e.g. `MD_LINK`)? No — `MD_LINK` requires markdown
  link syntax `[...](...)`, absent here; the new sentence is plain prose
  plus one backticked in-repo path that resolves.
- Could the leftover blank findings-table row in WP-0014 still trip
  `check_open_findings_gate`? No — the gate's regex requires a literal
  `LISS-\d{4}` token in the row's first cell; a row of empty cells does not
  match, confirmed by reading the regex directly, and by this review's own
  clean `check-contract-consistency.py` run showing no `open findings
  gate:` section.
- Could the rewording of ADR 0020 Rule 4 have silently changed what the
  rule requires (not just how it's cited)? No — the diff is confined to the
  citation clause; the rule's actual normative sentence ("a new trace is
  not created when...") is byte-identical before and after.
- Could this fix have touched WP-0014's already-Director-recorded
  Work-Plan Close section? No — confirmed by direct diff; the only hunk is
  above the `## Work-Plan Close` heading.
- Could LISS-0044 have been reclassified or closed as a side effect? No —
  no commit in the reviewed range touches its file; `Status: proposed`
  confirmed by direct read at `68cf5d6`.
- Could this fix have exceeded item-0014's authorized scope? No —
  `git diff d57606a..68cf5d6 --stat` shows exactly the two authorized files
  plus the new LISS-0045 issue record documenting the fix itself.

## Non-blocking observation

WP-0014's Work-Plan Review findings table is not literally row-free: after
removing the `LISS-0044` row, one empty data row (`|  |  |  |`) remains
between the header/separator and the new prose. This is cosmetic, not a
correctness defect — `check_open_findings_gate`'s regex cannot match it
(confirmed above), and it does not misrepresent findings status. Worth a
follow-up cosmetic touch-up whenever that file is next edited for another
reason; not worth reopening this Minor Fix Path correction for on its own.

## Decision

**Approved.**

All items in item-0014's Summary are independently confirmed fixed, both
fixes are structurally sound (not merely passing under today's file
layout), neither fix altered substantive meaning or exceeded authorized
scope, LISS-0044 remains untouched at `Status: proposed`, and this
confirmation itself satisfies context separation — it was produced in a
fresh context with no access to the fix's own reasoning, verified solely
against repository artifacts, live `gh` state, and an independently
re-run `scripts/check-contract-consistency.py`. PR #17's CI is green.
