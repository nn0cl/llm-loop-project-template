# LISS-0069: Add Antigravity to the contract-file list and Per-Agent-Tool Rule Applicability Registry

## Metadata

- Local issue ID: LISS-0069
- GitHub issue: none
- Status: done
- `Status` is the authoritative lifecycle field. For `Type: review-finding`,
  use `proposed | accepted | in_progress | resolved | closed | wont_do`.
- Phase: Architecture Path
- Type: architecture
- Priority: medium
- Initial planning size: M
- Current planning size: M
- Reclassification reason: N/A — first attempt. `M` because it edits an
  agent operating contract file (ADR 0006 governance: separate-context
  Reviewer plus mandatory AI work trace) even though the actual content
  is narrowly scoped and fully specified below.
- Owner/agent: Implementation group (dispatched from
  `docs/work-plans/WP-0025-ai-tool-support-status-survey.md`)
- Related branch: process/item-0021-status-survey (this issue's own
  execution branch is created off it, per the work plan)

## Summary

`docs/spike/case-0004-ai-tool-support-status-survey/case.md` found
Antigravity reads `AGENTS.md` natively (confirmed via
`ai.google.dev/gemini-api/docs/antigravity-agent`, a Google-official
domain) — the same file this repository already maintains as its
cross-tool canonical source, the same situation Codex is already in.
`docs/collaboration/prompt-instruction-change-control.md`'s own "Agent
Operating Contract Files" list and "Per-Agent-Tool Rule Applicability
Registry" table do not currently name Antigravity at all. This issue adds
it, stated explicitly rather than left implicit — matching this
repository's own discipline of never leaving a tool's support status to
be inferred.

## Acceptance Notes

### Before editing: independently re-verify the status report's own key citations

This issue's own scope includes a genuine, separate-context fact-check —
do not treat `docs/architecture/ai-tool-support-status.md` and
`docs/spike/case-0004-.../case.md` as already-verified just because they
were produced by the Design & Review group. Re-fetch at least these two
URLs directly and confirm the quotes match:

1. `https://ai.google.dev/gemini-api/docs/antigravity-agent` — confirm it
   states Antigravity reads `AGENTS.md` for project instructions.
2. `https://antigravity.google/docs/subagents/` — confirm the "maximum
   nesting depth of 10 levels" claim and the "peer agents whose ID is
   known" quote.

If either does not match what the status report or spike case claims,
STOP and report the discrepancy — do not silently correct the document
yourself or proceed as if the mismatch does not matter.

### The edit itself

In `docs/collaboration/prompt-instruction-change-control.md`:

1. Add a new bullet to the "Agent Operating Contract Files" list (after
   the existing `docs/templates/*.md` bullet, or wherever reads most
   naturally — this file's own convention, not a fixed position):

   ```markdown
   - `AGENTS.md` is also read natively by Codex CLI and by Google
     Antigravity (confirmed via primary source,
     `docs/spike/case-0004-ai-tool-support-status-survey/case.md`) —
     neither needs its own dedicated mirror file for this reason.
   ```

2. Add a new row to the "Per-Agent-Tool Rule Applicability Registry"
   table:

   ```markdown
   | Canonical source (also read directly, no mirror needed) | Codex CLI, Google Antigravity | Both tools read `AGENTS.md` natively — confirmed via primary source for Antigravity in `docs/spike/case-0004-ai-tool-support-status-survey/case.md`; no `.antigravity/` or equivalent mirror file exists or is needed for this reason. |
   ```

   Place it in the existing table, after the existing `Canonical source`
   row for `AGENTS.md` itself (or merge into that same row if that reads
   more naturally as a table edit — either is acceptable, state which was
   chosen in this issue's own Work Notes).

Do not touch any other row, bullet, or section of this file.

### Mandatory AI work trace

Create
`docs/collaboration/traces/2026-08-20-ai-tool-support-status-survey.md`
using `docs/templates/ai-work-trace.md`. State: which contract file
changed (`prompt-instruction-change-control.md`), why (Antigravity's own
confirmed `AGENTS.md`-native status, found by `case-0004`'s survey, was
previously undocumented), and what agent behavior is expected to change
(a future session working with Antigravity now has an explicit,
documented answer that no dedicated mirror file is needed for it, instead
of the gap being silently absent).

## Dependencies

- Parent: `docs/work-plans/WP-0025-ai-tool-support-status-survey.md`
- Depends on: `docs/spike/case-0004-ai-tool-support-status-survey/case.md`
  (`Status: closed`)
- Blocks: none
- Related: `docs/architecture/ai-tool-support-status.md`,
  `docs/backlog/item-0021-ai-tool-support-status-survey.md`

## Decisions Not Settled by the Design Agreement

- None — fully settled by
  `docs/collaboration/agreements/2026-08-20-ai-tool-support-status-survey.md`
  (`DA-2026-08-20-08`).

## Context

- Included: `docs/spike/case-0004-...md`'s full research log,
  `docs/architecture/ai-tool-support-status.md`'s full text,
  `docs/collaboration/prompt-instruction-change-control.md`'s current
  "Agent Operating Contract Files" and "Per-Agent-Tool Rule Applicability
  Registry" sections.
- Omitted: nothing else — this is a narrow, fully-specified addition.
- Assumptions: none — the exact text to insert is given verbatim above;
  the independent re-verification step is a genuine check, not a
  formality.

## References

- `docs/spike/case-0004-ai-tool-support-status-survey/case.md`
- `docs/architecture/ai-tool-support-status.md`
- `docs/collaboration/prompt-instruction-change-control.md`

## Work Notes

- 2026-08-20 — Design & Review group (Planner persona). Issue opened as
  part of WP-0025, scoped per the design agreement. Not yet dispatched.
- 2026-08-20 — Implementation group (Implementer persona), branch
  `wp-0025-execution` (branched from `process/item-0021-status-survey` at
  `7d61ab5`). Executed this issue in full.

  **Step 1 — independent re-verification (before any edit).** Fetched
  both URLs directly, independently of the Design & Review group's own
  citations:

  1. `https://ai.google.dev/gemini-api/docs/antigravity-agent` — found:
     "you can mount files like `AGENTS.md` for instructions and skills
     under `.agents/skills/` directly into the sandbox." This confirms
     Antigravity reads `AGENTS.md` for project-level instructions,
     matching `docs/architecture/ai-tool-support-status.md`'s Antigravity
     section and `docs/spike/case-0004-.../case.md`'s research log
     exactly.
  2. `https://antigravity.google/docs/subagents/` — found: "A maximum
     nesting depth of **10 levels** (layers of subagents beneath the
     primary agent) is strictly enforced to prevent runaway recursion or
     resource exhaustion," and separately: "Agents can communicate with
     parent agents, subagents, or peer agents whose ID is known." Both
     quotes match the status report and spike case exactly, word for
     word.

  **Result: no discrepancy found.** Both re-fetches confirmed the
  existing documents' claims exactly. Proceeded to the edit.

  **Step 2 — the edit.** Added the specified bullet to "Agent Operating
  Contract Files" (after the `docs/templates/*.md` bullet) and a **new
  row** (not a merge) to the "Per-Agent-Tool Rule Applicability
  Registry" table, titled `Canonical source (also read directly, no
  mirror needed)`, placed directly after the existing `AGENTS.md`
  `Canonical source` row. Chose a new row over merging because the
  existing `Canonical source` row states a fact about `AGENTS.md` itself
  (it is the literal-full-mirror group's source of truth), while Codex
  CLI and Antigravity reading it directly is a different kind of fact (a
  consuming-tool relationship) — merging the two into one row would
  overload it with two claims a later reader would have to disentangle.

  **Step 3.** Created
  `docs/collaboration/traces/2026-08-20-ai-tool-support-status-survey.md`
  per `docs/templates/ai-work-trace.md`.

  **Self-review (Full form, planning size M) — using
  `docs/templates/review-record.md`'s "Deterministic Verification
  Output" and "Falsification Search" sections, as the Implementer:**

  ### Deterministic Verification Output

  Command: `python3 scripts/check-contract-consistency.py`

  ```text
  references:
    docs/architecture/ai-tool-support-status.md:67 names '.cursor/worktrees.json', which does not exist
    docs/architecture/ai-tool-support-status.md:91 names 'github.com/xai-org/grok-build/.../16-subagents.md', which does not exist
    docs/architecture/ai-tool-support-status.md:110 names 'ANTIGRAVITY.md', which does not exist

  contract consistency: 3 failure(s)
  ```

  All 3 failures are pre-existing and confined to
  `docs/architecture/ai-tool-support-status.md`, a file this issue is not
  permitted to touch (out of scope; already committed at
  `7d61ab5`). Confirmed by re-running the same checker with this issue's
  own changes stashed (`git stash`): identical 3 failures, same lines,
  same exit code 1 — byte-identical output before and after this issue's
  edit. This issue's own diff introduces **zero new failures**; it is a
  strict no-regression change against a checker that already failed on
  an out-of-scope file before this issue started. (These 3 failures are
  the checker's `check_references` path-existence check flagging
  backtick-quoted strings that are not repository file paths at all — a
  Cursor-side config filename mentioned in prose, a GitHub URL fragment,
  and a hypothetical filename the source document explicitly states was
  *not* found — not evidence of a real broken reference. Not fixed here,
  since the owning file is out of this issue's scope; worth a follow-up
  item against `docs/architecture/ai-tool-support-status.md` or the
  checker's own exclusion list, not resolved by this issue.)

  Command: `git diff --stat` (against `7d61ab5`)

  ```text
   docs/collaboration/prompt-instruction-change-control.md | 5 +++++
   1 file changed, 5 insertions(+)
  ```

  Plus the untracked new trace file
  (`docs/collaboration/traces/2026-08-20-ai-tool-support-status-survey.md`)
  and this issue's own file — both expected, both within scope.

  ### Falsification Search

  | # | Failure scenario searched for | Grounds it does not occur | Result |
  |---|---|---|---|
  | 1 | The two re-fetched URLs contradict the status report or spike case (the exact scenario this issue's own Acceptance Notes require checking for) | Both quotes fetched independently match the existing documents word-for-word (see Step 1 above) | not reproduced |
  | 2 | The contract-file edit touches a row, bullet, or section other than the two specified | `git diff` shows exactly 5 inserted lines in one file, both insertions matching the specified bullet and table row; no other line in `prompt-instruction-change-control.md` changed | not reproduced |
  | 3 | The edit introduces a new checker regression | Checker output is byte-identical (3 pre-existing failures, same lines) with and without this issue's changes staged, confirmed via `git stash` A/B comparison | not reproduced |
  | 4 | The new table row duplicates or contradicts the existing `AGENTS.md` `Canonical source` row instead of stating a distinct fact | The existing row states `AGENTS.md` is the mirror group's source of truth; the new row states which *other tools* read it directly — different subjects, no overlapping claim, and the new row is textually distinct (different first column value) so no table-parsing tool could conflate them | not reproduced |
  | 5 | The trace file omits a required field from `docs/templates/ai-work-trace.md` | Every top-level template section (Request, Context Ledger, Routing, AI Execution Records, Optional Reference Total, Cost/Reasoning Control, Preflight Validation, Decisions Carried, Verification, Changed Files, Next Safe Action, Notes) is present and filled in the created trace file | not reproduced |

  ### Scenarios Not Searched

  - Whether Antigravity's own documentation has since changed again after
    this issue's own fetch timestamp (2026-08-20) — inherent to any
    point-in-time documentation citation; the spike's own "Open risks
    after close" already names Antigravity's documentation as the least
    stable of the five tools surveyed and recommends a sooner-than-usual
    re-check cadence, which this issue does not itself schedule.
  - Whether the pre-existing 3 checker failures in
    `docs/architecture/ai-tool-support-status.md` should be fixed —
    out of this issue's own scope by the task's explicit constraint; not
    evaluated for correctness beyond confirming they are not a regression
    this issue caused.

## Verification

- Independent re-fetch of the two named URLs, confirming the quotes
  match.
- `python3 scripts/check-contract-consistency.py` — no regression.
- `git diff` confined to
  `docs/collaboration/prompt-instruction-change-control.md`, the new
  trace file, and this issue's/work plan's own tracking files.
