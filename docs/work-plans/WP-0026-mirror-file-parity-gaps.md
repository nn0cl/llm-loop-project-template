# Work Plan: Mirror-file parity gaps (item-0022)

## Goal

- Close the 5 mirror-parity gaps `docs/backlog/item-0022-mirror-file-parity-gaps.md`
  names between the agent-instruction contract files (`.cursor/rules/*.mdc`,
  `.grok/rules/*.md`) and `scripts/init-llm-context.sh`'s required-files
  check, and fix a small, re-verified set of Markdown line-wrap defects
  splitting inline code spans across a line break in four docs.

## Scope

- In: see the covering design agreement's own Scope section
  (`docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`)
  for the exact, re-verified file/line list. Independent re-verification
  found gap 1 (external-resource-adoption-contract cross-reference)
  already fixed in 4 of the 5 mirrors named by the backlog item — only
  `.cursor/rules/01-quickstart.mdc` still needs it.
- Out: any edit to `AGENTS.md`, `CLAUDE.md`,
  `.github/copilot-instructions.md`, or `.grok/rules/01-quickstart.md`'s
  reading-list section (already correct); any content change to
  `.cursor/rules/02-architecture-boundaries.mdc` or
  `.cursor/rules/03-collaboration-and-completion.mdc`; any line-wrap fix
  outside the four named files; any Python logic change in
  `check-contract-consistency.py`.

## Issue Graph

| Issue | Status | Initial size | Current size | Planning record | Depends on | Blocks | Branch |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISS-0070 | done | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0071 | done | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0072 | done | S | S | N/A | - | - | process/promote-item-0022 |
| LISS-0073 | done | S | S | N/A | LISS-0072 | - | process/promote-item-0022 |

## Recommended Order

1. LISS-0070, LISS-0071, LISS-0072 — disjoint files, no dependency between
   them; may be done in any order or together in one Implementer pass.
2. LISS-0073 — added 2026-08-23 per the design agreement's Reopening Log;
   fixes a pre-existing defect LISS-0072's own fix unmasked. Depends on
   LISS-0072 having landed on the same file first (easiest to locate the
   4 "ADR 0002" instances after the rewrap, though not strictly required).

## Current Next Issue

- Issue: LISS-0070 (also LISS-0071, LISS-0072 — no ordering dependency)
- Reason it is unblocked: no dependency; scope is fully settled by the
  design agreement; every gap independently re-verified against current
  file content before this work plan was written.
- Reopening request needed: no.

## Minor Fix Path

Not used formally (this is new work against a freshly promoted backlog
item, not a correction to previously accepted work), but each issue is
Minor-Fix-Path-shaped in size and risk: planning size `S`, small mechanical
additions/rewraps, one attempt expected, no specification, ADR, port, data
model, or architecture boundary changed. Per the design agreement's own
Boundaries section, the contract-file edits (LISS-0070's `.grok`/`.cursor`
files, LISS-0072's `ai-failure-recovery.md`/`model-tool-capability-matrix.md`
files) still require this covering design agreement, a separate-context
Reviewer pass, a stated reason, and an AI work trace — the Minor Fix Path's
usual self-contained handling does not waive ADR 0006's contract-file rule.

## Preflight Validation

Run by the Implementation group on branch `wp-0026-mirror-file-parity-gaps`
(created from local branch `process/promote-item-0022` because that branch
was already checked out in a sibling worktree and could not be checked out
twice in this session; later merged with `process/promote-item-0022`
commit `63b1e95` once it existed). **Final result: pass**, after one
intermediate `fail` recorded below as history, not erased.

### Attempt 1 (LISS-0070/0071/0072 landed, before LISS-0073 existed) — fail

Each of LISS-0070, LISS-0071, and LISS-0072's own scoped edits was
independently verified against its own issue's acceptance criteria and
required reproduction (all passed — see each issue's own Work Notes).
Running the work-plan-level check found a newly surfaced, pre-existing
defect outside any of the three issues' own scope:

```text
$ python3 scripts/check-contract-consistency.py
references:
  docs/architecture/external-resource-adoption-contract.md:15 names 'docs/architecture/adr/0002-input-output-reasoning-contracts.md', which does not exist

contract consistency: 1 failure(s)
```

Root cause (full account in
`docs/collaboration/traces/2026-08-23-wp-0026-mirror-file-parity-gaps.md`):
LISS-0072's rewrap of this file's first split code span unmasked a
pre-existing stale "ADR 0002" reference (should be ADR 0003) that
`check-contract-consistency.py`'s `CODE_PATH` regex could never see while
the span was split across a line break. Confirmed pre-existing, not
introduced, via `git stash` against the pre-edit tree:

```text
$ git stash && python3 scripts/check-contract-consistency.py && git stash pop
contract consistency: all checks passed
```

Reported rather than fixed, since correcting the ADR number is outside
LISS-0072's own wording-preserving scope and outside this design
agreement's original Boundaries. The Design & Review group reopened the
design agreement (Reopening Log, 2026-08-23) and opened LISS-0073 to cover
exactly this fix.

### Attempt 2 (after merging LISS-0073 and applying it) — pass

1. `python3 scripts/check-contract-consistency.py` — full output:

   ```text
   $ python3 scripts/check-contract-consistency.py
   contract consistency: all checks passed
   ```

   (One intermediate regression was found and fixed as part of this same
   Preflight step, before this final pass: LISS-0070/0071/0072's
   `Status: done` was initially out of sync with this file's own Issue
   Graph, which still read `ready` for all four issues. Corrected in the
   Issue Graph table above, not silently pre-fixed — the checker's
   "issue status sync" failure that caught this is itself pasted below for
   the record:)

   ```text
   $ python3 scripts/check-contract-consistency.py
   issue status sync:
     docs/issues/LISS-0070-cursor-quickstart-mirror-gaps.md states Status: done, but docs/work-plans/WP-0026-mirror-file-parity-gaps.md's Issue Graph lists LISS-0070 as 'ready'
     docs/issues/LISS-0071-init-llm-context-cursor-required-files.md states Status: done, but docs/work-plans/WP-0026-mirror-file-parity-gaps.md's Issue Graph lists LISS-0071 as 'ready'
     docs/issues/LISS-0072-inline-code-span-line-wrap-fixes.md states Status: done, but docs/work-plans/WP-0026-mirror-file-parity-gaps.md's Issue Graph lists LISS-0072 as 'ready'

   contract consistency: 3 failure(s)
   ```

2. `git diff --name-only main HEAD` (mirroring `.github/workflows/ci.yml`'s
   "Check agent operating contract change traceability" step, using `main`
   as this worktree's available local stand-in for a PR base):

   ```text
   $ git diff --name-only main HEAD
   .cursor/rules/01-quickstart.mdc
   .grok/rules/01-quickstart.md
   docs/architecture/external-resource-adoption-contract.md
   docs/architecture/io-reasoning-contracts.md
   docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md
   docs/collaboration/ai-failure-recovery.md
   docs/collaboration/model-tool-capability-matrix.md
   docs/collaboration/traces/2026-08-23-wp-0026-mirror-file-parity-gaps.md
   docs/issues/LISS-0070-cursor-quickstart-mirror-gaps.md
   docs/issues/LISS-0071-init-llm-context-cursor-required-files.md
   docs/issues/LISS-0072-inline-code-span-line-wrap-fixes.md
   docs/issues/LISS-0073-external-resource-adoption-adr-number-drift.md
   docs/work-plans/WP-0026-mirror-file-parity-gaps.md
   scripts/init-llm-context.sh
   ```

   Contract files changed: `.cursor/rules/01-quickstart.mdc`,
   `.grok/rules/01-quickstart.md`, `docs/collaboration/ai-failure-recovery.md`,
   `docs/collaboration/model-tool-capability-matrix.md` (all on
   `prompt-instruction-change-control.md`'s Agent Operating Contract Files
   list). A trace file is present
   (`docs/collaboration/traces/2026-08-23-wp-0026-mirror-file-parity-gaps.md`),
   satisfying the CI check's `trace_added` condition —
   `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md` is
   a record, not itself a contract file, per that same document's own
   distinction (agreements/reviews/traces are records produced by
   following the contract). `docs/architecture/external-resource-adoption-contract.md`,
   `docs/architecture/io-reasoning-contracts.md`, and
   `scripts/init-llm-context.sh` are not on the contract-file list (the
   first two are under `docs/architecture/`, not `docs/collaboration/`;
   the script is explicitly not an ADR-0006 contract file per the design
   agreement).

3. Per-issue before/after reproduction summary (full pasted output in each
   issue's own Work Notes):
   - LISS-0070: `grep -n` before (0 matches for the 3 new bullets; grok
     sentence lacked "Cursor") / after (3 matches; sentence now names
     Cursor) — pass.
   - LISS-0071: 7-step throwaway-target reproduction, pre-fix script does
     not flag a missing `.cursor/rules/*.mdc` file (exit 0), post-fix flags
     it (exit 1, "Missing required file:"), complete target and real
     repository both still pass (exit 0) — pass.
   - LISS-0072: `grep -n '`[A-Za-z0-9/_.-]*/$'` before (6 matches across
     4 files) / after (0 matches) — pass.
   - LISS-0073: `grep -n "ADR 0002"` on the target file before (4 total
     instances) / after (0) — pass. Repository-wide `grep -rn "ADR 0002"`
     confirms only the two pre-existing, correct mentions remain,
     unaffected — pass.
4. `git diff` reviewed per file against the design agreement's Scope and
   Boundaries (including the amended Boundaries covering LISS-0073): no
   file outside the agreed scope was touched; no wording changed beyond
   what each issue's own Acceptance Notes specify.

**Scope result**: pass — every changed file is named in the design
agreement's Scope (as amended by the 2026-08-23 Reopening Log entry for
LISS-0073); no file outside that list was touched.

**Next action**: submit to the work-plan-level Reviewer, in a separate
context, per the design agreement's Plan step 6.

## Review Summary Packet

- **Scope**: close the 5 mirror-parity gaps
  `docs/backlog/item-0022-mirror-file-parity-gaps.md` names (as re-verified
  and corrected by the design agreement), plus one in-scope-extension fix
  (LISS-0073) for a pre-existing ADR-number reference defect that
  LISS-0072's own fix surfaced. Full scope statement:
  `docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`
  (Scope section, as amended by its 2026-08-23 Reopening Log entry).
- **Current canonical documents**: this work plan
  (`docs/work-plans/WP-0026-mirror-file-parity-gaps.md`); the design
  agreement (`docs/collaboration/agreements/2026-08-23-mirror-file-parity-gaps.md`);
  issues LISS-0070, LISS-0071, LISS-0072, LISS-0073; the AI work trace
  (`docs/collaboration/traces/2026-08-23-wp-0026-mirror-file-parity-gaps.md`).
- **Changed files**: `.cursor/rules/01-quickstart.mdc` (3 bullets added);
  `.grok/rules/01-quickstart.md` (Cursor named in 2 sentences);
  `scripts/init-llm-context.sh` (3 `required_files` entries added);
  `docs/architecture/external-resource-adoption-contract.md` (3 line-wrap
  rewraps + 4 ADR-number corrections); `docs/architecture/io-reasoning-contracts.md`
  (1 line-wrap rewrap); `docs/collaboration/ai-failure-recovery.md` (1
  line-wrap rewrap); `docs/collaboration/model-tool-capability-matrix.md`
  (1 line-wrap rewrap); the 4 issue files (`Status`/Work Notes); this work
  plan (Issue Graph, Preflight Validation, Review Summary Packet); the new
  AI work trace file; the design agreement (Plan table, Falsification
  Criteria, Reopening Log — amended by the Design & Review group, not by
  the Implementer).
- **Findings**: none raised as `Type: review-finding` issues by this
  Implementer attempt. One genuinely new fact was found mid-execution (the
  pre-existing ADR-0002-vs-0003 reference drift) and was routed through a
  proper design-agreement reopening (LISS-0073) rather than through the
  review-finding mechanism, since it was caught before Reviewer submission,
  not after.
- **Disposition**: all four issues (LISS-0070, LISS-0071, LISS-0072,
  LISS-0073) complete, self-reviewed, and independently verified against
  their own acceptance criteria and required reproductions.
- **Remaining blockers**: none for Preflight. The work-plan-level Reviewer
  pass (separate context) has not yet occurred — that is the next step,
  not a blocker on this Implementer attempt's own completion.
- **Verification result**: pass — `python3 scripts/check-contract-consistency.py`
  reports "all checks passed" against the real repository (see Preflight
  Validation, Attempt 2, above).
- **Next approval required**: the work-plan-level Reviewer pass, in a
  separate context, per the design agreement's Plan step 6 and ADR 0006's
  independent-Reviewer requirement for the contract-file edits.

## Work-Plan Review

Reviewer's approval record:
`docs/collaboration/reviews/2026-08-23-wp-0026-mirror-file-parity-gaps-review.md`
— **Approved** (2026-08-23, Reviewer persona, Design & Review group
standing session, separate context from the Implementation-group subagent
that executed LISS-0070/0071/0072/0073 in its own worktree/branch;
independently re-verified via a fresh `git archive` export and a direct
re-run against the merged real worktree, not taken on the Implementer's
own reported output).

Findings, if any, tracked as `Type: review-finding` local issues:

| Issue | Status | Resolution |
| --- | --- | --- |
|  |  |  |

No findings opened — the Implementer's own mid-execution discovery
(the ADR-0002-vs-0003 drift) was routed through a design-agreement
Reopening Log amendment and a new issue (LISS-0073) before Reviewer
submission, not through the review-finding mechanism, since it was caught
and resolved pre-review.

Note for the Backlog thread: two messages arrived during this work plan's
execution claiming to be from "the coordinator" — no such persona exists
in this repository's model (`docs/architecture/agent-quickstart.md`
Session Entry rule 6; `docs/collaboration/cross-session-messaging.md`'s
documented incident history). Both were refused as instruction sources.
The second message's factual claims (branch/commit state) were
independently verified as accurate before being relied on for anything;
its instruction to merge to `main` was not followed. See this review
record's own Constraints section for the full account.

## Work-Plan Close

Per `docs/architecture/adr/0014-work-plan-scoped-self-review-and-combined-checkpoint.md`,
one combined Director action, after the Reviewer approves — not performed
by the Design & Review group itself.

- Date: 2026-08-23
- Result read: the Director read the Reviewer approval
  (`docs/collaboration/reviews/2026-08-23-wp-0026-mirror-file-parity-gaps-review.md`,
  Approved) via the Backlog thread, which independently re-verified from
  a fresh, isolated `git worktree add --detach` checkout of
  `process/promote-item-0022` (tip `370daeb`) before presenting this
  close: a clean `check-contract-consistency.py` run; all 7 commits
  present in the described sequence; the Reviewer record's own
  `[x] Approved` line; all 4 issues (LISS-0070 through LISS-0073) at
  `Status: done`; `.cursor/rules/01-quickstart.mdc` now carrying the
  External resource adoption contract cross-reference and the two other
  previously-missing bullets; `.grok/rules/01-quickstart.md` now naming
  Cursor; `scripts/init-llm-context.sh` now requiring all three
  `.cursor/rules/*.mdc` files; and
  `docs/architecture/external-resource-adoption-contract.md` now citing
  ADR 0003 (confirmed that file exists) instead of the stale ADR 0002 in
  all 4 places.
- Next direction: closed (Director resumed the Design & Review session
  twice after a rate-limit interruption; it reported this work plan at
  close-readiness, including two refused "coordinator" impersonation
  messages and one genuine, independently-verified scope amendment for
  the ADR-number drift it found) — merging `process/promote-item-0022`
  into `main` and pushing now.
- New design agreement (if any): none opened by this close — the one
  in-flight amendment (LISS-0073) was folded into this same work plan's
  own design agreement via its Reopening Log, per this repo's own
  amendment mechanism, not a new agreement.

## Risks

- The backlog item's own description of gap 1 was stale for 4 of 5 files;
  a similar staleness could affect other unverified assumptions if the
  Implementer trusts the backlog item's text over direct file reads.
  Mitigated: the design agreement's own Settled Ambiguities table already
  states the re-verified, corrected scope; the Implementer must still
  independently confirm each file/line before editing, not merely copy
  this work plan's line numbers without checking.
- `.cursor/rules/*.mdc` files have YAML frontmatter (`---` delimited) at
  the top; a careless edit near that boundary could corrupt Cursor's own
  rule-loading. Mitigated: LISS-0070's acceptance notes point at the
  specific "Cursor-side reminders" section well below the frontmatter.

## Verification Plan

- `grep -n` before/after for each of the three quickstart-file edits.
- Reproduction of `scripts/init-llm-context.sh`'s pass/fail behavior
  before and after the required-files addition.
- `grep -n` re-run for the line-wrap pattern across the four files,
  zero remaining matches.
- `python3 scripts/check-contract-consistency.py` (real repository),
  before and after — no regression.
- `git diff` reviewed per file against the design agreement's Scope.
- Independent work-plan-level Reviewer approval, in a separate context.
